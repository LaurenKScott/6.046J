'''
Lower bounds for comparison sort = O(nlgn)
If we want to do better, then comparing elts is not the way
'''

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
print(count_sort(A, 5))


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
        C[digAi] -= 1
        B[C[digAi]] = A[m]
    return B

print(count_sort_dig(A, 1, 5))
# A is the input array, r is a chosen radix
def radix_sort(A, r):
    for i in range(r):
        pass

