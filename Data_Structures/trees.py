'''
insert(x), delete(x), successor(x)
rank(x) >> return index i of x in sorted order, select(i) >> return x of rank i
class RangeTree:
'''
'''
BST, Red-Black Tree
'''
# from random import randint
from re import X


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

'''
COLORING RULES FOR RB TREES:
Every node is either red or black. The root is black. Every NIL leaf is black
If a node is red, both its children must be black
For each node, all SIMPLE paths from that node to its descendant leaves must
containt the same number of black nodes
'''

class RBTree(BST):
    def __init__(self):
        super().__init__()

    def LeftRotate(self, node):
        # y is the original right child of node
        y = node.right
        # make y's left subtree node's new right subtree
        node.right = y.left
        # Now examining the LEFT subtree of the original RIGHT child of node
        if y.left is not None:
            y.left.p = node
        # set y's new parent to be node's parent. y and x now siblings
        y.p = node.p
        # if node was the root of the tree
        if node.p is None:
            # set y as the new root
            self.root = y
            # if node was originally its parent's left child (node.key < node.p.key)
        elif node == node.p.left:
            # make y the left child
            node.p.left = y
        # else, node must be the right child of its parent (node.key > node.p.key)
        else:
            # make y the right child
            node.p.right = y
        # finally, make y node's parent, such that node is left child of y
        y.left = node
        node.p = y

    def RightRotate(self,node):
        # we look to node's original left child, call it y
        y = node.left
        # first, make y's old right subtree into node's new left subtree
        node.left = y.right
        # if y has a right child
        if y.right is not None:
            # make node its parent
            y.right.p = node
        # y's new parent is node's old parent
        y.p = node.p
        # if node was originally the root of the tree
        if node.p is None:
            # make y the root
            self.root = y
        # else, if node was its parent's right child (node.key > node.p.key)
        elif node == node.p.right:
            # make y the new right child 
            node.p.right = y
        # else, node must have been the left child of its parent (node.key < node.p.key)
        else:
            # make y the new left child 
            node.p.left = y
        # finally, set node's parent as y, with node being the right child of y
        y.right = node
        node.p = y

    def RBInsert(self, node):
        y = None
        x = self.root
        while x is not None:
            y = x 
            # if node.key < x.key
            if node.key < x.key:
                # float down x's left subtree
                x = x.left
            # elif node.key >= x.key, float down x's right subtree
            else: x = x.right
        # continue until you hit a leaf. y's val will be the last non-NIL x val
        node.p = y
        # this can only happen if the tree was originally empty
        if y is None:
            # so set our insert node as the root
            self.root = node
        # next we figure out if node should be a left or right child of y
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node
        # make sure node is now a leaf before trying to rebalance
        node.left, node.right = None, None
        # Now set node's color to red
        node.color = 'r'
        # Fix the red-black balance of the tree using insert-fix
        self.RBInsertFix(node)

    def RBInsertFix(self, node):
        # while node has a red-colored parent
        while node.p and node.p.acolor == 'r':
            # CASE 1: PARENT OF NODE IS ITSELF A LEFT CHILD
            # if said parent is a LEFT child of its own parent 
            if node.p == node.p.p.left:
                # check the RIGHT child of parent's parent
                y = node.p.p.right
                # if y (aka node's UNCLE) is red
                if y.color == 'r': 
                    # make node.p and y black, and their parent node red
                    node.p.color = 'b' 
                    y.color = 'b'
                    node.p.p.color = 'r'
                    # now move on to node's grandparent
                    node = node.p.p
                # if node's uncle is black and node is a right child
                elif node == node.p.right:
                    node = node.p
                    self.LeftRotate(node)
                node.p.color = 'b'
                node.p.p.color = 'r'
                self.RightRotate(node)
            # else (node's parent is a right child of its own parent)
            else:
                # check the LEFT child of parent's parent - node's parent's sibling
                y = node.p.p.left
                # if y (node's parent's parent's right child aka the sibling of node.p) is red
                if y.color == 'r': 
                    # make node.p and y black, and their parent node red
                    node.p.color = 'b' 
                    y.color = 'b'
                    node.p.p.color = 'r'
                    # now move on to node's grandparent
                    node = node.p.p
                # if node's uncle is black and node is a right child
                elif node == node.p.left:
                    node = node.p
                    self.RightRotate(node)
                node.p.color = 'b'
                node.p.p.color = 'r'
                self.LeftRotate(node)
        self.root.color = 'b'

    def RBTransplant(self, nodex, nodey):
        pass
    def RBDelete(self, node):
        pass
    def RBDeleteFix(self, node):
        pass
    
A, B, C =  Node(15), Node(6), Node(18)
D, E, F, G =  Node(3), Node(7), Node(17), Node(20)
H, I, J = Node(2), Node(4), Node(13)
K = Node(9)

bstree = BST()
'''
A.left, A.right = B, C
B.p, B.left, B.right = A, D, E
C.p, C.left, C.right = A, F, G
D.p, D.left, D.right = B, H, I
E.p, E.right = B, J
F.p, G.p = C, C
H.p, I.p = D, D
J.p, J.left = E, K
K.p = J
'''

bstree.TreeInsert(A)

bstree.TreeInsert(B)
bstree.TreeInsert(C)
bstree.TreeInsert(D)
bstree.TreeInsert(E)
bstree.TreeInsert(F)
bstree.TreeInsert(G)
bstree.TreeInsert(H)
bstree.TreeInsert(I)
bstree.TreeInsert(J)
bstree.TreeInsert(K)
bstree.InOrderWalk(A)
print()

rbt = RBTree()
rbt.RBInsert(A)
