from core.context import SpinContext
from core.rng import RNG
from steps.build_board import BuildBoardStep
from steps.evaluate_win_step import EvaluateWinsStep

config = {
    "rows": 3,
    "cols": 3,
    "symbols": ["A", "B", "C", "D"],
    "weights": ["50", "30", "15", "5"],
    "payouts": {"A": 1, "B": 2, "C": 5, "D": 10}
}

ctx = SpinContext(bet=1.0, seed=1234, config=config)
ctx.rng = RNG(ctx.seed)

# Pipeline simple
BuildBoardStep().run(ctx)
EvaluateWinsStep().run(ctx)

print("Board:")
for row in ctx.board:
    print(row)
print("\nGanancias:", ctx.wins)
print("Total win:", ctx.total_win)
