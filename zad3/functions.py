import math

def linear(x):
    return 4 * x + 3


def absolute_x(x):
    return abs(x)


def polynomial(x):
    return ((2 * x + 2) * x + 4) * x - 1


def trigonometric(x):
    return math.sin(x)


def composite_1(x):
    return 4 * x * abs(x)


def composite_2(x):
    return math.sin(x) + ((2 * x + 2) * x + 4) * x - 1

