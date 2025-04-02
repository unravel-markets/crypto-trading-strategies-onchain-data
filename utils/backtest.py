import pandas as pd
def vectorized_backtest(price_series: pd.Series, signal_series: pd.Series, transaction_cost: float = 0.0005) -> pd.DataFrame:
    """
    Perform a vectorized backtest on price and signal series.
    
    Args:
        price_series (pd.Series): Price series of the asset
        signal_series (pd.Series): Signal series between -1 and 1
        transaction_cost (float): Transaction cost as a decimal (e.g., 0.001 for 0.1%)
    
    Returns:
        pd.DataFrame: DataFrame containing positions, returns, and cumulative returns
    """
    # Forward fill missing values
    price_series = price_series.ffill()
    signal_series = signal_series.ffill()
    
    # Calculate position changes (when signal changes)
    position_changes = signal_series.diff()
    
    # Calculate returns including transaction costs
    returns = price_series.pct_change()
    position_returns = signal_series.shift(1) * returns  # Shift to avoid look-ahead bias
    
    # Apply transaction costs only when position changes
    transaction_costs = abs(position_changes) * transaction_cost
    
    # Calculate net returns
    net_returns = position_returns - transaction_costs
    
    # Calculate cumulative returns
    cumulative_returns = (1 + net_returns).cumprod()
    
    # Create results DataFrame
    results = pd.DataFrame({
        'price': price_series,
        'signal': signal_series,
        'position': signal_series,
        'position_changes': position_changes,
        'returns': returns,
        'position_returns': position_returns,
        'transaction_costs': transaction_costs,
        'net_returns': net_returns,
        'cumulative_returns': cumulative_returns
    })
    
    return results