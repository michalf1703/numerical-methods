import math

def linear(x):
    return 4 * x + 3


def absolute_x(x):
    return abs(x)


#git funkcja
def polynomial(x):
    fx = 0.0
    parameters = [-3,-1,4,9]
    fx = horner(x, parameters)
    return fx


def trigonometric(x):
    return math.sin(x)


def composite_1(x):
    return 4 * x * abs(x)


def composite_2(x):
    return math.sin(x) + ((2 * x + 2) * x + 4) * x - 1
def composite_3(x):
    return abs(math.cos(3*x+1))


def horner(n, tab):
    result = 0
    for i in tab:
        result = result * n + i
    return result

