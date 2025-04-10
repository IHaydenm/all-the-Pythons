"""
TAREA: SISTEMAS DE ECUACIONES LINEALES
AUTOR: AOLS
"""
import numpy as np
from numpy import linspace
#1 
A = [[3, 2], [5, 2]]
B = [[4], [12]]
A_augmented= [[3, 2, 4], [5, 2, 12]]
x = np.linalg.solve(A,B)
print("THIS IS THE SOLUTION FOR #1: ", x)
A1 = np.array(A)
print(A1.shape)
B1 = np.array(B)
print(B1.shape)
#2
A = [[1, -1], [2, -1]]
B = [[7], [14]]
A_augmented = [[1, -1, 7], [2, -1, 14]]
x = np.linalg.solve(A,B)
print("THIS IS THE SOLUTION FOR #2: ", x)
A1 = np.array(A)
print(A1.shape)
B1 = np.array(B)
print(B1.shape)
#3
A = [[1, -1], [2, -2]]
B = [[7], [10]]
A_augmented = [[1, -1, 7], [2, -2, 10]]
x = np.linalg.solve(A,B)
print("THIS IS THE SOLUTION FOR #3: ", x)
A1 = np.array(A)
print(A1.shape)
B1 = np.array(B)
print(B1.shape)
#4
A = [[2, -3, 1], [1, -1, 2], [3, 1, -1]]
B = [[-1], [-3], [-9]]
A_augmented = [[2, -3, 1, -1], [1, -1, 2, -3], [3, 1, -1, -9]]
x = np.linalg.solve(A,B)
print("THIS IS THE SOLUTION FOR #4: ", x)
A1 = np.array(A)
print(A1.shape)
B1 = np.array(B)
print(B1.shape)
#5
A = [[1, -1, 4], [3, 0, 1], [-1, 1, -4]]
B = [[-5], [0], [20]]
A_augmented = [[1, -1, 4, -5], [3, 0, 1, 0], [-1, 1, -4, 20]]
x = np.linalg.solve(A,B)
print("THIS IS THE SOLUTION FOR #5: ", x)
A1 = np.array(A)
print(A1.shape)
B1 = np.array(B)
print(B1.shape)
#6
A = [[-1, 1, 2], [1, 2, 1], [-3, -1, 1]]
B = [[0], [6], [-6]]
A_augmented = [[-1, 1, 2, 0], [1, 2, 1, 6], [-3, -1, 1, -6]]
x = np.linalg.solve(A,B)
print("THIS IS THE SOLUTION FOR #6: ", x)
A1 = np.array(A)
print(A1.shape)
B1 = np.array(B)
print(B1.shape)
#7
A = [[-0.60, 0.20, 0.20], [0.10, -0.30, 0.20], [0.50, 0.10, -0.40]]
B = [[0], [0], [0]]
A_augmented = [[-0.60, 0.20, 0.20, 0], [0.10, -0.30, 0.20, 0], [0.50, 0.10, -0.40, 0]]
x = np.linalg.solve(A,B)
print("THIS IS THE SOLUTION FOR #7: ", x)
A1 = np.array(A)
print(A1.shape)
B1 = np.array(B)
print(B1.shape)
#8
A = [[-0.80, 0.70], [0.80, 0.70]]
B = [[0], [0]]
A_augmented = [[-0.80, 0.70, 0], [0.80, 0.70, 0]]
x = np.linalg.solve(A,B)
print("THIS IS THE SOLUTION FOR #8: ", x)
A1 = np.array(A)
print(A1.shape)
B1 = np.array(B)
print(B1.shape)
#9
A = [[-0.80, 0.80, 0.40], [0.30, 0.90, 0.40], [0.50, 0.10, -0.80]]
B = [[0], [0], [0]]
A_augmented = [[-0.80, 0.80, 0.40, 0], [0.30, 0.90, 0.40, 0], [0.50, 0.10, -0.80, 0]]
x = np.linalg.solve(A,B)
print("THIS IS THE SOLUTION FOR #9: ", x)
A1 = np.array(A)
print(A1.shape)
B1 = np.array(B)
print(B1.shape)
#10
A = [[-0.35, 0.30, 0.30, 0.20], [0.1, -0.90, 0.15, 0.10], [0.25, 0.35, -0.85, 0.30], [0, 0.25, 0.40, -0.60]]
B = [[0], [0], [0], [0]]
A_augmented = [[-0.35, 0.30, 0.30, 0.20, 0], [0.1, -0.90, 0.15, 0.10, 0], [0.25, 0.35, -0.85, 0.30, 0], [0, 0.25, 0.40, -0.60, 0]]
x = np.linalg.solve(A,B)
print("THIS IS THE SOLUTION FOR #10: ", x)
A1 = np.array(A)
print(A1.shape)
B1 = np.array(B)
print(B1.shape)
#15
A = [[1, 1, 1], [2, 3, -1], [6, -2, -3]]
B = [[6], [5], [-7]]
A_augmented = [[1, 1, 1, 6], [2, 3, -1, 5], [6, -2, -3, -7]]
x = np.linalg.solve(A,B)
print("THIS IS THE SOLUTION FOR #15: ", x)
A1 = np.array(A)
print(A1.shape)
B1 = np.array(B)
print(B1.shape)
