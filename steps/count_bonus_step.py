from core.step_base import Step

class CountBonusStep(Step):

    def run(self, context):
        config = context.config
        bonus_sym = config["bonus_symbol"]
        trigger = config["free_spins_trigger"]
        awarded = config["free_spins_awarded"]

        injections = context.state.get("injections", [])

        bonus_injected = sum(
            1 for row in injections for sym in row if sym==bonus_sym
        )

        context.state["bonus_count"] = bonus_injected

        # -----------------------------
        #  BASE
        # -----------------------------

        if not context.state.get("free_spins_active", False):

            if bonus_injected >= trigger:
                context.state["free_spins_active"] = True
                context.state["free_spins_left"] = awarded
                context.events.append("free_spins_triggered")
            else:
                context.events.append("bonus_counted")
                return

        # -----------------------------
        #  FREE SPINS
        # -----------------------------

        else:

            if bonus_injected>=1:
                context.state["free_spins_left"] += 1
                context.events.append("freespins_retrigger")

            return

