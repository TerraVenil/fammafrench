import pandas as pd
from pyfolio.timeseries import rolling_fama_french


def create_returns_plot():
    returns = pd.read_csv('SB1(daily_returns).csv', index_col=[0], parse_dates=True)
    rolling_fama_french(returns, factor_returns=None, rolling_window=len(returns))
    

if __name__ == "__main__":
    create_returns_plot()