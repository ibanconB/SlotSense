FIRESTORM_CONFIG = {
    # --- Dimensiones ---
    "rows": 3,
    "cols": 5,

    # --- Símbolos ---
    # 1–5: normales
    # 6: wild
    # 7: bonus (Volcano)
    "symbols": [1, 2, 3, 4, 5, 6, 7],

    # --- Probabilidades o distribución ---
    # (en el caso de reels, no se usan directamente)
    "reels": [
        [1, 2, 3, 4, 5, 6, 4, 2, 3, 1, 5, 4, 3, 6],
        [2, 3, 4, 5, 1, 6, 3, 1, 3, 2, 4, 5, 6, 1],
        [3, 4, 5, 6, 1, 2, 2, 5, 3, 1, 4, 6, 2, 5],
        [4, 5, 6, 1, 1, 2, 3, 6, 4, 1, 5, 2, 3, 3],
        [5, 6, 5, 1, 2, 3, 4, 1, 6, 2, 3, 4, 5, 4]
    ],

    # --- Reels para modo Free Spins ---
    "free_reels": [
        [1, 2, 3, 4, 5, 6, 6, 6, 2, 3, 4, 1],
        [2, 3, 4, 5, 6, 6, 6, 1, 3, 4, 5, 1],
        [3, 4, 5, 6, 6, 6, 1, 2, 5, 3, 4, 2],
        [4, 5, 6, 6, 6, 1, 2, 3, 4, 5, 1, 2],
        [5, 6, 6, 6, 1, 2, 3, 4, 5, 1, 2, 3]
    ],

    # --- Pagos (por símbolo base) ---
    # Pagos por cada símbolo de 3, 4 o 5 en línea (multiplicador * bet)
    "payouts": {
        1: 1.0,
        2: 1.5,
        3: 2.5,
        4: 4.0,
        5: 8.0
    },

    # --- Wild y Bonus ---
    "wild_symbol": 6,
    "non_paying_symbols": [7],

    "symbol_injection": {
        "wild_chance": 0.5,
        "bonus_chance": 0.0
    },

    # --- Líneas ganadoras (paylines) ---
    "paylines": [
        # filas horizontales
        [(0,0),(0,1),(0,2),(0,3),(0,4)],
        [(1,0),(1,1),(1,2),(1,3),(1,4)],
        [(2,0),(2,1),(2,2),(2,3),(2,4)],

        # diagonales
        [(0,0),(1,1),(2,2),(1,3),(0,4)],
        [(2,0),(1,1),(0,2),(1,3),(2,4)],

        # líneas en V y W
        [(0,0),(1,1),(2,2),(2,3),(2,4)],
        [(2,0),(1,1),(0,2),(0,3),(0,4)],
        [(1,0),(0,1),(1,2),(2,3),(1,4)],
        [(1,0),(2,1),(1,2),(0,3),(1,4)],
        [(0,0),(0,1),(1,2),(2,3),(2,4)]
    ],

    # --- Parámetros de evaluación ---
    "evaluationMode": "winningLines",
    "min_match": 3,

    # --- Bonus y Free Spins ---
    "bonus_symbol": 7,
    "free_spins_trigger": 3,
    "free_spins_awarded": 10,

    # --- Opciones varias ---
    "debug": True,
}
