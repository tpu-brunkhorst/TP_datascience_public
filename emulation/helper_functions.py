# helper_functions.py
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

import numpy as np
import pandas as pd

def generate_dummy_data(n_years=10, start_year=2000):
    """
    Generates dummy data with year-to-year increasing trends, annual, weekly, and daily seasonality,
    and temperature-dependent values. Temperatures are in Fahrenheit.
    Now includes autocorrelated noise in temperature.
    
    Parameters:
    - n_years: int, number of years to simulate
    - start_year: int, the year to start the datetime index
    
    Returns:
    - df: pandas DataFrame with a datetime index, 'value', and 'temperature' columns
    """
    n_days_per_year = 365
    n_hours_per_day = 24
    n_samples = n_years * n_days_per_year * n_hours_per_day

    time = np.arange(0, n_samples)

    # Seasonality components
    annual_cycle = -1.5* np.cos(2 * np.pi * time / (n_days_per_year * n_hours_per_day))
    weekly_cycle = -2 * np.cos(2 * np.pi * time / (7 * n_hours_per_day))
    daily_cycle = -2 * np.cos(2 * np.pi * time / n_hours_per_day)

    # Generate temperature data (in Fahrenheit)
    base_temp = 59  # Base temperature in Fahrenheit (equivalent to 15°C)
    temp_annual_variation = 18 * annual_cycle  # ±18°F variation annually
    temp_daily_variation = 9 * daily_cycle  # ±9°F variation daily
    
    # Generate autocorrelated noise
    phi = 0.9  # Autocorrelation coefficient
    epsilon = np.random.normal(0, 1, n_samples)
    temp_noise = np.zeros(n_samples)
    temp_noise[0] = epsilon[0]
    for t in range(1, n_samples):
        temp_noise[t] = phi * temp_noise[t-1] + epsilon[t]
    
    # Scale the noise to have a standard deviation of 3.6°F
    temp_noise = 3.6 * (temp_noise - temp_noise.mean()) / temp_noise.std()
    
    temperature = base_temp + temp_annual_variation + temp_daily_variation + temp_noise

    # Generate value data
    trend = 0.0002 * time
    seasonality =  0.5 * weekly_cycle + daily_cycle
    
    # Temperature effect on value (U-shaped)
    temp_effect = 0.01 * (temperature - 59)**2  # Centered at 59°F (15°C)
    
    # Combine components
    data = trend + seasonality + temp_effect

    # Create a datetime index
    date_range = pd.date_range(f'{start_year}-01-01', periods=n_samples, freq='H')

    # Create a DataFrame
    df = pd.DataFrame({
        'value': data,
        'temperature': temperature
    }, index=date_range)
    
    return df


def plot_dummy_data(df):
    # Create subplots
    fig, axs = plt.subplots(1, 4, figsize=(12, 5))
    fig.suptitle('Seasonality in Dummy Data', fontsize=16)

    # Year plot
    df.groupby('year')['value'].mean().plot(ax=axs[0])
    axs[0].set_title('Yearly Trend')
    axs[0].set_xlabel('Year')

    # Month plot
    df.groupby('month')['value'].mean().plot(ax=axs[1])
    axs[1].set_title('Monthly Seasonality')
    axs[1].set_xlabel('Month')

    # Day of week plot
    df.groupby('day_of_week')['value'].mean().plot(ax=axs[2])
    axs[2].set_title('Weekly Seasonality')
    axs[2].set_xlabel('Day of Week')

    # Hour of day plot
    df.groupby('hour_of_day')['value'].mean().plot(ax=axs[3])
    axs[3].set_title('Daily Seasonality')
    axs[3].set_xlabel('Hour of Day')

    for ax in axs:
        ax.set_ylabel('Average Value')
        ax.set_ylim(0)
        ax.grid()

    plt.tight_layout()

def plot_emulation_process_diagram():
    # Create a directed graph
    G = nx.DiGraph()

    # Add nodes
    nodes = [
        "Input\n(X)",
        "Expensive\nModel",
        "Synthetic\nData\n(y)",
        "Training\nData\n(X, y\npairs)",
        "Machine\nLearning\nModel\nTraining",
        "Diagnostic\nOutput",
        "New\nInput\n(X_new)",
        "Trained\nMachine\nLearning\nModel",
        "Fast\nApproximation\n(y_new_approx)"
    ]
    G.add_nodes_from(nodes)

    # Define positions for each node
    pos = {
        "Input\n(X)": (0, 0),
        "Expensive\nModel": (1, 0),
        "Synthetic\nData\n(y)": (2, 0),
        "Training\nData\n(X, y\npairs)": (0, -1),
        "Machine\nLearning\nModel\nTraining": (1, -1),
        "Diagnostic\nOutput": (2, -1),
        "New\nInput\n(X_new)": (0, -2),
        "Trained\nMachine\nLearning\nModel": (1, -2),
        "Fast\nApproximation\n(y_new_approx)": (2, -2),
    }

    # Add edges
    edges = [
        ("Input\n(X)", "Expensive\nModel"),
        ("Expensive\nModel", "Synthetic\nData\n(y)"),
        ("Input\n(X)", "Training\nData\n(X, y\npairs)"),
        ("Synthetic\nData\n(y)", "Training\nData\n(X, y\npairs)"),
        ("Training\nData\n(X, y\npairs)", "Machine\nLearning\nModel\nTraining"),
        ("Machine\nLearning\nModel\nTraining", "Diagnostic\nOutput"),
        ("Machine\nLearning\nModel\nTraining", "Trained\nMachine\nLearning\nModel"),
        ("New\nInput\n(X_new)", "Trained\nMachine\nLearning\nModel"),
        ("Trained\nMachine\nLearning\nModel", "Fast\nApproximation\n(y_new_approx)")
    ]
    G.add_edges_from(edges)

    # Set up the plot
    plt.figure(figsize=(8, 6))

    # Draw the graph
    nx.draw(G, pos, with_labels=True, node_color='lightblue', 
            node_size=5000, font_size=8, font_weight='bold', 
            arrows=True, arrowsize=20, edge_color='gray', node_shape='o')

    # Add a title
    plt.title("Emulation Modeling Process", fontsize=16, fontweight='bold')

    # Show the plot
    plt.tight_layout()