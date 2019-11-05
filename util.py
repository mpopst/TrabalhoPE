import numpy as np
from numpy.random import choice
## funções auxiliares

def validar_matriz(P: np.matrix, n):
    if P.shape[0] != n or P.shape[1] != n:
        raise ArithmeticError("tamanho ilegal")
    for i in range(0,n):
        if sum(prob for prob in np.squeeze(np.asarray(P[i,:]))) != 1:
            raise ArithmeticError("formato ilegal")
        
def simulaca_markov(P: np.array, i: int, n: int):
    size = P.shape[0]
    X = i-1
    size = P.shape[0]
    for k in range(0,n):
        probs = np.squeeze(np.asarray(P[X,:]))
        X = choice(size,1, p = probs)[0]       
    return X+1