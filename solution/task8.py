import numpy as np
import scipy.integrate as spi

def simpsons_rule(func, a, b, n):
    """
    Approximate integral of a function using Simpson's Rule.
    
    Parameters:
    func (callable): Function to integrate.
    a (float): Lower bound of integration.
    b (float): Upper bound of integration.
    n (int): Number of subintervals (must be even).
    
    Returns:
    float: Approximate integral value.
    """
    if n % 2 == 1:
        raise ValueError("Number of subintervals must be even.")
    
    x = np.linspace(a, b, n+1)
    y = func(x)
    
    h = (b - a) / n
    integral = (h / 3) * (y[0] + 4 * np.sum(y[1:n:2]) + 2 * np.sum(y[2:n-1:2]) + y[n])
    
    return integral

def f(x):
    return np.sin(x)