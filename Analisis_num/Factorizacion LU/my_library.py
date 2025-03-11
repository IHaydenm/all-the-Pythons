#Metodo de Gauss-Jordan
import numpy as np
#### EJERCICIO 1 ####
#A = np.array([[1,-2,3], [4,1,-1], [2, -1, 3]])
#b = np.array([[11], [4], [10]])
#### EJERCICIO 2 ####
#A = np.array([[1., -1., 3.], [3.,-3.,1.], [1., 1., 0.]])
#b = np.array([[2.], [-1.], [3.]])
#### EJERCICIO 2 REORDENADO####
#A = np.array([[1., 1., 0.], [1., -1., 3.], [3.,-3.,1.]])
#b = np.array([[3.], [2.], [-1.]])
print(A.dtype)
if np.linalg.det(A) != 0:
    print("El determinante es: ", round(np.linalg.det(A), 3))
    print("La solucion al sistema de ecuaciones lineales es: ")
    x =  np.linalg.solve(A,b)
    print(x)
else:
    print("La matriz A no es invertible (es singular)")
C= np. concatenate((A,b), axis = 1)
print(type(C))
print("Augmented matrix")
print(C)
sizeC = np.shape(C)
print("Augmented matrix size: ", sizeC)
print("Row count: ", sizeC[0])
print("Column count: ", sizeC[1]) 
def my_gauss_jordan(C, verbose=False):
    sizeC = C.shape

    for j in range (sizeC[1]-1):
        if verbose:
            print("------------------")
            print("Columna:", j)

        if C[j,j] !=1 and C[j,j] !=0:# Si ninguno es 1 o 0 encuentra el pivote
            C[j,:]=C[j,:]/C[j,j] #El : en C[j,:] es imprimir todo
            #if verbose:
            #print(C[j,:])
        elif C[j,j] == 0:
            indices = np.where(C[j+1:,j]!=0)[0]
            fila_a_intercambiar = indices[0]+j+1
            C[[j, fila_a_intercambiar]] = C[[fila_a_intercambiar, j]]
            print(C)
            C[j, :] = C[j, :]/C[j, j]
            if verbose:
                print("Found an element Zero!")
                print("indices: ", indices)
                print("Fila a permutar: ", fila_a_intercambiar)    
        else:
            if verbose:
                print("We have our pivot equal to 1 then the row is not modified")
                #print(C[j,:])

        for i in range (sizeC[0]):
            if verbose:
                print ("Row ", i)
            if i != j:
                C[i,:] = C[i,:] - C[i,j]*C[j,:]
                if verbose:
                    #print(C[i,:])
                    print(C)
            else:
                if verbose:
                    print("The indices are the same.")
    if verbose:
        print("Modified matriz: rref: Reduced Row Echelon Form")
        print(C)
    return C
A_rref = my_gauss_jordan(C,False)
print(A_rref)
#Metodo de eliminacion Gaussiana
 ########### EN CONSTRUCCION ###########
#Factorizacion LU
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

#Mostrar las matrizes
print("Mariz A: ")
print(A)
print("\n\nMatriz L (Triangular inferior): ")
print(L)
print("\n\nMatriz U (triangular superior): ")
print(U)

##### SUSTITUCION HACIA ADELANTE Y HACIA ATRAS #####
def forward_substitution(L, b):
    n = L.shape[0]
    y = np.zeros(n)

    for i in range(n):
        y[i] = (b[i] - np.dot(L[i, :i], y[:i])) / L[i, i]

    return y
def backward_substitution(U, y):
    n = U.shape[0]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):  # Iterates backwards
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]
    return x