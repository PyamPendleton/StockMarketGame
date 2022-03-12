import yfinance as yf
import finance_functions as ff
import urllib.request
import urllib.parse

##############
##   CODE   ##
##############

print('Enter a ticker symbol:')
name = input()
print('How far back would you like to look? (possible: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max)')
period = input()
print('How many data points? (possible: 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo)')
interval = input()
print(yf.Ticker(name).history(period=period,interval=interval))
ff.fib_retracement(name, period, interval)
# ff.golden_cross(name, period, interval)





##############
##   TEST   ##
##############

# # ticker returns as object
# msft = yf.Ticker("name")

# # Most of the data functions return pandas DataFrames
# msft_hist = msft.history(period="1mo")
# print(msft_hist)

# # date seems to remain even when we take a column by itself
# print(msft_hist['Open'])