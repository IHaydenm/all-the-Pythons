from trapezoidal import trapezoidal
from trapezoidal_simple import trapezoidal_simple
from simpson_simple import simpson_simple
from metodo_Simpson3_8 import simpson_3_8
import numpy as np
from math import exp
v = lambda t: 3 * (t**2) * exp(t**3)
n = 4 
a = 0
b = 1
numerical = trapezoidal(v, 0, 1, n)
print(numerical)
n = 1
numerical1 =  simpson_3_8(v, a, b)
print("8a: ", numerical1)
numerical2 = trapezoidal_simple(v, a, b)
print("8b: ",numerical2)
numerical3 =  simpson_simple(v, a, b)
print("8c: ",numerical3)