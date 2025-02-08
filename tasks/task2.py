from dataclasses import dataclass

a = None
b = None
tol = None

@dataclass
class Result:
    Root:float
    Iterations: int
    RelativeError: float

def init(A, B, Tol):
    global a, b, tol
    a = A
    b = B
    tol = Tol

def bisection_method(f, a, b, tol):
    if f(a) * f(b) >= 0:
        print("Invalid interval! f(a) and f(b) must have opposite signs.")
        return None, 0, None  # Return None for failure

    iterations = 0
    midpoint = (a + b) / 2
    prev_midpoint = a  # Used for relative error calculation

    while abs(f(midpoint)) > tol:
        iterations += 1
        if f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
            
        prev_midpoint, midpoint = midpoint, (a + b) / 2

        # Relative error calculation
        rel_error = abs((midpoint - prev_midpoint) / midpoint) if midpoint != 0 else None

        return midpoint, iterations, rel_error
    
def secant_method(f, x0, x1, tol):
    """Finds the root of f(x) using the Secant Method starting from x0 and x1."""
    iterations = 0
    prev_x = x0  # Used for relative error calculation

    while abs(f(x1)) > tol:
        iterations += 1
        x_temp = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))  # Secant formula
        x0, x1 = x1, x_temp

    # Relative error calculation
    rel_error = abs((x1 - prev_x) / x1) if x1 != 0 else None
    prev_x = x1

    return x1, iterations, rel_error

def f(x):
    return x**3 - x - 2

def solution():
    # Running Bisection Method
    root_bisection, iter_bisection, error_bisection = bisection_method(f, a, b, tol)
    print(f"\nBisection Method:\n  Root ≈ {root_bisection:.6f}\n  Iterations: {iter_bisection}\n  Relative Error: {error_bisection:.6f}")

    # Running Secant Method
    root_secant, iter_secant, error_secant = secant_method(f, a, b, tol)
    print(f"\nSecant Method:\n  Root ≈ {root_secant:.6f}\n  Iterations: {iter_secant}\n  Relative Error: {error_secant:.6f}")

    return {
        "BisectionMethod": Result(root_bisection, iter_bisection, error_bisection),
        "SecantMethod": Result(root_secant, iter_secant, error_secant)
    }