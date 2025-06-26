
# Geometric Brownian Motion (GBM) Simulation and Option Pricing

This Streamlit application demonstrates the concepts of Geometric Brownian Motion (GBM) and its application in financial modeling and option pricing. The app consists of three main components:

1. GBM Simulation
2. Parameter Analysis
3. Option Pricing with Black-Scholes Model

## Features

- Interactive GBM path simulation with adjustable parameters
- Comparison of GBM paths with different parameter sets
- Option pricing calculator using the Black-Scholes model
- Visualization of option values with respect to stock price

## Requirements

- Python 3.12
- Streamlit
- Plotly
- NumPy
- SciPy

## Installation and Running the App

1. Clone this repository:
   ```
   git clone https://github.com/your-username/gbm-option-pricing-app.git
   cd gbm-option-pricing-app
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

4. Open your web browser and go to `http://localhost:8501` to view the application.

## Docker Support

This application can also be run using Docker. To build and run the Docker container:

1. Build the Docker image:
   ```
   docker build -t gbm-option-pricing-app .
   ```

2. Run the Docker container:
   ```
   docker run -p 8501:8501 gbm-option-pricing-app
   ```

3. Open your web browser and go to `http://localhost:8501` to view the application.

## Usage

Navigate through the different pages using the sidebar to explore various aspects of Geometric Brownian Motion and option pricing:

- **GBM Simulation**: Adjust parameters to simulate and visualize GBM paths.
- **Parameter Analysis**: Compare GBM paths with different parameter sets side by side.
- **Option Pricing**: Calculate call and put option prices using the Black-Scholes model and visualize how they change with respect to the underlying asset price.

## License

This project is open-source and available under the MIT License.
