from typing import Tuple, List
import json
import os

count = 0 # used to count unamed portfolios

class Portfolio:
    version = '0.0.1'

    def __init__(self, portfolio: List[Tuple[str, int]] = None, name=None):
        self.portfolio = {}
        if portfolio is not None:
            if type(portfolio) is list:
                for s in portfolio:
                    self.add_stock(s[0], s[1])
            if type(portfolio) is dict:
                for s in portfolio:
                    self.add_stock(s, portfolio[s])
        self.name = name
        if self.name is None or type(self.name) is not str:
            self.name = f'unamed{count}'

    def __getitem__(self, symb: str) -> int:
        return self.portfolio[symb]

    def __setitem__(self, symb: str, quatity: int) -> None:
        if symb in self.portfolio:
            self.portfolio[symb] = int(quatity)
        elif self.is_valid_symblo(symb):
            self.portfolio[symb] = int(quatity)
        else:
            raise TypeError('Portfolio should be a valid symbol')

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
            raise RuntimeError('DUPLICATED STOCK: You cannot add a symbol that alread is in the portfolio')
        self.__setitem__(symb, quatity)

    def remove_stock(self, symb: str) -> None:
        del self.portfolio[symb]

    def update_stock(self, symb: str, quatity: int) -> None:
        self.__setitem__(symb, quatity)

    def save(self, path: str = '.') -> str:
        complete_path = path
        with open(complete_path, 'w') as outfile:
            Jportfolio = {
                'name': self.name,
                'version': self.version,
                'portfolio': self.portfolio
            }
            json_object = json.dumps(Jportfolio, indent=4)
            outfile.write(json_object)
        return complete_path

    @property
    def symbols(self):
        return self.portfolio.keys()

    @property
    def quantities(self):
        return self.portfolio.values()

    @staticmethod
    def load(path: str) -> 'Portfolio':
        with open(path, 'r') as infile:
            data = json.load(infile)

        prt = Portfolio(data['portfolio'], data['name'])

        if data['version'] != prt.version:
            print(f'WARNING: Load a different version -- current {prt.version} -- Loaded {data["version"]}')

        return prt

    @staticmethod
    def is_valid_symblo(sym):
        return type(sym) is str