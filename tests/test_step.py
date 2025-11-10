import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.context import   SpinContext
from core.step_base import Step


class DummyStep(Step):
    name = "dummy-step"

    def run(self, context):
        context.board = "test_board"
        context.total_win = 50
        context.events.append("dummy_step_ran")


def test_dummy_step_run():
    context = SpinContext(bet=1.0, seed=1234)
    step = DummyStep()
    step.run(context)

    assert context.board == "test_board"
    assert context.total_win == 50
    assert "dummy_step_ran" in context.events

    print("DummyStep ha modificado context")
