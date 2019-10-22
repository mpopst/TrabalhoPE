import numpy as np





## funções auxiliares

def validar_matriz(P: np.array, n):
    if P.shape[0] != n or P.shape[1] != n:
        raise ArithmeticError("tamanho ilegal")
    for i in range(0,n):
        if sum(prob for prob in P[i,:]) != 1:
            raise ArithmeticError("formato ilegal")