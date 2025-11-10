import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.context import SpinContext

def test_spin_context_init():

    context = SpinContext(
        bet=1.0,
        seed=1234,
        config={"reel_set":"BASE"},
        state={"freespins":2}
    )

    assert context.bet == 1.0
    assert context.seed == 1234
    assert context.config["reel_set"] == "BASE"
    assert context.state["freespins"] == 2

    assert context.board is None
    assert context.wins == []
    assert context.total_win == 0
    assert context.events == []
    assert context.payout == 0
    assert context.state_delta == {}

    print(" SpinContext inicializado correctamente")