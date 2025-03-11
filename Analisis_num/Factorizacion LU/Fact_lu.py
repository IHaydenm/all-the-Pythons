import numpy as np
def lu_decomposition(A):
    n = A.shape[0]
    L = np.zeros_like(A)
    U = np.zeros_like(A)
    for i in range(n):
        for j in range(i, n):
            U[i, j] = A[i, j] - np.dot(L[i, :i], U[:i, j])
        for j in range(i+1, n):
            L[j, i] = (A[j, i] - np.dot(L[j, :i], U[:i, i])) /U[i, i]
        L[i, i] = 1
    return L, U
#### EJERCICIO 1 ####
