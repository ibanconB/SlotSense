import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.context import  SpinContext
from core.step_base import Step
from core.engine import BaseEngine

# --- Steps genéricos de prueba ---
class StepA(Step):
    def run(self, ctx):
        ctx.events.append("StepA")
        ctx.total_win += 10


class StepB(Step):
    def run(self, ctx):
        ctx.events.append("StepB")
        ctx.total_win *= 2


# --- Test del engine base ---
def test_base_engine_executes_steps_in_order():
    # 1. crear contexto y steps
    ctx = SpinContext(bet=1.0, seed=42)
    steps = [StepA(), StepB()]

    # 2. crear engine base con esos steps
    engine = BaseEngine(steps)

    # 3. ejecutar spin
    result_ctx = engine.spin(ctx)

    # 4. comprobar orden y cálculos
    assert result_ctx.events == ["StepA", "StepB"]
    assert result_ctx.total_win == 20
    assert result_ctx.payout == 20

    print(" BaseEngine ejecutó Steps en orden correctamente")