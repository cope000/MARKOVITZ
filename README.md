# Markowitz Portfolio Optimization Notebook

This repository contains a single Jupyter notebook titled `Tesis_ALAN_TOMAS_ARELLANO (Versión 18-04) OK (3).ipynb`.
The notebook demonstrates portfolio construction using the Markowitz mean-variance framework. It downloads financial
data with **yfinance**, calculates returns and risk metrics using **pandas** and **numpy**, and uses **scipy** to compute
an efficient frontier. Visualizations are generated with **matplotlib** and **seaborn**.

## Requirements

- Python 3.8 or later
- `yfinance`
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scipy`
- `jupyter` (to run the notebook)

Install these packages with `pip`:

```bash
pip install yfinance pandas numpy matplotlib seaborn scipy jupyter
```

## Running the notebook

1. Make sure the dependencies above are installed in your Python environment.
2. Launch Jupyter from the repository directory:

```bash
jupyter notebook
```

3. Open `Tesis_ALAN_TOMAS_ARELLANO (Versión 18-04) OK (3).ipynb` in your browser and run the cells in order.

## Setting up a Python environment

If you do not already have a Python environment prepared, you can create one using `venv`:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install yfinance pandas numpy matplotlib seaborn scipy jupyter
```

Once activated and dependencies installed, you can run the notebook as described above.
