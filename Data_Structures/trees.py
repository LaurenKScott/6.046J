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
    # prints node keys in sorted order

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

    def TreeMax(self, node):
        while node.right is not None:
            node = node.right
        return node
    
    def Successor(self, node):
        if node.right is not None:
            return self.TreeMin(node.right)
        par = node.p
        while (par is not None) and (node == par.right):
            node = par
            par = par.p 
        return par
    
    def Predecessor(self, node):
        # if there exists a value < node.key
        if node.left is not None:
            # node's predecessor is the maximum value in its left subtree
            return self.TreeMax(node.left)
        # else (if there is no left subtree of node)
        # explore node's parent
        par = node.p
        # while not the left child of root, AND
        # node is the left child of its parent (key < parent.key)
        while (par is not None) and (node == par.left):
            # keep going
            node, par = par, par.p
        # now you have either found the root OR the min value for which
        # node.key < par.key
        return par

    def TreeInsert(self, node):
        # start at the root
        x = self.root
        # Use y to track the parent of x as we traverse down 
        y = None
        while x is not None:
            # x becomes the new parent to track
            y = x
            # float down the appropriate subtree of x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        node.p = y
        if y is None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

    # this is a REPLACEMENT procedure, NOT a swap
    # nodex --> the node to be removed during Tree Delete
    # nodey --> the replacement node
    def TreeTransplant(self, nodex, nodey):
        # if x was the root of the BST
        if nodex.p is None:
            # make y the new root
            self.root = nodey
        # else if x was the left child of its parent node
        elif nodex.p.left == nodex:
            # make y the parents new left child
            nodex.p.left = nodey
        else:
            # make y the parents new right child
            nodex.p.right = nodey
        if nodey is not None:
            # assign y's new parent as x's former parent
            nodey.p = nodex.p

    def TreeDelete(self, node):
        if node.left is None:
            self.TreeTransplant(node, node.right)
        elif node.right is None:
            self.TreeTransplant(node, node.left)
        else:
            y = self.TreeMin(node.right)
            if y.p != node:
                self.TreeTransplant(y, y.right)
                y.right = node.right
                y.right.p = y
            self.TreeTransplant(node, y)
            y.left = node.left
            y.left.p = y

    
A, B, C =  Node(15), Node(6), Node(18)
D, E, F, G =  Node(3), Node(7), Node(17), Node(20)
H, I, J = Node(2), Node(4), Node(13)
K = Node(9)

bstree = BST()
A.left, A.right = B, C
B.p, B.left, B.right = A, D, E
C.p, C.left, C.right = A, F, G
D.p, D.left, D.right = B, H, I
E.p, E.right = B, J
F.p, G.p = C, C
H.p, I.p = D, D
J.p, J.left = E, K
K.p = J


bstree.TreeInsert(A)
bstree.InOrderWalk(A)