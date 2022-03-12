import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import urllib.request
import urllib.parse
import yfinance as yf


# Fibonacci Retracement calculator
def fib_retracement(ticker, period, interval):
 
  df = ticker.history(period=period,interval=interval)
  highest_swing = -1
  lowest_swing = -1

  for i in range(1,df.shape[0]-1):
    if df['High'][i] > df['High'][i-1] and df['High'][i] > df['High'][i+1] and (highest_swing == -1 or df['High'][i] > df['High'][highest_swing]):
      highest_swing = i
    if df['Low'][i] < df['Low'][i-1] and df['Low'][i] < df['Low'][i+1] and (lowest_swing == -1 or df['Low'][i] < df['Low'][lowest_swing]):
        lowest_swing = i


  ratios = [0,0.236, 0.382, 0.5 , 0.618, 0.786,1]
  colors = ["black","r","g","b","cyan","magenta","yellow"]
  levels = []

  max_level = df['High'][highest_swing]
  min_level = df['Low'][lowest_swing]

  for ratio in ratios:
    if highest_swing > lowest_swing: # Uptrend
      levels.append(max_level - (max_level-min_level)*ratio)
    else: # Downtrend
      levels.append(min_level + (max_level-min_level)*ratio)


  plt.rcParams['figure.figsize'] = [12, 7]

  plt.rc('font', size=14)

  plt.plot(df['Close'])
  start_date = df.index[min(highest_swing,lowest_swing)]
  end_date = df.index[max(highest_swing,lowest_swing)]
  for i in range(len(levels)):
    plt.hlines(levels[i],start_date, end_date,label="{:.1f}%".format(ratios[i]*100),colors=colors[i], linestyles="dashed")

  plt.legend()
  plt.show()




##############
##   CODE   ##
##############

print('Enter a ticker symbol:')
name = input()
ticker = yf.Ticker(name)
print('How far back would you like to look? (ex. 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max)')
period = input()
print('How many data points? (ex. 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo)')
interval = input()
print(ticker.history(period=period,interval=interval))
fib_retracement(ticker, period, interval)



##############
##   TEST   ##
##############

# ticker returns as object
msft = yf.Ticker("name")

# Most of the data functions return pandas DataFrames
msft_hist = msft.history(period="1mo")
print(msft_hist)

# date seems to remain even when we take a column by itself
print(msft_hist['Open'])