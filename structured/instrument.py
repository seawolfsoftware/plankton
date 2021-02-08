import oanda
import pandas as pd
import datetime

from enums.instrument import CandlestickGranularity, InstrumentName, PricingComponent


class Instrument(oanda.Oanda):
    """ Instrument is a Python wrapper class for instrument.py in Oanda v20 REST API. """

    def __init__(self, conf_file):
        super().__init__(conf_file)

    def get_candlestick_data_for_instrument(self, instrument, **kwargs):
        """

        :param instrument: InstrumentName(enum.Enum) (required)

        Kwargs:
            price:
                The Price component(s) to get candlestick data for. Can contain
                any combination of the characters "M" (midpoint candles) "B"
                (bid candles) and "A" (ask candles).
            granularity:
                The granularity of the candlesticks to fetch
            count:
                The number of candlesticks to return in the reponse. Count
                should not be specified if both the start and end parameters
                are provided, as the time range combined with the graularity
                will determine the number of candlesticks to return.
            fromTime:
                The start of the time range to fetch candlesticks for.
            toTime:
                The end of the time range to fetch candlesticks for.
            smooth:
                A flag that controls whether the candlestick is "smoothed" or
                not.  A smoothed candlestick uses the previous candle's close
                price as its open price, while an unsmoothed candlestick uses
                the first price from its time range as its open price.
            includeFirst:
                A flag that controls whether the candlestick that is covered by
                the from time should be included in the results. This flag
                enables clients to use the timestamp of the last completed
                candlestick received to poll for future candlesticks but avoid
                receiving the previous candlestick repeatedly.
            dailyAlignment:
                The hour of the day (in the specified timezone) to use for
                granularities that have daily alignments.
            alignmentTimezone:
                The timezone to use for the dailyAlignment parameter.
                Candlesticks with daily alignment will be aligned to the
                dailyAlignment hour within the alignmentTimezone.  Note that
                the returned times will still be represented in UTC.
            weeklyAlignment:
                The day of the week used for granularities that have weekly
                alignment.

        :endpoint /v3/instruments/{instrument}/candles
        :return:
        """

        response = self.ctx.instrument.candles(
            instrument, **kwargs)

        print('HTTP response status:', response.status)
        print('HTTP response headers:', response.headers)
        print('HTTP response body:', response.body)

        candles = [cs.dict() for cs in response.get('candles')]

        # returning df for testing right now, will remove
        dataframe = pd.DataFrame(response.get('candles'))

        return InstrumentName[instrument], \
            candles, \
            dataframe


x = Instrument('oanda.cfg')

print(x.get_candlestick_data_for_instrument(InstrumentName.CAD_JPY.name,
                                            granularity=CandlestickGranularity.M1.name,
                                            price=PricingComponent.BA.name,
                                            fromTime='2016-10-17'))
