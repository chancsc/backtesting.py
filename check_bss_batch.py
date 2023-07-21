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

Sample data of 'stock_list.txt':
AAPL
ABNB
AMZN

"""

import subprocess
import json
import argparse

def execute_check_bss(stock_ticker):
    cmd = f"python check_bss.py {stock_ticker}"
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running check_bss.py with {stock_ticker}:")
        print(e)

def main():
    parser = argparse.ArgumentParser(description='Check BSS for stock tickers.')
    parser.add_argument('--file', type=str, default='stock_list_us.json',
                        help='Path to JSON file containing stock data (default: stock_list_us.json)')
    args = parser.parse_args()

    with open(args.file, "r") as file:
        stock_data = json.load(file)

    for stock in stock_data:
        ticker = stock["ticker"]
        name = stock["name"]
        print(f"Checking for: {name}")
        execute_check_bss(ticker)

if __name__ == "__main__":
    main()
