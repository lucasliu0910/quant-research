import pandas as pd

LOOKBACK = 20

def compute_momentum_signal(df: pd.DataFrame):
    df = df.copy()
    df['momentum'] = df['Close'].pct_change(LOOKBACK)
    df['signal'] = (df["momentum"] > 0).astype(int)
    return df

