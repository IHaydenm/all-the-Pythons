import numpy as np   
import math
def my_Bisection(f, a, b, tol):
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception("The scalars a and b do not bound to a root")
    m = (a + b)/2
    if np.abs(f(m))<tol:
        return m
    elif np.sign(f(a)) == np.sign(f(m)):
        return my_Bisection(f, m, b, tol)
    elif np.sign(f(b)) == np.sign(f(m)):
        return my_Bisection(f, a, m, tol)
##### EXAMPLE 1 
print("THIS WILL BE THE FIRST EXAMPLE")
f = lambda x: 4*(x**3) - 6*(x**2) + 3*x - 2 
root = my_Bisection(f, 1, 2, 0.1)
print("THIS IS THE SOLUTION TO THE ECUATION:  ", root)