from core.step_base import Step

class EvaluateWinsStep(Step):
    """
    Step responsable de evaluar las combinaciones ganadoras.
    Puede manejar diferentes modos de evaluación según el config.
    """

    def run(self, ctx):
        mode = ctx.config.get("evaluationMode", "winningLines")

        if mode == "winningLines":
            ctx.total_win, ctx.wins = self.evaluate_winning_lines(ctx)
        # En el futuro podrías añadir más modos, como:
        # elif mode == "scatterPays":
        #     ctx.total_win, ctx.wins = self.evaluate_scatter_pays(ctx)

        ctx.events.append("wins_evaluated")

    # Aquí pegamos el método genérico:
    def evaluate_winning_lines(self, ctx):
        board = ctx.board
        config = ctx.config
        payouts = config.get("payouts", {})
        paylines = config.get("paylines", [])
        wild_symbol = config.get("wild_symbol")
        non_paying = set(config.get("non_paying_symbols", []))
        min_match = config.get("min_match", 3)
        bet = ctx.bet

        total_win = 0
        wins = []

        if not board or not paylines:
            return 0, []

        for line_index, line_coords in enumerate(paylines):
            line_symbols = [board[r][c] for r, c in line_coords]
            base_symbol = next(
                (s for s in line_symbols if s != wild_symbol and s not in non_paying),
                None
            )
            if base_symbol is None:
                continue

            streak = 0
            for symbol in line_symbols:
                if symbol == base_symbol or symbol == wild_symbol:
                    streak += 1
                else:
                    break

            if streak >= min_match:
                symbol_payout = payouts.get(base_symbol, 0)
                win_amount = symbol_payout * streak * bet
                if win_amount > 0:
                    total_win += win_amount
                    wins.append({
                        "line": line_index,
                        "symbol": base_symbol,
                        "count": streak,
                        "win": win_amount
                    })

        return total_win, wins

