import numpy as np


def horner(n, tab):
    result = 0
    for i in tab:
        result = result * n + i
    return result

def function(x, flag):
    fx = 0.0
    if flag == '1':
        parameters = [4, 3, 2, -1]
        fx = horner(x, parameters)
    if flag == '2':
        fx = 2 * np.sin(x) + np.cos(x)
    if flag == '3':
        fx = 7 ** x - 4
    if flag == '4':
        parameters = [1, 0, 0, 0]
        fx = horner(x, parameters) + 5**x - np.sin(x)
    return fx


