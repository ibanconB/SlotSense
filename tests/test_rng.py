import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.rng import RNG


def test_rng_reproducibility():
    rng1 = RNG(seed=123)
    rng2 = RNG(seed=123)
    rng3 = RNG(seed=999)


    # Seed igual -> resultado igual

    seq1 = [rng1.randint(0,100) for _ in range(5)]
    seq2 = [rng2.randint(0,100) for _ in range(5)]


    assert  seq1 == seq2, f"Las secuencias con misma seed deberían ser iguales: {seq1} vs {seq2}"

    # Seed diferente -> resultado diferente
    seq3 = [rng3.randint(0,100) for _ in range(5)]
    assert seq1 != seq3,"Las secuencias con distinta seed deberían ser diferentes"


    print(" RNG produce secuencias deterministas correctamente")