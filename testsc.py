# e.g. usage: python testsc.py MSFT

import sys
from backtesting import Backtest, Strategy
from backtesting.test.__init__ import _read_file
from backtesting.lib import crossover

from backtesting.test.__init__ import SMA

# Check if the stockSymbol is provided as a command-line argument
if len(sys.argv) < 2:
    print("Please provide the stock symbol as a command-line argument.")
    sys.exit(1)

stockSymbol = sys.argv[1]
# Use the stock symbol to load the corresponding stock data
stockTicker = _read_file(stockSymbol)  # Replace `_read_file` with the actual function to load stock data

class SmaCross(Strategy):
    def init(self):
        price = self.data.Close
        self.ma1 = self.I(SMA, price, 10)
        self.ma2 = self.I(SMA, price, 20)

    def next(self):
        if crossover(self.ma1, self.ma2):
            self.buy()
        elif crossover(self.ma2, self.ma1):
            self.sell()

bt = Backtest(stockTicker, SmaCross, commission=.002, exclusive_orders=True)
stats = bt.run()
bt.plot()
