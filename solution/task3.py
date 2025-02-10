import numpy as np

def gauss_seidel(A, b, x0, tol, max_iter):
        n = len(b)
        x = np.array(x0, dtype=float)  # Convert initial guess to a NumPy array
    
        for _ in range(max_iter):
            x_new = np.copy(x)
        
            for i in range(n):
                sum1 = sum(A[i][j] * x_new[j] for j in range(n) if j != i)
                x_new[i] = (b[i] - sum1) / A[i][i]
        
            # Check convergence (stop if max difference is below tolerance)
            if np.linalg.norm(x_new - x, ord=np.inf) < tol:
                return x_new
        
            x = x_new
    
        return x


def solution(A, b, max_iter, tol):
    x0 = [0, 0, 0]
    # Solve using Gauss-Seidel method
    return (np.round(gauss_seidel(A, b, x0, tol, max_iter), 4))