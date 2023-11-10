import numpy as np
import scipy as sp
import pandas as pd

# May need adaptations according to the format received by finance and management portfolios libs

def compute_covariances_and_means (portfolio, type_period='months'):
    """
    Receives a portfolio.
    Returns an approximate covariance matrix of the portfolio
    and an array of the approximate expected value of each stock.
    """
    # data = something something from finance lib
    df = pd.DataFrame(data)
    returns = df.pct_change().dropna() # convert into percentage and drop rows with missing values
    returns_covariance_matrix = returns.cov()
    returns_means = returns.mean()

    return returns_covariance_matrix, returns_means

def monte_carlo_simulation (portfolio, num_periods, file_path=None, type_period='months', num_trials=1000):
    """
    Receives a portfolio, a file path to save the results of the simulation in npy, an amount of
    periods and the type of period (days, months or years), the number of periods to iterate, the
    type of periods (days, months or years) and the number of trials for each period for the Monte
    Carlo simulation.
    Returns an array of simulated returns and the portfolio in list format.
    """
    # data = blah blah blah
    df = pd.DataFrame(data)
    returns_covariance_matrix, returns_means = compute_covariances_and_means(portfolio, type_period)

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
        if not file_path_simulation.endswith('.npy'):
            raise ValueError(f'Not supported file path: {file_path}. File must be in npy format.')
        np.save(file_path, simulated_returns)

    return simulated_returns, portfolio

def load_monte_carlo_simulation (portfolio, file_path, type_period='months'):
    """
    Receives a portfolio and a file path of the simulation in npy.
    Returns an array of returns simulated by a Monte Carlo simulation, the portfolio and the type of period.
    """
    if not file_path.endswith('.npy'):
        raise ValueError(f'Not supported file path: {file_path}. File must be in npy format.')
    simulated_returns = np.load(file_path)

    return simulated_returns, portfolio, type_period   

def portfolio_expected_return (portfolio, num_periods, type_period='months', simulation_path=None, num_trials=1000):
    """
    Receives a portfolio, an amount of periods, the type of period (days, months or years) and the
    file path of the simulation to be loaded, if any.
    Runs a Monte Carlo simulation if no simulation is loaded.
    Returns an approximation of the expected value using a Monte Carlo simulation.
    """
    if simulation_path is not None:
        simulated_returns = load_monte_carlo_simulation(portfolio, simulation_path, type_period)[0][-1]
    else: # run a Monte Carlo simulation without saving it
        simulated_returns = monte_carlo_simulation(portfolio, None, None, num_periods, type_period, num_trials)[0][-1]

    return np.mean(simulated_returns)

def portfolio_risk_index (portfolio, type_period='months'):
    """
    Receives a portfolio.
    Returns a risk index.
    """
    returns_covariance_matrix, _ = compute_covariances_and_means(portfolio, type_period)

    asset_weights = np.array([asset[1] for asset in portfolio])
    asset_weights = asset_weights / asset_weights.sum()

    portfolio_variance = np.dot(asset_weights, np.dot(returns_covariance_matrix, asset_weights))
    portfolio_risk = np.sqrt(portfolio_variance)

    return portfolio_risk

def portfolio_scores_at_percentiles (portfolio, percentiles=[5, 10, 50, 90, 100], num_periods=30, type_period='months', simulation_path=None):
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

    percentiles = np.array(percentiles)
    scores = np.zeros((num_periods+1, np.shape(percentiles)[0]))
    for period in range(num_periods+1):
        scores[period] = sp.stats.scoreatpercentile(simulated_returns[period], percentiles)
    
    return scores