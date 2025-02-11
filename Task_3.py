import numpy as np

def task3(tol, max_iter):
    def gauss_seidel(A, b, x0, tol, max_iter):
        n = len(b)
        x = np.array(x0, dtype=float)  # Convert initial guess to a NumPy array
        for i in range(n):
            if A[i][i] == 0:
                print("There is no possible solutions")
    
        for _ in range(max_iter):
            x_new = np.copy(x)
        
            for i in range(n):
                sum1 = sum(A[i][j] * x_new[j] for j in range(n) if j != i)
                x_new[i] = (b[i] - sum1) / A[i][i]
        
            # Check convergence
            if np.linalg.norm(x_new - x, ord=np.inf) < tol:
                return x_new
        
            x = x_new
    
        return x  # Return the last computed solution

    # Coefficients matrix A and constant terms vector b
    A = np.array([[1, 1, 1], 
                  [1, 0, 1], 
                  [0, 1, 1]], dtype=float)

    b = np.array([9, 3, 7], dtype=float)

    x0 = np.zeros(len(b))

    # Solve using Gauss-Seidel method
    solution = gauss_seidel(A, b, x0, tol=1e-6, max_iter=100)

    print("Solution:", np.round(solution, 4))