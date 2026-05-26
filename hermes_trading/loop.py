"""Simple reliability loop that fetches price and logs a paper trade example."""
import time
import json
from .adapters.price import fetch_price
from pathlib import Path

STATE_DIR = Path("state")
TRADES_FILE = STATE_DIR / "trades.jsonl"

class WorkerLoop:
    def __init__(self, asset, goal):
        self.asset = asset
        self.goal = goal
        STATE_DIR.mkdir(parents=True, exist_ok=True)

    def run_forever(self):
        print("Worker starting for", self.asset)
        while True:
            try:
                price = fetch_price(self.asset)
                # Example: write a heartbeat trade-like log for testing
                entry = {"time": time.time(), "asset": self.asset, "price": price, "note": "heartbeat"}
                with open(TRADES_FILE, "a") as f:
                    f.write(json.dumps(entry) + "\n")
                print("Logged heartbeat", entry)
            except Exception as e:
                print("Adapter error", e)
            time.sleep(60)
