from core.engine import BaseEngine
from steps.build_board import BuildBoardStep
from steps.evaluate_win_step import EvaluateWinsStep

class GenericEngine(BaseEngine):
    """
    Motor genérico: ejecuta un spin básico con Steps genéricos.
    """

    def __init__(self, steps = None):
        if steps is None:
            steps = [
                BuildBoardStep(),      # Genera el tablero inicial
                EvaluateWinsStep(),    # Evalúa las ganancias del tablero
            ]
        super().__init__(steps)

