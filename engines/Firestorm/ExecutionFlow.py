from core.engine import BaseEngine
from steps.build_reel_board_step import BuildReelBoardStep
from steps.evaluate_win_step import EvaluateWinsStep


class Firestorm(BaseEngine):
    def __init__(self):
        # modo base
        steps = [
            BuildReelBoardStep(),
            EvaluateWinsStep(),
        ]
        super().__init__(steps)

    def initializeInjections(self, ctx):
        rows = ctx.config["rows"]
        cols = ctx.config["cols"]

        ctx.state["injections"] = [
            [None for _ in range(cols)]
            for _ in range(rows)
        ]

    def setWildSymbols(self, ctx):
        inj_cfg = ctx.config.get("symbol_injection", {})
        chance = inj_cfg.get("wild_chance", 0)  # porcentaje
        wild_sym = ctx.config["wild_symbol"]

        rows = ctx.config["rows"]
        cols = ctx.config["cols"]

        rng = ctx.rng.fork("WildInjection")
        injections = ctx.state["injections"]

        for r in range(rows):
            for c in range(cols):
                roll = rng.rand("wild.roll") * 100

                if roll < chance:
                    injections[r][c] = wild_sym

    def spin(self, context, as_json=False):
        context.events.append("spin_start")
        context.config["active_reels"] = context.config.get("reels")

        self.initializeInjections(context)

        for step in self.steps:
            step.run(context)

        context.payout = context.total_win
        context.events.append("spin_end")

        result = context.to_dict()
        return result if not as_json else context.to_json()
