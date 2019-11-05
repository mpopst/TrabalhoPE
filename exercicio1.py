from util import validar_matriz, simulaca_markov
import numpy as np

def exercicio1(P: np.array, i: int, j: int, n: int, qtd: int):
    validar_matriz(P,5)
    return sum(1 for k in range(qtd) if simulaca_markov(P, i, n) == j)/qtd