import oanda
import numpy as np
import pandas as pd
from pylab import mpl, plt



oanda = oanda.Oanda('oanda.cfg')

ins = oanda.get_instruments()


# retrieves EOD data and stores it in a df object
raw = pd.read_csv('pyalgo_eikon_eod_data.csv', index_col=0, parse_dates=True).dropna()
# raw.info()

symbol = 'EUR='

# the time series data for the specified symbol is selected from the original df
data = pd.DataFrame(raw[symbol])

# renames the single column to 'price'
data.rename(columns={symbol: 'price'}, inplace=True)


data['SMA1-shorter'] = data['price'].rolling(42).mean()
data['SMA2-longer'] = data['price'].rolling(252).mean()

# data.plot(title='EUR/USD | 42 & 252 days SMAs', figsize=(10, 6))


# Market positioning over time based on the strategy with two SMAs
data['position'] = np.where(data['SMA1-shorter'] > data['SMA2-longer'], 1, -1)
# data.dropna(inplace=True)
# data['position'].plot(ylim=[-1.1, 1.1],
#                       title='Market Positioning',
#                       figsize=(10, 6))

data['returns'] = np.log(data['price'] / data['price'].shift(1))

# Plots the log returns as a histogram (freq distribution)
# data['returns'].hist(bins=35, figsize=(10, 6))

data['strategy'] = data['position'].shift(1) * data['returns']
# print(data[['returns', 'strategy']].sum())
print('~~~~~~~~~~~~')
print(data[['returns', 'strategy']].sum().apply(np.exp))

plt.style.use('seaborn')
mpl.rcParams['savefig.dpi'] = 300
mpl.rcParams['font.family'] = 'serif'






plt.show()
