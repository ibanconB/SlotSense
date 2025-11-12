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

    def spin(self, context, as_json=False):
        context.events.append("spin_start")
        context.config["active_reels"] = context.config.get("reels")

        for step in self.steps:
            step.run(context)

        context.payout = context.total_win
        context.events.append("spin_end")

        result = context.to_dict()
        return result if not as_json else context.to_json()
