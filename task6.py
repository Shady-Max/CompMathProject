import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x_values, y_values, x_target):
    """
    Perform Lagrange Interpolation to estimate f(x_target) using given data points.
    
    Parameters:
    x_values (list or numpy array): x-coordinates of given points.
    y_values (list or numpy array): Corresponding y-coordinates of given points.
    x_target (float): The x-value at which interpolation is performed.
    
    Returns:
    float: Estimated value of f(x_target).
    """
    n = len(x_values)
    result = 0.0

    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if i != j:
                term *= (x_target - x_values[j]) / (x_values[i] - x_values[j])
        result += term

    return result

# Given data points
x_data = np.array([5, 6, 7, 8])
y_data = np.array([25, 36, 49, 64])

# Estimate f(5.5) using Lagrange Interpolation
x_target = 5.5
estimated_value = lagrange_interpolation(x_data, y_data, x_target)

# Display result
print(f"Estimated f(5.5) using Lagrange Interpolation: {estimated_value}")

# Plot the interpolation
x_plot = np.linspace(min(x_data), max(x_data), 100)
y_plot = [lagrange_interpolation(x_data, y_data, x) for x in x_plot]

plt.scatter(x_data, y_data, color='red', label='Data Points')
plt.plot(x_plot, y_plot, color='blue', label='Lagrange Interpolation')
plt.scatter(x_target, estimated_value, color='green', marker='o', label=f'Estimated f(5.5) = {estimated_value:.2f}')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.title('Lagrange Interpolation')
plt.grid()
plt.show()
