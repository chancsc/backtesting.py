# This python script is used to Check Buy/Sell Signal (check_bss) & chart
# it can display the chart, if there's buy/sell signal, send telegram notification

# e.g. usage: 
# 1. python check_bss.py MSFT
# 2. python check_bss.py MSFT --oBrowser=1 (optional parameter:
#    1 = open browser and display chart
#    0 = default value if parameter omitted, will not open browser )

import sys
from backtesting import Backtest, Strategy
from backtesting.test.__init__ import _read_file
from backtesting.lib import crossover
from backtesting.test.__init__ import SMA

from get_stock_data import generate_stock_data
import argparse

parser = argparse.ArgumentParser(description='Display stock chart in a web browser.')
parser.add_argument('stockSymbol', type=str, help='The stock symbol to analyse')
parser.add_argument('--oBrowser', type=int, choices=[0, 1],
                    help='Optional parameter for displaying browser (0 for default, 1 for alternative)')

args = parser.parse_args()
stockSymbol = args.stockSymbol
oBrowser = args.oBrowser

# Example usage:
generate_stock_data(stockSymbol)

# Use the stock symbol to load the corresponding stock data
stockTicker = _read_file(stockSymbol)  # Replace `_read_file` with the actual function to load stock data

class SmaCross(Strategy):
    def init(self):
        price = self.data.Close
        self.ma1 = self.I(SMA, price, 10)
        self.ma2 = self.I(SMA, price, 20)

    def next(self):
        if crossover(self.ma1, self.ma2):
            #10 days MA cross above 20 days MA, buy
            self.buy()
        elif crossover(self.ma2, self.ma1):
            #20 days MA cross above 10 days MA, sell
            self.sell()

bt = Backtest(stockTicker, SmaCross, commission=.002, exclusive_orders=True)
stats = bt.run()
bt.plot(filename=stockSymbol, open_browser=oBrowser)
