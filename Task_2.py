import math

# Function definition
def f(x):
    return x**3 - x - 2

# Bisection Method
def bisection_method(a, b, tol):
    if f(a) * f(b) >= 0:
        print("Bisection method cannot proceed. f(a) and f(b) must have opposite signs.")
        return None, None
    
    iter_count = 0
    c_old = a  # Initial value for error calculation

    while (b - a) / 2 > tol:
        c = (a + b) / 2
        iter_count += 1

        if f(c) == 0:
            break  # Found exact root

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        # Relative error calculation
        rel_error = abs((c - c_old) / c)
        c_old = c
    
    return c, iter_count

# Secant Method
def secant_method(x0, x1, tol):
    iter_count = 0
    x_old = x0  # Initial value for error calculation

    while abs(x1 - x0) > tol:
        if f(x1) - f(x0) == 0:
            print("Division by zero detected in Secant Method.")
            return None, None
        
        x_new = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        iter_count += 1

        # Relative error calculation
        rel_error = abs((x_new - x_old) / x_new)
        x_old = x_new

        if abs(f(x_new)) < tol:
            break

        x0, x1 = x1, x_new

    return x_new, iter_count

# User input for interval and tolerance
a = float(input("Enter the starting value of the interval (a): "))
b = float(input("Enter the ending value of the interval (b): "))
tolerance = float(input("Enter the tolerance level: "))

# Run methods and display results
root_bisection, iters_bisection = bisection_method(a, b, tolerance)
root_secant, iters_secant = secant_method(a, b, tolerance)

print("\nResults:")
if root_bisection is not None:
    print(f"Bisection Method: Root ≈ {root_bisection}, Iterations = {iters_bisection}")

if root_secant is not None:
    print(f"Secant Method: Root ≈ {root_secant}, Iterations = {iters_secant}")
