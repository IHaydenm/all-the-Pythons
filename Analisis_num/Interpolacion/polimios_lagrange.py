import numpy as np
import matplotlib.pyplot as plt
x0 = 1.8
increment = 0.1
x1 = x0 + increment
x = np.array([x0, x1])
print("x: ", x)
y = np.log(x)
print("y: ", y)

# Exact/Analytical Solution
dydx_exact = 1/x0
print("dydx_exact: ", dydx_exact)

# Numerical Solution
dydx_num = np.diff(y)/np.diff(x)
print("dydx_num: ", dydx_num)
############ NUEVA PARTE 25/03/2025 ##################
def forward(f, x0, increment): # FORWARD EULER
    dydx_num = (f(x0+increment)-f(x0))/increment;
    print("dydx_num: ", dydx_num)
    return dydx_num
def backward(f, x0, decrement): # BACKWARD EULER
    dydx_num = (f(x0+decrement)-f(x0))/decrement;
    print("dydx_num: ", dydx_num)
    return dydx_num
def central (f, x0, h): # CENTRAL
    dydx_num = (f(x0+h)-f(x0-h))/(2*h);
    print("dydx_num: ", dydx_num)
    return dydx_num
def exact(Df, x0):
    #Exact/Analytical Solution
    dydx_exact = Df(x0)
    print("dydx_exact: ", dydx_exact)
    return dydx_exact
def plot_resultsLabels(x0, f, dydx_exact, dydx_num):
    y0 = f(x0)
    #Dominio para gradicar la funcion
    x_vals = np.linspace(x0-1, x0+1, 100)
    y_vals = f(x_vals)
    #Recta tangente (usamos la derivada exacta)
    tangent_line = dydx_exact * (x_vals - x0) + y0
    #print(tangent_line)
    #Recta tangente (usamos derivada numerica)
    tangent_lineNum = dydx_num * (x_vals - x0) + y0
    #print(tangent_lineNum)
    fig = plt.figure()
    fig.suptitle('Aproximacion de la derivada', fontsize = 12)
    plt.plot(x_vals, y_vals, 'b', label = f'Función original')
    plt.plot(x0, y0, 'o', color='red')
    plt.plot(x_vals, tangent_line, 'g--', label = f'Recta tangente exacta: {round(dydx_exact, 4)}')
    plt.plot(x_vals, tangent_lineNum, 'r--', label = f'Recta tangente aproximada: {round(dydx_num[0], 4)}')
    plt.grid()  
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    return None
##### FUNCTION CALLING ##### 
f = lambda X: np.log(x)
Df = lambda x: 1/x
x0 = 1.8
h = 0.01
dydx_exact = exact(Df, x0)
############################
increment = h
dydx_num = forward (f, x0, increment)
plot_resultsLabels(x0, f, dydx_exact, dydx_num)