import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.context import SpinContext
from core.rng import RNG

def test_spin_context_init():
    config = {
        "rows": 3,
        "cols": 3,
        "symbols": ["A", "B", "C", "D"],
        "weights": [40, 30, 20, 10],
        "reel_set": "BASE",
    }

    context = SpinContext(
        bet=1.0,
        seed=1234,
        config=config,
        state={"freespins": 2}
    )

    # Crear y asignar RNG
    context.rng = RNG(context.seed)

    # Verificar datos básicos
    assert context.bet == 1.0
    assert context.seed == 1234
    assert context.config["reel_set"] == "BASE"
    assert context.state["freespins"] == 2

    # Verificar valores por defecto
    assert context.board is None
    assert context.wins == []
    assert context.total_win == 0
    assert context.events == []
    assert context.payout == 0
    assert context.state_delta == {}

    print("✅ SpinContext inicializado correctamente con RNG")
