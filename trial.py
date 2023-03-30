import matplotlib.pyplot as plt
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yfin


yfin.pdr_override()

def plot_stock(stock_name, time_period):
    # Fetch stock data
    end_date = pd.to_datetime('today')
    start_date = end_date - pd.to_timedelta(time_period, unit='D')
    stock_data = pdr.get_data_yahoo(stock_name, start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))

    # Plot stock data
    plt.figure(figsize=(10, 5))
    plt.plot(stock_data['Close'])
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.title(f'{stock_name} Stock Prices for the Last {time_period} Days')
    plt.grid()
    plt.show()


plot_stock("AAPL", 60)

