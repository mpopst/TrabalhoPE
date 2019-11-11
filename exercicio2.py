import numpy as np
from util import validar_matriz, simulaca_markov

def simula_limite(P: np.matrix, X_0: int, n:int):
    soma = 0
    X = X_0
    for i in range(n):
        X = simulaca_markov(P, X, 1)
        soma += X**2
    return soma/n

def exercicio2(P: np.matrix, X_0: int, n: int, qtd: int):
    validar_matriz(P, 4)
    ans = 0
    for k in range(qtd):
        ans += simula_limite(P, X_0, n)
    return ans/qtd
