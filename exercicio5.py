import numpy as np

def kernel_f(x, xl, sigma, l):
    return sigma**2*np.exp(-.5 * (1/l**2) * (x-xl)**2)

def K(X, Xl, sigma, l):
    n, m = X.shape[0], Xl.shape[0]
    K = np.zeros((n, m))
    for i in range(n):
        for j in range(m):
            K[i,j] = kernel_f(X[i], Xl[j], sigma, l)
    return K

def exercicio5(X, X_new, Y, sigma):
    KXX = K(X, X, 1, 1)
    KXnX = K(X_new, X, 1, 1)
    KXXn = K(X, X_new, 1, 1)
    KXnXn = K(X_new, X_new, 1, 1)
    
    aux = KXnX.dot(np.linalg.inv(KXX+sigma**2*np.identity(KXX.shape[0])))

    mean = aux.dot(Y)
    covariance = KXnXn + sigma**2*np.identity(KXnXn.shape[0]) - aux.dot(KXXn)

    return(mean, covariance)

