'''
insert(x), delete(x), successor(x)
rank(x) >> return index i of x in sorted order, select(i) >> return x of rank i
class RangeTree:
'''
'''
BST, Red-Black Tree
'''
# from random import randint
class Node:
    def __init__(self, key):
        self.key = key
        self.p = None
        self.left, self.right = None, None
        self.color = None

class Tree:
    def __init__(self):
        self.root = None
class BST(Tree):
    def __init__(self):
        super().__init__()
    # prints 
    def InOrderWalk(self, node):
        if node is not None:
            self.InOrderWalk(node.left)
            print(node.key, end="   ")
            self.InOrderWalk(node.right)

    def TreeSearch(self, node, val):
        while (node is not None) and (node.key != val):
            if val < node.key:
                node = node.left
            else:
                node = node.right
        return node

    def TreeMin(self, node):
        while node.left is not None:
            node = node.left
        return node

A, B, C, D, E, F, G = Node(6), Node(5), Node(7), Node(2), Node(5), Node(8), Node(11)
bstree = BST()
A.left, A.right = B, C
B.p, B.left, B.right = A, D, E
C.p, C.right = A, F
D.p = B
E.p = B
F.p, F.right = C, G
G.p = F

bstree.root = A
bstree.InOrderWalk(A)
start = bstree.root
print()
print(bstree.TreeSearch(start, 7))
print(bstree.TreeSearch(start, 11))
