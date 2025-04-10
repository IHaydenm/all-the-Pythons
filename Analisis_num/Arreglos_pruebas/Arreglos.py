"""
ACCESO A ARREGLOS EN PYTHON

a = [45, 848, 44, 14, 23, 54, 14, 4, 26, 47]
b = [34, 76, 91, 101, 2, 853, 36, 85, 99, 467]
elemento1 = b[0]
elemento4 = b[3]
print("Este es el valor en pos. 1: ", elemento1)
print("Este es el valor en pos. 4: ", elemento4)
print(a+b)

"""
"""
    ARREGLOS NUMERICOS EN PYTHON
    
import numpy as np
from numpy import linspace
x = np.linspace(0,2,3)
print('x:', X)
y = np.linspace(4, 5, 2)
print('y:', y)
print(x+y)
"""
"""
import numpy as np
from numpy import zeros
x = zeros(3, int)
print(x)
y = zeros(3)
print(y)
print(len(y))
#######
from numpy import array
x = array([0, 1, 2])
print(x)
x = array([0., 1., 2.,])
print(x)
"""
import numpy as np
matriz = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(matriz)
matriz1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matriz1)