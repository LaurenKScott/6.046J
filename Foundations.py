'''
Naive sorting algorithms
'''
import math
import random
'''
INSERTION SORT: 
O(n) space complexity
Loop invariant - 
Initialization: At start of for loop, the subarray A[0..j-1] --> A[0] is ALREADY sorted bc only 1 element 
Maintenance: A[i] and A[i+1 == j] are only swapped if A[i] > A[j] so the other values in the array are not 
affected. Then we move on to examine elements to the left (i-=1) of j's new placement, swapping if needed
This continues until the start of the array is reached (i= -1 < 0) OR A[i] <= A[j]. Jth element is placed 
directly after ith element (A[i+1] = key) once this condition has been reached. key won't be reassigned until
it has been compared and appropriately placed (while loop has ended, next for iteration begun)
Termination: the for loop examines all elements from j = 1 to j = A.length (recall 0 indexing and range() doc)
'''
# INSERTION SORT: O(n) space, O(n^2) time (worst case = reverse order list)
# A is an array of integers
def InsertionSort(A):
    for j in range(1, len(A)):
        key = A[j]
        # The subarray from [0..j-1] is already sorted
        i = j-1
        # Examine the sorted subarray, comparing each value to key
        while i >= 0 and A[i] > key: 
            # If A[i] > A[j],
            # Swap A[i] with A[i+1] = key
            A[i], A[i+1] = A[i+1], A[i]
            # Decrement i
            i -= 1
        # After entire subarray examined, i < 0 or A[j] > A[i]. place key
        A[i+1] = key
    return A

# MERGE SORT: O(n^2) space, O()
# A is an array of integers, p, q, r are indices such that p <= q <r < A.length
def Merge(A, p, q, r):
    # Define beginning indices of subarrays
    # left half should be length (q-p) + 1
    # right half should be length(r-q) 
    # total lengt h= left + right = q-p + 1 + r-q = r - p
    n1 = (q - p) + 1
    n2 = r - q
    left = []
    right = []
    # range = (0...q-p)
    for i in range(n1):
        left.append(A[p+i])
    # set last element of left to infinity so we don't have to deal with out of range indices
    left.append(math.inf)
    # range = (0...r-q-1)
    for j in range(n2):
        right.append(A[q+j+1])
    # same. set last element of right to infinity so no out of range compares 
    right.append(math.inf)
    i = 0
    j = 0
    k = p
    while k <= r:
        # if left array contains next lowest value
        if left[i] < right[j]:
            # place value from left array into A[k] and increment i
            A[k] = left[i]
            i += 1
        else:
            # same but for right, increment j
            A[k] = right[j]
            j += 1
        k += 1

def MergeSort(A, p, r):
    if p < r:
        # Take q to be the halfway point between p and r
        q = (p + r) // 2
        # Recursive calls to mergesort on left and right halves of A
        # LEFT: p --> q
        MergeSort(A, p, q)
        # RIGHT: q+1 --> r
        MergeSort(A, q+1, r)
        Merge(A, p, q, r)
        return A

def ins_test():
    print("\nINSERTION SORT DEMO", end="\n-----------------------------\n")
    AList = [random.choice(range(10)) for x in range(16)]
    
    print("\nUNSORTED:", AList, end="\n\n")
    print("\nSORTED:", InsertionSort(AList))

def merge_test():
    print("\n\n\nMERGE SORT DEMO", end="\n------------------------------\n")
    BList = [random.choice(range(10)) for x in range(16)]

    print("\nUNSORTED:", BList)
    print("\nSORTED:", MergeSort(BList, 0 , len(BList)-1))

# Given integer c map to binary array
def BinaryArray(c):
    barr = []
    if c == 0:
        barr.append(0)
    while c > 0:
        barr.append(c%2)
        c = c // 2
    return barr

def barr_to_str(barr):
    revbarr = [str(d) for d in barr[::-1]]
    bstr = ''.join(revbarr)
    return bstr

# Binary array 
def IncBinArr(barr):
    carry = 1
    i = 0
    while i < len(barr) and carry == 1:
        if barr[i] == 0:
            barr[i] = 1
            carry = 0
            continue
        elif barr[i] == 1:
            barr[i] = 0
        i+=1
    if i == len(barr) and carry == 1:
        barr.append(1)
    return barr
# UNIT TESTING
if __name__ == '__main__':

    barr15 = BinaryArray(15)
    bstr15 = barr_to_str(barr15)
    print(barr15, bstr15, sep="   ")
    inc15 = IncBinArr(barr15)
    print(inc15, barr_to_str(inc15), sep="   ")
    barr16 = BinaryArray(16)
    print(barr16, barr_to_str(barr16))
    barr12 = BinaryArray(12)
    bstr12 = barr_to_str(barr12)
    inc12 = IncBinArr(barr12)
    print(barr12, bstr12, sep="   ")
    print(inc12, barr_to_str(inc12))
    print(BinaryArray(13), barr_to_str(BinaryArray(13)))


