[![](https://i.imgur.com/E8Kj69Y.png)](https://kernc.github.io/backtesting.py/)

Backtesting.py
==============

Backtest trading strategies with Python.

[**Original Project website**](https://kernc.github.io/backtesting.py) + [Documentation]

[Documentation]: https://kernc.github.io/backtesting.py/doc/backtesting/


Installation
------------

```bash
$ gitclone https://github.com/chancsc/backtesting.py.git
$ pip install yfinance
$ pip install pandas seaborn
$ pip install tabulate
$ pip install bokeh


May need these (install 1 by 1 and try run the command e.g.: python  bss_1.py CPNG 3 10 
$ sudo apt-get install libblas-dev
$ sudo apt-get install libhdf5-dev
$ sudo apt-get install libhdf5-serial-dev
$ sudo apt-get install libatlas-base-dev
```

To start
--------
Call the most basic program to generate chart with 10 & 20 days MA (moving average), buy/sell indicators etc.
   By default, the script will pull data from 1 Jan {current year} --> {today}.

```python
python check_bss.py TSLA
```

Back-test single stock
----------------------

Run single check, NOT to open browser

```python
python check_bss.py MSFT --browser=0
```

Run single check, NOT open browser, NOT display table in console

```python
python check_bss.py AAPL --browser=0 --table=0
```

Run singgle check, NOT to open browser, NOT display table, year 2022

```python
python check_bss.py AAPL --browser=0 --table=0 --year=2022
```

Download stock data to csv
---------------------------

Download YTD data for single stock

```python
python get_stock_data_SA.py --stock=IQ
```

Download specific date range data for single stock

```python
python get_stock_data_SA.py --stock=IQ --sdate=01/01/2022 --edate=01/01/2023
```

Batch mode
==========

Batch mode, default retrieve current year data, back-test based on stock_list_us.json 

```python
python check_bss_batch.py
```

Batch mode, for year 2021 & export data to log

```python
python check_bss_batch.py --year=2021 > PL2021-5-10.txt 2>&1
```

Batch mode, for year 2022, specify stocklist file, output to log

```python
python check_bss_batch.py --year=2022 --file=stock_list_test.json > output.txt 2>&1
```



Cronjob setup
--------------

```bash
$ crontab -e
```

Scheduled to check US stock list on every Tue - Sat morning (SG Time, 6 am)

```bash
0 6 * * 2-6 ~/code/backtesting.py/run_check_bss_batch.sh
```

Scheduled to check US stock list on every Mon - Fri (SG Time 7:30 pm)

```bash
30 17 * * 1-5 ~/code/backtesting.py/run_check_bss_batch_asia.sh
```


Note on chart
-------------
    
    10 days MA above 20 days MA --> Bullish (not neccessaary, depend on stock)
    
    20 day MA above 10 days MA —> Bearish (not neccessaary, depend on stock)
    
    Arrow up or down doesn’t represent bullish or bearish
    
    Green & Red parallel short bar doesn’t represent bullish or bearish

```python
python check_bss.py TSLA
```

Enhancement
-----------
Added new table output in the console for ease of reference.
   Size negative value = short the stock

```python
+--------+---------------+--------------+--------------+-------------+
|   Size |   Entry Price |   Exit Price | Entry Time   | Exit Time   |
+========+===============+==============+==============+=============+
|    -52 |       190.997 |       193.13 | 2023-03-07   | 2023-03-29  |
+--------+---------------+--------------+--------------+-------------+
|     51 |       193.516 |       186.32 | 2023-03-29   | 2023-04-17  |
+--------+---------------+--------------+--------------+-------------+
|    -51 |       185.947 |       165.65 | 2023-04-17   | 2023-05-16  |
+--------+---------------+--------------+--------------+-------------+
|     63 |       165.981 |       279.56 | 2023-05-16   | 2023-07-20  |
+--------+---------------+--------------+--------------+-------------+
```


Read this [user guide](https://github.com/chancsc/backtesting.py/blob/master/doc/examples/Quick%20Start%20User%20Guide.ipynb) for more details usage


Usage (from orginal author)
-----
```python
from backtesting import Backtest, Strategy
from backtesting.lib import crossover

from backtesting.test import SMA, GOOG


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


bt = Backtest(GOOG, SmaCross, commission=.002,
              exclusive_orders=True)
stats = bt.run()
bt.plot()
```

Results in:

```text
Start                     2004-08-19 00:00:00
End                       2013-03-01 00:00:00
Duration                   3116 days 00:00:00
Exposure Time [%]                       94.27
Equity Final [$]                     68935.12
Equity Peak [$]                      68991.22
Return [%]                             589.35
Buy & Hold Return [%]                  703.46
Return (Ann.) [%]                       25.42
Volatility (Ann.) [%]                   38.43
Sharpe Ratio                             0.66
Sortino Ratio                            1.30
Calmar Ratio                             0.77
Max. Drawdown [%]                      -33.08
Avg. Drawdown [%]                       -5.58
Max. Drawdown Duration      688 days 00:00:00
Avg. Drawdown Duration       41 days 00:00:00
# Trades                                   93
Win Rate [%]                            53.76
Best Trade [%]                          57.12
Worst Trade [%]                        -16.63
Avg. Trade [%]                           1.96
Max. Trade Duration         121 days 00:00:00
Avg. Trade Duration          32 days 00:00:00
Profit Factor                            2.13
Expectancy [%]                           6.91
SQN                                      1.78
Kelly Criterion                        0.6134
_strategy              SmaCross(n1=10, n2=20)
_equity_curve                          Equ...
_trades                       Size  EntryB...
dtype: object
```
[![plot of trading simulation](https://i.imgur.com/xRFNHfg.png)](https://kernc.github.io/backtesting.py/#example)

Find more usage examples in the [documentation].


Features
--------
* Simple, well-documented API
* Blazing fast execution
* Built-in optimizer
* Library of composable base strategies and utilities
* Indicator-library-agnostic
* Supports _any_ financial instrument with candlestick data
* Detailed results
* Interactive visualizations

![xkcd.com/1570](https://imgs.xkcd.com/comics/engineer_syllogism.png)


Bugs
----
Before reporting bugs or posting to the
[discussion board](https://github.com/kernc/backtesting.py/discussions),
please read [contributing guidelines](CONTRIBUTING.md), particularly the section
about crafting useful bug reports and ```` ``` ````-fencing your code. We thank you!


Alternatives
------------
See [alternatives.md] for a list of alternative Python
backtesting frameworks and related packages.

[alternatives.md]: https://github.com/kernc/backtesting.py/blob/master/doc/alternatives.md
