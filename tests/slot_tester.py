import sys, os, importlib, argparse, time, json, statistics

# --- Añadir raíz del proyecto al path ---
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.context import SpinContext
from core.rng import RNG


# ====================================================
#   FUNCIÓN PRINCIPAL
# ====================================================

def run_test(engine, spins, bet, config, seed=None, json_output=False):
    total_bet = 0
    total_won = 0
    results = []

    t0 = time.time()

    for i in range(spins):
        ctx_seed = (seed + i) if seed is not None else None
        ctx = SpinContext(bet=bet, seed=ctx_seed, config=config)
        ctx.rng = RNG(ctx.seed, debug=config.get("debug", False))

        result = engine.spin(ctx)

        if spins == 1:
            print(json.dumps(result, separators=(',', ':')))
            if json_output:
                return  # si pedimos JSON, no mostramos nada más

        total_bet += bet
        total_won += result["creditsWon"]
        results.append(result["creditsWon"])

    duration = time.time() - t0
    rtp = (total_won / total_bet) * 100 if total_bet else 0
    hit_rate = (sum(1 for w in results if w > 0) / spins) * 100
    avg_win = statistics.mean(results)
    max_win = max(results)

    if spins > 1:
        print(f"\n--- Tester Report ({spins} spins) ---")
        print(f"Juego: {engine.__class__.__name__}")
        print(f"Apuesta: {bet}")
        print(f"RTP estimado: {rtp:.2f}%")
        print(f"Hit rate: {hit_rate:.2f}%")
        print(f"Ganancia media: {avg_win:.2f}")
        print(f"Máxima ganancia: {max_win:.2f}")
        print(f"Tiempo total: {duration:.2f}s")


# ====================================================
#   CARGA DINÁMICA DEL JUEGO
# ====================================================

def load_game(game_name):
    """
    Carga dinámica según la estructura:
    engines/<GameName>/ExecutionFlow.py
    engines/<GameName>/config.py
    """
    try:
        # Convertir a formato de carpeta: firestorm -> Firestorm
        game_folder = game_name[0].upper() + game_name[1:]

        engine_module = importlib.import_module(f"engines.{game_folder}.ExecutionFlow")
        config_module = importlib.import_module(f"engines.{game_folder}.config")

        # Clase principal = mismo nombre que la carpeta (Firestorm)
        EngineClass = getattr(engine_module, game_folder)
        game_config = getattr(config_module, f"{game_folder.upper()}_CONFIG")

        return EngineClass(), game_config

    except (ModuleNotFoundError, AttributeError) as e:
        print(f"Error: no se pudo cargar el juego '{game_name}'.")
        print(f"Detalles: {e}")
        sys.exit(1)


# ====================================================
#   CLI
# ====================================================

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Slot Tester - ejecuta spins para debug o simulación.")
    parser.add_argument("-g", "--game", default="firestorm", help="Nombre del juego (carpeta en /engines). Ej: firestorm")
    parser.add_argument("-t", type=int, default=1, help="Número de spins a ejecutar (por defecto: 1)")
    parser.add_argument("-b", type=float, default=1.0, help="Valor de la apuesta por spin")
    parser.add_argument("-r", type=int, default=None, help="Seed inicial (si se omite, usa aleatoria)")
    parser.add_argument("--json", action="store_true", help="Muestra solo el resultado del spin en formato JSON")
    args = parser.parse_args()

    engine, config = load_game(args.game)
    run_test(engine, spins=args.t, bet=args.b, config=config, seed=args.r, json_output=args.json)
