# Importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

# setting the start and end date
start_date = "2023-01-01"
end_date = pd.Timestamp.today().strftime('%Y-%m-%d')  # Get today's date
# set stock data
ticker = "BTC-USD"
df = yf.download(ticker, start=start_date, end=end_date, auto_adjust=True)

print(df.head())