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

        if board is None:
            raise ValueError("Can´t evaluate wins without board")

        total_win = 0
        wins = []

        # count syms and calculate total pay
        symbol_counts = {}
        for row in board:
            for symbol in row:
                symbol_counts[symbol] = symbol_counts.get(symbol, 0)+1

        # calculate winnins by sym
        for symbol, count in symbol_counts.items():
            payout = payouts.get(symbol,0)
            symbol_win = payout * count * context.bet
            if symbol_win > 0:
                wins.append({"symbol":symbol, "count":count, "win": symbol_win})
                total_win += symbol_win

        context.wins = wins
        context.total_win = total_win
        context.events.append("wins_evaluated")





