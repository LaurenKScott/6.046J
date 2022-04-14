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
emx = [
    [2, 3, 1, 5],
    [6, 13, 5, 19],
    [2, 19, 10, 23],
    [4, 10, 11, 31]
]

'''
# LUP Decomposition of a matrix, A
# Find 3 (n*n) matrices, L, U, and P, such that PA = LU
# L is a unit LOWER TRIANGULAR matrix
# U is an UPPER TRIANGULAR matrix
# P is a PERMUTATION matrix
'''


# INITIALIZES THE L MATRIX. THIS IS NOT THE FINAL DECOMP
def get_L(A):
    # Lower triangular matrix has ones on main diagonal, 0's above the diagonal
    # and original matrix entries below the diagonal
    n = len(A)
    L = []
    # Create row L[j][*] from entries of A[j][*]
    for j in range(n):
        # MAIN DIAGONAL of A is A[x][x] for all x in n
        # populate main diagonal with ones (if x == j, we are on main bc A[j][x] == A[x][x])
        # else, if x < j, we are BELOW the diagonal. so populate with A[j][x]
        # everything else (ABOVE diagonal) is 0
        row = [1 if x==j else (0 if x > j else None)  for x in range(n)]
        L.append(row)
    return L

def get_U(A):
    n = len(A)
    U = []
    for j in range(n):
        row = [None if x > j else 0 for x in range(n)]
        U.append(row)
    return U

# REQUIRES SQUARE MATRIX INPUT, assume list of list representation      
def LUP_Decomp(A):
    # pivot starts at a11 downto ann
    # v is remaining column values
    # omega_t is remaining row values
    # A' is submatrix square
    # pivot remains untouched
    n = len(A)
    L = get_L(A) # 1's on diagonal, 0s above diagonal
    U = get_U(A) # 0s below diagonal
    
    for k in range(n):
        U[k][k] = A[k][k]
        for i in range(k+1, n):
            L[i][k] = A[i][k] / A[k][k] # L[i][k] = v[i][*]
            U[k][i] = A[k][i] # U[k][i] = wT
        for i in range(k+1, n):
            for j in range(k+1, n):
                A[i][j] = A[i][j] - (L[i][k] * U[k][j])
    return L, U
    
   
print(LUP_Decomp(emx))

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

