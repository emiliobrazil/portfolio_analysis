import os
import numpy as np
import scipy as sp
import pandas as pd

def compute_covariances_and_means (df):
    """
    Computes an approximation of the covariance matrix and the expected returns for a given portfolio.

    Parameters:
    - df (pd.DataFrame): DataFrame containing historical stock prices.

    Returns:
    - tuple: Returns a tuple containing approximations of the covariance matrix and expected returns.
    """
    returns = df.pct_change().dropna() # Convert into percentage and drop rows with missing values
    returns_covariance_matrix = returns.cov()
    returns_means = returns.mean()

    return returns_covariance_matrix, returns_means

def monte_carlo_simulation (portfolio, df, num_periods, file_path=None, num_trials=1000):
    """
    Performs a Monte Carlo simulation for a given portfolio.

    Parameters:
    - portfolio (list): List representing the portfolio with stock weights.
    - df (pd.DataFrame): DataFrame containing historical stock prices.
    - num_periods (int): Number of simulation periods.
    - file_path (str, optional): File path to save the simulation results. Defaults to None.
    - num_trials (int, optional): Number of trials for each period. Defaults to 1000.

    Returns:
    - np.ndarray: Array of simulated portfolio returns.
    """
    returns_covariance_matrix, returns_means = compute_covariances_and_means(df)
    assets_values_at_last_date = df.iloc[-1:].to_numpy() # Get the most recent values for each asset
    asset_weights = np.array([asset[1] for asset in portfolio])
    portfolio_value_at_last_date = assets_values_at_last_date * asset_weights

    simulated_returns = np.zeros((num_periods+1, num_trials))
    num_assets = len(portfolio)
    simulated_returns[0] = np.full(num_trials, np.sum(portfolio_value_at_last_date))

    for idx in range(num_trials): # Run a Monte Carlo simulation
        simulated_portfolio_values = portfolio_value_at_last_date
        for period in range(1,num_periods+1): # Assume log returns are in a multivariate normal distribution
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
    Loads a Monte Carlo simulation from a saved file.

    Parameters:
    - file_path (str): File path of the saved simulation in npy format.

    Returns:
    - np.ndarray: Matrix of returns simulated by the Monte Carlo simulation.
    """
    if not file_path.endswith('.npy'):
        raise ValueError(f'Not supported file path: {file_path}. File must be in npy format.')
    simulated_returns = np.load(file_path)

    return simulated_returns

def portfolio_expected_return (simulation):
    """
    Computes the approximate expected return for a Monte Carlo simulation.

    Parameters:
    - simulation (np.ndarray): Matrix corresponding to a Monte Carlo simulation.

    Returns:
    - float: Approximation of the expected value.
    """
    return np.mean(simulation[-1])

def portfolio_risk_index (portfolio, df):
    """
    Computes the approximate risk index for a given portfolio.

    Parameters:
    - portfolio (list[tuple[str, int]]): List with elements of the form tuple[str, int]
    representing the portfolio with stock assets and their amount.
    - df (pd.DataFrame): DataFrame containing historical stock prices.

    Returns:
    - float: Risk index.
    """
    returns_covariance_matrix, _ = compute_covariances_and_means(df)

    asset_weights = np.array([asset[1] for asset in portfolio])
    asset_weights = asset_weights / asset_weights.sum()

    portfolio_variance = np.dot(asset_weights, np.dot(returns_covariance_matrix, asset_weights))
    portfolio_risk = np.sqrt(portfolio_variance)

    return portfolio_risk

def portfolio_scores_at_percentiles (simulation, percentiles=[5, 10, 50, 90, 95], num_periods=30):
    """
    Computes approximate scores at specified percentiles for a Monte Carlo simulation.

    Parameters:
    - simulation (np.ndarray): Matrix corresponding to a Monte Carlo simulation.
    - percentiles (array-like, optional): Array-like object of percentiles to calculate scores. Defaults to [5, 10, 50, 90, 95].
    - num_periods (int, optional): Number of periods to iterate. Defaults to 30.

    Returns:
    - np.ndarray: Scores at the specified percentiles.
    """
    if np.shape(simulation)[0] < num_periods+1:
        raise ValueError(f'Matrix corresponding to the simulation must have at least {num_periods+1} rows. Simulation matrix shape: {np.shape(simulated_returns)}.')
    percentiles = np.array(percentiles)
    scores = np.zeros((num_periods+1, np.shape(percentiles)[0]))
    for period in range(num_periods+1):
        scores[period] = sp.stats.scoreatpercentile(simulation[-num_periods-1+period], percentiles)

    return scores

def test(): # Test all functions

    np.random.seed(1) # Set seed for reproducibility

    cov_matrix = np.array([[0.01, -0.005, 0.002, 0.001],
                           [-0.005, 0.02, -0.003, 0.0015],
                           [0.002, -0.003, 0.015, -0.002],
                           [0.001, 0.0015, -0.002, 0.01]])
    means_array = np.array([0.1, 0.05, 0.02, 0.15])
    sample = np.random.multivariate_normal(means_array, cov_matrix, size=100)
    log_returns = 0.02 * np.cumsum(sample, axis=0) # Scale log_returns with a 0.02 scaling factor
    prices = np.exp(log_returns)

    data = pd.DataFrame(prices, columns=['Stock1', 'Stock2', 'Stock3', 'Stock4'])
    portfolio_list = [('Stock1', 40), ('Stock2', 30), ('Stock3', 200), ('Stock4', 100)]

    script_directory = os.getcwd()
    file_path = os.path.join(script_directory, "simulation_test.npy")

    simulation = monte_carlo_simulation (portfolio_list, data, 100, file_path)
    print(f'The risk index for 100 period units is approximately {portfolio_risk_index (portfolio_list, data)}.')
    print(f'The expected return after 100 period units is approximately {portfolio_expected_return(simulation)}.')
    print(f'The scores at percentiles 5, 10, 50, 90, 95 for the next 30 period units in order are approximately\n{portfolio_scores_at_percentiles (simulation)}.')

    loaded_simulation = load_monte_carlo_simulation(file_path)
    print('The simulation was successfully loaded!' if np.array_equal(simulation, loaded_simulation) else 'The loading failed...')
    
if __name__ == '__main__':
    test()