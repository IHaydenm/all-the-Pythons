import numpy as np
#### EJERCICIO 1 ####
#A = np.array([[1,-2,3], [4,1,-1], [2, -1, 3]])
#b = np.array([[11], [4], [10]])
#### EJERCICIO 2 ####
A = np.array([[1., -1., 3.], [3.,-3.,1.], [1., 1., 0.]])
b = np.array([[2.], [-1.], [3.]])
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