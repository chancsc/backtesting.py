"""Data and utilities for testing."""
import pandas as pd


def _read_file(stock_symbol):
    from os.path import dirname, join

    filename = f"{stock_symbol}.csv"
    return pd.read_csv(join(dirname(__file__), filename),
                       index_col=0, parse_dates=True, infer_datetime_format=True)


# Example usage: Pass the stock symbol when calling the function
# to facilitate the testing file _test.py

stockTicker = _read_file('GOOG')
"""DataFrame of daily NASDAQ:TSLA (Tesla) stock price data from 2004 to 2013."""

#EURUSD = _read_file('EURUSD')
"""DataFrame of hourly EUR/USD forex data from April 2017 to February 2018."""


def SMA(arr: pd.Series, n: int) -> pd.Series:
    """
    Returns `n`-period simple moving average of array `arr`.
    """
    return pd.Series(arr).rolling(n).mean()
