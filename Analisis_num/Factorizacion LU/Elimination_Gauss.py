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
A=np.array([[2, 3, 2, 4], [4, 10, -4, 0],[-3, -2, -5, -2],[-2, 4, 4, -7]], dtype = float)
#### Ejemplo 2 ####
A=np.array([[1, 4, 6],[2, -1, 3],[3, 2, 5]], dtype = float)
#### Ejemplo 3 ####
A=np.array([[2, 3, 1],[-1, 2, -3],[5, -1, -2]], dtype = float)

#Realizar la factorizacion sin permutaciones
print(lu_decomposition(A))
print("\n\n")
L,U = lu_decomposition(A)
