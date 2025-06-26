
import streamlit as st
import plotly.graph_objects as go
import numpy as np

st.set_page_config(page_title="QuLab", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab")
st.divider()

st.markdown('''
# Exploring Probability Distributions

In this lab, we will explore various probability distributions and their properties. We'll focus on the following distributions:

1. Normal Distribution
2. Binomial Distribution
3. Poisson Distribution

We'll visualize these distributions, calculate probabilities, and explore how changing parameters affects their shapes and properties.

## Key Concepts

- **Probability Density Function (PDF)**: A function that describes the relative likelihood for a continuous random variable to take on a given value.
- **Cumulative Distribution Function (CDF)**: A function that gives the probability that a random variable is less than or equal to a certain value.
- **Parameters**: Values that define the shape and behavior of a distribution (e.g., mean and standard deviation for the normal distribution).

Let's explore each distribution in detail and see how they behave under different conditions!
''')

# Your code starts here
page = st.sidebar.selectbox(label="Navigation", options=["Normal Distribution", "Binomial Distribution", "Poisson Distribution"])

if page == "Normal Distribution":
    from application_pages.normal_distribution import run_normal_distribution
    run_normal_distribution()
elif page == "Binomial Distribution":
    from application_pages.binomial_distribution import run_binomial_distribution
    run_binomial_distribution()
elif page == "Poisson Distribution":
    from application_pages.poisson_distribution import run_poisson_distribution
    run_poisson_distribution()
# Your code ends

st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity. "
           "This lab was generated using the QuCreate platform. QuCreate relies on AI models for generating code, which may contain inaccuracies or errors")
