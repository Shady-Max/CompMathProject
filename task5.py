import numpy as np
import matplotlib.pyplot as plt

def polynomial_curve_fitting():
    # Given data points
    x = np.array([0, 1, 2, 3, 4])
    y = np.array([0, 1, 4, 9, 16])
    
    # Fit a quadratic curve (degree 2 polynomial)
    coefficients = np.polyfit(x, y, 2)  # Quadratic fit
    a, b, c = coefficients
    
    # Generate fitted values
    x_fit = np.linspace(min(x), max(x), 100)
    y_fit = a * x_fit**2 + b * x_fit + c
    
    # Plot original points and fitted curve
    plt.scatter(x, y, color='red', label='Data Points')
    plt.plot(x_fit, y_fit, label=f'Best Fit: y = {a:.2f}x² + {b:.2f}x + {c:.2f}', color='blue')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.title('Quadratic Curve Fitting')
    plt.grid()
    plt.show()
    
    return coefficients  # Return coefficients for verification

# Run the function
polynomial_curve_fitting()
