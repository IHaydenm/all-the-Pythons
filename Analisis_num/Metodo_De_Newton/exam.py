"""
AUTOR: ALSO
EXAMEN 1

PARTE 1
import numpy as np
def my_bisection (f , a , b , tol ) :
    if np.sign (f(a)) == np.sign (f(b)) :
        print ( " The scalars a and b do not bound a root . " )
        return None
    m = (a + b)/2
    if np.abs (f(m)) < tol:
        return m
    elif np.sign (f(a)) == np.sign (f(m)) :
        return my_bisection (f , m , b , tol )
    elif np.sign (f(b)) == np . sign (f(m)) :
        return my_bisection (f , a , m , tol )
    # Definicion de la funcion
    def f (x) :
        return (x**3) - 2
    # Llamada a la funcion
    root = my_bisection (f , 0 , 2 , 1e-4)
    print ( "Raiz aproximada: " , root )
"""
"""
PARTE 4
import numpy as np
import sympy as sp
from sympy import diff
from sympy . abc import x
from sympy import lambdify

max_iter = 10
## Algoritmo del Metodo Newton
def newton (f , Df , x0 , epsilon , max_iter ) :
    xn = x0
    for n in range (0 , max_iter ) :
        fxn = f ( xn )
        if abs ( fxn ) < epsilon :
            print(" Found solution after" , n , " iterations ." )
            return xn
        Dfxn = Df ( xn )
        if Dfxn == 0:
            print (" Zero derivative . No solution found . ")
            return None
        xn = xn - fxn / Dfxn
    print ("Exceeded maximum iterations . No solution found . ")
    return None
### Ejemplo 1
f = x **2 -2 
print ("f= " , f )
print ("tipo de dato: " , type ( f ) )
f_prime = diff (f, x)
print ("f_prime= " , f_prime )
print ( " tipo de dato " , type ( f_prime ) )
f = lambdify (x , f )
print ("tipo de dato: " , type ( f ) )
print (f(2))
f_prime = lambdify (x, f_prime )
print (f_prime (2) )
# ##### Llamando el metodo de Newton
newton (f, f_prime, 1.5, 1e-6, max_iter )
# ##### Llamando el metodo de Newton
newton (f, f_prime, 3, 1e-6, max_iter )
# ##### Llamando el metodo de Newton
newton (f, f_prime, 10, 1e-6, max_iter )
"""
"""
PARTE 3
import numpy as np
def newton (f , Df , x0 , epsilon , max_iter ) :
    xn = x0
    for n in range (0 , max_iter ) :
        fxn = f ( xn )
        if abs (fxn ) < epsilon :
            print ("Found solution after " , n ,"iterations .")
            return xn
        Dfxn = Df ( xn )
        if Dfxn == 0:
            print (" Zero derivative . No solution found .")
            return None
        xn = xn - fxn / Dfxn
    print (" Exceeded maximum iterations . No solution found . ")
    return None
# Definicion de la funcion y su derivada
def f (x) :
    return 3 - np.exp(x)
def Df (x) :
    return -(np.exp(x))
# Llamada a la funcion para 1
root = newton (f , Df , 1 , 1e-4 , 20)
print (" Raiz aproximada: ", root)
# Llamada a la funcion para 2
root = newton (f , Df , 2 , 1e-4 , 20)
print (" Raiz aproximada: ", root)
# Llamada a la funcion para 4
root = newton (f , Df , 4 , 1e-4 , 20)
print (" Raiz aproximada: ", root)
# Llamada a la funcion 8
root = newton (f , Df , 8 , 1e-4 , 20)
print (" Raiz aproximada: ", root)
# Llamada a la funcion para 16
root = newton (f , Df , 16 , 1e-4 , 20)
print (" Raiz aproximada: ", root)
"""