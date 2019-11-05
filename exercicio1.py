from util import validar_matriz
import numpy as np

def exercicio1(P: np.array, i: int, j: int, n: int, qtd: int):
    validar_matriz(P,5)
    return sum(1 for k in range(qtd) if simulacao(P, i, n) == j)/qtd


def simulacao(P: np.array, i: int, n: int):
    X = i-1
    somas_parciais = np.cumsum(P, 1)
    size = P.shape[0]
    for k in range(0,n):
        aleatorio = np.random.rand()
        s = 0
        l = -1
        while s<aleatorio and l<size:
            l+=1
            s+=somas_parciais[X,l]
        X = l
    return X+1