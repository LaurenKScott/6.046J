'''
A demonstration of the STACK and QUEUE data structures, implemented in python

REFERENCE: INTRODUCTION TO ALGORITHMS, CLRS, CHAPTER 10
'''
import random as rnd

# Node object for implementing a SINGLY linked list
# Key can be any type, next is always initialized as None (pop/enqueue will handle linkage)
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

"""
define a parent class, InOut, which contains methods used by both Stack and Queue
self.size: represents # of elements in structure
self.head: in stack, analogous to TOP of stack. In queue, analogous to front of a register line
"""

class InOut:
    def __init__(self):
        self.size = 0
        self.head = None

    # O(1): Check if structure is empty
    def isEmpty(self):
        if self.head is None:
            return True
        return False
    
    # O(1): Return structure size (defined here as number of nodes in structure)
    def getSize(self):
        return self.size

    # O(n): FOR VISUALIZATION PURPOSES ONLY, prints string representation of current structure
    def __str__(self):
        if self.isEmpty():
            return ""
        current = self.head
        rep = str(current.key)
        while current.next:
            rep += " --> " + str(current.next.key)
            current = current.next
        return rep

    def iter(self):
        list_rep = []
        current = self.head
        while current:
            list_rep.append(current)
            current = current.next
        return list_rep



"""
STACK == LAST IN, FIRST OUT
naive method: implement using array (see python time complexity)
Custom class implementation (linked list concept)
"""
class Stack(InOut):
    # S.head represents the index of the LAST inserted element
    # No need to keep track of a tail
    def __init__(self):
        super().__init__()

    # PUSH: Append/addition method specific to Stack
    # O(1): Adds a node with given key to END of stack and updates self.size
    def push(self, node):
        node.next = self.head
        self.head = node
        self.size += 1

    # POP: Removal method specific to Stack 
    # O(1): Removes and returns the HEAD node in stack. sets new head and updates self.size
    def pop(self):
        # if stack is empty, there are no items to pop. Error
        if self.isEmpty():
            raise Exception("STACK UNDERFLOW: Cannot pop from empty stack")
        else: 
            pop_node = self.head
            #new head is next element in stack [item inserted immediately prev to head]
            self.head = self.head.next
            self.size -= 1
            # We want to return the orig. key passed when initializing node, 
            # not Node object pointer
        return pop_node

    #MULTIPOP: Remove and return the HEAD node K times
    def multipop(self, k):
        while not self.isEmpty() and k > 0:
            self.pop()
            k -= 1

"""
QUEUE == FIRST IN, FIRST OUT
Analogous to a line of people at a cash register. First come, first served
"""

class Queue(InOut):
    # Q.head represents the FIRST element inserted
    # Q.tail represents the LAST element inserted 
    def __init__(self):
        #Initializes head and size attr
        super().__init__()
        self.tail = None
    
    # ENQUEUE: Append/addition method specific to Queue
    # O(1): add a new node to the tail of queue, update self.size
    def enqueue(self, node):
        
        if self.isEmpty():
            # When enqueueing to empty Queue, need to set head and tail
            # (In a list of 1 element, that elt. is both first and last)
            self.head = node 
            self.tail = node
        else:
            # Node linked to the TAIL end of the queue ('back of the line')
            self.tail.next = node
            self.tail = node
        self.size += 1

    # DEQUEUE: Removal method specific to Queue
    # O(1): Removes and returns node key from HEAD of queue, update self.size
    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue underflow: No items in queue")
        else:
            ret_node = self.head
            # set new head by "moving" one up in line
            self.head = self.head.next
            self.size -= 1
        return ret_node.key
    
test_stack = Stack()
test_queue = Queue()

stack_vals = rnd.sample(range(-10, 10), 12)
for val in stack_vals:
    node = Node(val)
    test_stack.push(node)

