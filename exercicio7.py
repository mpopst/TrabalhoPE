import numpy as np 
from exercicio6 import exercicio6

def black_sholes(S_0, r, sigma, t, Wt):
    expoente = ((r - ((sigma**2))/2) * t) + (sigma * Wt)
    return S_0 * np.exp(expoente)


def simula_black_sholes(S_0, r, sigma, T=1):
    if T != 1: raise NotImplementedError
    qtd_particao = 100
    W = exercicio6(qtd_particao)[0]
    ans = [black_sholes(S_0,r,sigma,t/100,W[t]) for t in range(100)]
    return ans

def simula_black_sholes_so_o_final(S_0,r,sigma,T):
    return simula_black_sholes(S_0, r, sigma,T)[-1]

def precifica_call(S_0, r, sigma, T, K, N):
    soma = 0
    for ST in [simula_black_sholes_so_o_final(S_0,r,sigma,T) for n in range(N)]:
        soma += np.exp(-r*T) * max(ST-K,0)
    return soma/N
