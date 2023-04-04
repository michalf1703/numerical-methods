import numpy as np


def horner(n, tab):
    result = 0
    for i in tab:
        result = result * n + i
    return result

def function(x, flag):
    fx = 0.0
    if flag == '1':
        parameters = [2, 3, 4, -1]
        fx = horner(x, parameters)
    if flag == '2':
        parameters = [1, 0, 0, 2, -3]
        fx = horner(x, parameters)
    if flag == '3':
        parameters = [2, -3, -5]
        fx = horner(x, parameters)
    if flag == '4':
        fx = 3 * np.sin(x) - np.cos(x)
    if flag == '5':
        fx = np.cos(x) + 2 * np.sin(x)
    if flag == '6':
        fx = 7 ** x - 4
    if flag == '7':
        fx = 10 ** x - 2
    if flag == '8':
        parameters = [1, 0, 0, 0]
        fx = horner(x, parameters) + 5**x - np.sin(x)
    if flag == '9':
        parameters = [2, 0, 0, 0, 0]
        fx = horner(x, parameters) + 2**x - np.cos(x)
    return fx

