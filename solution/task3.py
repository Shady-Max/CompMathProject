import numpy as np


def gauss_seidel(A, b, x0, tol, max_iter):
    n = len(b)
    A = np.array(A, dtype=float)
    b = np.array(b, dtype = float)
    x = np.array(x0, dtype=float)  # Convert initial guess to a NumPy array

    for i in range(n):
        if A[i][i] == 0:
            return "There is no solution for this matrix using Gauss-Seidel Method"
        
    for _ in range(max_iter):
        x_new = np.copy(x)
        
        
        for i in range(n):
            sum1 = sum(A[i][j] * x_new[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum1) / A[i][i]
        
        # Check convergence
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new
        
        x = x_new
    
    return np.round(x, 4)  # Return the last computed solution

# Coefficients matrix A and constant terms vector b
A = np.array([[1, 1, 1], 
              [1, 0, 1], 
              [0, 1, 1]], dtype=float)

b = np.array([9, 3, 7], dtype=float)

x0 = np.zeros(len(b))

# Solve using Gauss-Seidel method
solution = gauss_seidel(A, b, x0, tol=1e-1, max_iter=1)

print("Solution:", solution)