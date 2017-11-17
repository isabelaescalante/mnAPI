import numpy as np
import math

def simpson_simple(f_string, b, a, n) :
    f = lambda x: eval(f_string)
    h = (b - a) / n

    sum_odd = 0
    sum_even = 0

    for i in range(0, int(n - 1)):
        x = a + (i + 1) * h
        if (i + 1) % 2 == 0:
            sum_even += f(x)
        else:
            sum_odd += f(x)

    xi = h / 3 * (f(a) + 2 * sum_even + 4 * sum_odd + f(b))
    return [xi]


def simpson_multiple(x_array, y_array) :
    x = x_array
    y = y_array
    if y.size != y.size:
        raise ("Error: 'x' & 'y' deben ser iguales.")

    h = x[1] - x[0]
    n = x.size

    sum_odd = 0
    sum_even = 0

    for i in range(1, n - 1):
        if (i + 1) % 2 == 0:
            sum_even += y[i]
        else:
            sum_odd += y[i]

    xi = h / 3 * (y[0] + 2 * sum_even + 4 * sum_odd + y[n - 1])
    return [xi]


def trapezoidal_simple(f, b, a, n) :
    xi = f + b + a + n
    '''
    h = (b - a) / n

    sum_x = 0

    for i in range(0, n - 1):
        x = a + (i + 1) * h
        sum_x += f(x)

    xi = h / 2 * (f(a) + 2 * sum_x + f(b))
    '''
    xi = round(xi, 4)
    return [xi]

def trapezoidal_multiple(x_array, y_array):
    x = np.array(x_array)
    y = np.array(y_array)
    if y.size != y.size:
        raise ("Error: 'x' & 'y' deben ser iguales.")

    h = x[1] - x[0]
    n = x.size

    sum_x = 0

    for i in range(1, n - 1):
        sum_x += y[i]

    xi = h / 2 * (y[0] + 2 * sum_x + y[n - 1])
    return [xi]
