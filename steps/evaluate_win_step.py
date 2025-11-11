from lib2to3.fixes.fix_input import context

from core.step_base import Step

class EvaluateWinsStep(Step):
    """
        Evalua ganancias del board
        Calcula valor de payout definido en config
    """

    #TODO: hay que crear metodos para diferentes formas de ganar

    name = "evaluate_wins"

    def run(self, context):
        board= context.board
        payouts = context.config.get("payouts",{})
        mode = context.config.get("evaluationMode", "winningLines")

        if board is None:
            raise ValueError("Can´t evaluate wins without board")

        if mode == "winningLines":
            total_win, wins = self.evaluate_winning_lines(context)
        else:
            raise ValueError(f"Evaluation mode {mode} not supported")

        context.wins = wins
        context.total_win = total_win
        context.events.append("wins_evaluated")

    # ==============================================================
    # EVALUATION METHODS
    # ==============================================================

    def evaluate_winning_lines(self, context):
        """
        Evalúa filas horizontales: paga si hay 3+ símbolos consecutivos iguales.
        """
        board = context.board
        payouts = context.config.get("payouts", {})
        bet = context.bet
        cols = context.config.get("cols", 3)
        total_win = 0
        wins = []

        # Si el board es plano (lista única), dividir en filas
        if board and isinstance(board[0], str):
            board = [board[i:i + cols] for i in range(0, len(board), cols)]

        for row_idx, row in enumerate(board):
            streak_symbol = row[0]
            streak_len = 1

            for col in row[1:]:
                if col == streak_symbol:
                    streak_len += 1
                else:
                    if streak_len >= 3:
                        win = payouts.get(streak_symbol, 0) * streak_len * bet
                        if win > 0:
                            wins.append({
                                "row": row_idx,
                                "symbol": streak_symbol,
                                "count": streak_len,
                                "win": win
                            })
                            total_win += win
                    streak_symbol = col
                    streak_len = 1

            # revisa racha final
            if streak_len >= 3:
                win = payouts.get(streak_symbol, 0) * streak_len * bet
                if win > 0:
                    wins.append({
                        "row": row_idx,
                        "symbol": streak_symbol,
                        "count": streak_len,
                        "win": win
                    })
                    total_win += win

        return total_win, wins






