import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

nasdaq_listed = pd.read_csv('./data/nasdaq-listed.csv')
valid_tickers = set(nasdaq_listed['Symbol'])

# Create ticker variable using user input
ticker_input = input("Ticker: ").upper()

# Check validity against valid tickers
while ticker_input not in valid_tickers:
    print("Invalid Ticker.")
    ticker_input = input("Ticker: ").upper()

ticker = yf.Ticker(ticker_input)
data = ticker.history(period="1mo", interval="1d") # Pandas dataframe of activity throughout the past month

plt.figure(figsize=(12, 6))
# Line plot
plt.plot(data.index, data['Open'], label="Opening Price")
plt.plot(data.index, data['Close'], label="Closing Price")

# Visual additions
plt.xlabel('Date')
plt.ylabel('Price (USD)')

plot_title = f"{ticker_input} Prices at Close"
plt.title(plot_title)
plt.legend(title="Legend")
plt.grid()

# Show plot
plt.show()