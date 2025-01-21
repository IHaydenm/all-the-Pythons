import random as rd
#aqui creamos la funcion 
def UtilizingFunction(containerMeasure): 
    t = int(rd.random()*10)  
    print(t) 
    containerMeasure = t^3 - (2*(t^2)) - (2*(t)) + 15 
    return containerMeasure

measure = int(input("DAME LA ALTURA DEL TANQUE DE AGUA (RECUERDA QUE ESTA EN CM.):  "))
calcFillingTime = UtilizingFunction(measure) 
print("ESTE ES EL RESULTADO: ", calcFillingTime)
