import yfinance as yf
import matplotlib.pyplot as plt

from signal_generator import compute_momentum_signal
from backtest import backtest


def main():
    # 1. 下載資料（單一股票先測通流程）
    df = yf.download("TSLA", start="2018-01-01")

    # 2. 產生 momentum signal
    df = compute_momentum_signal(df)

    # 3. backtest
    df = backtest(df)

    # 4. 看最後結果
    print(df.tail())

    # 5. 畫 equity curve
    plt.figure()
    df["equity_curve"].plot(title="Momentum Strategy Equity Curve")
    plt.show()


if __name__ == "__main__":
    main()