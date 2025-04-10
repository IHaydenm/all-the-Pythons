"""
    BISECION
    AUTOR: AOLS
"""
import numpy as np
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
print("THIS IS THE BEGINING OF THE FIRST EXAMPLE\n\n")
f = lambda x: 4*(x**3) - 6*(x**2) + 3*x - 2 ## FUNCTION DELCARATION
root = my_Bisection(f, 1, 2, 1e-5)
print("THIS IS THE SOLUTION TO THE FIRST ECUATION:  ", root) ##FIRST EXAMPLE ENDES HERE
##### EXAMPLE 2
print("THIS IS THE BEGINING OF THE SECOND EXAMPLE\n\n")
g = lambda x: x - 2**-x
root2 = my_Bisection(g, 0, 1, 1e-5)
print("THIS IS THE SOLUTION TO THE ECUATION:  ", root2) ##SECOND EXAMPLE ENDS HERE
##### EXAMPLE 3
print("THIS IS THE BEGINING OF THE THRID EXAMPLE\n\n")
h = lambda x: np.exp(x) - x**2 + 3*x + 2
root3 = my_Bisection(h, -1, 0, 1e-5)
print("THIS IS THE SOLUTION TO THE ECUATION:  ", root3) ##THIRD EXAMPLE ENDS HERE
##### EXAMPLE 4
print("THIS IS THE BEGINING OF THE FOURTH EXAMPLE\n\n")
l = lambda x: (2*x * np.cos(2*x)) - ((x+1)**2)
root4 = my_Bisection(l, -3, -2, 1e-5)
root4_1 = my_Bisection(l, -1, 0, 1e-5)
print("THESE ARE THE SOLUTIONS TO THE ECUATION:\nA)  " , root4, "\nB)", root4_1) ##FOURTH EXAMPLE ENDS HERE
##### EXAMPLE 5
print("THIS IS THE BEGINING OF THE FIFTH EXAMPLE\n\n")
t = lambda x: (x * np.cos(x)) - ((-2*x**2)) + 3*x - 1
root5 = my_Bisection(t, 0.2, 0.3, 1e-5)
root5_1 = my_Bisection(t, 1.2, 1.3, 1e-5)
print("THESE ARE THE SOLUTIONS TO THE ECUATION:\nA)  ", root5, "\nB)", root5_1) ##FIFTH EXAMPLE ENDS HERE