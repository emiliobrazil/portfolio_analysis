import numpy as np
import scipy as sp
import pandas as pd

def compute_covariances_and_means (df):
    """
    Receives a data frame corresponding to an amount of periods and the portfolio.
    Returns an approximate covariance matrix of the portfolio
    and an array of the approximate expected value of each stock.
    """
    returns = df.pct_change().dropna() # convert into percentage and drop rows with missing values
    returns_covariance_matrix = returns.cov()
    returns_means = returns.mean()

    return returns_covariance_matrix, returns_means

def monte_carlo_simulation (portfolio, df, num_periods, file_path=None, num_trials=1000):
    """
    Receives a list corresponding to a portfolio, a data frame corresponding to an amount of periods
    and the portfolio, a file path to save the results of the simulation in npy and the number of trials
    for each period for the Monte Carlo simulation.
    Returns an array of simulated returns and the portfolio in list format.
    """
    returns_covariance_matrix, returns_means = compute_covariances_and_means(df)
    assets_values_at_last_date = df.iloc[-1:].to_numpy() # get the most recent values for each asset
    asset_weights = np.array([asset[1] for asset in portfolio])
    portfolio_value_at_last_date = assets_values_at_last_date * asset_weights

    simulated_returns = np.zeros((num_periods+1, num_trials))
    num_assets = len(portfolio)
    simulated_returns[0] = np.repeat(np.sum(portfolio_value_at_last_date))

    for idx in range(num_trials): # run a Monte Carlo simulation
        simulated_portfolio_values = portfolio_value_at_last_date
        for period in range(1,num_periods+1): # assume log returns are in a multivariate normal distribution
            log_return_variations = np.random.multivariate_normal(returns_means, returns_covariance_matrix)
            period_log_returns = log_return_variations + np.log(simulated_portfolio_values)
            simulated_portfolio_values = np.exp(period_log_returns)
            simulated_returns[period][idx] = np.sum(simulated_portfolio_values)
    
    if file_path is not None:
        if not file_path.endswith('.npy'):
            raise ValueError(f'Not supported file path: {file_path}. File must be in npy format.')
        np.save(file_path, simulated_returns)

    return simulated_returns

def load_monte_carlo_simulation (file_path):
    """
    Receives a file path of the simulation in npy.
    Returns a matrix of returns simulated by a Monte Carlo simulation.
    """
    if not file_path.endswith('.npy'):
        raise ValueError(f'Not supported file path: {file_path}. File must be in npy format.')
    simulated_returns = np.load(file_path)

    return simulated_returns

def portfolio_expected_return (simulation):
    """
    Receives the simulation to be loaded.
    Simulation must be a matrix or a file path to an npy file.
    Returns an approximation of the expected value.
    """
    if isinstance(simulation, str):
        simulated_returns = load_monte_carlo_simulation(simulation)[-1]
    elif isinstance(simulation, np.ndarray):
        simulated_returns = simulation

    return np.mean(simulated_returns)

def portfolio_risk_index (portfolio, df):
    """
    Receives a list corresponding to a portfolio and a data frame
    corresponding to an amount of periods and the portfolio.
    Returns a risk index.
    """
    returns_covariance_matrix, _ = compute_covariances_and_means(df)

    asset_weights = np.array([asset[1] for asset in portfolio])
    asset_weights = asset_weights / asset_weights.sum()

    portfolio_variance = np.dot(asset_weights, np.dot(returns_covariance_matrix, asset_weights))
    portfolio_risk = np.sqrt(portfolio_variance)

    return portfolio_risk

def portfolio_scores_at_percentiles (simulation, percentiles=[5, 10, 50, 90, 95], num_periods=30):
    """
    Receives the simulation to be loaded, an array-like of
    percentiles and the number of periods to iterate.
    Returns the score at the percentiles.
    """
    if isinstance(simulation, str):
        simulated_returns = load_monte_carlo_simulation(simulation)[-1]
    elif isinstance(simulation, np.ndarray):
        simulated_returns = simulation

    percentiles = np.array(percentiles)
    scores = np.zeros((num_periods+1, np.shape(percentiles)[0]))
    for period in range(num_periods+1):
        scores[period] = sp.stats.scoreatpercentile(simulated_returns[-num_periods-1+period], percentiles)

    return scores