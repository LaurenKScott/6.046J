'''
REVIEW OF FFT


let A, B be matrices of 
POLYNOMIAL A(X) WITH DEGREE N-1 --> HIGHEST NONZERO COEFF
A(x) = SIGMA(bounds j=0 upto j=n-1) a(sub_j) * x^j
a is the jth coefficient, x is raised to the jth power
'''
import math

xt = complex(4, 5)
print(xt.real)
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
# A is input array of complex numbers
def DFT(k, A):
    n = len(A)
    # output array of 
    conj = []
    for k in range(n):
        #noting that python supports complex numbers. format is a+bj
        xk = 0
        for t in range(n):
            # angle = 2*pi*k*t/n
            angle = (math.pi * 2 * k * t) / n
            ta = complex(math.cos(angle), math.sin(angle)) 
            xt = A[t] + ta
            xk += xt
        conj.append(xk)
    return conj

            


