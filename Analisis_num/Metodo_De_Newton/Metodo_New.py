"""
METODO DE NEWTON SIN AUTOMATIZACION DE DERIVADAS
AUTOR: AOLS
"""
import numpy as np
def newton(f, Df, x0, epsilon, max_iter):
    xn=x0
    for n in range (0, max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print("Found solutions after", n, "iterations")
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print("zero derivatie. No solution found.")
            return None
        xn = xn - fxn/Dfxn
        print("Exceeded maximum iterations. No solutions found.")
        return None
###### EXAMPLE 1 #######
print("EXAMPLE 1")
f = lambda x: x**x-2
Df = lambda x: 2*x
estimate = newton(f, Df, 1.5, 1e-6, 100)
print("estimate = ", estimate)
###### EXAMPLE 2 #######
print("EXAMPLE 2")
f = lambda x: x**3 + 4*x**2 - 10
Df = lambda x: 3*x**2 + 4*x
estimate = newton(f, Df, 1.5, 1e-6, 100)
print("estimate = ", estimate)
###### EXAMPLE 3 #######
print("EXAMPLE 3")
f = lambda x: np.sqrt(x) - np.cos(x)
Df = lambda x: 1/(2*np.sqrt(x) + np.sin(x))
estimate = newton(f, Df, 1.5, 1e-6, 100)
print("estimate = ", estimate)
###### EXAMPLE 4 #######
print("EXAMPLE 4")
f = lambda x: x**2 - 10*np.cos(x)
Df = lambda x: 2*x + 10*np.sin(x)
estimate = newton(f, Df, 1.5, 1e-6, 100)
print("estimate = ", estimate)
###### EXAMPLE 5 #######
print("EXAMPLE 5")
f = lambda x: x**3 - x**2 - 1
Df = lambda x: 3*x**2 - 2*x
estimate = newton(f, Df, 1.5, 1e-6, 100)
print("estimate = ", estimate)
###### EXAMPLE 6 #######
print("EXAMPLE 6")
f = lambda x: x**(1/3)
Df = lambda x: (1/3)*x**(-2/3)
estimate = newton(f, Df, 1.5, 1e-6, 100)
print("estimate = ", estimate)
###### EXAMPLE 7 #######
print("EXAMPLE 7")
f = lambda x: x**5 - 5*x + 3
Df = lambda x: 5*x**4 - 5
estimate = newton(f, Df, 1.5, 1e-6, 100)
print("estimate = ", estimate)