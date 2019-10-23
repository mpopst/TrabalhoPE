import numpy as np

def martingal():
    ans = 1
    while True:
        ans *= _executa_xn_()
        yield ans  

def _executa_xn_():
    if np.random.uniform() > 0.5:
        return 1.5
    else:
        return 0.5
