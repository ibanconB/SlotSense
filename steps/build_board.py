from core.step_base import Step

class BuildBoardStep(Step):
    """
    Step genérico: construye un tablero inicial (board)
    usando los símbolos definidos en ctx.config y el RNG de ctx.
    """

    name = "build_board"

    def run(self, ctx):
        rng = ctx.rng.fork(self.__class__.__name__)

        rows = ctx.config.get("rows", 3)
        cols = ctx.config.get("cols", 3)
        symbols = ctx.config.get("symbols", [])
        weights = ctx.config.get("weights")

        if not symbols:
            raise ValueError("Config must include 'symbols' list")

        # Si existen pesos, crear lista de tuplas [(symbol, prob), ...]
        if weights:
            seq = list(zip(symbols, weights))
        else:
            # Si no hay pesos, asignar probabilidad uniforme
            prob = 100 / len(symbols)
            seq = [(s, prob) for s in symbols]

        board = []

        for r in range(rows):
            row = []
            for c in range(cols):
                symbol = rng.weighted_choice(seq)
                row.append(symbol)
            board.append(row)

        ctx.board = board
        if getattr(ctx.rng, "debug", False):
            ctx.rng.trace.extend(rng.trace)
            ctx.rng.forks[self.__class__.__name__] = rng.seed
        ctx.events.append("board_built")
