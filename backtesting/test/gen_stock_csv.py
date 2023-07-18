# usage:
# python gen_stock_csv.py --stock=TSLA --sdate=01/01/2020 --edate=15/07/2023

import argparse
import yfinance as yf
import pandas as pd

def download_stock_data(symbol, start_date, end_date):
    # Download stock data
    data = yf.download(symbol, start=start_date, end=end_date)

    # Select required columns
    data = data[['Open', 'High', 'Low', 'Close', 'Volume']]

    # Reset index
    data.reset_index(inplace=True)

    # Save data to CSV
    data.to_csv(f'{symbol}.csv', index=False)

    print('Data downloaded successfully.')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download daily stock data')
    parser.add_argument('--stock', type=str, help='Stock symbol')
    parser.add_argument('--sdate', type=str, help='Start date (DD/MM/YYYY)')
    parser.add_argument('--edate', type=str, help='End date (DD/MM/YYYY)')
    args = parser.parse_args()

    stock_symbol = args.stock
    start_date = pd.to_datetime(args.sdate, dayfirst=True).strftime('%Y-%m-%d')
    end_date = pd.to_datetime(args.edate, dayfirst=True).strftime('%Y-%m-%d')

    download_stock_data(stock_symbol, start_date, end_date)
