import numpy as np
## funções auxiliares

def validar_matriz(P: np.matrix, n):
    if P.shape[0] != n or P.shape[1] != n:
        raise ArithmeticError("tamanho ilegal")
    for i in range(0,n):
        if sum(prob for prob in np.squeeze(np.asarray(P[i,:]))) != 1:
            raise ArithmeticError("formato ilegal")
        
def simulaca_markov(P: np.array, i: int, n: int):
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