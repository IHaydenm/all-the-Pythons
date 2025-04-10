import numpy as np
import matplotlib.pyplot as plt
"""
def plot_bisection(f, a_original, b_original, m_array):
    Grafica de la convergencia del metodo de biseccion.
    x = np.linspace(a_original - 0.1, b_original + 0.1, 400)
    y = f(x)
    plt.plot(x, y, label=f(x), color="green")
    plt.axhline(0, color="black", linestyle ='--', linewidth=0.8)
    for i in range(len(m_array)):
        plt.scatter(m_array, f(m_array[i]), color="red", label='Punto Medio!' if i == 0 else "")
    plt.xlabel("X")
    plt.ylabel(f(x))
    plt.title("GRAFICA PARA METODO DE BISECCION")
    plt.legend()
    plt.grid()
    plt.show()
    """
def my_bisection5(f, a, b, tol, max_iter, show_steps=False):
    if np.sign(f(a)) == np.sign(f(b)):
        raise ValueError("Los valores en a y b deben tener signos opuestos (f(a)*f(b))<0")
    iter_counter = 0
    a_original = a
    b_original = b
    m_array = []
    while iter_counter < max_iter:
        m = (a+b)/2
        m_array.append(m)
        if show_steps: 
            print(f"Iteracion {iter_counter}: a = {a}, b = {b}, m = {m}, f(m) = {f(m)}")
        if(np.abs(f(m))<tol):
            if np.sign(f(a)) == np.sign(f(m)):
                a = m
            else: 
                b = m 
            iter_counter += 1
            raise ValueError("El metodo no convergio en el numero maximo de iteraciones.")    
    
##### EJEMPLO 1 #####
f = lambda x: x**2 - 2
root = my_bisection5(f, 0, 2, 1e-5, 10, show_steps=False)
print("Solucion aproximada:  ", root)
