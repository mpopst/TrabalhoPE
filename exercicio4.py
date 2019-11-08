import numpy as np

def entre_chegadas(lamb: int, T: int) -> np.array:
    ans = [0]
    while ans[-1] < T:
        ans.append(ans[-1] + np.random.exponential(lamb))
    return np.array(ans[1:-1])

def teorema448(n: int, lamb: int, T: int) -> np.array:
    # Seja n um parâmetro que representa a quantidade de processos de poisson que 
    # iremos gerar, sendo o lambda de cada um igual a lambda/n
    # Simulamos todos os n processos (talvez paralelamente), pegando os tempos de mudança 
    # de cada um em n arrays
    # Então, juntamos os arrays
    return