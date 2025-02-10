import numpy as np
import plotly.graph_objects as go

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
    x_values = np.array(x_values)
    y_values = np.array(y_values)

    n = len(x_values)
    result = 0.0

    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if i != j:
                term *= (x_target - x_values[j]) / (x_values[i] - x_values[j])
        result += term

    return result

def solution(x_data, y_data, x_target):
    estimated_value = lagrange_interpolation(x_data, y_data, x_target)

    x_plot = np.linspace(min(x_data), max(x_data), 100)
    y_plot = [lagrange_interpolation(x_data, y_data, x) for x in x_plot]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=x_data, y=y_data, mode='markers', marker=dict(color='red', size=8),
        name='Data Points'
    ))

    fig.add_trace(go.Scatter(
        x=x_plot, y=y_plot, mode='lines', line=dict(color='blue'),
        name='Lagrange Interpolation'
    ))

    fig.add_trace(go.Scatter(
        x=[x_target], y=[estimated_value], mode='markers',
        marker=dict(color='green', size=10, symbol='circle'),
        name=f'Estimated f({x_target}) = {estimated_value:.2f}'
    ))

    fig.update_layout(
        title='Lagrange Interpolation',
        xaxis_title='X-axis',
        yaxis_title='Y-axis',
        showlegend=True,
        xaxis_showgrid=True,
        yaxis_showgrid=True 
    )

    return (
        f"Estimated f(5.5) = {estimated_value}",
        fig.to_json()
    )