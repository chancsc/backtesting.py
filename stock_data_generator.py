# this file as a lib / support file to be call by another script, to generate a csv file
# for the selected stock
# Example usage:
# generate_stock_data('TSLA')


import os
import yfinance as yf
import pandas as pd
from datetime import date, datetime

def generate_stock_data(symbol, start_date=None, end_date=None):
    if start_date is None:
        start_date = '01/01/' + str(date.today().year)
    if end_date is None:
        end_date = date.today().strftime('%d/%m/%Y')

    start_date = pd.to_datetime(start_date, dayfirst=True).strftime('%Y-%m-%d')
    end_date = pd.to_datetime(end_date, dayfirst=True).strftime('%Y-%m-%d')

    # Define the sub-directory path
    sub_directory = 'backtesting/test/'

    # Create the sub-directory if it doesn't exist
    if not os.path.exists(sub_directory):
        os.makedirs(sub_directory)

    # Check if the CSV file exists or its date is older than today
    csv_file = os.path.join(sub_directory, f'{symbol}.csv')
    if not os.path.exists(csv_file) or datetime.fromtimestamp(os.path.getmtime(csv_file)).date() < date.today():
        if os.path.exists(csv_file):
            os.remove(csv_file)
            print('Existing CSV file deleted.')

        # Download stock data
        data = yf.download(symbol, start=start_date, end=end_date)
        # Select required columns
        data = data[['Open', 'High', 'Low', 'Close', 'Volume']]
        # Reset index
        data.reset_index(inplace=True)
        # Save data to CSV
        data.to_csv(csv_file, index=False)

        print('Data downloaded successfully.')
    else:
        print('CSV file is up to date.')


# Generate stock data with default parameters
#generate_stock_data('TSLA')
