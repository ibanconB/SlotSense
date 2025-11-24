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

    def setWildSymbols(self, context):
        inj_cfg = context.config.get("symbol_injection", {})
        chance = inj_cfg.get("wild_chance", 0)  # porcentaje
        wild_sym = context.config["wild_symbol"]

        rows = context.config["rows"]
        cols = context.config["cols"]

        rng = context.rng.fork("WildInjection")
        injections = context.state["injections"]

        for r in range(rows):
            for c in range(cols):
                roll = rng.rand("wild.roll") * 100

                if roll < chance:
                    injections[r][c] = wild_sym

    def setBonusSymbols(self, context):
        inj_cfg = context.config.get("symbol_injection", {})
        chance = inj_cfg.get("bonus_chance",0)
        bonus_sym = context.config.get("bonus_symbol")

        rows = context.config["rows"]
        cols = context.config["cols"]

        rng = context.rng.fork("BonusInjection")
        injections = context.state["injections"]

        bonus_count = 0
        bonus_max = 0

        for r in range(rows):
            for c in range(cols):

                if bonus_count >= bonus_max:
                    return

                roll = rng.rand("bonus.roll")*100

                if roll < chance:
                    injections[r][c] = bonus_sym
                    bonus_count +=1



    def spin(self, context, as_json=False):
        context.events.append("spin_start")
        context.config["active_reels"] = context.config.get("reels")

        self.initializeInjections(context)
        self.setWildSymbols(context)

        #TODO: add bonus symbols injections

        for step in self.steps:
            step.run(context)

        context.payout = context.total_win
        context.events.append("spin_end")

        result = context.to_dict()
        return result if not as_json else context.to_json()
