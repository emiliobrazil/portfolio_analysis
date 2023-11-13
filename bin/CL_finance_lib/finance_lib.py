import yfinance as yf
import pandas as pd

def is_valid(symbol: str) -> bool:
  """
  input:
      symbol: a str that represents a stok
  output:
      bool: True if the symbol is a stock that is possible to recover at least one month of historic, 
      False otherwise
  """
  symbol_stock = yf.Ticker(symbol + '.SA')
  history = symbol_stock.history(period="1mo")
  if not history.empty:
    return True
  else:
    print(f'Stock {symbol} not found or may have been delisted.')
    return False
    
    
def history(symbols: list, start_date: str, end_date: str, interval: str):
    """
    input:
        symbols: A list of str that represent the stocks to recover the history
        start_date: Time object that represent the first day of the historical data. 
        	    Format: "YYYY-MM-DD"
        end_date: Time object that represent the last day of the historical data. 
        	  Format: "YYYY-MM-DD"
        interval: the interval of the historical: {1d, 5d, 1wk, 1mo, 3mo, 1y}    
    output:
        dataframes: List of Pandas DataFrames, where each DataFrame corresponds to the historical data for a valid stock in symbols
    """
    dataframes = {}
    for symbol in symbols:
      if is_valid(symbol):
        symbol_history = yf.Ticker(symbol + '.SA').history(start=start_date, end=end_date, interval=interval)
        dataframes[symbol] = symbol_history

    return dataframes
