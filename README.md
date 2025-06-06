# MARKOVITZ

This repository contains a simple implementation of a Markowitz portfolio simulation.
The original notebook was converted into a standalone Python module located at
`markovitz.py`.

## Usage

1. Install the required packages:
   ```bash
   pip install numpy pandas matplotlib yfinance scipy
   ```

2. Run the script:
   ```bash
   python markovitz.py
   ```

The script downloads historical prices for a list of Argentine tickers, generates
random portfolios, highlights the minimum variance portfolio and plots the
results.
