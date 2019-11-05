import numpy as np

def passo_aleatorio(sigma: float) -> float:
    return sigma**2 * np.random.normal()
    
def exercicio6(num_passo: int) -> (np.array, int):
    var = 1/num_passo
    # passos = np.array([passo_aleatorio(tamanho_passo) for k in range(num_passo)])
    passos = np.random.normal(0, var**0.5, num_passo)
    caminho = np.cumsum(passos, 0)
    M1 = np.amax(caminho)
    return caminho, M1

# ans = 0
# iteqtd = 100000
# for i in range(iteqtd):
#     x,y = exercicio6(1000)
#     ans += y
# avg = ans/iteqtd
# print('ans: ' + str(ans) + " avg: " + str(avg))
    

