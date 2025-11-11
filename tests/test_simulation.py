import statistics
from core.context import SpinContext
from core.rng import RNG
from engines.generic_engine import GenericEngine

#TODO: hay que hacer que reciba argumentos para 1. Spin normal 2. Miles de spins

CONFIG = {
    "rows": 3,
    "cols": 3,
    "symbols": ["A", "B", "C", "D"],
    "weights": ["50", "30", "15", "5"],
    "payouts": {"A": 1, "B": 2, "C": 5, "D": 10},
}

def make_context(seed):
    ctx = SpinContext(bet=1.0, seed=seed, config=CONFIG)
    ctx.rng = RNG(ctx.seed)
    return ctx


# --- 1️⃣ Test: un solo spin ---
def test_single_spin():
    engine = GenericEngine()
    ctx = make_context(seed=123)

    result = engine.spin(ctx)
    print("\nResultado del spin único:")
    print(result)

    assert "reelLayout" in result
    assert "creditsWon" in result
    assert result["creditsWon"] >= 0


# --- 2️⃣ Test: simulación masiva ---
def test_massive_simulation():
    engine = GenericEngine()
    total_spins = 10_000
    total_bet = 0
    total_won = 0
    wins = []

    for seed in range(total_spins):
        ctx = make_context(seed)
        result = engine.spin(ctx)
        total_bet += ctx.bet
        total_won += result["creditsWon"]
        wins.append(result["creditsWon"])

    rtp = (total_won / total_bet) * 100
    avg_win = statistics.mean(wins)
    max_win = max(wins)
    hit_rate = (sum(1 for w in wins if w > 0) / total_spins) * 100

    print(f"\n--- Resultados de simulación ({total_spins} spins) ---")
    print(f"RTP estimado: {rtp:.2f}%")
    print(f"Hit rate: {hit_rate:.2f}%")
    print(f"Ganancia media: {avg_win:.2f}")
    print(f"Máxima ganancia: {max_win:.2f}")

    assert 0 <= rtp <= 300  # valores razonables