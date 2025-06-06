"""Markowitz portfolio analysis utilities."""

from dataclasses import dataclass
from typing import List, Tuple

import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from scipy.optimize import minimize


@dataclass
class PortfolioResult:
    return_: float
    risk: float
    weights: np.ndarray


def download_data(tickers: List[str], start: str, end: str) -> pd.DataFrame:
    """Download adjusted close prices for a list of tickers."""
    data = yf.download(tickers, start=start, end=end, auto_adjust=False, progress=False)
    return data["Adj Close"].dropna(how="all")


def calculate_returns(prices: pd.DataFrame) -> pd.DataFrame:
    """Compute daily percentage returns."""
    return prices.pct_change().dropna()


def simulate_random_portfolios(returns: pd.DataFrame, num_portfolios: int) -> Tuple[pd.DataFrame, List[np.ndarray]]:
    """Generate random portfolios and return statistics."""
    results = []
    weights_list = []
    mean_returns = returns.mean() * 252
    cov = returns.cov() * 252

    for _ in range(num_portfolios):
        weights = np.random.random(len(mean_returns))
        weights /= np.sum(weights)
        weights_list.append(weights)

        port_return = np.dot(weights, mean_returns)
        port_risk = np.sqrt(np.dot(weights.T, np.dot(cov, weights)))
        results.append((port_return, port_risk))

    df = pd.DataFrame(results, columns=["Return", "Risk"])
    return df, weights_list


def min_variance_portfolio(results: pd.DataFrame, weights_list: List[np.ndarray]) -> PortfolioResult:
    """Return the minimum variance portfolio from simulation results."""
    idx = results["Risk"].idxmin()
    return PortfolioResult(return_=results.loc[idx, "Return"], risk=results.loc[idx, "Risk"], weights=weights_list[idx])


def plot_efficient_frontier(results: pd.DataFrame, min_port: PortfolioResult) -> None:
    """Plot the efficient frontier and highlight the minimum variance portfolio."""
    plt.figure(figsize=(10, 6))
    plt.scatter(results["Risk"], results["Return"], c=results["Return"], cmap="viridis", alpha=0.5)
    plt.scatter(min_port.risk, min_port.return_, color="red", marker="*", s=200, label="Min Variance")
    plt.xlabel("Volatility")
    plt.ylabel("Expected Return")
    plt.title("Efficient Frontier")
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_portfolio_weights(tickers: List[str], weights: np.ndarray) -> None:
    """Plot a pie chart of portfolio weights."""
    plt.figure(figsize=(8, 8))
    plt.pie(weights, labels=tickers, autopct="%1.1f%%", startangle=90)
    plt.axis("equal")
    plt.title("Minimum Variance Portfolio Composition")
    plt.show()


# Example usage
if __name__ == "__main__":
    TICKERS = [
        "ALUA.BA", "BBAR.BA", "BMA.BA", "BYMA.BA", "CECO2.BA",
        "CEPU.BA", "COME.BA", "CRES.BA", "CVH.BA", "EDN.BA",
        "GGAL.BA", "LOMA.BA", "MIRG.BA", "PAMP.BA", "SUPV.BA",
        "TECO2.BA", "TGNO4.BA", "TGSU2.BA", "TRAN.BA", "VALO.BA",
        "YPFD.BA",
    ]

    prices = download_data(TICKERS, start="2018-01-01", end="2022-12-31")
    returns = calculate_returns(prices)

    simulations, weight_list = simulate_random_portfolios(returns, num_portfolios=5000)
    min_port = min_variance_portfolio(simulations, weight_list)

    print("Minimum variance portfolio:")
    print("Return:", min_port.return_)
    print("Risk:", min_port.risk)
    print("Weights:")
    for t, w in zip(TICKERS, min_port.weights):
        print(f"  {t}: {w:.2%}")

    plot_efficient_frontier(simulations, min_port)
    plot_portfolio_weights(TICKERS, min_port.weights)
