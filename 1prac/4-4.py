#4.4 copirka
import matplotlib.pyplot as plt

from dateutil import rrule
import collections
import yfinance
import datetime
import dateutil
import numpy


def loadCharts(instrument: str) ->dict:
    msft = yfinance.Ticker(instrument)
    return msft.history('1mo', '1mo', '2021-1-1', '2022-1-1')['Close']

aapl_stats = loadCharts('AAPL')
msft_stats = loadCharts('MSFT')
google_stats = loadCharts('GOOGL')

date_range = rrule.rrule(rrule.MONTHLY, dtstart = datetime.datetime(2021, 1, 1), until = datetime.datetime(2022, 1, 1))
date_values = []
aapl_values = []
msft_values = []
google_values = []

for date in date_range:
    date_values.append(date)
    aapl_values.append(aapl_stats.get(date))
    msft_values.append(msft_stats.get(date))
    google_values.append(google_stats.get(date))

    
plt.plot(date_values, aapl_values, color = 'r', label = 'AAPL')
plt.plot(date_values, msft_values, color = 'g', label = 'MSFT')
plt.plot(date_values, google_values, color = 'b', label = 'GOOGL')

plt.xlabel('Date')
plt.ylabel('Price')

plt.show();
