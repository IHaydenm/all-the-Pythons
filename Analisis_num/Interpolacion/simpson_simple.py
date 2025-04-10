def simpson_simple(f, a, b):
    h = (b - a) / 2
    c = (a + b) / 2
    return (h / 3) * (f(a) + 4 * f(c) + f(b))
def application():
    from math import exp 
    v = lambda t: 3 * (t ** 2) * exp(t ** 3)
    numerical = simpson_simple(v, 0, 1)
    V = lambda t: exp(t ** 3)
    exact = V(1) - V(0)
    error = abs(exact - numerical)
    print("Simpson 1/3 simple {:.16f}, error: {:g}".format(numerical, error))