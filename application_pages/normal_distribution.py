
import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy import stats

def run_normal_distribution():
    st.header("Normal Distribution")
    
    st.markdown('''
    The Normal Distribution, also known as the Gaussian distribution, is a continuous probability distribution that is symmetric about the mean. It is characterized by two parameters:
    
    1. $\mu$ (mu): The mean of the distribution
    2. $\sigma$ (sigma): The standard deviation of the distribution
    
    The probability density function (PDF) of the normal distribution is given by:
    
    $$f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{1}{2}(\frac{x-\mu}{\sigma})^2}$$
    
    Where:
    - $x$ is the random variable
    - $e$ is the base of the natural logarithm
    - $\pi$ is the mathematical constant pi
    
    Let's explore how changing these parameters affects the shape of the distribution!
    ''')
    
    col1, col2 = st.columns(2)
    
    with col1:
        mu = st.slider("Mean (μ)", -5.0, 5.0, 0.0, 0.1)
    with col2:
        sigma = st.slider("Standard Deviation (σ)", 0.1, 5.0, 1.0, 0.1)
    
    x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
    y = stats.norm.pdf(x, mu, sigma)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='PDF'))
    fig.update_layout(
        title='Normal Distribution PDF',
        xaxis_title='x',
        yaxis_title='Probability Density',
        showlegend=True
    )
    
    st.plotly_chart(fig)
    
    st.markdown('''
    ### Observations:
    
    1. The peak of the distribution is at the mean (μ).
    2. The curve is symmetric around the mean.
    3. Increasing σ makes the distribution wider and flatter.
    4. Decreasing σ makes the distribution narrower and taller.
    5. Changing μ shifts the entire distribution left or right.
    
    ### Properties of the Normal Distribution:
    
    1. About 68% of the data falls within one standard deviation of the mean.
    2. About 95% of the data falls within two standard deviations of the mean.
    3. About 99.7% of the data falls within three standard deviations of the mean.
    
    This is known as the "68-95-99.7 rule" or the "empirical rule".
    ''')
    
    # Calculate probabilities
    z_score = st.number_input("Enter a z-score to calculate probabilities:", value=1.0, step=0.1)
    
    less_than_prob = stats.norm.cdf(z_score)
    greater_than_prob = 1 - less_than_prob
    
    st.write(f"Probability of a value less than {z_score} standard deviations from the mean: {less_than_prob:.4f}")
    st.write(f"Probability of a value greater than {z_score} standard deviations from the mean: {greater_than_prob:.4f}")

