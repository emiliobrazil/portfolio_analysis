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

count = 0 # used to count unamed portfolios

class Portfolio:
    version = '0.0.1'
    def __init__(self, portfolio: List[Tuple[str, int]] = None, name = None):
        self.portfolio = []
        if portfolio is not None:
            for s in portfolio:
                self.add_stock(s)
        self.name = name
        if self.name is None or type(self.name) is not str :
            self.name = f'unamed{count}'


    def __getitem__(self, key: int) -> Tuple[str, int]:
        return self.portfolio[key]
    

    def __setitem__(self, key: int, value: Tuple[str, int]) -> None:
        if type(value[0]) is str:
            self.portfolio[key] = (value[0], int(value[1]))
        else:
            raise TypeError('Portfolio should be (STR, INT) and the first element is not a STR')


    def __len__(self):
        return len(self.portfolio)

    def add_stock(self, stock: Tuple[str, int], key = -1):
        if type(stock[0]) is str:
            self.portfolio.append((stock[0], int(stock[1])))
        else:
            raise TypeError('Portfolio should be (STR, INT) and the first element is not a STR')
        

    def __str__(self) -> str:
        return f'{self.name} : {str(self.portfolio)}'
    

    def __repr__(self) -> str:
        return f'{self.name} : {repr(self.portfolio)}'

    
    def save(self, path: str = '') -> str:
        complete_path = path + os.sep + self.name + 'jprt'
        with open(complete_path, 'w') as outfile:
            Jportfolio = {
                'name': self.name, 
                'version': self.version,
                'portfolio':self.portfolio
                }
            json_object = json.dumps(Jportfolio)
            outfile.write(json_object)
        return complete_path

    @property
    def keys(self):
        return [x[0] for x in self.portfolio]
    
    @property
    def values(self):
        return [x[1] for x in self.portfolio]

    @staticmethod
    def load(path: str) -> 'Portfolio':
        with open(path, 'r') as infile:
            data = json.load(infile)

        prt = Portfolio(data['portfolio'], data['name'])

        if data['version'] != prt.version:
            print(f'WARNING: Load a different version -- current {prt.version} -- Loaded {data["version"]}')

        return prt
    
def test():
    prt = Portfolio([['PETR', 100], ['QTR02', 20]], 'myportifolio')
    prt.add_stock(('nstock', 2000))
    print(prt)

if __name__ == '__main__':
    test()

