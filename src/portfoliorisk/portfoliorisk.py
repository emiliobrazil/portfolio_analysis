import datetime
import numpy as np
import pandas as pd
import yfinance as yf

# May need adaptations according to the format received by finance and management portfolios libs

def portfolio_expected_return (portfolio, period, num_trials=10000):
    """
    Receives a portfolio and a period of time.
    Returns an approximation of the expected value using a Monte Carlo simulation.
    """
    # data = something something from finance lib
    df = pd.DataFrame(data)
    returns = df.pct_change().dropna() # convert into percentage and drop rows with missing values
    returns_covariance_matrix = returns.cov()
    returns_means = returns.mean()

    assets_values_at_last_date = df.iloc[-1:].to_numpy() # get the most recent values for each asset
    asset_weights = np.array([asset[1] for asset in portfolio])
    asset_weights = asset_weights / asset_weights.sum()
    portfolio_value_at_last_date = assets_values_at_last_date * asset_weights

    portfolio_returns = np.zeros(num_trials)
    num_assets = len(portfolio)

    for idx in range(num_trials):
        simulated_portfolio_values = portfolio_value_at_last_date
        for day in range(period):
            simulated_variations = np.random.multivariate_normal(returns_means, returns_covariance_matrix)
            simulated_portfolio_values *= simulated_variations
        simulated_return = simulated_portfolio_values.sum()
        portfolio_returns[idx] = simulated_return
    
    return np.mean(portfolio_returns)
