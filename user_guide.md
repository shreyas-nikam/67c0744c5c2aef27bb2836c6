id: 67c0744c5c2aef27bb2836c6_user_guide
summary: Lab 67c0744c5c2aef27bb2836c6 User Guide
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# QuLab User Guide: Exploring Geometric Brownian Motion and Option Pricing

This codelab provides a comprehensive guide to using the QuLab application, designed to explore the concepts of Geometric Brownian Motion (GBM) and its application in financial modeling, specifically option pricing. GBM is a fundamental concept in finance used to model the random walk of asset prices over time.  This application allows you to simulate GBM paths, analyze the impact of different parameters, and price options using the Black-Scholes model.  This guide will walk you through each feature of the application, helping you understand how each parameter influences the results.

## Navigating the Application

Duration: 00:01

The application is divided into three main sections, accessible through the sidebar navigation:

*   **GBM Simulation:** This section allows you to simulate various paths of a stock price based on GBM parameters.
*   **Parameter Analysis:** This section allows you to compare two sets of GBM parameters side-by-side to visualize their impact on stock price paths.
*   **Option Pricing:** This section demonstrates the Black-Scholes option pricing model, a widely used method for valuing European options.

## GBM Simulation

Duration: 00:05

This section focuses on simulating the Geometric Brownian Motion (GBM) process. Here, you can visualize how different parameters influence potential stock price trajectories.

1.  **Initial Stock Price (S0):**  Enter the starting price of the stock. This is the price at time zero.
2.  **Drift (μ):**  This represents the average rate of return of the stock. A positive drift indicates an upward trend, while a negative drift indicates a downward trend.
3.  **Volatility (σ):** This represents the degree of price fluctuation. Higher volatility leads to more erratic price movements.
4.  **Time Horizon (T):**  This defines the length of time over which the simulation runs, expressed in years.
5.  **Time Step (dt):**  This represents the increment of time in each step of the simulation. A smaller time step leads to a smoother, more precise simulation, but requires more computation.
6.  **Number of Simulations:** This specifies the number of possible stock price paths that will be generated and displayed on the chart.

Once you have entered the desired parameters, the application will generate a plot displaying multiple GBM paths. Each line on the plot represents a possible trajectory for the stock price over the specified time horizon.  Observe how changes to the drift and volatility affect the overall shape and spread of the simulated paths.

<aside class="positive">
Experiment with different values for volatility (σ). Observe how higher volatility results in a wider range of potential stock prices at any given point in time. This reflects the increased uncertainty associated with more volatile assets.
</aside>

## Parameter Analysis

Duration: 00:07

This section allows you to directly compare the impact of different GBM parameters on simulated stock price paths. By adjusting parameters for two different sets, you can gain insights into their relative influence.

1.  **Initial Settings**: Set the Initial stock price, time horizon and time step. These parameters are shared between both simulation sets, in order to isolate the impact of Drift and Volatility.
2.  **Set 1 Parameters:** Define the `Drift (μ1)` and `Volatility (σ1)` for the first set of simulations.
3.  **Set 2 Parameters:** Define the `Drift (μ2)` and `Volatility (σ2)` for the second set of simulations.
4.  **Number of Simulations per set:** Specify the number of simulations to run for *each* parameter set.

The resulting plot will display two sets of GBM paths, distinguished by color (blue for Set 1, red for Set 2). By comparing the paths, you can directly observe the effects of different drift and volatility values. For instance, a higher drift will generally lead to paths trending upwards more steeply, while higher volatility will create a wider range of potential price outcomes.

<aside class="negative">
Be mindful of the time step (dt).  Extremely small time steps can significantly increase computation time, while excessively large time steps can lead to inaccurate simulations.
</aside>

## Option Pricing

Duration: 00:08

This section demonstrates the Black-Scholes model, a cornerstone of option pricing theory. Here, you can calculate the theoretical price of European call and put options.

1.  **Current Stock Price (S):**  Enter the current market price of the underlying asset.
2.  **Strike Price (K):**  Enter the price at which the option holder can buy (for a call option) or sell (for a put option) the underlying asset.
3.  **Time to Maturity (T):**  Enter the time remaining until the option expires, expressed in years.
4.  **Risk-Free Rate (r):**  Enter the rate of return on a risk-free investment, such as a government bond.
5.  **Volatility (σ):**  Enter the expected volatility of the underlying asset's price. This is a crucial input, often estimated from historical data or implied from market option prices.

Based on these inputs, the application calculates and displays the theoretical prices of both call and put options using the Black-Scholes formula.  The application also generates a plot showing how the values of call and put options change as the underlying stock price varies. The dashed line on the chart indicates the current stock price, and helps in visualizing the option's value "in the money", "at the money", and "out of the money."

<aside class="positive">
Understand the relationships between the inputs and the calculated option prices. For example, increasing volatility generally increases the prices of both call and put options, reflecting the increased uncertainty and potential for large price movements.
</aside>

<aside class="negative">
The Black-Scholes model has limitations. It assumes constant volatility, a risk-free interest rate, and no dividends. Keep in mind that real-world markets may deviate from these assumptions.
</aside>

By working through these sections, you should gain a better understanding of Geometric Brownian Motion, parameter sensitivity, and its application in option pricing using the Black-Scholes model.  This application is a powerful tool for exploring these fundamental concepts in quantitative finance.
