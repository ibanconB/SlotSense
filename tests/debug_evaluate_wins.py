import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.context import SpinContext
from core.rng import RNG
from engines.generic_engine import GenericEngine
from steps.evaluate_win_step import EvaluateWinsStep

CONFIG = {
    "rows": 3,
    "cols": 3,
    "symbols": ["A", "B", "C", "D"],
    "weights": ["50", "30", "15", "5"],
    "payouts": {"A": 1, "B": 2, "C": 5, "D": 10},
    "evaluationMode": "winningLines"
}

def make_context(seed):
    ctx = SpinContext(bet=1.0, seed=seed, config=CONFIG)
    ctx.rng = RNG(ctx.seed)
    return ctx

def debug_winning_lines():
    engine = GenericEngine()
    wins_detected = 0

    for seed in range(20):
        ctx = make_context(seed)
        result = engine.spin(ctx)
        board = result["reelLayout"]
        credits = result["creditsWon"]

        # imprimir de forma legible
        print(f"\nSpin {seed}:")
        print(f"Layout: {board}")
        print(f"CreditsWon: {credits}")
        if credits > 0:
            print("➡️ ¡GANADOR!")
            wins_detected += 1

    print(f"\nTotal de spins con ganancia: {wins_detected}/20")

if __name__ == "__main__":
    debug_winning_lines()
