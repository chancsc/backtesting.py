# This  script is used to Check Buy/Sell Signal (check_bss) & chart.
# It can display the chart, if there's buy/sell signal, send telegram notification
#
# it will retrieve current year data by default, use get_stock_data_SA.py to get 
# data for different period
#
# browser & table parameter are optional, if ommitted, will display table in 
# console, and open browser to display chart

import sys
from backtesting import Backtest, Strategy
from backtesting.test.__init__ import _read_file
from backtesting.lib import crossover
from backtesting.test.__init__ import SMA

from get_stock_data import generate_stock_data
import argparse
import datetime

current_year = datetime.date.today().year

parser = argparse.ArgumentParser(description='Display stock chart in a web browser.')
parser.add_argument('stockSymbol', type=str, help='The stock symbol to analyze')
parser.add_argument('--browser', type=int, choices=[0, 1], default=1,
                    help='Optional parameter for displaying browser (1 = open browser)')
parser.add_argument('--table', type=int, choices=[0, 1], default=1,
                    help='Optional parameter for hiding table in console (1 = Display)')
parser.add_argument('--year', type=int, default=datetime.date.today().year,
                    help='Optional parameter for specifying the year')

args = parser.parse_args()
stockSymbol = args.stockSymbol
Browser = args.browser
sTable = args.table

if args.year == current_year:
    sdate = None
    edate = None
else:
    year = args.year
    sdate = f"01/01/{args.year}"
    edate = f"31/12/{args.year}"

# Example usage:
generate_stock_data(stockSymbol, sdate, edate)

# Use the stock symbol to load the corresponding stock data
stockTicker = _read_file(stockSymbol)  # Replace `_read_file` with the actual function to load stock data

class SmaCross(Strategy):
    def init(self):
        price = self.data.Close
        self.ma1 = self.I(SMA, price, 5)
        self.ma2 = self.I(SMA, price, 10)

    def next(self):
        if crossover(self.ma1, self.ma2):
            #10 days MA cross above 20 days MA, buy
            self.buy()
        elif crossover(self.ma2, self.ma1):
            #20 days MA cross above 10 days MA, sell
            self.sell()

bt = Backtest(stockTicker, SmaCross, commission=.002, exclusive_orders=True)
stats = bt.run()
bt.plot(filename=stockSymbol, open_browser=Browser, showTable=sTable)
