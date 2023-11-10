import json
import numpy as np
import scipy as sp
import pandas as pd

# May need adaptations according to the format received by finance and management portfolios libs

def compute_covariances_and_means (portfolio):
    """
    Receives a portfolio.
    Returns an approximate covariance matrix of the portfolio
    and an array of the approximate expected value of each asset.
    """
    # data = something something from finance lib
    df = pd.DataFrame(data)
    returns = df.pct_change().dropna() # convert into percentage and drop rows with missing values
    returns_covariance_matrix = returns.cov()
    returns_means = returns.mean()
    return returns_covariance_matrix, returns_means

def monte_carlo_simulation (portfolio, file_path_simulation=None, file_path_portfolio=None, num_periods, type_period='months', num_trials=1000):
    """
    Receives a portfolio, a file path to save the results of the simulation in npy, an amount of
    periods and the type of period (days, months or years), a file path to save the portfolio in
    JSON, the number of periods to iterate and the type of periods (days, months or years).
    Returns an array of simulated returns and the portfolio in list format.
    """
    # data = blah blah blah
    df = pd.DataFrame(data)
    returns_covariance_matrix, return_means = compute_covariances_and_means(portfolio)

    assets_values_at_last_date = df.iloc[-1:].to_numpy() # get the most recent values for each asset
    asset_weights = np.array([asset[1] for asset in portfolio])
    portfolio_value_at_last_date = assets_values_at_last_date * asset_weights

    simulated_returns = np.zeros(num_trials)
    num_assets = len(portfolio)

    for idx in range(num_trials): # run a Monte Carlo simulation
        simulated_portfolio_values = portfolio_value_at_last_date
        for day in range(num_periods): # assume log returns are in a multivariate normal distribution
            log_return_variations = np.random.multivariate_normal(returns_means, returns_covariance_matrix)
            period_log_returns = log_return_variations + np.log(simulated_portfolio_values)
            simulated_portfolio_values = np.exp(period_log_returns)
        simulated_return = simulated_portfolio_values.sum()
        simulated_returns[idx] = simulated_return
    
    if file_path_simulation is not None:
        if not file_path_simulation.endswith('.npy'):
            raise ValueError(f'Not supported file path: {file_path_simulation}. File must be in npy format.')
        np.save(file_path_simulation, simulated_returns)
    
    if file_path_portfolio is not None:
        if not file_path_portfolio.endswith('.json'):
            raise ValueError(f'Not supported file path: {file_path_portfolio}. File must be in JSON format.')
        with open(file_path_portfolio, 'w') as json_file:
            json.dump(portfolio, json_file)
    
    return simulated_returns, portfolio

def load_monte_carlo_simulation (portfolio, file_path, type_period='months'):
    """
    Receives a portfolio or its file path in JSON and a file path of the simulation in npy.
    Returns an array of returns simulated by a Monte Carlo simulation, the portfolio and the type of period.
    """
    if isinstance(portfolio, str):
        if portfolio.endswith('.json'):
            with open(portfolio, 'r') as json_file:
                open_portfolio = json.load(json_file)
        else:
            raise ValueError(f'Not supported file path: {portfolio}. File must be in JSON format.')
    else:
        open_portfolio = portfolio
    if not file_path.endswith('.npy'):
        raise ValueError(f'Not supported file path: {file_path}. File must be in npy format.')
    simulated_returns = np.load(file_path)
    return simulated_returns, open_portfolio, type_period   

def portfolio_expected_return (portfolio, num_periods, type_period='months', simulation_path=None, num_trials=1000):
    """
    Receives a portfolio, an amount of periods, the type of period (days, months or years) and the
    file path of the simulation to be loaded, if any.
    Runs a Monte Carlo simulation if no simulation is loaded.
    Returns an approximation of the expected value using a Monte Carlo simulation.
    """
    if simulation_path is not None:
        simulated_returns = load_monte_carlo_simulation(portfolio, simulation_path, type_period)[0]
    else: # run a Monte Carlo simulation without saving it
        simulated_returns = monte_carlo_simulation(portfolio, None, None, num_periods, type_period, num_trials)[0]

    return np.mean(simulated_returns)

def portfolio_risk_index (portfolio):
    """
    Receives a portfolio.
    Returns a risk index.
    """
    if isinstance(portfolio, str):
        if portfolio.endswith('.json'):
            with open(portfolio, 'r') as json_file:
                open_portfolio = json.load(json_file)
        else:
            raise ValueError(f'Not supported file path: {portfolio}. File must be in JSON format.')
    else:
        open_portfolio = portfolio

    returns_covariance_matrix, _ = compute_covariances_and_means(open_portfolio)

    asset_weights = np.array([asset[1] for asset in open_portfolio])
    asset_weights = asset_weights / asset_weights.sum()

    portfolio_variance = np.dot(asset_weights, np.dot(returns_covariance_matrix, asset_weights))
    portfolio_risk = np.sqrt(portfolio_variance)

    return portfolio_risk

def portfolio_percentiles (portfolio, percentiles=[5, 10, 50, 90, 100], num_periods=30, type_period='months', simulation_path=None):
    """
    Receives a portfolio, an array-like of percentiles and a file path to load
    a saved simulation, if any.
    Runs a Monte Carlo simulation if no simulation is loaded.
    Returns the score at the percentiles.
    """
    if simulation_path is not None:
        simulated_returns = load_monte_carlo_simulation(portfolio, simulation_path, type_period)[0]
    else:
        simulated_returns = monte_carlo_simulation(portfolio, None, None, num_periods, type_period, num_trials)[0]
    scores = sp.stats.scoreatpercentile(simulated_returns, percentiles)
    return scores