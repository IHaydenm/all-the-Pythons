def simpson(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("n must be even to apply Simpson's 1/3 rule.")
    h = (b - a) / n
    f_sum = 0
    for i in range(1, n, 2):
        x = a + i * h
        f_sum += 4 * f(x)
    for i in range(2, n - 1, 2):
        x = a + i * h
        f_sum += 2 * f(x)
    return h / 3 * (f(a) + f_sum + f(b))