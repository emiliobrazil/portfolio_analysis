from datetime import datetime
from time import time
import numpy as np
import pandas as pd

try:
    from CL_portfoliorisk import compute_log_covariances_and_means, compute_pct_covariances_and_means, monte_carlo_simulation, portfolio_scores_at_percentiles, portfolio_expected_return, portfolio_risk_index

except:
    from .CL_portfoliorisk import compute_log_covariances_and_means, compute_pct_covariances_and_means, monte_carlo_simulation, portfolio_scores_at_percentiles, portfolio_expected_return, portfolio_risk_index

class CL_simulation:
    def __init__(self, portfolio_list, stock_matrix, num_periods=30, period='1d', run_now = True):
        if run_now:
            today_date = datetime.datetime.now().strftime('%Y-%m-%d') 
            start_year = str(int(today_date[:4]) - 5) # 5 years before today
            start_date = start_year + today_date[4:]
            self.portfolio_list = portfolio_list
            self.num_periods = num_periods
            self.period = period
            self.period_started = today_date
            self.period_ended = start_date
            self.time_started = time()
            self._run_simulation(portfolio_list, stock_matrix)
            self.time_ended = time()
            self.risk_index = portfolio_risk_index (portfolio_list, stock_matrix)

    def _run_simulation(self, portfolio_list, stock_matrix):
        simulation = monte_carlo_simulation (portfolio_list, stock_matrix, self.num_periods)
        self.data = pd.DataFrame(np.concatenate((portfolio_scores_at_percentiles(simulation, [10, 25, 50, 75, 90]), portfolio_expected_return (simulation)[:, np.newaxis]), axis=1),
                            columns=['p10', 'p25', 'p50', 'p75', 'p90', 'expected_return'])
        self.risk_index = portfolio_risk_index (portfolio_list, stock_matrix)

    def to_dict(self) -> dict:
        return{
            'portfolio_list': self.portfolio_list,
            'num_periods': self.num_periods,
            'period': self.period,
            'period_started': self.period_started,
            'period_ended': self.period_ended,
            'time_started': self.time_started,
            'time_ended': self.time_ended,
            'data': self.data.to_dict(),
            'risk_index': self.risk_index
        }
    
    @staticmethod
    def from_dict(sml_dict):
        sml = CL_simulation(None, None, run_now = False)
        sml.portfolio_list = sml_dict['portfolio_list']
        sml.num_periods = sml_dict['num_periods']
        sml.period = sml_dict['period']
        sml.period_started = sml_dict['period_started']
        sml.period_ended = sml_dict['period_ended']
        sml.time_started = sml_dict['time_started']
        sml.time_ended = sml_dict['time_ended']
        sml.risk_index = sml_dict['risk_index']
        sml.data = pd.DataFrame(sml_dict['data'])
        return sml

def test():
    np.random.seed(1) # Set seed for reproducibility
    cov_matrix = np.array([[0.01, -0.005, 0.002, 0.001],
                       [-0.005, 0.02, -0.003, 0.0015],
                       [0.002, -0.003, 0.015, -0.002],
                       [0.001, 0.0015, -0.002, 0.01]])
    means_array = np.array([0.001, 0.0005, 0.0002, 0.0015])
    sample = np.random.multivariate_normal(means_array, cov_matrix, size=200)
    log_returns = np.cumsum(sample, axis=0)
    prices = np.exp(log_returns)
    data = pd.DataFrame(prices, columns=['Stock1', 'Stock2', 'Stock3', 'Stock4'])
    portfolio_list = [('Stock1', 40), ('Stock2', 30), ('Stock3', 200), ('Stock4', 100)]
    
    sim1 = CL_simulation(portfolio_list, data)
    print(f"The simulation's information is given by:\n{sim1.to_dict()}.")
    print(f"The simulation's percentiles and expected return are given by:\n{sim1.data}")
    sim2 = CL_simulation.from_dict(sim1.to_dict())
    print('Hey! It worked! Dictionary successfuly loaded!' if sim1.to_dict() == sim2.to_dict() else 'Oh, no! Something went wrong when loading the dictionary...')

if __name__ == '__main__':
    test()
