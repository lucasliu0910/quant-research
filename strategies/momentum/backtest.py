import pandas as pd

def backtest(df: pd.DataFrame):
    """
    df needs:
    - Close
    - signal
    """

    df = df.copy()

    # 1. daily returns
    df["returns"] = df["Close"].pct_change()

    # 2. avoid look-ahead bias
    df["strategy_returns"] = df["signal"].shift(1) * df["returns"]

    # 3. cumulative returns
    df["equity_curve"] = (1 + df["strategy_returns"]).cumprod()

    return df