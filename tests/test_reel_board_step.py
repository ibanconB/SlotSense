import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.context import SpinContext
from core.rng import RNG
from steps.build_reel_board_step import BuildReelBoardStep

def test_build_reel_board():
    TEST_CONFIG = {
        "rows": 3,
        "cols": 5,
        "reels": [
            [1, 2, 3, 4, 5],
            [5, 4, 3, 2, 1],
            [2, 3, 4, 5, 1],
            [1, 1, 2, 2, 3],
            [5, 5, 4, 3, 2]
        ]
    }

    ctx = SpinContext(bet=1.0, seed=1234, config=TEST_CONFIG)
    ctx.rng = RNG(ctx.seed, debug=True)

    step = BuildReelBoardStep()
    step.run(ctx)

    print("Board generado:")
    for row in ctx.board:
        print(row)

    print("\nTrace RNG:")
    print(ctx.rng.trace)

if __name__ == "__main__":
    test_build_reel_board()
