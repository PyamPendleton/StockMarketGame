import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

####################################
# Fibonacci Retracement calculator #
def fib_retracement(name, period, interval):
  ticker = yf.Ticker(name)
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

  df['Close'].plot(title="Fibonacci Retracement overlayed on "+name+" prices")
  start_date = df.index[min(highest_swing,lowest_swing)]
  end_date = df.index[max(highest_swing,lowest_swing)]
  for i in range(len(levels)):
    plt.hlines(levels[i],start_date, end_date,label="{:.1f}%".format(ratios[i]*100),colors=colors[i], linestyles="dashed")

  plt.legend()
  plt.savefig("fib_retrace_"+name+".png")
####################################


####################################
# Golden Cross calculator          #
def golden_cross(name, period, interval):
  df = yf.download(name, period=period, interval=interval)

  # We compute our simple moving averages
  df["50_sma"] = df["Adj Close"].rolling(50).mean()
  df["200_sma"] = df["Adj Close"].rolling(200).mean()

  # This is important so that we have both SMA starting a the same time.
  df = df.dropna() 

  # We compute our 50 SMA > 200 SMA
  df["golden_cross_signal"] = df.apply(lambda row: 1 if row[f"50_sma"] > row[f"200_sma"]  else 0, axis=1)

  # To store when our golden cross are happening
  list_golden_cross_ts = []
  first_golden_cross = False

  # We take the date where the first 50 SMA > 200 SMA appears
  for idx, each in df["golden_cross_signal"].iteritems():
      if each == 1:
          # If its the first golden cross we see we add the timestamp
          if first_golden_cross:
              list_golden_cross_ts.append(idx)
              first_golden_cross = False
      else:
          first_golden_cross = True

  # We plot our prices / SMAs and Golden Cross dates
  fig, axes = plt.subplots(1,1, figsize=(8,4))
  df[["200_sma","50_sma","Adj Close"]].plot(figsize=(8,4), grid=True, title="SMA 50 vs SMA 200 on "+name+" prices", ax=axes)

  for each in list_golden_cross_ts:
      axes.axvline(x=each, label="Golden Cross", c="yellow")
      
  axes.legend()
  fig.tight_layout()
  plt.savefig("golden_cross_"+name+".png")
####################################

