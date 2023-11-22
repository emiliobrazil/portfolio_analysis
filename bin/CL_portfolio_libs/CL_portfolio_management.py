"""
Portfolio Management Module

Description: This module provides classes and functions for managing a portfolio of stocks and their quantities.
The stock is represented by str and the quantites by int.

License: Apache License, Version 2.0
(See https://www.apache.org/licenses/LICENSE-2.0 for details)

Author: Emilio Vital Brazil
Date: November 4, 2023
"""

from typing import Tuple, List
import json
import os
import pandas as pd
import datetime

try:
    from CL_simulation_class import CL_simulation as CLsml
    from CL_finance import is_valid_stock, MeanPriceMatrix
except:
    from .CL_simulation_class import CL_simulation as CLsml
    from .CL_finance import is_valid_stock, MeanPriceMatrix

count = 0 # used to count unamed portfolios

class Portfolio:
    version = '0.0.2'
    def __init__(self, portfolio: List[Tuple[str, int]] = None, name = None):
        self.portfolio = {}
        self.simulations = []
        self.__readForSimulation__ = False

        if portfolio is not None:
            if type(portfolio) is list:
                    for s in portfolio:
                        self.add_stock(s[0],s[1])
            if type(portfolio) is dict:
                for s in portfolio:
                    self.add_stock(s, portfolio[s])
        self.name = name
        if self.name is None or type(self.name) is not str :
            self.name = f'unamed{count}'
        self.__is_running = False


    def __getitem__(self, symb: str) -> int:
        return self.portfolio[symb]
    

    def __setitem__(self, symb: str, quatity: int) -> None:
        if self.locked:
            print('Portifolio Loked - Not possible to change it')
            return
        if symb in self.portfolio:
            self.portfolio[symb] = int(quatity)
        elif self.is_valid_symblo(symb):
            self.portfolio[symb] = int(quatity)
        else:
            print(f'Portfolio should be a valid symbol - {symb} discarded')

    def __len__(self):
        return len(self.portfolio)


    def __str__(self) -> str:
        return f'{self.name} : {str(self.portfolio)}'
    

    def __repr__(self) -> str:
        return f'{self.name} : {repr(self.portfolio)}'


    def copy(self) -> 'Portfolio':
        return Portfolio(self.portfolio, self.name)


    def add_stock(self, symb: str, quatity: int):
        if symb in self.portfolio:
            quatity += self.portfolio[symb]
        self.__setitem__(symb, quatity)
        

    def portifolio_matrix(self, period='1mo'):
        symbols = [asset[0] for asset in self.portfolio_list]
        today_date = datetime.datetime.now().strftime('%Y-%m-%d') 
        start_year = str(int(today_date[:4]) - 5) # 5 years before today
        start_date = start_year + today_date[4:]
        prices = MeanPriceMatrix(symbols, start_date, today_date, period)
        stock_matrix = prices.get_portifolio_matrix
        return pd.DataFrame(stock_matrix)

    def remove_stock(self, symb: str) -> None:
        if self.locked:
            print('Portifolio Loked - Not possible to change it')
            return
        if symb in self.portfolio:
            del self.portfolio[symb]


    def update_stock(self,  symb: str, quatity: int) -> None:
        self.__setitem__(symb, quatity)


    def lock(self):
        self.__readForSimulation__ = True

    def save(self, path: str = '.') -> str:
        complete_path = path + os.sep + self.name + '.jprt'
        with open(complete_path, 'w') as outfile:
            Jportfolio = {
                'name': self.name, 
                'version': self.version,
                'portfolio': self.portfolio,
                'simulations': [d.to_dict() for d in self.simulations]
                }
            json_object = json.dumps(Jportfolio, indent=4)
            outfile.write(json_object)
        return complete_path

    def run_simulation(self, period: str = '1mo') -> bool:
        if self.is_running:
            print('Simulation already running, NOT possible run another, WAIT!!')
            return False
        self.__readForSimulation__ = True
        self.__is_running = True
        #TODO multi_thread
        sml = CLsml(self.portfolio_list, self.portifolio_matrix(), period=period)
        self.__is_running = False
        if sml is not None:
            self.simulations.append(sml)
            return True
        else:
            return False
    
    @property
    def portfolio_list (self):
         if type(self.portfolio) is list:
             return self.portfolio
         elif type(self.portfolio) is dict:
             return list(self.portfolio.items())
        
    @property
    def is_running(self):
        return self.__is_running

    @property
    def last_simulation(self):
        if len(self.simulations) > 0:
            return self.simulations[-1]
        return {}


    @property
    def symbols(self):
        return self.portfolio.keys()
    

    @property
    def quantities(self):
        return self.portfolio.values()
    

    @property
    def locked(self):
        return self.__readForSimulation__


    @staticmethod
    def load(path: str) -> 'Portfolio':
        with open(path, 'r') as infile:
            data = json.load(infile)

        prt = Portfolio(data['portfolio'], data['name'])

        prt.simulations = [CLsml.from_dict(dt) for dt in data['simulations'] if len(dt) > 0] 

        if data['version'] != prt.version:
            print(f'WARNING: Load a different version -- current {prt.version} -- Loaded {data["version"]}')
        if len(prt.simulations) > 0:
            prt.lock()
        return prt
    
    @staticmethod
    def is_valid_symblo(sym):
        return type(sym) is str and is_valid_stock(sym)
    

def test():
    prt = Portfolio([['PETR4', 100], ['VALE3', 400], ['PETR4', 100], ['ABEV3', 1000]], 'test')
    prt.add_stock('nstock', 2000)
    prt.add_stock('ITUB4', 300)
    print(prt)
    fileName = prt.save()
    print(f'Portfolio saved on: {fileName}')
    ptr2 = Portfolio.load(fileName)
    print(f'Portfolio {ptr2.name} loaded from: {fileName}')
    print(ptr2.symbols)
    print(ptr2.quantities)
    ptr2.update_stock('PETR4', 300)
    ptr2.name = 'new_test'
    ptr2.remove_stock('nstock')
    ptr2.remove_stock('VALE3')
    print(ptr2.last_simulation)
    print(ptr2)
    print(repr(ptr2))
    ptr2.run_simulation('1d')
    ptr2.save()
    ptr3 = Portfolio('new_test')
    print(ptr3)
    print(prt.portifolio_matrix)
    
if __name__ == '__main__':
    test()