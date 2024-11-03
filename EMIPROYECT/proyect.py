import random as random
#THIS WILL CREATE THE FUNCTION
def UtilizingFunction(containerMeasure): 
    t = int(random.random()*10)  
    print(t) 
    containerMeasure = t^3 - (2*(t^2)) - (2*(t)) + 15 
    return containerMeasure

measure = int(input("DAME LA ALTURA DEL TANQUE DE AGUA (RECUERDA QUE ESTA EN CM.):  "))
calcFillingTime = UtilizingFunction(measure) 
print("ESTE ES EL RESULTADO: ", calcFillingTime)
