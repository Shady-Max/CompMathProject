import numpy as np

def task4(A):
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

    # User Input for 3x3 Matrix
    #print("Enter the 3x3 matrix row-wise (each row separated by spaces):")
    #A = np.array([list(map(float, input().split())) for _ in range(3)])

    # Performing LU Factorization
    L, U = lu_factorization(A)

    # Displaying the results
    print("\nLower Triangular Matrix L:")
    print(L)
    print("\nUpper Triangular Matrix U:")
    print(U)