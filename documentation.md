id: 67c0744c5c2aef27bb2836c6_documentation
summary: Lab 67c0744c5c2aef27bb2836c6 Documentation
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# QuLab: Exploring Geometric Brownian Motion and Option Pricing

This codelab will guide you through the QuLab application, which focuses on Geometric Brownian Motion (GBM) and its applications in financial modeling, particularly option pricing. GBM is a fundamental concept for modeling stock prices and other financial instruments. Understanding GBM is crucial for anyone working in quantitative finance, risk management, or investment analysis.

This application allows you to:

*   Simulate GBM paths with different parameters.
*   Visualize the impact of drift and volatility on stock price movements.
*   Analyze and compare different parameter sets.
*   Price European call and put options using the Black-Scholes model.

This codelab will walk you through each feature, explaining the underlying concepts and how to use the application effectively. By the end of this codelab, you should have a solid understanding of GBM and its applications.

## Setting up the Environment

Duration: 00:05

Before you begin, ensure you have the following:

*   Python 3.6 or higher installed.
*   Streamlit installed (`pip install streamlit`).
*   Plotly installed (`pip install plotly`).
*   Numpy installed (`pip install numpy`).
*   Scipy installed (`pip install scipy`)

Create a directory for your project, and save the provided `app.py` and the `application_pages` directory containing `gbm_simulation.py`, `parameter_analysis.py`, and `option_pricing.py` into that directory.

## Running the Application

Duration: 00:02

To run the application, navigate to the project directory in your terminal and execute the following command:

```console
streamlit run app.py
```

This will open the application in your web browser.

## Understanding the Main Application (`app.py`)

Duration: 00:05

The `app.py` file serves as the main entry point for the Streamlit application. Let's break down its key components:

```python
import streamlit as st
import plotly.graph_objects as go
import numpy as np

st.set_page_config(page_title="QuLab", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab")
st.divider()

st.markdown("""
In this lab, we will explore the concept of Geometric Brownian Motion (GBM) and its application in financial modeling. 
GBM is a continuous-time stochastic process widely used to model stock prices and other financial instruments.

The Geometric Brownian Motion is defined by the following stochastic differential equation:

$$dS_t = \mu S_t dt + \sigma S_t dW_t$$

Where:
- $S_t$ is the stock price at time $t$
- $\mu$ is the drift (expected return)
- $\sigma$ is the volatility
- $dW_t$ is a Wiener process (standard Brownian motion)

We'll simulate GBM paths, visualize them, and analyze their properties across different pages of this application.
""")

# Your code starts here
page = st.sidebar.selectbox(label="Navigation", options=["GBM Simulation", "Parameter Analysis", "Option Pricing"])

if page == "GBM Simulation":
    from application_pages.gbm_simulation import run_gbm_simulation
    run_gbm_simulation()
elif page == "Parameter Analysis":
    from application_pages.parameter_analysis import run_parameter_analysis
    run_parameter_analysis()
elif page == "Option Pricing":
    from application_pages.option_pricing import run_option_pricing
    run_option_pricing()
# Your code ends

st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity. "
           "This lab was generated using the QuCreate platform. QuCreate relies on AI models for generating code, which may contain inaccuracies or errors")
```

*   **Imports:** The code begins by importing necessary libraries: `streamlit` for creating the user interface, `plotly.graph_objects` for plotting, and `numpy` for numerical computations.
*   **Page Configuration:** `st.set_page_config` sets the page title and layout.
*   **Sidebar and Title:** The code adds an image to the sidebar and sets the title of the application.
*   **Introduction:** A markdown section provides a brief introduction to Geometric Brownian Motion (GBM) and its significance.  The mathematical formula for GBM is presented.
*   **Navigation:** A `st.sidebar.selectbox` creates a navigation menu in the sidebar, allowing users to choose between different sections: "GBM Simulation", "Parameter Analysis", and "Option Pricing".
*   **Page Routing:**  Based on the selected page, the corresponding function from the `application_pages` directory is called. For example, if "GBM Simulation" is selected, the `run_gbm_simulation()` function from `application_pages/gbm_simulation.py` is executed.
*   **Footer:** A footer with copyright information and a disclaimer is added to the bottom of the page.

## GBM Simulation Page (`gbm_simulation.py`)

Duration: 00:15

This page allows users to simulate and visualize GBM paths.

```python
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
```

*   **`simulate_gbm` function:**
    *   Takes initial stock price (`S0`), drift (`mu`), volatility (`sigma`), time horizon (`T`), time step (`dt`), and the number of simulations (`num_simulations`) as inputs.
    *   Calculates the number of steps based on `T` and `dt`.
    *   Creates a time grid using `np.linspace`.
    *   Generates random increments (`dW`) from a normal distribution, representing the Wiener process.
    *   Simulates the GBM paths using the following formula:
        ```
        S[:, t] = S[:, t-1] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * dW[:, t])
        ```
    *   Returns the time grid and the simulated stock prices.
*   **`run_gbm_simulation` function:**
    *   Sets the header for the page.
    *   Provides a description of the page.
    *   Creates two columns using `st.columns` to arrange input widgets.
    *   **Input Widgets:**  Uses `st.number_input` to allow users to set the following parameters:
        *   `S0`: Initial stock price.
        *   `mu`: Drift (expected return).
        *   `sigma`: Volatility.
        *   `T`: Time horizon in years.
        *   `dt`: Time step.
        *   `num_simulations`: Number of simulation paths to generate.
    *   Calls the `simulate_gbm` function with the user-defined parameters.
    *   **Plotting:** Creates a Plotly figure (`go.Figure`) and adds each simulation path as a separate trace.
    *   **Layout:** Updates the layout of the plot with a title and axis labels.
    *   **Display:** Displays the plot using `st.plotly_chart`.
    *   **Interpretation:** Provides a markdown section explaining the interpretation of the simulation results.

## Parameter Analysis Page (`parameter_analysis.py`)

Duration: 00:15

This page allows users to compare the effects of different parameter sets on GBM simulations.

```python
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
```

*   **`simulate_gbm` function:** (Same as in `gbm_simulation.py`)
*   **`run_parameter_analysis` function:**
    *   Sets the header and description.
    *   Creates three columns using `st.columns` for input widgets.
    *   **Input Widgets:**
        *   `col1`: `S0`, `T`, and `dt` (shared parameters for both sets).
        *   `col2`: `mu1` and `sigma1` (drift and volatility for the first parameter set).
        *   `col3`: `mu2` and `sigma2` (drift and volatility for the second parameter set).
        *   `num_simulations`: Number of simulations per parameter set.
    *   Calls the `simulate_gbm` function twice, once for each parameter set.
    *   **Plotting:** Creates a Plotly figure and adds the simulation paths for both sets, using different colors (blue and red) for differentiation.  The opacity is set to 0.3 to allow for easier visual distinction when paths overlap.
    *   **Layout:**  Updates the layout with a title, axis labels, and disables the legend to reduce clutter.
    *   **Display:** Displays the plot using `st.plotly_chart`.
    *   **Interpretation:** Provides a markdown section explaining the interpretation of the results, highlighting the impact of drift and volatility on the stock price paths.

## Option Pricing Page (`option_pricing.py`)

Duration: 00:20

This page implements the Black-Scholes model for pricing European call and put options.

```python
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
```

*   **`black_scholes_call` function:**
    *   Implements the Black-Scholes formula for a European call option.
    *   Takes the current stock price (`S`), strike price (`K`), time to maturity (`T`), risk-free rate (`r`), and volatility (`sigma`) as inputs.
    *   Calculates `d1` and `d2` as intermediate variables.
    *   Uses `scipy.stats.norm.cdf` to calculate the cumulative standard normal distribution function.
    *   Returns the call option price.
*   **`black_scholes_put` function:**
    *   Implements the Black-Scholes formula for a European put option.
    *   Takes the same inputs as the `black_scholes_call` function.
    *   Calculates `d1` and `d2` as intermediate variables.
    *   Uses `scipy.stats.norm.cdf` to calculate the cumulative standard normal distribution function.
    *   Returns the put option price.
*   **`run_option_pricing` function:**
    *   Sets the header and description, including the Black-Scholes formulas.
    *   Creates two columns using `st.columns` for input widgets.
    *   **Input Widgets:**
        *   `col1`: `S`, `K`, and `T`.
        *   `col2`: `r` and `sigma`.
    *   Calculates the call and put option prices using the `black_scholes_call` and `black_scholes_put` functions.
    *   **Output:** Displays the calculated option prices using `st.write`.
    *   **Plotting:**
        *   Creates a range of stock prices using `np.linspace`.
        *   Calculates the call and put option values for each stock price in the range.
        *   Creates a Plotly figure and adds traces for the call and put option values.
        *   Adds a vertical dashed line to indicate the current stock price.
    *   **Layout:** Updates the layout with a title, axis labels, and legend.
    *   **Display:** Displays the plot using `st.plotly_chart`.
    *   **Interpretation:** Provides a markdown section explaining the interpretation of the graph and the factors affecting option prices.

## Application Architecture

Duration: 00:05

Here's a simple diagram illustrating the application's architecture:

```
++    ++    +-+
|       app.py        |    | application_pages/gbm_simulation.py  |    | application_pages/parameter_analysis.py |
|  (Main Application) |    | (GBM Simulation Logic & UI)           |    | (Parameter Analysis Logic & UI)          |
++--+    ++    +-+
          |                calls                                        calls
          |
          |                +-+
          |                | application_pages/option_pricing.py |
          |                | (Option Pricing Logic & UI)          |
          |                +-+
          |                      uses
          |       +-+
          |       |         Plotly & Streamlit          |
          +->(Visualization and UI Frameworks)
                  +-+
```

*   `app.py`: The main script that orchestrates the application. It handles navigation and calls the appropriate modules based on user selection.
*   `application_pages`:  A directory containing modules for each specific functionality (GBM Simulation, Parameter Analysis, Option Pricing).  Each module is responsible for both the logic and the UI elements for its respective page.
*   Plotly & Streamlit: These frameworks provide the necessary tools for creating interactive visualizations and a user-friendly web interface.  Streamlit is used for building the UI and handling user input, while Plotly is used for generating the charts and graphs.

## Extending the Application

Duration: 00:10

Here are some ideas for extending this application:

*   **More Option Pricing Models:** Implement other option pricing models, such as the Binomial Tree model.
*   **Volatility Smiles:** Add functionality to visualize and analyze volatility smiles.
*   **Interactive Risk Analysis:** Allow users to perform interactive risk analysis by simulating portfolio performance under different scenarios.
*   **Backtesting:** Integrate historical data and backtesting capabilities.
*   **Advanced Charting:** Incorporate more advanced charting options, such as candlestick charts.

<aside class="positive">
This application provides a solid foundation for exploring financial modeling concepts. Feel free to experiment with the code and add new features to enhance its functionality.
</aside>

## Conclusion

Duration: 00:03

This codelab provided a comprehensive guide to the QuLab application, covering Geometric Brownian Motion simulation, parameter analysis, and option pricing using the Black-Scholes model. By understanding the code and experimenting with different parameters, you can gain valuable insights into the behavior of financial markets and the principles of quantitative finance. This application can serve as a powerful tool for learning, research, and development in the field of financial modeling.
