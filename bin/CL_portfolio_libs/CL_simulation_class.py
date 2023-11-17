from time import time
import pandas as pd

### Class to handle the simulations


class CL_simulation:
    # __init__(stock_matrix) run simulation
    # store: time started, time ended, started period (Data), ended period (Data), period, matrix
    # return dict if all stored informations:
    # 
    # This is FAKE implementatio just as mockup to test the possible interfaces
    def __init__(self, stock_matrix, period = '1d', run_now = True):
        if run_now:
            self.period = period
            self.period_started ='2023-11-15' # TODAY date
            self.period_ended ='2018-11-15' # 5 years before today
            self.time_started = time()
            self._run_simulation(stock_matrix)
            self.time_ended = time()

    def _run_simulation(self, stock_matrix):
        self.data = pd.DataFrame([[i+(j+1)*10 for j in range(5)] for i in range(30)], 
                            columns=['p10', 'p25', 'p50', 'p75', 'p90'])

    def to_dict(self) -> dict:
        return{
            'period': self.period,
            'period_started': self.period_started,
            'period_ended': self.period_ended,
            'time_started': self.time_started,
            'time_ended': self.time_ended,
            'data': self.data.to_dict()
        }
    
    @staticmethod
    def from_dict(sml_dict) -> None:
        sml = CL_simulation(None, period = '1d', run_now = False)
        sml.period = sml_dict['period']
        sml.period_started = sml_dict['period_started']
        sml.period_ended = sml_dict['period_ended']
        sml.time_started = sml_dict['time_started']
        sml.time_ended = sml_dict['time_ended']
        sml.data = pd.DataFrame(sml_dict['data'])
