
import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy import stats

def run_poisson_distribution():
    st.header("Poisson Distribution")
    
    st.markdown('''
    The Poisson Distribution is a discrete probability distribution that expresses the probability of a given number of events occurring in a fixed interval of time or space, assuming these events occur with a known constant mean rate and independently of the time since the last event. It is characterized by one parameter:
    
    $\lambda$ (lambda): The average number of events per interval
    
    The probability mass function (PMF) of the Poisson distribution is given by:
    
    $$P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}$$
    
    Where:
    - $k$ is the number of occurrences
    - $e$ is the base of the natural logarithm
    
    Let's explore how changing the lambda parameter affects the shape of the distribution!
    ''')
    
    lambda_param = st.slider("Average number of events (λ)", 0.1, 20.0, 5.0, 0.1)
    
    x = np.arange(0, int(lambda_param * 3) + 1)  # Adjust range based on lambda
    y = stats.poisson.pmf(x, lambda_param)
    
    fig = go.Figure()
    fig.add_trace(go.Bar(x=x, y=y, name='PMF'))
    fig.update_layout(
        title='Poisson Distribution PMF',
        xaxis_title='Number of Events',
        yaxis_title='Probability',
        showlegend=True
    )
    
    st.plotly_chart(fig)
    
    st.markdown('''
    ### Observations:
    
    1. The distribution is discrete, taking only non-negative integer values.
    2. As λ increases, the distribution becomes more symmetric and approaches a normal distribution.
    3. For small values of λ, the distribution is skewed to the right.
    4. The peak of the distribution occurs near the value of λ.
    
    ### Properties of the Poisson Distribution:
    
    1. Mean (Expected value): $E(X) = \lambda$
    2. Variance: $Var(X) = \lambda$
    3. Standard Deviation: $\sigma = \sqrt{\lambda}$
    
    The Poisson distribution has the unique property that its mean and variance are equal.
    ''')
    
    # Calculate probabilities
    k = st.number_input("Enter a number of events (k) to calculate probabilities:", min_value=0, value=min(5, int(lambda_param)), step=1)
    
    exact_prob = stats.poisson.pmf(k, lambda_param)
    less_than_prob = stats.poisson.cdf(k, lambda_param)
    greater_than_prob = 1 - stats.poisson.cdf(k-1, lambda_param)
    
    st.write(f"Probability of exactly {k} events: {exact_prob:.4f}")
    st.write(f"Probability of {k} or fewer events: {less_than_prob:.4f}")
    st.write(f"Probability of more than {k} events: {greater_than_prob:.4f}")

    st.markdown(f'''
    ### Summary Statistics:
    
    - Mean: {lambda_param:.2f}
    - Variance: {lambda_param:.2f}
    - Standard Deviation: {np.sqrt(lambda_param):.2f}
    ''')
    
    st.markdown('''
    ### Applications of the Poisson Distribution:
    
    1. Modeling rare events: Number of car accidents, natural disasters, or defects in manufacturing.
    2. Queueing theory: Arrivals at a service center or calls to a help desk.
    3. Biology: Number of mutations in a given DNA sequence or cell divisions in a time interval.
    4. Finance: Number of trades in a given time period or defaults in a loan portfolio.
    
    The Poisson distribution is particularly useful when dealing with counts of events over time or space, especially when these events are rare and independent.
    ''')
