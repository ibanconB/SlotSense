import json
from itertools import chain


class SpinContext:
    """
        Contiene toda la informacion de un spin:
            - Entradas (bet, seed, config, state)
            - Datos en juego (reels seleccionados, creditsWon, eventos)
            - Resultado final (payout, state_delta)
    """

    def __init__(self, bet, seed, config=None, state=None):
        # --- Entradas ---
        self.bet = bet  # apuesta total
        self.seed = seed  # semilla usada por el RNG
        self.config = config or {}  # reels, modo de juego, etc.
        self.state = state or {}  # estado persistente (features, contadores...)

        # --- Datos en juego ---
        self.board = None  # matriz o reels del spin
        self.wins = []  # lista de combinaciones ganadoras
        self.total_win = 0  # ganancia acumulada
        self.events = []  # eventos (features activadas, cascadas, etc.)

        # --- Salida final ---
        self.payout = 0  # créditos finales ganados
        self.state_delta = {}  # cambios a persistir

    def to_dict(self):
        """Convierte el contexto en un diccionario limpio, listo para serializar a JSON."""

        flattened_board = list(chain.from_iterable(self.board)) if self.board else []

        return {
                "reelLayout": flattened_board,
                "creditsWon": self.total_win,
                "bet": self.bet,
                "wins": self.wins,
                "events": self.events,
            }

    def to_json(self):
        """Devuelve el contexto serializado en formato JSON."""
        return json.dumps(self.to_dict(), separators=(',', ':'))