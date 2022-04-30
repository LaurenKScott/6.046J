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
'''
print(count_sort(A, 5))

