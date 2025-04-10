"""
METODO DE NEWTON SIN AUTOMATIZACION DE DERIVADAS
AUTOR: AOLS
"""
import numpy as np
import sympy as sp
from sympy.abc import x
from sympy import lambdify

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
###### EXAMPLE 1 ######
print("EXAMPLE 1\n")
f = lambda x: x**2 - 2
f_prime = sp.diff(f,x)
print(f_prime)
f= lambdify(x,f)
f_prime = lambdify(x,f_prime)
estimate = newton(f, f_prime, 1.5, 1e-4, 10)
print("THIS IS THE ESTIMATE " , estimate)
###### EXAMPLE 2 ######
print("\EXAMPLE 2\n")
f = lambda x: x*3 + 4*x*2-10
f_prime = sp.diff(f,x)
print(f_prime)
f= lambdify(x,f)
f_prime = lambdify(x,f_prime)
estimate = newton(f, f_prime, 1.5, 1e-4, 10)
print("THIS IS THE ESTIMATE " , estimate)
###### EXAMPLE 3 ######
print("EXAMPLE 3")
f = lambda x: np.sqrt(x) - np.cos(x)
f_prime = sp.diff(f,x)
print(f_prime)
f= lambdify(x,f)
f_prime = lambdify(x,f_prime)
estimate = newton(f, f_prime, 1.5, 1e-4, 10)
print("THIS IS THE ESTIMATE " , estimate)
###### EXAMPLE 4 ######
print("EXAMPLE 4")
f = lambda x: x**2-10*np.cos(x)
f_prime = sp.diff(f,x)
print(f_prime)
f= lambdify(x,f)
f_prime = lambdify(x,f_prime)
estimate = newton(f, f_prime, 1.5, 1e-4, 10)
print("THIS IS THE ESTIMATE " , estimate)
##### EXAMPLE 5#####
print("EXAMPLE 5")
f = lambda x: x*3-x*2-1
f_prime = sp.diff(f,x)
print(f_prime)
f= lambdify(x,f)
f_prime = lambdify(x,f_prime)
estimate = newton(f, f_prime, 1.5, 1e-4, 10)
print("THIS IS THE ESTIMATE " , estimate)
###### EXAMPLE 6 ######
print("EXAMPLE 6")
f = lambda x: x**(1/3)
f_prime = sp.diff(f,x)
print(f_prime)
f= lambdify(x,f)
f_prime = lambdify(x,f_prime)
estimate = newton(f, f_prime, 1.5, 1e-4, 10)
print("THIS IS THE ESTIMATE " , estimate)
###### EXAMPLE 7 ######
print("EXAMPLE 7")
f = lambda x: x**5 - 5*x + 3
f_prime = sp.diff(f,x)
print(f_prime)
f= lambdify(x,f)
f_prime = lambdify(x,f_prime)
estimate = newton(f, f_prime, 1.5, 1e-4, 10)
print("THIS IS THE ESTIMATE " , estimate)