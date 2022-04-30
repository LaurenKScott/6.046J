'''
REVIEW OF FFT


let A, B be matrices of 
POLYNOMIAL A(X) WITH DEGREE N-1 --> HIGHEST NONZERO COEFF
A(x) = SIGMA(bounds j=0 upto j=n-1) a(sub_j) * x^j
a is the jth coefficient, x is raised to the jth power
'''


'''
HORNERS RULE FOR EVALUATION IN O(N) TIME
ADDITION AND SUBTRACTION TAKE O(N) TIME (ADDITIVE COEFFICIENTS THEN HORNER --> 2*N)
POLYNOMIAL MULTIPLICATION AND DIVISION: C(x) = A(x)*B(x) = SIGMA(bounds j=0 upto j=n-1) c(sub_j) * x^j
    c(sub_j) = SIGMA(bounds k=0 upto k=j) a(sub_k)*b(sub_j-k)
INTERPOLATION (FINDING COEFFICIENTS FROM SAMPLES):
EVALUATION: 
'''

# Differing representations of polynomial in program
# sample matrix (Vandermonde) and coefficient vector

vandermonde = [[]] # n-1 * n-1 dimensions
coefficients = [] # n-1 * 1

# Since each evaluation of sample x (dot product of row (Vandermonde) w coeff vector) takes O(n),
# and n sample x's need to be evaluated to determine unique polynomial of degree n-1,
# we have O(n^2) operations required to multiply polynomials using this rep

# SOLUTION: clever choice of sample points allows for O(n*lgn) EVAL AND INTERPOLATION
