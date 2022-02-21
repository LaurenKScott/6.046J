# CHAPTER 10.2: LINKED LISTS

"""
NOTE: PYTHON DOES NOT INCLUDE LIST TYPE 
PYTHON 'LIST' ACTUALLY ANALOGOUS TO ARRAY TYPE 
[] vs [headnode <--> node <--> node <--> ... <--> tailnode]
"""

# Define a NODE object to package information
class Node:
    # Prev, next pointers (default is None)
    # Key represents [INT] datatype, the "value" stored in the node
    def __init__(self, key):
        self.prev = None
        self.next = None
        self.key = key

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Inserts a NODE with KEY value to HEAD of LinkedList
    # O(1)
    def ListInsert(self, key):
        # Create new node with given key
        nod = Node(key)
        # If LinkedList was prev empty, nod.next == None. Else, nod.next == previous HEAD
        nod.next = self.head
        if self.head is not None:
            # Only if Linked list NOT empty prior to insert
            self.head.prev = nod
        self.head = nod
        self.size += 1

    # NOTE: WE ARE DELETING THE NODE, not the node with KEY value. Deleting the node takes O(1)
    # But if we want to delete node with given KEY value, we must first do ListSearch (O(n))
    def ListDelete(self, node):
        # If node to remove was not the HEAD node, then splice out safely
        if node.prev is not None: 
            node.prev.next = node.next
        # else we must reassign the HEAD
        else: 
            self.head = node.next
        # If the NODE to remove is not TAIL, splice out safely
        if node.next is not None:
            node.next.prev = node.prev
        # In singly linked non circular list we do not care about tail
        self.size -= 1
    
    # Input: skey (searchKey), the key value we are looking for in the list
    # Returns None if skey not in LinkedList, or NODE object if skey == NODE.key
    # Complexity O(n) in worst case: must check all nodes
    def ListSearch(self, skey):
        # Start at head of LinkedList
        current = self.head
        # Move to the next node until either: 
        # searchKey is found (== current.key) OR LinkedList ends (current=None)
        while (current is not None) and (current.key != skey):
            current = current.next
        # If LinkedList ends without finding searchKey, current == None so returns None
        # If searchKey is found, returns the NODE storing searchKey
        return current

    def __str__(self):
        elt = 0
        curr = self.head
        rep = str(curr.key)
        while elt < self.size:
            rep += " <--> " + str(curr.next.key)
            curr = curr.next
            elt += 1 
        return rep

class SentinelList(LinkedList):
    def __init__(self):
        super().__init__()
        self.nil = Node(None)
        self.head, self.tail = self.nil, self.nil
        self.tail.next, self.head.prev = self.nil, self.nil

    def SentinelInsert(self, key):
        nod = Node(key)
        nod.next = self.nil.next
        self.nil.next.prev = nod
        self.nil.next = nod
        nod.prev = self.nil
        self.size += 1

    def SentinelDelete(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
    
    def SentinelSearch(self, skey):
        nod = self.nil.next
        while nod != self.nil and nod.key != skey:
            nod = nod.next
        return nod

class npNode:
    def __init__(self, key):
        self.key = key
        self.np = None
    
    """
    a <--> b <--> c <--> d 
    0 --> None
    10
    01 
    11
    00
    """
