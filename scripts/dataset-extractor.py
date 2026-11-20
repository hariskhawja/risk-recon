import yfinance as yf

tickers = ["SPY", "QQQ", "IWM", "TLT", "GLD"]

prices = yf.download(
    tickers,
    start="2010-01-01",
    end="2026-11-01",
    interval="1d",
    auto_adjust=True
)["Close"]

prices = prices.dropna()
returns = prices.pct_change().dropna()

returns.to_csv("etf_returns.csv")
