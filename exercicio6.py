import numpy as np

def exercicio6(qtd_divisoes: int) -> (np.array, int):
    var = 1/qtd_divisoes
    passos = np.concatenate([np.array([0]), np.random.normal(0, var**0.5, qtd_divisoes-1)])
    caminho = np.cumsum(passos, 0)
    M1 = np.amax(caminho)
    return caminho, M1