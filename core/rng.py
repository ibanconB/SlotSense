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
        return self.random.choice(seq)

    def shuffle(self, seq):
        """Shuffle a list (in-place)"""
        self.random.shuffle(seq)
        return seq

    def weighted_choice(self, seq):
        """
        Devuelve un elemento de seq según sus probabilidades relativas.

        Ejemplo:
            seq = (
                ('A', '50.00'),
                ('B', '40.00'),
                ('C', '10.00')
            )
        'A' tiene un 50% de probabilidad, 'B' un 40%, 'C' un 10%.
        """

        if not seq:
            raise ValueError("weighted_choice requiere una secuencia no vacía")

        # Normalizar las probabilidades
        total = sum(float(prob) for _, prob in seq)
        pick = self.random.random() * total
        cumulative = 0.0

        for value, prob in seq:
            cumulative += float(prob)
            if pick < cumulative:
                return value

        # Por si acaso (errores de redondeo)
        return seq[-1][0]