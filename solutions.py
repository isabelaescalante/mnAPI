from __future__ import print_function

import math
from sympy import Derivative

def biseccion(f_string, a, b, tol, iter_max) :
    f = lambda x: eval(f_string)
    fa = f(a)
    fb = f(b)
    #print(f_string)

    #if fa * fb > 0:
        #raise Exception("Error: La funcion no cambia de signo al final.")

    delta_x = math.fabs(b - a) / 2

    x = 0
    for iter in range(0, int(iter_max + 1)):
        x = (a + b) / 2
        fx = f(x)

        #print('iter: %.3d\t x: %+.4f\t fx: %+.4f\t delta_x: %+.4f\n' % (iter, x, fx, delta_x), end="")

        if delta_x <= tol and math.fabs(fx) <= tol:
            converged = True
            break

        if (fa * fx > 0):
            a = x
            fa = fx
        else:
            b = x

        delta_x = delta_x / 2

    root = x
    return [root]


def newtonRapson(f_string, df_string, x0, tol, iter_max) :
    f = lambda x: eval(f_string)
    df = lambda x: eval(df_string)
    x = x0
    fx = f(x)
    dfx = df(x)

    #print("iter: 0 x: %.4f\t dfx: %.4f\t Fx: %.4f\n" % (x, dfx, fx), end="")

    for iter in range(1, int(iter_max + 1)):
        deltaX = -fx / dfx
        x += deltaX
        fx = f(x)
        dfx = df(x)

        #print("iter: %.3d\t x: %.4f\t dfx: %.4f\t fx: %.4f\t deltaX: %.4f\n" % (iter, x, dfx, fx, deltaX), end="")

        if math.fabs(deltaX) <= tol and math.fabs(fx) <= tol or dfx == 0:
            converged = True
            break

    root = x
    return [root]

'''
if __name__ == '__main__':
    f = "0.95*x**3 - 5.9*x**2 + 10.9*x - 6"
    df = "2.85*x**2 - 11.8*x + 10.9"
    x = 3.5
    print(newtonRapson(f, df, x, 0.01, 3))
'''