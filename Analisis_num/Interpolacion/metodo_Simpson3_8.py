def simpson_3_8(f, a, b):
    h = b - a
    c = a + h
    d = a + (2*h)
    return (3 * h/8) * (f(a) + 3 * f(c) + 3 * f(d) + f(b))
def application():
    from math import exp
    v = lambda t: 3 * (t ** 2) * exp(t ** 3)
    numerical = simpson_3_8(v, 0, 1)
    # Compare with exact result
    V = lambda t: exp(t ** 3)
    exact = V(1) - V(0)
    error = abs(exact - numerical)
    print("{:.16f}, error: {:g}".format(numerical, error))
if __name__ == "__main__":
    application()