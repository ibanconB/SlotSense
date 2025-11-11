import json

from core.context import SpinContext
from core.rng import RNG
from engines.generic_engine import GenericEngine

config = {
    "rows": 3,
    "cols": 3,
    "symbols": ["A", "B", "C", "D"],
    "weights": ["50", "30", "15", "5"],
    "payouts": {"A": 1, "B": 2, "C": 5, "D": 10},
    "debug": True
}

ctx = SpinContext(bet=1.0, config=config)
ctx.rng = RNG(ctx.seed, debug=True)

engine = GenericEngine()

# Puedes pedir el resultado como dict o JSON
result = engine.spin(ctx)
print(json.dumps(result, separators=(',', ':')))


