    # Portfolio statistics

    # daily_returns
    # cumulative_returns (port_val[-1]/port_val[0]) -1
    # avg_daily_returns = daily_ret.mean()
    # std_of_daily_ret = dailyret.std()

    # sharpe_ratio  (risk adjusted return)
    # this metric adjusts return for risk
    # * lower risk is better
    # * higher return is better
    # * Sharpe ratio also considers risk free rate of return
    #
    # Rp: portfolio return
    # Rf: fisk free rate
    # Qp: std dev of portfolio return
    # S = E{Rp - Rf}/std{Rp - Rf}
    # S = mean(d_ret - rf)/std(d_ret - Rf)
    #
    # sharpe ratio can vary widely depending on how frequently you sample
    # Original vision for sharpe ration is that it's an annual measure
    # Before sampling at frequencies other that annual we need to add an adjustment factor
    # SRannualized = K*SR
    # K = sqrt(#samples peer year)
    # 242, 52, 12
    #

