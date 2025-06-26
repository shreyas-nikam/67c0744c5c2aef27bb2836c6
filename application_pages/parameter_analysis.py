
import streamlit as st
import plotly.graph_objects as go
import numpy as np

def simulate_gbm(S0, mu, sigma, T, dt, num_simulations):
    num_steps = int(T / dt)
    time_grid = np.linspace(0, T, num_steps)
    dW = np.random.normal(0, np.sqrt(dt), (num_simulations, num_steps))
    
    S = np.zeros((num_simulations, num_steps))
    S[:, 0] = S0
    
    for t in range(1, num_steps):
        S[:, t] = S[:, t-1] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * dW[:, t])
    
    return time_grid, S

def run_parameter_analysis():
    st.header("Parameter Analysis")
    
    st.markdown("""
    This page allows you to analyze the impact of different parameters on the Geometric Brownian Motion (GBM) model.
    You can compare multiple parameter sets side by side to understand their effects on the stock price paths.
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        S0 = st.number_input("Initial stock price (S0)", min_value=1.0, value=100.0, step=1.0)
        T = st.number_input("Time horizon (T) in years", min_value=0.1, max_value=10.0, value=1.0, step=0.1)
        dt = st.number_input("Time step (dt)", min_value=0.001, max_value=0.1, value=0.01, step=0.001)
    
    with col2:
        mu1 = st.number_input("Drift 1 (μ1)", min_value=-1.0, max_value=1.0, value=0.05, step=0.01)
        sigma1 = st.number_input("Volatility 1 (σ1)", min_value=0.01, max_value=1.0, value=0.2, step=0.01)
    
    with col3:
        mu2 = st.number_input("Drift 2 (μ2)", min_value=-1.0, max_value=1.0, value=0.1, step=0.01)
        sigma2 = st.number_input("Volatility 2 (σ2)", min_value=0.01, max_value=1.0, value=0.3, step=0.01)
    
    num_simulations = st.number_input("Number of simulations per set", min_value=1, max_value=1000, value=50, step=1)
    
    time_grid, S1 = simulate_gbm(S0, mu1, sigma1, T, dt, num_simulations)
    _, S2 = simulate_gbm(S0, mu2, sigma2, T, dt, num_simulations)
    
    fig = go.Figure()
    
    for i in range(num_simulations):
        fig.add_trace(go.Scatter(x=time_grid, y=S1[i, :], mode='lines', name=f'Set 1 - Sim {i+1}',
                                 line=dict(color='blue', width=1), opacity=0.3))
        fig.add_trace(go.Scatter(x=time_grid, y=S2[i, :], mode='lines', name=f'Set 2 - Sim {i+1}',
                                 line=dict(color='red', width=1), opacity=0.3))
    
    fig.update_layout(
        title="Comparison of GBM Simulations with Different Parameters",
        xaxis_title="Time",
        yaxis_title="Stock Price",
        showlegend=False
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    ### Interpretation
    - Blue paths: Set 1 (μ1, σ1)
    - Red paths: Set 2 (μ2, σ2)
    
    Observe how changes in drift (μ) and volatility (σ) affect the behavior of the stock price paths:
    - Higher drift leads to a stronger upward trend in the paths.
    - Higher volatility results in wider spread and more extreme fluctuations in the paths.
    - The initial stock price (S0) sets the starting point for all paths.
    - The time horizon (T) determines how far into the future the simulation extends.
    """)
