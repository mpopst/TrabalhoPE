import numpy as np

def entre_chegadas(lamb: int, T: int):
    ans = [0]
    while ans[-1] < T:
        step = np.random.exponential(lamb)
        if ans[-1] + step > T:
            break
        else:
            ans.append(ans[-1] + step)
    return ans

def teorema448(lamb: int, T: int):
    n = int(lamb*T) #foi o melhor chute de como escolher n, pois é a esperança do processo de Poisson
    ans = [0]
    for i in range(n):
        ans.append(np.random.uniform(low=0, high=T))
    ans.sort()
    return ans

def estima_integral(temposMudanca, T):
    NT = len(temposMudanca)
    multiplicando = NT * (T - temposMudanca[-1])
    somatorio = 0
    for k in range(1,NT-1):
        somatorio += k * (temposMudanca[k+1] - temposMudanca[k])
    return somatorio * multiplicando

