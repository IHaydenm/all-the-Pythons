def trapezoidal_simple(f, a, b):
    h = b - a
    return h * (0.5 * f(a) + (3/8) * f(b))
def application():
    from math import exp
    v = lambda t: 3 * (t ** 2) * exp(t ** 3)
    numerical = trapezoidal_simple(v, 0, 1)
    # Compare with exact result
    V = lambda t: exp(t ** 3)
    exact = V(1) - V(0)
    error = abs(exact - numerical)
    print("{:.16f}, error: {:g}".format(numerical, error))