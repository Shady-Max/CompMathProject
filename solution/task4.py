import numpy as np

def lu_factorization(A):
    n = A.shape[0]
    L = np.eye(n)  # Lower triangular matrix with 1s on diagonal
    U = A.copy()   # Upper triangular matrix

    for i in range(n):
        for j in range(i+1, n):
            factor = U[j, i] / U[i, i]
            L[j, i] = factor
            U[j, i:] -= factor * U[i, i:]

    return L, U