# Dynamic programming problems
from math import inf
import random
'''
Rod-cutting problem: We have a rod of length n (inches). We also have a 
price table, p, which represents how much money (dollars) we would obtain 
by selling a length n (inches) rod. We want to find the maximum revenue (r(n))
obtainable by taking the length n rod and cutting into pieces, then selling each
piece according to price table p. Assume cutting is free for now.

MEMOIZATION
'''
# represent price table as an array 0 --> n
# Value p[n] represents the price we would get for selling length n piece
# note that p[0] == 0 
price_table = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
# there are 2^(n-1) ways to cut the rod, including making 0 cuts

# NAIVE METHOD: RECURSIVELY CUT
# n is rod length, p is price table 
def naive_cut(n, p):
    if n == 0:
        return 0
    # q is our maximum revenue. for now, -infinity
    q = -inf
    for i in range(1, n):
        q = max(q, p[i] + naive_cut(n-i, p))
    return q
# RUNTIME IS O(2^n)

# TOP-DOWN MEMOIZATION: RECURSIVE, BUT SAVES OLD SUBPROBLEMS
def memo_cut(n, p):
    r = [-inf] * n
    r.insert(0,p[0])
    return memo_cut_aux(n, p, r)
def memo_cut_aux(n, p, r):
    # if r[n] >= 0, we have examined this subproblem already
    if r[n] >= 0:
        return r[n]
    # otherwise, same as naive solution. recursively solve subprobs
    # BUT no need to solve the same subproblem mult times
    if n == 0:
        q = 0
    else:
        q = -inf
        for i in range(1, n+1):
            q = max(q, p[i]+ memo_cut_aux(n-i, p, r))
    r[n] = q
    return q

# BOTTOM-UP MEMOIZATION: sort subproblems by "size" (defns vary by problem)
# then solve each subproblem in order, smallest to largest
def bottom_up_cut(n, p):
    # array r will represent optimal solution for each size subproblem
    r = [None] * n
    r.insert(0,0)
    for j in range(1, n+1):
        q = -inf
        for i in range(1,j+1):
            q = max(q, p[i] + r[j-i])
        r[j] = q
    print(r)
    return r[n]

n = 10
p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 26]
print(bottom_up_cut(n, p))

def naive_fib(n):
    if n == 1 or n == 2:
        return 1
    else: 
        return naive_fib(n-1) + naive_fib(n-2)


mem = {0:0, 1:1, 2:1}
def memo_fib(n, mem):
    if n < len(mem):
        return mem[n]
    else:
        mem[n] = memo_fib(n-1, mem) + memo_fib(n-2, mem)
        return mem[n]

print(memo_fib(7, mem))