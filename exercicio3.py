import numpy as np

def martingal(ite: int):
    martingal = 1
    ans = []
    for i in range(ite):
        martingal *= _executa_xn_()
        ans.append(martingal)
    return ans
          

def _executa_xn_():
    if np.random.uniform() > 0.5:
        return 1.5
    else:
        return 0.5
