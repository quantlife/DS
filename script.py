import pandas as pd
from pyalgotrade.oanda_v20.static_feed import build_feed
from pyalgotrade import bar
import os
import matplotlib.pyplot as plt
import numpy as np

def get_oanda_instrument(instrument, start_date, end_date, access_token):
    feed = build_feed(instrument, start_date, end_date, '.', access_token=access_token, frequency=bar.Frequency.DAY, fake_volume_amount_for_every_bar=1000000)
    files = [f for f in os.listdir('.') if os.path.isfile(f)]

    for i in files:
        if instrument in i:
            if start_date[0:10] in i:
                if end_date[0:10] in i:
                    df = pd.read_csv(i, index_col = 'Date', usecols = ['Date', 'Close'], parse_dates = True)
    return df

def get_data(symbols, start_date, end_date, access_token):
    start_index = str(start_date[0:10])
    end_index = str(end_date[0:10])
    dates = pd.date_range(start_index, end_index)
    result = pd.DataFrame(index=dates)

    for symbol in symbols:
        df_temp = get_oanda_instrument(symbol, start_date, end_date, access_token)
        df_temp = df_temp.rename(columns = {'Close' : symbol})
        result = result.join(df_temp, how='inner')

    return result

def plot_data(df, d_ret, symbols, start_date, end_date, access_token):
    df = get_data(symbols, start_date, end_date, access_token)
    df = df/df.ix[0]

    #plt.subplot(211)
    #plt.plot(df)
    #plt.subplot(212)
    #plt.plot(d_ret)

    df.plot()
    d_ret.plot()
    d_ret.hist(bins=50)
    d_ret.plot(kind='scatter', x='XAU_USD', y='USD_JPY')
    beta_JPY, alpha_JPY = np.polyfit(d_ret['XAU_USD'], d_ret['USD_JPY'],1)
    print 'beta=', beta_JPY
    print 'alpha=', alpha_JPY
    plt.plot(d_ret['XAU_USD'], beta_JPY*d_ret['XAU_USD'] + alpha_JPY, '-', color='r')
    plt.show()

def daily_returns(df):
    #daily_returns = df.copy()
    daily_returns = (df[1:] / df[:-1].values) - 1
    daily_returns.ix[0, :] = 0 # set daily returns for row 0 to 0
    # fx_data_df[1:] picks all the rows from 1 till the end
    # fx_data_df[:-1] picks all the rows from 0 till last-1
    # .values - the reason is to access the underlying numPy array
    # (when given 2 DataFrames Pandas will try to match each row based
    # on index when performing element wise arithmatic operations
    # so efforts of shifting values by 1 will be lost if we don't use .values attribute
    # daily_returns = (fx_data_df / fx_data_df.shift(1)) -  1 # much easier with Pandas!
    return daily_returns

def portfolio(daily_returns):#, weights):
    # this portfolio function gets tickers and weights tuple
    # and based on this data culates portfolio daily return data_frame

    weights = pd.DataFrame([[0.2, 0.2, 0.2, 0.2, 0.2]])
    weights = weights.T.iloc[:, 0]
    portfolio_cumulative_returns = daily_returns.sum(axis=0)
    daily_returns = daily_returns.mul(weights.values, axis=1)
    portfolio_daily_returns = daily_returns.sum(axis = 1)

    #portfolio_daily_returns = daily_returns
    s = portfolio_daily_returns.std()
    m = portfolio_daily_returns.mean()
    portfolio_sharpe = m/s
    return portfolio_daily_returns, portfolio_cumulative_returns, portfolio_sharpe



def scatterplots(daily_returns):
    # alpha - is the constant where the line intersects y-axis
    # alpha stands for premium
    # beta - is the slope of approximation line
    # beta stands for relation of the stock to the benchmark

    # slope != correlation
    # correlation - is how tightly the data fits the line

    daily_returns[['XAU_USD', 'USD_JPY']].plot(kind='scatter', x='XAU', y='JPY')
    plt.show()

def test_run():
    symbols = ['USD_JPY', 'GBP_USD', 'EUR_USD', 'USD_CAD', 'XAU_USD']
    access_token = "2083ca82dc72d18268041c6727fe9571-48085b81004b174dcb52d6db6a5a0df1"
    start_date = '2017-01-20T00:00:00.0Z'
    end_date = '2017-07-27T00:00:00.0Z'

    fx_data_df = get_data(symbols, start_date, end_date, access_token)

    dly_rtrns = daily_returns(fx_data_df)
    print dly_rtrns.head()

    p_daily, p_cumul, sharpe = portfolio(dly_rtrns)
    print p_daily.head()
    print '___________'
    print p_daily.tail()
    print '___________'
    print p_cumul.head()
    print sharpe
"""
    mean = dly_rtrns.mean()
    std = dly_rtrns.std()
    kurtosis = dly_rtrns.kurtosis()
    correlation = dly_rtrns.corr(method='pearson')
    print kurtosis
    # real world use of kurtosis:
    # if the distribution is gaussian, we sould say the returns
    # is normally distributed. However assuming ND ignores kurtosis -
    # the probability in the tails.
    # Measure of curtosis tells us how much different our histogram is from traditional gaussian distribution:
    #Positive Kurtosis = fat tails
    #Negative Kurtosis = skinny tails

    print mean
    print std
    print correlation

    #plot_data(fx_data_df, dly_rtrns, symbols, start_date, end_date, access_token)
    #scatterplots(dly_rtrns)
"""
if __name__ == "__main__": # if run standalone
    test_run()
