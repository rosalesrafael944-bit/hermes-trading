import traceback
import yfinance as yf
try:
    df = yf.download("SPY", period="1d", interval="1m", progress=False, threads=False)
    print("yfinance rows:", len(df))
    if len(df) > 0:
        # robustly get the last close as a Python float
        last_close = df["Close"].iloc[-1]
        # if it's a Series (rare), take the first element; else convert to float
        if hasattr(last_close, "item"):
            last_close_val = float(last_close.item())
        else:
            last_close_val = float(last_close)
        print("last close:", last_close_val)
    else:
        print("No rows returned")
except Exception as e:
    print("ERROR:", repr(e))
    traceback.print_exc()
