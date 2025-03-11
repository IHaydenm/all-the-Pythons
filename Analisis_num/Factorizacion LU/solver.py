import my_library as myL
import numpy as np
#C = np.array([[2, 3, 2, 4, 4], [4, 10,-4, 0,-8], [-3, -2, -5, -2, -4], [-2, 4, 4, -7, -1]])
#A_rref = myL.my_gauss_jordan(C, verbose=False)
#print(A_rref)  
A = np.array([[2, 3, 2, 4], [4, 10,-4, 0], [-3, -2, -5, -2], [-2, 4, 4, -7]])
L, U = myL.lu_decomposition(A)
print(L, U) 