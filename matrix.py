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


'''
# LUP Decomposition of a matrix, A
# Find 3 (n*n) matrices, L, U, and P, such that PA = LU
# L is a unit LOWER TRIANGULAR matrix
# U is an UPPER TRIANGULAR matrix
# P is a PERMUTATION matrix
'''
# From Ax = b, PA = LU, we have PAx=Pb ==> LUx = Pb
# A = P(inv)LU
# L, U are matrices (see above comments for definitions)
# b is the resulting vector from computing Ax
# pi is an array representation of P 
def LUP_Solve(L, U, pi, b):
    n = L.rows
    x = [] # new length n vector
    # for each row in L, calculate y using forward substitution
    for i in range(n):
        # Let Ux = y, so that Ly = Pb
        # Forward substition: Pb has b*pi_i as its ith elt
        # y[i] = b*pi[i] - SUM(L[i][j]*y[j]) <-- sum from j=1 to i-1
        print(i, 'y')
    # Now use backwards substitution to solve for x
    for i in range(n, 0, -1):
        print(i, 'x')
