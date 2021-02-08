import oanda
import pandas as pd
import datetime

from enums.instrument import CandlestickGranularity


class Instrument(oanda.Oanda):
    """ Instrument is a Python wrapper class for instrument.py in Oanda v20 REST API. """

    def __init__(self, conf_file):
        super().__init__(conf_file)

    # /v3/instruments/{instrument}/candles
    def retrieve_data(self, instrument, granularity, price):
        raw = self.ctx.instrument.candles(
            instrument=instrument,
            # fromTime=start, toTime=end,
            granularity=granularity, price=price)
        candles_raw = raw.get('candles')
        candles = [cs.dict() for cs in candles_raw]
        instrument = raw.get('instrument')
        granularity = raw.get('granularity')
        return instrument, granularity, candles

        # if price == 'A':
        #     for cs in raw:
        #         cs.update(cs['ask'])
        #         del cs['ask']
        # elif price == 'B':
        #     for cs in raw:
        #         cs.update(cs['bid'])
        #         del cs['bid']
        # elif price == 'M':
        #     for cs in raw:
        #         cs.update(cs['mid'])
        #         del cs['mid']
        # else:
        #     raise ValueError("price must be either 'B', 'A' or 'M'.")
        # if len(raw) == 0:
        #     return pd.DataFrame()  # return empty DataFrame if no data
        # data = pd.DataFrame(raw)
        # data['time'] = pd.to_datetime(data['time'])
        # data = data.set_index('time')
        # data.index = pd.DatetimeIndex(data.index)
        # for col in list('ohlc'):
        #     data[col] = data[col].astype(float)
        # return data


# start = datetime.datetime(2005, 5, 30)
# end = datetime.datetime(2010, 5, 17)

x = Instrument('oanda.cfg')
print(x.retrieve_data('EUR_USD', 'S5', 'M'))
print(CandlestickGranularity.H1)
print(repr(CandlestickGranularity.H1))
print(type(CandlestickGranularity.H1.name))
