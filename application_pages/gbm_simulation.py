
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

def run_gbm_simulation():
    st.header("Geometric Brownian Motion Simulation")
    
    st.markdown("""
    This page allows you to simulate and visualize Geometric Brownian Motion (GBM) paths.
    Adjust the parameters below to see how they affect the simulated stock price paths.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        S0 = st.number_input("Initial stock price (S0)", min_value=1.0, value=100.0, step=1.0)
        mu = st.number_input("Drift (μ)", min_value=-1.0, max_value=1.0, value=0.05, step=0.01)
        sigma = st.number_input("Volatility (σ)", min_value=0.01, max_value=1.0, value=0.2, step=0.01)
    
    with col2:
        T = st.number_input("Time horizon (T) in years", min_value=0.1, max_value=10.0, value=1.0, step=0.1)
        dt = st.number_input("Time step (dt)", min_value=0.001, max_value=0.1, value=0.01, step=0.001)
        num_simulations = st.number_input("Number of simulations", min_value=1, max_value=1000, value=10, step=1)
    
    time_grid, S = simulate_gbm(S0, mu, sigma, T, dt, num_simulations)
    
    fig = go.Figure()
    for i in range(num_simulations):
        fig.add_trace(go.Scatter(x=time_grid, y=S[i, :], mode='lines', name=f'Simulation {i+1}'))
    
    fig.update_layout(
        title="Geometric Brownian Motion Simulations",
        xaxis_title="Time",
        yaxis_title="Stock Price",
        legend_title="Simulations"
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    ### Interpretation
    - Each line represents a possible path for the stock price over time.
    - The spread of the paths shows the uncertainty in future stock prices.
    - Higher volatility (σ) leads to wider spread of possible outcomes.
    - The drift (μ) influences the overall trend of the paths.
    """)
