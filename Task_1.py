import numpy as np
import matplotlib.pyplot as plt

def task1(a, b, points, approx_root, true_root):
    # Function definition
    def f(x):
        return np.e - x - x**2  # Given function f(x) = e - x - x^2

    # Step 1: Generate x values and evaluate f(x)
    x_values = np.linspace(a, b, points)  # Generate points within the interval
    y_values = f(x_values)  # Compute function values

    # Step 2: Plot the function
    plt.axhline(0, color='black', linewidth=1)  # x-axis
    plt.axvline(0, color='black', linewidth=1)  # y-axis
    plt.plot(x_values, y_values, label="f(x) = e - x - x²", color='b')
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Graphical Method for Finding Root")
    plt.legend()
    plt.grid()
    plt.show()

    # Step 3: Compute absolute error
    abs_error = abs(true_root - approx_root)
    print(f"Absolute error: {abs_error}")
