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
        # everything ABOVE diagonal is 0 x>j means column > row so to the right or above main
        # else None (to fill in later w/ LU decomp)
        row = [1 if x==j else (0 if x > j else None)  for x in range(n)]
        L.append(row)
    return L

def get_U(A):
    n = len(A)
    U = []
    for j in range(n):
        # 0s below the diagonal 
        row = [None if x > j else 0 for x in range(n)]
        U.append(row)
    return U

# REQUIRES SQUARE MATRIX INPUT, assume list of list representation      
def LU_Decomp(A):
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
    
def LUP_Decomp(A):
    n = len(A)
    pi = [x for x in range(n)]
    for k in range(n): # go row by row. O(n)
        p = 0
        for i in range(k, n): # O(n-k)
            if abs(A[i][k]) >  p: #we want to choose a large p to pivot on
                p = abs(A[i][k])
                k_pr = i #k_pr will be the row number we swap
        if p == 0: # all potential pivots = 0, determinant 0 --> singular
            raise Exception("Singular matrix") 
        # swap row places in permutation array
        pi[k], pi[k_pr] = pi[k_pr], pi[k] 
        # now swap each entry in row k w row k_pr
        for i in range(n): 
            A[k][i], A[k_pr][i] = A[k_pr][i], A[k][i]
        # create v vector s.t. v = v/pivot value
        for i in range(k+1, n):
            A[i][k] = A[i][k] / A[k][k]
            for j in range(k+1, n):
                A[i][j] = (A[i][j] - (A[i][k]*A[k][j]))
    return pi, A

#PA=LU so PAx = LUx = Pb
def LUP_Solve(pi, A, b):
    n = len(A)
    x = [None] * n
    # y = U*x 
    y = [None] * n
    for i in range(n):
        y[i] = b[pi[i]]
        for j in range(i):
            y[i] -= A[i][j]*y[j]
    for i in range(n-1, -1, -1):
        x[i] = y[i]
        for j in range(i+1,n):
            x[i] -= (A[i][j]*x[j])
        x[i] = round(x[i]/A[i][i], 2)
    return x

Apr = [[1., 5., 4.],[2.,0.,3.],[5.,8.,2.]]
#bA = [12.,9.,5.]
Bpr = [[1., 2., 0.],[3., 4., 4.],[5., 6., 3.]]
bB = [3., 7., 8.]
decompB = LUP_Decomp(Bpr)
piB = decompB[0]
mB = decompB[1]
#decomp_result = LUP_Decomp(Apr)
#pi = decomp_result[0]
#mA = decomp_result[1]
print(LUP_Solve(piB, mB, bB))
