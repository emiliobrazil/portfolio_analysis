"""
Finance Lib

Description: The Finance Lib simplifies the management of your investments. It introduces two fundamental classes, Stock and StockValidator, designed to help you efficiently track and manage individual stock holdings.

The Stock class enables you to specify a stock symbol, start date, and end date for historical data. It will raise a ValueError if the symbol is invalid.

The StockValidator class is responsible for ensuring the validity of stock symbols within the Brazilian market. It also provides a handy list of Brazilian stock tickers for reference.

These core components of Finance Lib's streamline your portfolio management tasks, helping you make well-informed investment decisions.

License: Apache License, Version 2.0
(See https://www.apache.org/licenses/LICENSE-2.0 for details)

Author: Letícia Aleixo
Date: November 9, 2023
"""


import yfinance as yf
import pandas as pd
import investpy as invpy


class StockValidator:
    def __init__(self, symbol: str):
        """
        Initialize a StockValidator object with the specified symbol.
        Args:
            symbol (str): The symbol of the stock.

        Attributes:
            symbol (str): The symbol of the stock.
            brazilian_tickers (list): List of Brazilian stock tickers.
            is_valid (bool): True if the stock symbol is valid in the Brazilian market, False otherwise.
        """
        self.symbol = symbol
        self.brazilian_tickers = self.brazilian_stocks()
        self.is_valid = self.is_valid_symbol()


    def brazilian_stocks(self):
        """
        Retrieve a list of Brazilian stock tickers from an external data source.
        Returns:
            list: A list of Brazilian stock tickers.
        """
        ticker_list = []
        stock_data = invpy.stocks.get_stocks("Brazil")
        for symbol in range(len(stock_data["symbol"])):
            string_ticker = str(stock_data["symbol"][symbol])
            ticker_list.append(f'{string_ticker}')
        brazilian_tickers = sorted(ticker_list)
        return brazilian_tickers


    def is_valid_symbol(self) -> bool:
        """
        Check if the stock symbol is valid in the Brazilian market and has historical data available.

        Returns:
            bool: True if the stock symbol is valid and has historical data, False otherwise.
        """
        if self.symbol in self.brazilian_tickers:
          try:
            symbol_stock = yf.Ticker(self.symbol + '.SA')
            historical_data = symbol_stock.history(period="1y")
            if not historical_data.empty:
              return True
          except:
            print(f'Stock {self.symbol} not found on B3 or may have been delisted.')
            return False
        else:
          return False
          
   
class Stock(StockValidator):
    """
      Represents a stock with a specified symbol and date range.

      This class extends the StockValidator class to validate the stock symbol 
        and provides a date range for historical data retrieval.

      Args:
          symbol (str): The symbol of the stock.
          start_date (str): The start date for historical data in the format 'YYYY-MM-DD'.
          end_date (str): The end date for historical data in the format 'YYYY-MM-DD'.

      Attributes:
          start_date (str): The start date for historical data.
          end_date (str): The end date for historical data.
          symbol (str): The symbol of the stock.

      Raises:
          ValueError: If the specified stock symbol is not valid.

      Usage:
      To create a Stock instance, provide a valid stock symbol, a start date, 
        and an end date. If the symbol is not valid, a ValueError will be raised.

      Example:
      >>> stock = Stock('PETR4', '2023-01-01', '2023-12-31')
    """
    def __init__(self, symbol:str, start_date: str, end_date: str):
      self.start_date = start_date
      self.end_date = end_date
      self.symbol = symbol
      super().__init__(symbol)
      if self.is_valid == False:
        raise ValueError(f"{self.symbol} is not a valid symbol.")


    def get_history(self):
      '''
      Return:
        The transaction history of the given symbol.
        Information contained in the history: Open, High, Low, Close, Volume, 
                                              Dividends and Stock Splits.

      Attention: History is only updated on business days.
      '''
      return yf.Ticker(self.symbol + '.SA').history(start= self.start_date, 
                                                    end= self.end_date)


    def open_price(self):
      '''
      The opening price is the value of the share, index or financial instrument
      at the beginning of the time period considered.
      '''
      return self.get_history()[['Open']]
      

    def high_price(self):
      '''
      The maximum price represents the highest value achieved by the financial 
      instrument during the period of time considered.
      '''
      return self.get_history()[['High']]


    def low_price(self):
      '''
      The minimum price is the lowest value that the financial instrument has 
      reached during the period of time considered.
      '''
      return self.get_history()[['Low']]


    def close_price(self):
      '''
      The closing price is the value of the share, index or financial instrument
      at the end of the period of time considered.
      '''
      return self.get_history()[['Close']]
    

    def volume(self):
      '''
      This column represents the volume of trades carried out during the period 
      of time considered.
      '''
      return self.get_history()[['Volume']]


    def dividends(self):
      '''
      This column may contain information about dividends paid during the time
      period considered, if available.
      '''
      return self.get_history()[['Dividends']]
    

    def stock_splits(self):
      '''
      If there is information about stock splits during the time period, this 
      column may indicate the stock splits that occurred.
      '''
      return self.get_history()[['Stock Splits']]
