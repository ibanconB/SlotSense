import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import argparse
import time
import json
import statistics
from core.context import SpinContext
from core.rng import RNG
from engines.generic_engine import GenericEngine


# ==========================
# CONFIGURACIÓN BASE
# ==========================
DEFAULT_CONFIG = {
    "rows": 3,
    "cols": 3,
    "symbols": ["A", "B", "C", "D"],
    "weights": ["50", "30", "15", "5"],
    "payouts": {"A": 1, "B": 2, "C": 5, "D": 10},
    "debug": False
}


# ==========================
# TESTER
# ==========================
def run_test(spins, bet, config, seed=None):
    engine = GenericEngine()
    total_bet = 0
    total_won = 0
    results = []

    t0 = time.time()

    for i in range(spins):
        ctx_seed = (seed + i) if seed is not None else None
        ctx = SpinContext(bet=bet, seed=ctx_seed, config=config)
        ctx.rng = RNG(ctx.seed, debug=config.get("debug", False))

        result = engine.spin(ctx)

        # Si solo hay 1 spin → mostrar el JSON y salir
        if spins == 1:
            print(json.dumps(result, separators=(',', ':')))
            return  # <-- evita que se ejecute el report

        total_bet += bet
        total_won += result["creditsWon"]
        results.append(result["creditsWon"])

    # --- Solo se ejecuta si spins > 1 ---
    duration = time.time() - t0
    rtp = (total_won / total_bet) * 100 if total_bet else 0
    hit_rate = (sum(1 for w in results if w > 0) / spins) * 100
    avg_win = statistics.mean(results)
    max_win = max(results)

    print(f"\n--- Tester Report ({spins} spins) ---")
    print(f"Bet: {bet}")
    print(f"RTP estimado: {rtp:.2f}%")
    print(f"Hit rate: {hit_rate:.2f}%")
    print(f"Ganancia media: {avg_win:.2f}")
    print(f"Máxima ganancia: {max_win:.2f}")
    print(f"Tiempo: {duration:.2f}s")


# ==========================
# CLI
# ==========================
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Slot Tester - ejecuta spins para debug o simulación.")
    parser.add_argument("-t", "--spins", type=int, default=1, help="Número de spins (por defecto: 1)")
    parser.add_argument("-b", "--bet", type=float, default=1.0, help="Valor de la apuesta por spin")
    parser.add_argument("-r", "--seed", type=int, default=None, help="Seed inicial (si se omite, usa aleatoria)")
    args = parser.parse_args()

    run_test(spins=args.spins, bet=args.bet, config=DEFAULT_CONFIG, seed=args.seed)
