import numpy as np

def entre_chegadas(lamb: int, T: int) -> np.array:
    ans = [0]
    while ans[-1] < T:
        ans.append(ans[-1] + np.random.exponential(lamb))
    return np.array(ans[1:-1])

