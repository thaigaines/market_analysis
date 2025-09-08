import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

nasdaq_listed = pd.read_csv('./data/nasdaq-listed.csv')
valid_tickers = set(nasdaq_listed['Symbol'])
valid_periods = ['5d', '1mo', '3mo', '1y']
valid_responses = ['y', 'n']

def is_valid_input(valid_items, prompt, normalize=str): # passing in function parameter w/ a default behavior of str() which converts to string (does nothing). Optional parameter
    while True:
        user_input = normalize(input(prompt))
        if user_input in valid_items:
            return user_input
        print("Invalid input.")


# Check for valid ticker
ticker_input = is_valid_input(valid_tickers, "Ticker: ", str.upper)

# Prompt about another ticker
add_another = is_valid_input(['y', 'n'], "Add another to compare? (y/n): ", str.lower)

# Check valid input for the period
period_input = is_valid_input(valid_periods, f"Period ({', '.join(valid_periods)}): ", str.lower)

# Plot visual elements
plt.figure(figsize=(12, 6))
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.grid()

# Run response scenarios

## Single stock
if add_another == 'n':
    # Ticker class object
    ticker = yf.Ticker(ticker_input)

    # Pandas df of activity throughout past period
    data = ticker.history(period=period_input, interval="1d")

    # Plot points
    plt.plot(data.index, data['Open'], label="Opening Price")
    plt.plot(data.index, data['Close'], label="Close Price") # Create line plot with these values along each axis

    plot_title = f"{ticker_input} Prices at Open / Close"
    plt.title(plot_title)
    plt.legend(title="Legend")


## Stock comparison
else:
    ticker_input2 = is_valid_input(valid_tickers, "Ticker: ", str.upper)

    # Ticker objects and pandas df's of past period
    ticker1, ticker2 = yf.Ticker(ticker_input), yf.Ticker(ticker_input2)
    data1, data2 = ticker1.history(period=period_input, interval="1d"), ticker2.history(period=period_input, interval="1d")

    plt.plot(data1.index, data1['Close'], label=f"{ticker_input} Close Price")
    plt.plot(data2.index, data2['Close'], label=f"{ticker_input2} Close Price")

    plot_title = f"{ticker_input} & {ticker_input2} Prices at Close"
    plt.title(plot_title)
    plt.legend(title="Legend")


# Show plot
plt.show()