# this is the standalone (SA) stock data retrieval program

# usage:
# python get_stock_data_SA.py --stock=TSLA --sdate=01/01/2020 --edate=15/07/2023
# can also just pass-in stock ticker, default to YTD data
# python get_stock_data_SA.py --stock=TSLA


import argparse
import os
import yfinance as yf
import pandas as pd
from datetime import date

def download_stock_data(symbol, start_date, end_date):
    # Download stock data
    data = yf.download(symbol, start=start_date, end=end_date)

    # Select required columns
    data = data[['Open', 'High', 'Low', 'Close', 'Volume']]

    # Reset index
    data.reset_index(inplace=True)

    # Define the sub-directory path
    sub_directory = 'backtesting/test/'

    # Create the sub-directory if it doesn't exist
    if not os.path.exists(sub_directory):
        os.makedirs(sub_directory)

    # Delete existing CSV file if it exists
    csv_file = os.path.join(sub_directory, f'{symbol}.csv')
    if os.path.exists(csv_file):
        os.remove(csv_file)
        print('Existing CSV file deleted.')

    # Save data to CSV
    data.to_csv(csv_file, index=False)

    print('Data downloaded successfully.')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download daily stock data')
    parser.add_argument('--stock', type=str, help='Stock symbol', required=True)
    parser.add_argument('--sdate', type=str, help='Start date (DD/MM/YYYY)', default='01/01/' + str(date.today().year))
    parser.add_argument('--edate', type=str, help='End date (DD/MM/YYYY)', default=date.today().strftime('%d/%m/%Y'))
    args = parser.parse_args()

    stock_symbol = args.stock
    start_date = pd.to_datetime(args.sdate, dayfirst=True).strftime('%Y-%m-%d')
    end_date = pd.to_datetime(args.edate, dayfirst=True).strftime('%Y-%m-%d')

    download_stock_data(stock_symbol, start_date, end_date)
