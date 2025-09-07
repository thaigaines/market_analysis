import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

nasdaq_listed = pd.read_csv('./data/nasdaq-listed.csv')
valid_tickers = set(nasdaq_listed['Symbol'])
valid_periods = ['1d', '5d', '1mo', '3mo', '1y']

# Take ticker input
ticker_input = input("Ticker: ").upper()
# Check for validity
while ticker_input not in valid_tickers:
    print("Invalid ticker.")
    ticker_input = input("Ticker: ").upper()

# Take input for the period
period_input = input(f"Period ({', '.join(valid_periods)}): ").lower()
while period_input not in valid_periods:
    print("Invalid Input.")
    period_input = input("Period (1d, 5d, 1mo, 3mo, 1y): ").lower()

# Create ticker class object
ticker = yf.Ticker(ticker_input)
 # Pandas dataframe of activity throughout past month
data = ticker.history(period=period_input, interval="1d")

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