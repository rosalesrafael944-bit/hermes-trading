import traceback
import yfinance as yf
try:
    df = yf.download("SPY", period="1d", interval="1m", progress=False, threads=False)
    print("yfinance rows:", len(df))
    if len(df) > 0:
        print("last close:", float(df["Close"].iloc[-1]))
    else:
        print("No rows returned")
except Exception as e:
    print("ERROR:", repr(e))
    traceback.print_exc()
