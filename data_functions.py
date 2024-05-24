import pandas as pd
import numpy as np
import MetaTrader5 as mt5
import datetime
import random
import string


def get_data(currency):
    mt5.initialize()
    ohlc_data = pd.DataFrame(mt5.copy_rates_range(currency, mt5.TIMEFRAME_M5, datetime.datetime(2015, 1, 1), datetime.datetime.now()))
    ohlc_data.rename(columns={'open': 'Open', 'high': 'High', 'low': 'Low', 'close': 'Close'}, inplace=True)
    ohlc_data.dropna(inplace=True)

    return ohlc_data


def calc_prof(enter,close):
    prof=enter-close
    return prof


def candletype(candle):
    if candle['Close']>candle['Open']:
        
        return 1
    else:
        return -1
    
    
    
def generate_random_id(length=3):
    characters = string.ascii_letters + string.digits
    random_id = ''.join(random.choice(characters) for _ in range(length))
    return random_id
