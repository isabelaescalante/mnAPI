import numpy as np
import math
from scipy.optimize import curve_fit

def exponencial(x_array, y_array) :
    x_string = str(x_array)
    y_string = str(y_array)
    x = np.fromstring(x_string, dtype=float, sep=',')
    y = np.fromstring(y_string, dtype=float, sep=',')

    popt, pcov = curve_fit(lambda t,a,b: a*np.exp(b*t),  x,  y)

    result = popt.tolist()
    string_result = "a: " + str(result[0]) + ", b: " + str(result[1])
    return string_result

def polinomial(x_array, y_array, n) :
    x_string = str(x_array)
    y_string = str(y_array)

    x = np.fromstring(x_string, dtype=float, sep=',')
    y = np.fromstring(y_string, dtype=float, sep=',')
    
    result = np.polyfit(x,y,n)

    final = result.tolist()
    size = int(len(final))
    resultado = ""
    for i in range(0, size) :
        resultado += "a" + str(i) + "= " + str(final[i]) + " "

    return resultado
    

if __name__ == '__main__':
    x = "1.2, 2.5, 3.3, 6.7, 4.5"
    y = "2.5, 2.2, 3.4, 12.8, 7.2"
    x1 = "1, 2, 3, 4, 5"
    y1 = "1.25, 2.4, 3.6, 4.75, 5"
    print(exponencial(x,y))
    print(polinomial(x1, y1, 2))
