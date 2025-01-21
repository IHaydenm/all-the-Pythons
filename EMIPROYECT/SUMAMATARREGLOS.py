import random as rd

#area de definicion de funciones propias
#funcion propia que establece el tamaño de una matriz

def tamMatr (fil,col):
    mtmp=[]
    for i in range (fil):
        mtmp.append([])
        mtmp[i]=[None]*col
    return mtmp    

#funcion propia que permite llenar una matriz con numero aleatorios decimales 
def llenaMatr(mtmp,fil,col):
    for i in range (fil):
        for j in range (col):
            mtmp[i][j]=rd.random()*100
    return mtmp

#funcion propia que suma dos matrices 
def SumaMatr(mtmpA,mtmpB,fil,col):
    mtmp=tamMatr(fil,col)
    for i in range (fil):
        for j in range (col):
            mtmp[i][j]=mtmpA[i][j]+mtmpB[i][j]
    return mtmp

#area del codigo general

f=int(input("Proporcione el numero de filas: "))
c=int(input("Proporcione el numero de columnas: "))

matrA=tamMatr(f,c)
matrB=tamMatr(f,c)
matrA=llenaMatr(matrA,f,c)
matrB=llenaMatr(matrB,f,c)

print("Matriz A",matrA)
print("Matriz B",matrB)

matrS=SumaMatr(matrA,matrB,f,c)
print("La suma de matrices es", matrS)

#ahora con arreglos

sumaNP=np.array(matrA)+np.array(matrB)
print("La suma con arreglos de matrices es", sumaNP)

