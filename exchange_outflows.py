import matplotlib.pyplot as plt

from utils.backtest import vectorized_backtest

import pandas as pd
import numpy as np
import requests

if __name__ == "__main__":

    long_only = True

    # call the unravel.markets API to retriece exchange outflow data for BTC between 2022-01-01 and 2024-01-01, with a demo API key
    url = 'https://unravel.markets/api/v1/normalized-series?ticker=BTC&series=exchange_outflow'
    headers = {
        'X-API-KEY': 'DEMO-KEY' # replace with your own API key, sign up at unravel.markets
    }
    response = requests.get(url, headers=headers).json()
    signal = pd.Series(response['data'], index=pd.to_datetime(response['index']))

    if long_only == False:
        # rescale signal to be between -1 and 1
        signal = signal * 2.0 - 1.0

    # fetch BTC price data for the same period from binance
    url = 'https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=1000&startTime=1640995261000'
    response = requests.get(url, headers=headers).json()
    price = pd.Series([float(x[4]) for x in response], index=pd.to_datetime([x[0] for x in response], unit='ms'))
    price = price.reindex(signal.index)

    # Run backtest
    results = vectorized_backtest(price, signal)
    
    # Print summary statistics
    print("\nBacktest Summary:")
    print(f"Total Return: {(results['cumulative_returns'].iloc[-1] - 1) * 100:.2f}%")
    print(f"Total Transaction Costs: {results['transaction_costs'].sum() * 100:.2f}%")
    
    print(f"Sharpe Ratio: {results['net_returns'].mean() / results['net_returns'].std() * np.sqrt(365)}")
    print(f"Volatility: {results['net_returns'].std() * np.sqrt(365) * 100:.2f}%")

    # Plot the results
    plt.figure(figsize=(12, 6))
    plt.plot(results['cumulative_returns'], label='Cumulative Returns')
    plt.plot(results['signal'], label='Signal')
    plt.legend()
    plt.show()