"""
Program: Check Buy/Sell Signal in batch

Description:
This program reads a list of stock tickers from 'stock_list_us.json' and calls the 'check_bss.py' script
for each stock ticker, passing it as a parameter. The 'check_bss.py' script is responsible for 
checking Buy/Sell signals (BSS) for a given stock.

Instructions:
1. Ensure 'check_bss.py' and 'stock_list_us.json' are present in the same directory as this script.
2. 'check_bss.py' should accept a single argument (stock ticker) when executed from the command line.
   Example: python check_bss.py TSLA
3. The output of 'check_bss.py' will be displayed in the terminal for each stock ticker.

Sample data of 'stock_list_us.json':
AAPL
ABNB
AMZN

Usage:

Parameter
file: optional, if omitted, default to stock_list_us.json
year: optional, if omitted, default to current year

Note: 
if runnign the batch multiple time a day, please manually remove the csv file to force refresh / redownload

$ ptyon check_bss_batch.py
$ ptyon check_bss_batch.py --file=stock_list_asia.json
$ ptyon check_bss_batch.py --file=stock_list_test.json --year=2022
$ ptyon check_bss_batch.py --year=2022 > PL.txt 2>&1   (<-- output the result to PL.txt)
"""

import subprocess
import json
import argparse
import datetime

def execute_check_bss(stock_ticker, year=None):
    # batch mode, don't need to display the BSS table in console, and don't open browser
    cmd = f"python check_bss.py {stock_ticker} --browser=0 --table=0"

    if year:
        # Modify the command to include the year value
        cmd += f" --year={year}"
        
    # print("cmd = ", {cmd})
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running check_bss.py with {stock_ticker}:")
        print(e)

def main():
    parser = argparse.ArgumentParser(description='Check BSS for stocks.')
    parser.add_argument('--file', type=str, default='stock_list_us.json',
                        help='Path to JSON file containing stock data (default: stock_list_us.json)')
    parser.add_argument('--year', type=int, default=datetime.date.today().year,
                        help='Year for checking BSS (optional)')
    args = parser.parse_args()

    with open(args.file, "r") as file:
        stock_data = json.load(file)

    for stock in stock_data:
        ticker = stock["ticker"]
        execute_check_bss(ticker, args.year)
        # name = stock["name"]
        # print("")
        # print(f"Checking for: {name}")


if __name__ == "__main__":
    main()
