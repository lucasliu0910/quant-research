import yfinance as yf
from strategies.momentum.signal import compute_momentum_signal
from strategies.momentum.backtest import backtest

# 1. 抓資料
df = yf.download("AAPL", start="2018-01-01")

# 2. 產生 signal
df = compute_momentum_signal(df)

# 3. backtest
df = backtest(df)

# 4. 看結果
print(df[["equity_curve"]].tail())

# 5. 畫圖
df["equity_curve"].plot()