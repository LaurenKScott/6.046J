"""

Heap data structure: represented with array

"""
import random
class Heap:
    def __init__(self):
        self.array = [None]
        self.heap_size = len(self.array) -1
    # any given node has a parent placed at i // 2th index in array
    def parent(self, i):
        return i // 2 
    # if left child exists, it is at the 2*i th index from array
    def left_child(self, i):
        return 2*i 
    # right child same but shifted right one index
    def right_child(self, i):
        return (2*i)+1
    # RETURN new array after adding value to ensure updated rep
    def addHeap(self, value):
        self.array.append(value)
        self.heap_size += 1
        return self
    # a, b = b, a. tuple swapping to help with heapify procedures
    def swap(self, ind1, ind2):
        self.array[ind1], self.array[ind2] = self.array[ind2], self.array[ind1]
        return self.array
    # for ease of printing only
    def __str__(self):
        return str(self.array)

"""
KEY FEATURE OF MAX HEAP: for all i (except root) in A
where i is the node/ index and A is the array representation of heap
A[parent(i)] >= A[i]

ALL PARENT NODES HAVE KEY/VALUE >= KEY/VALUE OF THEIR CHILDREN
"""
class MaxHeap(Heap):

    def __init__(self):
        super().__init__()

    # Takes an input array (unsorted), returns max heap 
    def BuildMaxHeap(self):
        half = (self.heap_size // 2) + 1
        # split heap in half, (examining non-leaves) from BOTTOM TO ROOT
        # work linearly down to root (recall root is at index 1)
        # calls to MAXHEAPIFY
        for i in range(half, 0, -1):
            self.MaxHeapify(i)
        return self.array

    # MaxHeapify takes in an index i and examines the value of i compared to its children
    # if A[i] < A[child(i)], then swap
    def MaxHeapify(self, i):
        left = self.left_child(i)
        rght = self.right_child(i)
        # check that index not out of range (incomplete trees) then compare values
        if (left <= self.heap_size) and (self.array[left] > self.array[i]):
            largest_found = left
        else: largest_found = i
        # Same but for right child of i
        if (rght <= self.heap_size) and (self.array[rght] > self.array[largest_found]):
            largest_found = rght
        # if i is not >= to BOTH its left and right children, then the child node with 
        # greater value becomes new parent node 
        if largest_found != i:
            self.swap(i, largest_found)
            self.MaxHeapify(largest_found)
            
        return self.array

    def Heapsort(self):
        self.BuildMaxHeap()
        for i in range(self.heap_size, 0, -1):
            self.swap(i, 1)
            self.heap_size -= 1
            self.MaxHeapify(1)
        return self   
            
"""
KEY FEATURE OF MAX HEAP: for all i (except root) in A
where i is the node/ index and A is the array representation of heap
A[parent(i)] <= A[i]

ALL PARENT NODES HAVE KEY/VALUE <= KEY/VALUE OF THEIR CHILDREN
"""
class MinHeap(Heap):
    def __init__(self):
        super().__init__()
    
    # SAME procedure for max heap, but with min-heapify procedure
    def BuildMinHeap(self):
        half = self.heap_size // 2
        # split heap in half, (examining non-leaves) from BOTTOM TO ROOT
        # work linearly down to root (recall root is at index 1)
        # calls to MAXHEAPIFY
        for i in range(half, 0, -1):
            self.MinHeapify(i)
    
    # MaxHeapify takes in an index i and examines the value of i compared to its children
    # if A[i] < A[child(i)], then swap
    def MinHeapify(self, i):
        left = self.left_child(i)
        rght = self.right_child(i)
        # check that index not out of range (incomplete trees) then compare values
        if (left <= self.heap_size) and (self.array[left] < self.array[i]):
            least_found = left
        else: least_found = i
        # Same but for right child of i
        if (rght <= self.heap_size) and (self.array[rght] < self.array[least_found]):
            least_found = rght
        # if i is not <= to BOTH its left and right children, then the child node with 
        # lesser value becomes new parent node 
        if least_found != i:
            self.swap(i, least_found)
            self.MinHeapify(least_found)

print("testing...")
for i in range(1000):
    nmx = MaxHeap()
    arr = random.sample(range(-5,15), 12)
    for val in arr:
        nmx.addHeap(val)
    nmx = nmx.Heapsort()

    if (nmx.array[1:] != sorted(nmx.array[1:])):
        print("FAILURE: ROUND", i, "\n", nmx)
print("DONE!")
'''
So why heaps?

Consider how long it takes for an unsorted array to be turned into a Maxheap
(see bound and proof on pg 159)
At first appears to be O(nlgn) but actually it is O(n) BECAUSE MAX-HEAPIFY COST VARIES BY HEIGHT OF NODE
MAX-HEAPIFY: T(n) <= T(2n/3) + O(1), where O(1) represents time to perform swaps and comparisons
T(n) = aT(n/b) + f(n)
a = 1, b = 3/2, f(n) = 1, n^(log_b(a)) = n^(log_3/2(1)) = n^0 
when f(n) is theta n^(log_b(a)), T(n) = lg(n)

each MAX-HEAPIFY call costs theta(h) where h is th e
the number of times MAX-HEAPIFY is called = n
so total cost is theta(n*sigma(h/2^h)) see summation formulae
== theta(n)

LINEAR SORTING TIME
'''

