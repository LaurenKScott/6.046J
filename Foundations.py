'''
Naive sorting algorithms
'''
import math
import random
# A is an array
def InsertionSort(A):
    for j in range(1, len(A)):
        key = A[j]
        # The subarray from [0..j-1] is already sorted
        i = j-1
        while i >= 0 and A[i] > key:
            # Swap A[i] with A[i+1]
            A[i], A[i+1] = A[i+1], A[i]
            i -= 1
        A[i+1] = key
    return A
AList = random.sample(range(-10,10),12)
