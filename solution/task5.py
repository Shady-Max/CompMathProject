import numpy as np
import plotly.graph_objects as go

def polynomial_curve_fitting(x,y):
    # Given data points
    x = np.array(x)
    y = np.array(y)
    
    # Fit a quadratic curve (degree 2 polynomial)
    coefficients = np.polyfit(x, y, 2)  # Quadratic fit
    a, b, c = coefficients
    
    # Generate fitted values
    x_fit = np.linspace(min(x), max(x), 100)
    y_fit = a * x_fit**2 + b * x_fit + c
    
    # Plot original points and fitted curve
    scatter_trace = go.Scatter(
        x=x, y=y, mode='markers', marker=dict(color='red'), name='Data Points'
    )

    curve_trace = go.Scatter(
        x=x_fit, y=y_fit, mode='lines', line=dict(color='blue'), 
        name=f'Best Fit: y = {a:.2f}x² + {b:.2f}x + {c:.2f}'
    )

    fig = go.Figure(data=[scatter_trace, curve_trace])
    fig.update_layout(
        title='Quadratic Curve Fitting',
        xaxis_title='X-axis',
        yaxis_title='Y-axis',
        showlegend=True,
        xaxis_showgrid=True,
        yaxis_showgrid=True 
    )
    
    return fig.to_json()