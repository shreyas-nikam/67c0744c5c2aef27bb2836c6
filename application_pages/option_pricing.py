
import streamlit as st
import plotly.graph_objects as go
import numpy as np
from scipy.stats import norm

def black_scholes_call(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)

def black_scholes_put(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

def run_option_pricing():
    st.header("Option Pricing with Black-Scholes Model")
    
    st.markdown("""
    This page demonstrates option pricing using the Black-Scholes model, which assumes that the underlying asset follows
    Geometric Brownian Motion (GBM). You can calculate both call and put option prices and visualize how they change
    with respect to the underlying asset price.
    
    The Black-Scholes formula for a European call option is:
    
    $$C = SN(d_1) - Ke^{-rT}N(d_2)$$
    
    And for a European put option:
    
    $$P = Ke^{-rT}N(-d_2) - SN(-d_1)$$
    
    Where:
    - $C$ is the call option price
    - $P$ is the put option price
    - $S$ is the current stock price
    - $K$ is the strike price
    - $r$ is the risk-free interest rate
    - $T$ is the time to maturity
    - $N(.)$ is the cumulative standard normal distribution function
    - $d_1 = \frac{\ln(S/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}}$
    - $d_2 = d_1 - \sigma\sqrt{T}$
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        S = st.number_input("Current stock price (S)", min_value=1.0, value=100.0, step=1.0)
        K = st.number_input("Strike price (K)", min_value=1.0, value=100.0, step=1.0)
        T = st.number_input("Time to maturity (T) in years", min_value=0.1, max_value=10.0, value=1.0, step=0.1)
    
    with col2:
        r = st.number_input("Risk-free rate (r)", min_value=0.0, max_value=0.2, value=0.05, step=0.01)
        sigma = st.number_input("Volatility (σ)", min_value=0.01, max_value=1.0, value=0.2, step=0.01)
    
    call_price = black_scholes_call(S, K, T, r, sigma)
    put_price = black_scholes_put(S, K, T, r, sigma)
    
    st.markdown(f"### Option Prices")
    st.write(f"Call Option Price: ${call_price:.2f}")
    st.write(f"Put Option Price: ${put_price:.2f}")
    
    # Create a range of stock prices to plot option values
    stock_prices = np.linspace(max(0, S - 50), S + 50, 100)
    call_values = [black_scholes_call(s, K, T, r, sigma) for s in stock_prices]
    put_values = [black_scholes_put(s, K, T, r, sigma) for s in stock_prices]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=stock_prices, y=call_values, mode='lines', name='Call Option'))
    fig.add_trace(go.Scatter(x=stock_prices, y=put_values, mode='lines', name='Put Option'))
    fig.add_trace(go.Scatter(x=[S, S], y=[0, max(max(call_values), max(put_values))], mode='lines', name='Current Stock Price', line=dict(dash='dash')))
    
    fig.update_layout(
        title="Option Values vs. Stock Price",
        xaxis_title="Stock Price",
        yaxis_title="Option Value",
        legend_title="Option Type"
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    ### Interpretation
    - The graph shows how call and put option values change with the underlying stock price.
    - Call options increase in value as the stock price increases, while put options decrease.
    - The dashed line represents the current stock price.
    - Options are more valuable when they are "in the money" (stock price > strike price for calls, stock price < strike price for puts).
    - Higher volatility (σ) generally increases option prices due to greater uncertainty.
    - Longer time to maturity (T) typically increases option values due to more time for favorable price movements.
    """)
