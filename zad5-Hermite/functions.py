from numpy import sin, cos, mean, min, max

def polynomial(x, tab):
    numOfFactors = len(tab)
    result = 0
    for i in range(numOfFactors - 1):
        if (i == (numOfFactors - 1)):
            result += tab[i]
        result += tab[i] * x ** (numOfFactors - 1 - i)

    return result


f1 = lambda x: abs(2 * x - 3)

f2 = lambda x: x + 2

f3 = lambda x: cos(2 * x)

f4 = lambda x: x * x

f5 = lambda x: cos(sin(x))

f6 = lambda x: 0.5 * x ** 3 + 3 * x ** 2 + 3 * x - 2  # 3x^4 - 2x^3 + 4x^2 + x + 1


def mean_error(actual_y, approx_y):
    for i in range(len(actual_y)):
        actual_y[i] = abs(actual_y[i] - approx_y[i])

    return mean(actual_y)

def max_deviation(actual_y, approx_y):
    for i in range(len(actual_y)):
        actual_y[i] = abs(actual_y[i] - approx_y[i])

    return max(actual_y)

def min_deviation(actual_y, approx_y):
    for i in range(len(actual_y)):
        actual_y[i] = abs(actual_y[i] - approx_y[i])

    return min(actual_y)
