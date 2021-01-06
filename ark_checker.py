import csv
import yfinance as yf
import pandas as pd
import json
import matplotlib

with open('arkk.csv') as csvfile:
    df = pd.read_csv(csvfile)
    for ticker in df["ticker"].dropna():
        print(ticker)
        stock = yf.Ticker(ticker.split()[0])
        df['sector'] = stock.info["sector"]

    df["ticker"].hist(by=df['sector'])