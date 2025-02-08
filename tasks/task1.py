import numpy as np
from scipy.optimize import bisect
import plotly.graph_objects as go
import json

a=None
b=None
points=None

def f(x):
    return np.e - x - x**2

def solution():
    x_values = np.linspace(a, b, points)  # Generate points within the interval
    y_values = f(x_values)  # Compute function values

    # Step 3: Plot the function
    fig = go.Figure()

    fig.add_shape(type="line", x0=min(x_values), x1=max(x_values), y0=0, y1=0,
              line=dict(color="black", width=1))
    
    fig.add_shape(type="line", x0=0, x1=0, y0=min(y_values), y1=max(y_values),
              line=dict(color="black", width=1))

    fig.add_trace(go.Scatter(x=x_values, y=y_values, mode="lines", name="f(x) = e - x - x²", line=dict(color='blue')))

    fig.update_layout(
        title="Graphical Method for Finding Root",
        xaxis=dict(title="x", showgrid=True, zeroline=True, zerolinecolor='black'),
        yaxis=dict(title="f(x)", showgrid=True, zeroline=True, zerolinecolor='black'),
        legend=dict(x=0.8, y=1),
    )
    
    return fig.to_json()

def task1_calculate_error(approx_root):
    true_root = bisect(f, a, b)
    abs_error = abs(true_root - approx_root)
    return abs_error

    