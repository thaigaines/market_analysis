import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

nasdaq_listed = pd.read_csv('./data/nasdaq-listed.csv')
valid_tickers = set(nasdaq_listed['Symbol'])

# Ticker class object
ticker_input = input("Ticker: ").upper()
# Check for validity
while ticker_input not in valid_tickers:
    print("Invalid ticker.")
    ticker_input = input("Ticker: ").upper()

period_input = input("Period (1d, 5d, 1mo, 3mo, 1y): ").lower()
while period_input not in ['1d', '5d', '1mo', '3mo', '1y']:
    print("Invalid Input.")
    period_input = input("Period (1d, 5d, 1mo, 3mo, 1y): ").lower()

ticker = yf.Ticker(ticker_input)
data = ticker.history(period=period_input, interval="1d") # Pandas dataframe of activity throughout past month

plt.figure(figsize=(12, 6))
# Line Plot
plt.plot(data.index, data['Open'], label="Opening Price")
plt.plot(data.index, data['Close'], label="Close Price") # Create line plot with these values along each axis
# Visuals
plt.xlabel('Date')
plt.ylabel('Price (USD)')

plot_title = f"{ticker_input} Prices at Open / Close"
plt.title(plot_title)
plt.legend(title="Legend")
plt.grid()

plt.show()