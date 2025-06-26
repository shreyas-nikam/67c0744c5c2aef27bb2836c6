
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
