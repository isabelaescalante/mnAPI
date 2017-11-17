import numpy as np

def lagrange(x_array, y_array, x_int) :
    x = list(x_array)
    y = list(y_array)
    n = len(x)
    y_int = 0

    for i in range(0, n):
        p = y[i]
        for j in range(0, n):
            if i != j:
                p = p * (x_int - x[j]) / (x[i] - x[j])
        y_int = y_int + p

    return y_int

'''
if __name__ == '__main__' :
    x = np.array([2, 3, 5])
    y = np.array([6, 19, 99])
    x_int = 4
    print(lagrange(x, y, x_int))
'''