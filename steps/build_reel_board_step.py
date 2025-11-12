from core.step_base import Step

class BuildReelBoardStep(Step):
    """
           Step genérico: construye el tablero usando reels definidos en config.
            No conoce wilds, bonus ni reglas especiales.
    """

    def run(self, context):
        reels = context.config.get("reels")
        rows = context.config.get("rows")
        cols = context.config.get("cols")

        if not reels or len(reels) != cols:
            raise ValueError("Config must define a reels list with one list per column")


        board =[[None for _ in range(cols)] for _ in range(rows)]

        rng = context.rng.fork(self.__class__.__name__)

        for col in range(cols):
            reel = reels[col]
            reel_len =len(reel)
            start_pos = rng.randint(0, reel_len - 1, label=f"reel_{col}_start")
            for row in range(rows):
                symbol = reel[(start_pos + row) % reel_len]
                board[row][col] = symbol

        context.board = board
        context.events.append("reel_board_built")