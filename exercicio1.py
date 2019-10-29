from util import validar_matriz
import numpy as np

def exercicio1(P: np.matrix, i: int, j: int, epsilon: float):
    validar_matriz(P,5)
    p_minus = np.array([1 if elem == i else 0 for elem in range(1,6)])
    #p = p_minus.__copy__()
    p = np.array([0 for elem in range(1,6)])
    while (np.abs(p - p_minus) < epsilon): #TODO ver como que faz isso em Python
        p_minus, p = p, np.matmul(p_minus,P)
    return p[j-1]