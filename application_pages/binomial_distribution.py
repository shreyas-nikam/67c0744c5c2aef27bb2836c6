
import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy import stats

def run_binomial_distribution():
    st.header("Binomial Distribution")
    
    st.markdown('''
    The Binomial Distribution is a discrete probability distribution that models the number of successes in a fixed number of independent Bernoulli trials. It is characterized by two parameters:
    
    1. $n$: The number of trials
    2. $p$: The probability of success on each trial
    
    The probability mass function (PMF) of the binomial distribution is given by:
    
    $$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$$
    
    Where:
    - $k$ is the number of successes
    - $\binom{n}{k}$ is the binomial coefficient ("n choose k")
    
    Let's explore how changing these parameters affects the shape of the distribution!
    ''')
    
    col1, col2 = st.columns(2)
    
    with col1:
        n = st.slider("Number of trials (n)", 1, 100, 20)
    with col2:
        p = st.slider("Probability of success (p)", 0.0, 1.0, 0.5, 0.01)
    
    x = np.arange(0, n+1)
    y = stats.binom.pmf(x, n, p)
    
    fig = go.Figure()
    fig.add_trace(go.Bar(x=x, y=y, name='PMF'))
    fig.update_layout(
        title='Binomial Distribution PMF',
        xaxis_title='Number of Successes',
        yaxis_title='Probability',
        showlegend=True
    )
    
    st.plotly_chart(fig)
    
    st.markdown('''
    ### Observations:
    
    1. The distribution is discrete, taking only integer values from 0 to n.
    2. When p = 0.5, the distribution is symmetric.
    3. When p < 0.5, the distribution is skewed to the right.
    4. When p > 0.5, the distribution is skewed to the left.
    5. As n increases, the distribution becomes more "bell-shaped" and approaches a normal distribution.
    
    ### Properties of the Binomial Distribution:
    
    1. Mean (Expected value): $E(X) = np$
    2. Variance: $Var(X) = np(1-p)$
    3. Standard Deviation: $\sigma = \sqrt{np(1-p)}$
    ''')
    
    # Calculate probabilities
    k = st.number_input("Enter a number of successes (k) to calculate probabilities:", min_value=0, max_value=n, value=min(10, n), step=1)
    
    exact_prob = stats.binom.pmf(k, n, p)
    less_than_prob = stats.binom.cdf(k, n, p)
    greater_than_prob = 1 - stats.binom.cdf(k-1, n, p)
    
    st.write(f"Probability of exactly {k} successes: {exact_prob:.4f}")
    st.write(f"Probability of {k} or fewer successes: {less_than_prob:.4f}")
    st.write(f"Probability of more than {k} successes: {greater_than_prob:.4f}")

    st.markdown(f'''
    ### Summary Statistics:
    
    - Mean: {n*p:.2f}
    - Variance: {n*p*(1-p):.2f}
    - Standard Deviation: {np.sqrt(n*p*(1-p)):.2f}
    ''')
