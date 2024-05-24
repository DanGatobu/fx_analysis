def calculate_smma(data, period):
    """
    Calculate the Smoothed Moving Average (SMMA) for a given dataset and period.
    
    Parameters:
    data (pd.Series): Series of closing prices.
    period (int): The period over which to calculate the SMMA.
    
    Returns:
    pd.Series: Series containing the SMMA values.
    """
    smma = data.copy()
    smma.iloc[:period] = data.iloc[:period].mean()  # Initialize the first SMMA value as the SMA

    for i in range(period, len(data)):
        smma.iloc[i] = ((smma.iloc[i-1] * (period - 1)) + data.iloc[i]) / period

    return smma




def calculate_rsi(prices, period=14):

    # Calculate the daily price changes
    delta = prices.diff()
    
    # Calculate the gains (positive changes) and losses (negative changes)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    
    # Calculate the average gains and losses
    avg_gain = gain.rolling(window=period, min_periods=1).mean()
    avg_loss = loss.rolling(window=period, min_periods=1).mean()
    
    # Calculate the Relative Strength (RS)
    rs = avg_gain / avg_loss
    
    # Calculate the RSI
    rsi = 100 - (100 / (1 + rs))
    
    return rsi


