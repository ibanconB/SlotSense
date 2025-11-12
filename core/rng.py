import hashlib
import random


class RNG:
    """
    RNG determinista con traza opcional de llamadas (debug mode).
    - Si debug=False: rendimiento normal, sin traza.
    - Si debug=True: registra cada sorteo con etiqueta y valor.
    """

    def __init__(self, seed:int, debug = False):
        self.seed= seed
        self.random= random.Random(seed)
        self.debug = debug
        self.trace = []
        self.forks = {}

    # =============================
    # INTERNAL
    # =============================

    def _record(self, label: str, value):
        """Registra valor si debug=True."""
        if self.debug:
            self.trace.append((label, value))
        return value



    # =============================
    # RNG
    # =============================
    def rand(self, label="rand"):
        """Devuelve un float entre 0 y 1."""
        return self._record(label, self.random.random())

    def randint(self, a, b, label="randint"):
        """Devuelve un entero entre a y b."""
        return self._record(label, self.random.randint(a, b))

    def choice(self, seq, label="choice"):
        """Devuelve un elemento aleatorio de la secuencia."""
        return self._record(label, self.random.choice(seq))

    def weighted_choice(self, seq, label="weighted_choice"):
        """
        Selecciona un elemento de seq = [(valor, peso), ...]
        según su probabilidad relativa.
        """
        total = sum(float(p) for _, p in seq)
        pick = self.rand(label=f"{label}.pick") * total
        acc = 0.0
        for v, p in seq:
            acc += float(p)
            if pick < acc:
                return self._record(label, v)
        return self._record(label, seq[-1][0])  # fallback

    def fork(self, tag: str):
        h = hashlib.blake2s(f"{self.seed}|{tag}".encode(), digest_size=8).hexdigest()
        new_seed = int(h, 16)
        child = RNG(new_seed, debug=self.debug)

        if self.debug:
            if not hasattr(self, "forks"):
                self.forks = {}
            self.forks[tag] = new_seed

            # compartir el mismo registro de trazas
            child.trace = self.trace

        return child
