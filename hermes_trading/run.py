"""Entry point for the worker."""
import argparse
import yaml
from .loop import WorkerLoop

def load_goal(path="state/goal.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--asset", default=None)
    args = parser.parse_args()
    goal = load_goal()
    asset = args.asset or goal.get("asset", "SPY")
    loop = WorkerLoop(asset, goal)
    loop.run_forever()

if __name__ == "__main__":
    main()
