import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Step 1: Load metadata to create a mapping from symbols to business names
metadata = pd.read_csv('symbols_valid_meta.csv')
symbol_to_name_mapping = dict(zip(metadata['Symbol'], metadata['Security Name']))  # Maps "Symbol" to "Security Name"

# Step 2: Dynamically load stock data based on filenames in the STOCKS folder
def load_data(file_name, stocks_folder="STOCKS/"):
    file_path = os.path.join(stocks_folder, file_name)
    return pd.read_csv(file_path, parse_dates=['Date'])

# Map filenames to stock symbols (based on your STOCKS folder)
symbol_file_mapping = {
    'DVN': 'DVN.csv',
    'DUOT': 'DUOT.csv',
    'A': 'A.csv',
    'DVAX': 'DVAX.csv',
    'DVD': 'DVD.csv',
    'DVA': 'DVA.csv',
    'AA': 'AA.csv'
}

# Extract symbols and create a data dictionary
symbols = list(symbol_file_mapping.keys())
stock_data_dict = {symbol: load_data(symbol_file_mapping[symbol]) for symbol in symbols}

# Step 3: Compute daily returns and cumulative returns for each stock
for symbol, data in stock_data_dict.items():
    data['Daily Return'] = data['Adj Close'].ffill().pct_change()  # Replaced fillna(method='pad') with ffill()
    data['Cumulative Return'] = (1 + data['Daily Return']).cumprod()

# Step 4: Plot stock prices and cumulative returns over time
fig, axes = plt.subplots(2, 1, figsize=(10, 8))

for symbol, data in stock_data_dict.items():
    business_name = symbol_to_name_mapping.get(symbol, symbol)  # Get business name; fallback to symbol
    # Plot adjusted close prices
    axes[0].plot(data['Date'], data['Adj Close'], label=business_name)
    # Plot cumulative returns
    axes[1].plot(data['Date'], data['Cumulative Return'], label=business_name)

axes[0].set_title('Adjusted Close Prices')
axes[0].set_xlabel('Date')
axes[0].set_ylabel('Price')
axes[0].legend()

axes[1].set_title('Cumulative Returns')
axes[1].set_xlabel('Date')
axes[1].set_ylabel('Cumulative Return')
axes[1].legend()

plt.tight_layout()
plt.show()

# Step 5: Compare multiple stocks using subplots
fig, subplot_axes = plt.subplots(len(symbols), 1, figsize=(10, 12))

for idx, (symbol, data) in enumerate(stock_data_dict.items()):
    business_name = symbol_to_name_mapping.get(symbol, symbol)  # Get business name; fallback to symbol
    subplot_axes[idx].plot(data['Date'], data['Adj Close'], label=business_name)
    subplot_axes[idx].set_title(f'Adjusted Close Price: {business_name}')
    subplot_axes[idx].set_xlabel('Date')
    subplot_axes[idx].set_ylabel('Price')
    subplot_axes[idx].legend()

plt.tight_layout()
plt.show()

# Step 6: Identify and annotate peaks and drops for each stock
for symbol, data in stock_data_dict.items():
    business_name = symbol_to_name_mapping.get(symbol, symbol)  # Get business name; fallback to symbol
    max_price_date = data.loc[data['Adj Close'].idxmax(), 'Date']
    max_price = data['Adj Close'].max()
    min_price_date = data.loc[data['Adj Close'].idxmin(), 'Date']
    min_price = data['Adj Close'].min()

    plt.figure(figsize=(10, 6))
    plt.plot(data['Date'], data['Adj Close'], label=business_name)
    plt.title(f'{business_name} Adjusted Close Prices with Peaks and Drops')
    plt.xlabel('Date')
    plt.ylabel('Adjusted Close Price')

    # Annotate peak
    plt.annotate(f'Peak: {max_price:.2f}',
                 xy=(max_price_date, max_price),
                 xytext=(max_price_date, max_price + 50),
                 arrowprops=dict(facecolor='green', shrink=0.05))

    # Annotate drop
    plt.annotate(f'Drop: {min_price:.2f}',
                 xy=(min_price_date, min_price),
                 xytext=(min_price_date, min_price - 50),
                 arrowprops=dict(facecolor='red', shrink=0.05))

    plt.legend()
    plt.show()
