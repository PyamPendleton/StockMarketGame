import numpy as np
import pandas as pd
import matplotlib
import urllib.request
import urllib.parse
import yfinance as yf



# with urllib.request.urlopen('http://python.org/') as response:
# html = response.read()

# msft returns as object
msft = yf.Ticker("MSFT")
# Most of the data functions return pandas DataFrames
msft_hist = msft.history(period="1mo")
print(msft_hist)

# date seems to remain even when we take a column by itself
print(msft_hist['Open'])

