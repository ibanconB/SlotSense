import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.context import SpinContext
from core.rng import RNG
from engines.generic_engine import GenericEngine

def test_generic_engine_spin():
    # --- Configuración del spin ---
    config = {
        "rows": 3,
        "cols": 3,
        "symbols": ["A", "B", "C", "D"],
        "weights": ["50", "30", "15", "5"],
        "payouts": {"A": 1, "B": 2, "C": 5, "D": 10}
    }

    # --- Crear contexto ---
    ctx = SpinContext(
        bet=1.0,
        seed=123,
        config=config
    )
    ctx.rng = RNG(ctx.seed)

    # --- Crear motor genérico ---
    engine = GenericEngine()

    # --- Ejecutar spin ---
    result = engine.spin(ctx)

    # --- Validaciones básicas ---
    assert result.board is not None
    assert isinstance(result.board, list)
    assert result.wins is not None
    assert result.total_win >= 0
    assert "board_built" in result.events
    assert "wins_evaluated" in result.events

    # --- Salida visible ---
    print("\n=== SPIN COMPLETO ===")
    for row in result.board:
        print(row)
    print("\nGanancias:", result.wins)
    print("Total Win:", result.total_win)
    print("Eventos:", result.events)
