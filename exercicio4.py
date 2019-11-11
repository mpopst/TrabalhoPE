import numpy as np

def entre_chegadas(lamb: int, T: int):
    ans = [0]
    while ans[-1] < T:
        ans.append(ans[-1] + np.random.exponential(lamb))
    ans.append(T)
    return ans

def teorema448(lamb: int, T: int):
    n = lamb*T
    ans = [0, 5]
    for i in range(n):
        ans.append(np.random.uniform(low=0, high=T))
    ans.sort()
    return ans