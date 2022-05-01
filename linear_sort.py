'''
Lower bounds for comparison sort = O(nlgn)
If we want to do better, then comparing elts is not the way
'''
from Foundations import InsertionSort
# COUNTING SORT
# given length n array, A of unsorted elts, where all elts <= some k
# 

A = [2, 5, 3, 0, 2, 3, 0, 3]
def count_sort(A, k):
    n = len(A)
    # initialize output array, B, which will hold the sorted elts
    B = [None] * (n+1)
    # initialize working storage array, C = [0...k].
    # at first, C[i] = 0 for all i
    C = [0] * (k+1)
    for j in range(n):
        # C[A[j]] counts how many times A[j] occurs in A
        C[A[j]] += 1
        # in other words C[i] counts elements EQUAL to i
    for i in range(1, k+1):
        # now C[i] counts elements LESS THAN or EQUAL to i
        C[i] += C[i-1]
        # for all i, C[i] >= C[i-1]
    for j in range(n-1, -1, -1):
        B[C[A[j]]] = A[j]
        # decrement C[A[j]] STABLE SORT SEE BELOW
        C[A[j]] -= 1
    # get rid of leading [None] val 
    return B[1:]

'''
What's so great about COUNTING SORT? 
it runs in O(n+k). that means, if k = O(n), then the entire sort
runs in LINEAR TIME. but how do we know k? sometimes we have an input 
array with a well-defined max (example: range of test scores)

STABLE SORT:
the elements that occur first in A, will occur first in B also
this is why decrementing C is so important
'''
#print(count_sort(A, 5))


def count_sort_dig(A, digit, r):
    B = [None] * len(A)
    C = [0] * r
    for i in range(len(A)):
        digAi = (A[i] // (r**digit)) % r
        C[digAi] += 1
        # now C[digAi] has # of occurences of digAi in A
    for j in range(1, r):
        C[j] += C[j-1]
        # now C[i] contains # elements in A less than or equal to i
    # working backwards from len(A) to 0
    for m in range(len(A)-1, -1, -1):
        digAi = (A[m]//(r**digit)) % r
        # decrement C FIRST. ensures stable sort.
        # if A[i] == A[j] but i<j, then i will appear BEFORE j in 
        # the sorted output list. this is def of stable sort
        C[digAi] -= 1
        B[C[digAi]] = A[m]
    return B

Q = [4329, 457, 657, 839, 436, 720, 355]
#print(count_sort_dig(Q, 0, 10))
# A is the input array, r is a chosen radix
def radix_sort(A, d):
    for i in range(d):
        A = count_sort_dig(A, i, 10)
    return A
#print(radix_sort(Q, 4))

'''
EXPLAIN WHY SORTING BY LEAST SIG DIG. 
stable sort: 
tie-breaking: if digit[i] is equal for #s k and m,
then the previous column's sort result (less significant
digit) will break the tie due to stability of counting 
sort. say k = 572, n = 482 and m = 475. least sig dig is [0] bc 
of our definition in count_sort_dig k[0] == n[0] < m[0] 
(since 2<5). our order is now k < n < m.
next step k[1] == m[1] < n[1]. since k before m in previous 
step, k before m here. Our order becomes k < m < n. 
next m[2] == n[2] < k[2]. m before n in previous step, m before
n here. the tie breaker of next least significant digit has 
already been considered in our previous step. now we have
m < n < k. 475 < 482 < 572 correct
'''

# TAKEAWAY: SMART RADIX CHOICE --> LINEAR SORT

'''
BUCKET SORT: AVERAGE CASE O(n)
'''
def bucket_sort(A):
    n = len(A)
    B = [] 
    for i in range(n):
        # B[i] is an empty list for all i initially
        B.append([])
    for i in range(n):
        d = int(n*A[i])
        B[d].append(A[i])
    for j in range(n):
        # use insertionsort to sort each list in place
        B[j] = InsertionSort(B[j])
    print(B)
    k = 0
    for i in range(len(B)):
        for j in range(len(B[i])):
            A[k] = B[i][j]
            k += 1
    return A

B = [0.450, 0.978, 0.524, 0.191, 0.154, 0.534, 0.090, 0.988, 0.823, 0.399]

print(bucket_sort(B))