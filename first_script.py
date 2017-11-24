import pandas as pd
from pyalgotrade.oanda_v20.static_feed import build_feed
from pyalgotrade import bar
import os

def get_oanda_instrument(instrument, start_date, end_date, access_token):
    emulate_calls = False
    feed = build_feed(instrument, start_date, end_date, '.', access_token, frequency = bar.Frequency.DAY, fake_volume_amount_for_every_bar=1000000)

    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    if instrument in files:
        if start_date in files:
            if end_date in files:
                f = files
                print f

    df = pd.read_csv("{}".format(f))
    return df


def test_run():
    instrument = "EUR_USD"
    access_token = "2083ca82dc72d18268041c6727fe9571-48085b81004b174dcb52d6db6a5a0df1"
    #file_name = 'EUR_USD-2016-01-20T00.00.00.000000Z-2017-07-27T00.00.00.000000Z-86400-None-oanda'
    start_date = '2017-01-20T00:00:00.0Z'
    end_date = '2017-07-27T00:00:00.0Z'

    x = get_oanda_instrument(instrument, start_date, end_date, access_token)
    print type(x)
    print x.head()

if __name__ == "__main__": # if run standalone
    test_run()

"""
def get_data(symbols, dates, access_token):
    #Read FX data (close) for given symbols from CSV files.
    df = pd.DataFrame(index=dates)

    for symbol in symbols:
        df_temp = pd.read_csv(get_oanda_instrument(symbol, access_token), index_col='Date',
                              parse_dates=True, usecols=['Date', 'Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp)
        if symbol == 'SPY':  # drop dates SPY did not trade
            df = df.dropna(subset=["SPY"])

    return df
"""




"""
    df = pd.read_csv("{}.csv".format(file_name))
    print df.head()
    print type(df)

    mean_vol = get_mean_volume(file_name)
    print mean_vol

    max_close = get_max_close(file_name)
    print max_close

    symbols = ('EUR_USD', 'BB')
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        for s in symbols:
            if s in f:
                print f

"""


    #do something
    #print inspect.stack()[0][1]
    #print inspect.getfile(inspect.currentframe())

"""
    df = pd.read_csv("data/IBM.csv")
    # TODO: Your code here
    df[['High', 'Close']].plot()
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.title('Histogram of IQ')
    plt.show()  # must be called to show plots
    for symbol in ['AAPL', 'IBM']:
        print
        "Mean Volume"
        print
        symbol, get_mean_volume(symbol)
    """

"""
def test_run():
    #function called by Test Run.
    for symbol in ['AAPL', 'IBM']:
        print "Max close"
        print symbol, get_max_close(symbol)
"""

def select_rows():
    df = pd.read.csv("data/AAPL.csv")
    print df[10:21] # rows between index 10 and 20





def get_max_close(symbol):
    """Return the maximum closing value for stock indicated by symbol.

    Note: Data for a stock is stored in file: data/<symbol>.csv
    """

    df = pd.read_csv("{}.csv".format(symbol)) # read in data
    return df['Close'].max()  # compute and return max

def get_mean_volume(symbol):
    """Return the mean volume for stock indicated by symbol.
    Note: Data for a stock is stored in file: data/<symbol>.csv
    """
    df = pd.read_csv("{}.csv".format(symbol))  # read in data
    return df['Volume'].mean()  # TODO: Compute and return the mean volume for this stock
