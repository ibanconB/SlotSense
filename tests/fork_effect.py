import random
import hashlib

# ==============================
#  RNG SIN FORK
# ==============================
class RNGSimple:
    def __init__(self, seed):
        self.random = random.Random(seed)

    def next(self, label):
        val = self.random.random()
        print(f"{label}: {val:.4f}")
        return val


# ==============================
#  RNG CON FORK
# ==============================
class RNG:
    def __init__(self, seed):
        self.seed = seed
        self.random = random.Random(seed)

    def rand(self, label):
        val = self.random.random()
        print(f"{label}: {val:.4f}")
        return val

    def fork(self, tag):
        h = hashlib.blake2s(f"{self.seed}|{tag}".encode(), digest_size=8).hexdigest()
        new_seed = int(h, 16)
        print(f"Fork '{tag}' → new_seed = {new_seed}")
        return RNG(new_seed)


# ==============================
#  ESCENARIO 1 — SIN FORK
# ==============================
def spin_without_fork():
    print("\n=== SIN FORK ===")
    rng = RNGSimple(1234)

    # Step 1: Build board (3 sorteos)
    for i in range(3):
        rng.next(f"BuildBoard #{i+1}")

    # Step 2: Evaluate wins (1 sorteo)
    rng.next("EvaluateWins")


# ==============================
#  ESCENARIO 2 — CON FORK
# ==============================
def spin_with_fork(extra_draws_in_board=False):
    print("\n=== CON FORK ===")
    rng_main = RNG(1234)

    # Fork para cada Step
    rng_board = rng_main.fork("BuildBoardStep")
    rng_eval = rng_main.fork("EvaluateWinsStep")

    # Step 1: Build board (3 sorteos)
    for i in range(3 + (1 if extra_draws_in_board else 0)):
        rng_board.rand(f"BuildBoard #{i+1}")

    # Step 2: Evaluate wins (1 sorteo)
    rng_eval.rand("EvaluateWins")


# ==============================
#  PRUEBA
# ==============================
spin_without_fork()

print("\n>>> Ahora simulamos un cambio en BuildBoardStep (añadimos un sorteo extra)")
def spin_without_fork_modified():
    rng = RNGSimple(1234)
    for i in range(4):  # ← cambio: un sorteo extra
        rng.next(f"BuildBoard #{i+1}")
    rng.next("EvaluateWins")
spin_without_fork_modified()

# --- Con fork ---
spin_with_fork()
print("\n>>> Ahora el mismo cambio en BuildBoardStep, pero con fork")
spin_with_fork(extra_draws_in_board=True)
