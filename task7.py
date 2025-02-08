import numpy as np

def newtons_forward_difference(x_values, y_values):
    """
    Compute Newton's Forward Difference Table.
    
    Parameters:
    x_values (list or numpy array): x-coordinates of given points.
    y_values (list or numpy array): Corresponding y-coordinates of given points.
    
    Returns:
    numpy array: Forward difference table.
    """
    n = len(y_values)
    diff_table = np.zeros((n, n))
    diff_table[:, 0] = y_values
    
    for j in range(1, n):
        for i in range(n - j):
            diff_table[i][j] = diff_table[i + 1][j - 1] - diff_table[i][j - 1]
    
    return diff_table

def second_derivative_newton_forward(x_values, y_values, h):
    """
    Compute the second derivative using Newton's Forward Difference Formula.
    
    Parameters:
    x_values (list or numpy array): x-coordinates of given points.
    y_values (list or numpy array): Corresponding y-coordinates of given points.
    h (float): Step size (assuming equally spaced x-values).
    
    Returns:
    float: Approximate second derivative at the first data point.
    """
    diff_table = newtons_forward_difference(x_values, y_values)
    return diff_table[0, 2] / (h**2)

# Given data points
x_data = np.array([5, 6, 7, 8])
y_data = np.array([25, 36, 49, 64])
h = x_data[1] - x_data[0]  # Step size

# Compute second derivative at x = 5
second_derivative = second_derivative_newton_forward(x_data, y_data, h)
print(f"Approximate second derivative at x=5: {second_derivative}")