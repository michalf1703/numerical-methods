import numpy as np

# Funkcja realizująca algorytm Hornera
def horner(n, tab):
    result = 0
    for i in tab:
        result = result * n + i
    return result

# Funkcja kwadratowa y = x^2 + x + 3
def quadratic_function(x: float) -> float:
    parameters = [1, 1, 3]
    return horner(x, parameters)

# Funkcja trygonometryczna y = cos(x) * (x + 8)
def trigonometric_function(x: float) -> float:
    return np.cos(x) * (x + 8)

# Funkcja losowa y = 1/(x^2)
def random_function(x: float) -> float:
    return 1/(x*x)

# Druga funkcja kwadratowa y = x^4 - 3x^3 + 2x^2 - 3
def quadratic_function2(x:float) -> float:
    parameters = [1, 0, 0, 2, -3]
    return horner(x, parameters)

# Druga funkcja trygonometryczna y = 3sin(x) - cos(x)
def trigonometric_function2(x:float)->float:
    return 3*np.sin(x) - np.cos(x)

# Funkcja obliczająca wartość funkcji zgodnie z przekazanym parametrem flag
def function_value(x: float, flag: str) -> float:
    if flag == '1':
        return quadratic_function(x)
    elif flag == '2':
        return trigonometric_function(x)
    elif flag == '3':
        return random_function(x)
    elif flag == '4':
        return quadratic_function2(x)
    elif flag == '5':
        return trigonometric_function2(x)
