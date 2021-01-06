import csv
import yfinance as yf

arkk = yf.Ticker("ARKK")
arkq = yf.Ticker("ARKQ")
arkw = yf.Ticker("ARKW")
arkf = yf.Ticker("ARKF")

print(arkk.info)
print(arkq.info)
print(arkw.info)
print(arkf.info)