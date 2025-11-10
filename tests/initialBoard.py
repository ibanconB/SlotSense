from core.context import SpinContext
from core.rng import RNG
from steps.build_board import BuildBoardStep

config = {
    "rows": 3,
    "cols": 3,
    "symbols": ["A", "B", "C"],
    "weights": ["50.00", "40.00", "10.00"]
}
for seed in [1, 2, 3, 4]:
    ctx = SpinContext(bet=1.0, seed=seed, config=config)
    ctx.rng = RNG(ctx.seed)
    BuildBoardStep().run(ctx)
    print(f"Seed {seed}:")
    for row in ctx.board:
        print(row)
    print("-" * 20)
