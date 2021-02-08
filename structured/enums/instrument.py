import enum


class PricingComponent(enum.Enum):
    """
    An enum class to represent Pricing Component.

    https://developer.oanda.com/rest-live-v20/primitives-df/#PricingComponent

    Can contain any combination of the characters:
    “M” (midpoint candles)
    “B” (bid candles) and
    “A” (ask candles).

    """
    M = "M",
    B = "B",
    A = "A",
    BA = "BA"


class CandlestickGranularity(enum.Enum):
    """
   An enum class to represent Candlestick Granularity.

   https://developer.oanda.com/rest-live-v20/instrument-df/#CandlestickGranularity

    S5 : 5 second candlesticks, minute alignment
    W: aligned to start of week
    M: aligned to first day of the month

    """
    S5 = "S5",
    S10 = "S10",
    S15 = "S15",
    S30 = "S30",
    M1 = "M1",
    M2 = "M2",
    M4 = "M4",
    M5 = "M5",
    M10 = "M10",
    M15 = "M15",
    M30 = "M30",
    H1 = "H1",
    H2 = "H2",
    H3 = "H3",
    H4 = "H4",
    H6 = "H6",
    H8 = "H8",
    H12 = "H12",
    D = "D",
    W = "W",
    M = "M"


class InstrumentName(enum.Enum):
    """
    An enum class to represent Instrument Names.

    https://developer.oanda.com/rest-live-v20/primitives-df/#InstrumentName

    A string containing the base currency and quote currency delimited by a “_”.

    """
    CAD_SGD = 'CAD_SGD',
    GBP_NZD = 'GBP_NZD',
    ZAR_JPY = 'ZAR_JPY',
    EUR_HUF = 'EUR_HUF',
    EUR_DKK = 'EUR_DKK',
    USD_MXN = 'USD_MXN',
    GBP_USD = 'GBP_USD',
    NZD_HKD = 'NZD_HKD',
    AUD_CHF = 'AUD_CHF',
    CAD_JPY = 'CAD_JPY',
    GBP_SGD = 'GBP_SGD',
    USD_SEK = 'USD_SEK',
    AUD_HKD = 'AUD_HKD',
    AUD_NZD = 'AUD_NZD',
    AUD_JPY = 'AUD_JPY',
    EUR_ZAR = 'EUR_ZAR',
    SGD_CHF = 'SGD_CHF',
    AUD_SGD = 'AUD_SGD',
    EUR_JPY = 'EUR_JPY',
    USD_CHF = 'USD_CHF',
    USD_TRY = 'USD_TRY',
    GBP_JPY = 'GBP_JPY',
    EUR_CZK = 'EUR_CZK',
    CHF_ZAR = 'CHF_ZAR',
    EUR_TRY = 'EUR_TRY',
    USD_JPY = 'USD_JPY',
    USD_NOK = 'USD_NOK',
    TRY_JPY = 'TRY_JPY',
    USD_DKK = 'USD_DKK',
    CHF_JPY = 'CHF_JPY',
    EUR_PLN = 'EUR_PLN',
    SGD_JPY = 'SGD_JPY',
    AUD_CAD = 'AUD_CAD',
    NZD_USD = 'NZD_USD',
    EUR_CHF = 'EUR_CHF',
    NZD_SGD = 'NZD_SGD',
    USD_HKD = 'USD_HKD',
    CHF_HKD = 'CHF_HKD',
    USD_CAD = 'USD_CAD',
    USD_CNH = 'USD_CNH',
    USD_CZK = 'USD_CZK',
    GBP_ZAR = 'GBP_ZAR',
    EUR_HKD = 'EUR_HKD',
    HKD_JPY = 'HKD_JPY',
    EUR_AUD = 'EUR_AUD',
    USD_SGD = 'USD_SGD',
    EUR_SEK = 'EUR_SEK',
    GBP_HKD = 'GBP_HKD',
    EUR_NZD = 'EUR_NZD',
    EUR_CAD = 'EUR_CAD',
    USD_HUF = 'USD_HUF',
    NZD_CAD = 'NZD_CAD',
    EUR_SGD = 'EUR_SGD',
    AUD_USD = 'AUD_USD',
    EUR_USD = 'EUR_USD',
    GBP_AUD = 'GBP_AUD',
    USD_PLN = 'USD_PLN',
    SGD_HKD = 'SGD_HKD',
    CAD_HKD = 'CAD_HKD',
    GBP_CAD = 'GBP_CAD',
    USD_SAR = 'USD_SAR',
    GBP_PLN = 'GBP_PLN',
    EUR_NOK = 'EUR_NOK',
    NZD_CHF = 'NZD_CHF',
    USD_ZAR = 'USD_ZAR',
    NZD_JPY = 'NZD_JPY',
    USD_THB = 'USD_THB',
    GBP_CHF = 'GBP_CHF',
    EUR_GBP = 'EUR_GBP',
    CAD_CHF = 'CAD_CHF'
