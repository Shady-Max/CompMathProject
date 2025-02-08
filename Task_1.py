import numpy as np
import matplotlib.pyplot as plt

# Function definition
def f(x):
    return np.e - x - x**2  # Given function f(x) = e - x - x^2

# Step 1: User Input
a = float(input("Enter the start of the interval: "))  # Example: 0
b = float(input("Enter the end of the interval: "))    # Example: 2
points = int(input("Enter the number of points to plot: "))  # More points = smoother curve

# Step 2: Generate x values and evaluate f(x)
x_values = np.linspace(a, b, points)  # Generate points within the interval
y_values = f(x_values)  # Compute function values

# Step 3: Plot the function
plt.axhline(0, color='black', linewidth=1)  # x-axis
plt.axvline(0, color='black', linewidth=1)  # y-axis
plt.plot(x_values, y_values, label="f(x) = e - x - x²", color='b')
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Graphical Method for Finding Root")
plt.legend()
plt.grid()
plt.show()

# Step 4: User provides an approximate root (observed from the graph)
approx_root = float(input("Enter the approximate root observed from the graph: "))

# Step 5: User provides a numerical root (e.g., from a precise method)
true_root = float(input("Enter the accurate root (e.g., from a numerical method): "))

# Step 6: Compute absolute error
abs_error = abs(true_root - approx_root)
print(f"Absolute error: {abs_error}")
