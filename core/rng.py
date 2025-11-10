import random


class RNG:
    """
    Generador de numeros aleatorios/
    Permite reproducir spins usando la misma seed
    """

    def __init__(self, seed:int):
        self.seed= seed
        self.random= random.Random(seed)

    def rand(self):
        "devuelve float entre 0.0 y 1.0"
        return  self.random.random()

    def randint(self, a:int, b:int):
        """Return int between a and b inclusive"""
        return self.random.randint(a,b)

    def choice(self,seq):
        """Return random element from a sequence"""
        return self.random.choice(sq)

    def shuffle(self, seq):
        """Shuffle a list (in-place)"""
        self.random.shuffle(seq)
        return seq