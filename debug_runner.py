import traceback
from hermes_trading.run import load_goal
from hermes_trading.loop import WorkerLoop

try:
    print("DEBUG: loading goal.yaml")
    goal = load_goal()
    print("DEBUG: goal loaded:", goal)
    asset = goal.get("asset", "SPY")
    print("DEBUG: creating WorkerLoop for", asset)
    loop = WorkerLoop(asset, goal)
    print("DEBUG: calling run_forever (will run one iteration then exit for debug)")
    # call one iteration of the loop manually if available, else call run_forever with a short timeout
    # We will try to call run_forever but stop after a short sleep if it blocks.
    import threading, time
    t = threading.Thread(target=loop.run_forever, daemon=True)
    t.start()
    time.sleep(6)
    print("DEBUG: waited 6 seconds, thread alive:", t.is_alive())
    print("DEBUG: check state/trades.jsonl exists:", __import__('pathlib').Path('state/trades.jsonl').exists())
except Exception as e:
    print("DEBUG ERROR:", repr(e))
    traceback.print_exc()
