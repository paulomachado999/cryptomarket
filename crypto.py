import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
import cryptocompare
from datetime import datetime, timedelta

# Get all available cryptocurrencies
all_crypto = cryptocompare.get_coin_list()
crypto_tickers = list(all_crypto.keys())

# Function to get historical data for a cryptocurrency
def get_crypto_data(ticker, start_date, end_date):
    data = yf.download(f"{ticker}-USD", start=start_date, end=end_date)
    return data

# Function to plot the price history of a cryptocurrency
def plot_crypto_price(data):
    plt.figure(figsize=(12, 6))
    data['Close'].plot()
    plt.title('Cryptocurrency Price History')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.show()

# Function to plot the price and volume of a cryptocurrency
def plot_crypto_price_volume(data):
    fig, ax1 = plt.subplots(figsize=(12, 6))
    ax1.plot(data.index, data['Close'], color='blue')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Price (USD)', color='blue')
    ax1.tick_params('y', colors='blue')

    ax2 = ax1.twinx()
    ax2.bar(data.index, data['Volume'], color='green')
    ax2.set_ylabel('Volume', color='green')
    ax2.tick_params('y', colors='green')

    plt.title('Cryptocurrency Price and Volume')
    plt.show()

# Example usage
start_date = datetime.now() - timedelta(days=365)
end_date = datetime.now()
bitcoin_data = get_crypto_data('BTC', start_date, end_date)
plot_crypto_price(bitcoin_data)
plot_crypto_price_volume(bitcoin_data)
