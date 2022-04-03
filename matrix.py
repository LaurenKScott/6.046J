'''
MATRIX OPERATIONS IN PYTHON

Why are matrices useful?
Stochastic matrix (probability and stats)
Adjacency and edge-weight matrices (graph theory)
Linear transformations/combinations (physics)
Tensor (physics)
Systems of equations, polynomial operations
Encryption, machine learning
'''
# Matrix as a list of lists (array of arrays whatever)
example_matrix = [
    [1, 3, -1, 9],
    [-4, 0, 9, -5],
    [2, 6, 2, -9],
    [7, 10, -1, 4]
]

'''
# LUP Decomposition of a matrix, A
# Find 3 (n*n) matrices, L, U, and P, such that PA = LU
# L is a unit LOWER TRIANGULAR matrix
# U is an UPPER TRIANGULAR matrix
# P is a PERMUTATION matrix
'''
# REQUIRES SQUARE MATRIX INPUT      
def LUP_Decomp(A):
    n = len(A)
    L = []
    U = []
    pi = [None for i in range(n+1)]
    for i in range(1, n+1):
        pi[i] = i
    pi = pi[1:]
    return pi
print(LUP_Decomp(example_matrix))

# From Ax = b, PA = LU, we have PAx=Pb ==> LUx = Pb
# A = P(inv)LU
# L, U are matrices (see above comments for definitions)
# b is the resulting vector from computing Ax
# pi is an array representation of P 
def LUP_Solve(L, U, pi, b):
    #n is number of rows
    n = len(L)
    x = [] # new length n vector
    y = []
    # for each row in L, calculate y using forward substitution
    for i in range(n):
        # Let Ux = y, so that Ly = Pb
        # Forward substition: Pb has b*pi_i as its ith elt
        # y[i] = b*pi[i] - SUM(L[i][j]*y[j]) <-- sum from j=1 to i-1
        y[i] = b[pi]
        for j in range(i):
            y[i] -= (L[i][j])*y[j]
    print(y)
    # Now use backwards substitution to solve for x
    for i in range(n, 0, -1):
        print(i, 'x')

#pass a list of lists
class Matrix:
    def __init__(self, rows, cols):
        # rows = int number of rows
        self.rows = rows
        # cols = int number of columns
        self.cols = cols
        # initialize an empty (0x0) matrix
        self.mat = []
        for i in range(rows):
            # get row by row input from the user, strip any whitespaces
            # ignore any inputs outside of column range
            row_input = input("Enter one integer per entry, separated by space ").strip().split()[:cols]
            # make that row into a list of integers (assume int input)
            ri = list(map(int, row_input))
            # append it to our list-of-lists matrix
            self.mat.append(ri)
    def get_mat(self):
        return self.mat
    def get_entry(self, i, j):
        if i < self.rows and j < self.cols:
            return self.mat[i][j]
        else:
            return False
