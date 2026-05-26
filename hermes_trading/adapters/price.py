"""Price adapter using yfinance for simple fetch."""
import yfinance as yf

def fetch_price(ticker: str) -> float:
    """
    Fetch a recent price for ticker and return a Python float.
    Raises RuntimeError on failure.
    """
    # Try the fast download first
    try:
        data = yf.download(ticker, period="1d", interval="1m", progress=False, threads=False)
        if data is None or data.empty:
            # fallback to Ticker.history
            t = yf.Ticker(ticker)
            data = t.history(period="2d", interval="1m")
        if data is None or data.empty:
            raise RuntimeError("yfinance returned no data for " + ticker)
        last = data["Close"].iloc[-1]
        # If last is a pandas scalar/Series, convert safely
        if hasattr(last, "item"):
            return float(last.item())
        return float(last)
    except Exception as e:
        # Re-raise as RuntimeError so callers see a consistent exception type
        raise RuntimeError(f"fetch_price error for {ticker}: {e}")
