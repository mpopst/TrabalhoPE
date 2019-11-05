import numpy as np
from util import validar_matriz, simulaca_markov

def exercicio2(P: np.matrix, X_0: int, n: int, qtd: int):
    validar_matriz(P, 4)
    ans = 0
    for k in range(qtd):
        ans += (simulaca_markov(P,X_0, n))**2
    return ans/qtd
