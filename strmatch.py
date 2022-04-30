
'''
STRING MATCHING: THE GOAL
often we search a large string (e.g. a textbook or webpage) for occurrences of 
some smaller substring (e.g. a single word)
How can we do this efficiently?
'''
import math
'''
FIRST, THE NAIVE METHOD

'''
# text --> string, usually very large
# pattern --> a shorter string, the pattern we want to find
# O(m*(n-m+1))
def naive_str_match(text, pattern):
    n = len(text)
    m = len(pattern)
    # Initialize s(hift) variable. starts as 0, goes to n-m
    s = 0
    # found flag allows us to find all matches before returning anything
    found = False
    # runs n-m times
    while s <= n-m:
        window = text[s:s+m] # length m window 
        # compares EACH char of pattern, window, therefore O(m) comparisons required
        if pattern == window:
            print("Match found at", s)
            found = True
        # slide window over 1
        s += 1
    return found

'''
IMPROVEMENT 1: RABIN-KARP
Choose a radix, d, and interpret each character as an int in (0...d]
Then, use a simple hash function to assign a SINGLE value representing the 
hash of our pattern string (as opposed to each character having its hash value). 
Using radix d is how we are able to compute this hash numerically despite dealing 
with chars. Next, we take each length m window of text (m is the length of the 
pattern string) and compute its hash value. IF the hash value for the window equals
the hash value of the pattern, we have a potential match. we then compare each character
of the potential match to the corresponding char of the pattern (as in the naive method)
This will determine if the match is a TRUE match, or a different string that happens to 
have the same hash value
'''
# d is our radix, here I choose 256 for UNICODE characters

d = 256
# text --> string
# pattern --> string (short compared to text)
# q --> int, a prime number
def rabin_karp(text, pattern, q):
    n = len(text)
    m = len(pattern)
    # h represents the hash value of the highest-order character in the string
    # for a length m string, highest order character is at the 0th index, value is d**(m-1)
    h = (d**(m-1)) % q
    # initialize p(attern) and t(ext) hash values --> yields ints
    # p only calculated once (see 1st for loop below)
    # t will be calculated many times as the window slides over
    p = 0
    t = 0
    found = False
    # PREPROCESSING STEP: assign hash values to the pattern and the 1st window 
    # O(m) OCCURS ONCE
    for i in range(m):
        # ord() --> input single unicode char, get back int
        p = ((d*p)+ ord(pattern[i])) % q 
        t = ((d*t) + ord(text[i])) % q
    # THE SLIDING WINDOW. O(n-m)
    for s in range((n-m)+1):
        # if hash values are equal, we have a POTENTIAL match. Further checking is needed
        if p == t:
            # window is the current length m block of text being examined
            window = text[s:s+m]
            #print(p, t, s, window)
            # we do a direct char by char comparison of pattern to window. O(m)
            if pattern == window:
                print("Match found at:", s)
                found = True
        # avoid out of range error that would occur at the very end of text
        if s < n-m:
            # calculate hash value for the next window of text (current window shifted over one)
            # t-(h*ord(text[s])) >> current text hash MINUS its highest order digit's hash
            # add next character as new lowest order digit, calculate new hash
            t = (d*(t-(h*ord(text[s]))) + ord(text[s+m])) % q #O(1)
    return found
'''
WHY RABIN-KARP?
At first glance, it looks like the same running time as naive version O(m*(n-m+1))
HOWEVER, this eliminates the char by char comparison needed every time by the naive algorithm
In Rabin-Karp, the O(m) preprocessing step occurs only once. Then, (n-m) hash values are compared 
Since the hash values are ints, the comparisons are each O(1). Only if the hash values of pattern and
text window match do we perform the O(m) char by char comparison from naive algrorithm. So Rabin-Karp
only performs O(m*(n-m+1) + O(m)) operations in the WORST case. We can minimize these comparisons by cleverly
choosing q. If q is sufficiently large prime, there is a greatly reduced chance that 2 strings have the 
same hash value. So, making q a prime integer allows for fewer false matches, and fewer char by char comparisons overall.

Assuming a cleverly-chosen q, Rabin-Karp will return c potential matches, each requiring O(m) steps to 
verify. On average, it runs in O((n-m+1)+cm) or O(n + (c-1)m + 1) == O(n+m)
'''


'''
DETERMINISTIC FINITE AUTOMATON: A STATE MACHINE SOLUTION
M is our automaton
M ::= (Q, q0, A, Sigma, Delta)
Q is the set of states
q0 is the start state
A(subset of) Q is the subset of accepting states
Sigma is the input alphabet
Delta is function Q x Sigma into Q, called transition function of M
M INDUCES a final state function Phi 
'''
# a is the accepting state, delta is a mapping(dict) computed below
# returns BOOL found and PRINTS pattern at first found position
def finite_automaton_matcher(text, delta, a):
    found = False
    n = len(text)
    # start state is 0
    q = 0
    for i in range(n): # O(n)
        q = delta[(q, text[i])] # O(1) since delta pre-computed
        if q == a: # O(1)
            print("Pattern found. Shift equals", (i-a)+1)
            found = True
    return found

'''
Computing the delta "function" (here, a dict) maps state, character tuple to the next state
for all chars in sigma (alphabet of possible characters)
and for all states in 0...m
'''
# INPUT: pattern(string), and sigma(string): sigma is set of unique characters in our alphabet
# OUTPUT: delta, a dictionary mapping (q,char) pairs to a new value for q
# where q is a state in our state machine
def compute_delta(pattern,sigma):
    m = len(pattern)
    delta = {}
    for q in range(m+1): #O(m)
        for char in sigma: #(|sigma|)
            k = min(m , q+2) # max value of m
            #length k prefix of p
            pk = pattern[:k]
            # length q prefix of p PLUS char of alphabet 
            pqa = pattern[:q] + char
            # examine the length k SUFFIX of pqa
            while pk != pqa[-k:] and k>0: # char to char comparison, length k
                k -= 1 # k
                pk = pattern[:k]
            else:
                delta[(q,char)] = k
                continue
    return delta

'''
Overall analysis: innermost while loop runs a maximum of (k == m) comparisons 
THEN has to decrement k up to (k==m times) so WHILE loop takes O(k^2) == O(m^2) in worst case
The inner for loop (for char in sigma) runs O(|sigma|) times
Finally, the outermost for loop (q = 0 upto m) runs O(m) times
TOTAL: O((m^3)*|sigma|) JUST FOR COMPUTING DELTA 
Computing delta occurs once before running finite_automaton_matcher, which runs in O(n)

SO, all told we have O((m^3))*|sigma|) + O(n). dominating term depends on m vs n
OOF THAT'S BAD FAM. can reduce to m*|sigma| BUT
Let's try bypassing need for a delta function altogether...
'''


'''
KNUTH-MORRIS-PRATT ALGORTIHM
Pre-compute an auxillary func pi, computed in time O(m) and stored in length-m array
for state machine Q = q0 .. qm, and alphabet |sigma| = chars, pi[qi] has info req for computing delta(qi, char)
BUT pi[q] DOES NOT DEPEND ON CHAR

Consider the following question: 
given that certain pattern characters P[1..q] match text (with shift s) T[s+1...s+q],
what is the SMALLEST shift s' > s such that for SOME k < q, P[1...k] = T[s'+1...s'+k]
where s' + k = s + q?

s and q are givens, and s' = s + q - k
SO pi[q] ::= max(k: k < q AND Pk is a SUFFIX of pq)
'''
def kmp_matcher(text,pattern):
    n = len(text)
    m = len(pattern)
    pi = compute_prefix(pattern) #O(m)
    q = 0
    found = False
    for i in range(n): # O(n)
        while q > 0 and pattern[q] != text[i]: # O(1) char comparison
            q = pi[q-1] # MAXIMUM O(m)
        if pattern[q] == text[i]: # O(1) char comparison
            q += 1
        if q == m: # O(1) int comparison
            print("Pattern found. Shift equals", i-m+1)
            found = True
            q = pi[q-1]
    return found

  
# INPUT: pattern(string)
# OUTPUT: pi, a length m array composed of shift values we compose
# by definition pi[q] ::= max(k: k < q && pk is a SUFFIX of pq)
# RUNS IN O(m)
def compute_prefix(pattern):
    m = len(pattern)
    pi = [0] * m # O(1) time to assign, O(m) space
    k = 0
    for q in range(1,m): #O(m-1)
        while k > 0 and pattern[k] != pattern[q]: #O(1) comparison
            k = pi[k] #O(1) assignment, k < q
        if pattern[k] == pattern[q]: #O(1) comparison, DOES NOT REENTER WHILE LOOP
            k += 1  #O(1) increment k max value m-1
        pi[q] = k #O(1) reassign pi[q] = 0 to k
    return pi


box = 'aaaa'
dna = 'ttaaataatcacctacattcatcaacacctgtcaccgcgggcaaagaagcaattgccactacggtcgtcatcagggcgtacggtagggactatccgtgtttaaggaggtctaaataggaaactcaattcttataaaatgtgttcatgt'
bases= 'acgt'
rabin_karp(dna, box, 24151)
seq = '78216654857478461551811468660326773098550947419861681946078380010481458111663542411085863374184049655935320791415231222158295825199741993361739172307'
pat = '7419'
compute_prefix(pat)
kmp_matcher(seq, pat)

# EXERCISE: GET DELTA COMPUTATION TIME DOWN TO O(m*|sigma|)
# Hint: Show that delta[(q,a)] == delta[(pi[q], a)] IF q==m OR pattern[q+1] != a

# k is the longest length prefix of the pattern that is also a suffix of equal length
# 

# when q == m, pattern[q] is last char of pattern, pattern[k] is ??
p = 'ababaca'
m = len(p)
#print(p[:m]) + 'd'


# repetition factor, r of a string x. x has repetition factor r if x can be written
# as x = (y)^r, where y is some substring of x, and r denotes concatenating y with itself
# r times. Example let x = abababab = (ab)^4. y=ab, r=4. r > 0. x,y exist in same alphabet
# let rho(x) be largest r such that x has repetition factor r
# EXERCISE

def repetition_matcher(text, pattern):
    m, n = len(pattern), len(text)
    #rho_list = compute_rho(pattern)
    #k = 1 + max(rho_list)
    k = 2
    q, s = 0, 0
    found = False
    while s <= (n-m):
        if pattern[q] == text[q+s]:
            q += 1
            if q == m: # every character in pattern is a match
                print("Pattern found. Shift equals", s)
                found = True 
        if (pattern[q] != text[q+s]) or (q==m):
            q = 0
            s += max(1, math.ceil(q/k))
    return found
def compute_rho(pat):
    m = len(pat)
    rho = compute_prefix(pat)
    for q in range(m):
        if rho[q] != 0:
            print(pat[:q+1])
    return rho
print(compute_rho('ababaca'))