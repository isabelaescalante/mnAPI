import math
import numpy as np

def pivote(m, n, i):
    max = -1e100
    for r in range(i, n):
        if np.any(max < abs(m[r][i])):
            max_row = r
            max = abs(m[r][i])
    m[i], m[max_row] = m[max_row], m[i]

def solve_sistema(m_string):
    m_string += ' '
    aSplit = m_string.split('; ')

    m = []

    for item in aSplit:
            subl = []
            for num in item.split():
                subl.append(float(num))
            if (len(subl) != 0):
                m.append(subl)

    n = len(m)
    for i in range(n):
        pivote(m, n, i)
        for j in range(i+1, n):
            m[j] = [m[j][k] - m[i][k]*m[j][i]/m[i][i] for k in range(n+1)]

    x = [0] * n
    for i in range(n-1, -1, -1):
        s = sum(m[i][j] * x[j] for j in range(i, n))
        x[i] = (m[i][n] - s) / m[i][i]

    resultado = ""
    size = int(len(x))
    for i in range(0, size) :
        resultado += "x" + str(i) + "= " + str(x[i]) + " "
    
    return resultado


if __name__ == '__main__':
    m_string = "1 2 -1 3; 0 -3 7 2; 5 2 0 2"
    print(solve_sistema(m_string))

