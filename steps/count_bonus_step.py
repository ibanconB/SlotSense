from core.step_base import Step

class CountBonusStep(Step):

    def run(self, context):
        config = context.config

        bonus_sym = config["bonus_symbol"]
        trigger = config["free_spins_trigger"]
        awarded = config["free_spins_awarded"]

        total_bonus = 0

        for row in context.board:
            for sym in row:
                if sym == bonus_sym:
                    total_bonus += 1

        injections = context .state.get("injections", [])
        for row in injections:
            for sym in row:
                if sym == bonus_sym:
                    total_bonus += 1

        context.state["bonus_count"] = total_bonus

        if total_bonus >= trigger:
            context.state_delta["free_spins"] = awarded
            context.events.append("free_spins_triggered")
        else:
            context.events.append("bonus_counted")
