import math


def knots_x(knots_number: int, lower_range: float, upper_range: float):
    x = []
    #obliczanie węzłów Czebyszewa (jakiś x) na przedziale [-1,1] wzór cos(pi * (2i + 1) / (2*n + 1)) i przeskalowanie
    #ich do przedziału podanego w programie wzór (x[i] * (b - a) + (a + b)) / 2
    for i in range(knots_number):
        x.append((math.cos(math.pi * (2 * i + 1) / (2 * knots_number + 1)) *
                  (upper_range - lower_range) + (lower_range + upper_range)) * 0.5)

    return x

#obliczanie wartości funkcji (wybranej w menu) dla poszczególnych węzłów
def knots_y(x: [], function):
    y = []
    for knot in x:
        y.append(function(knot))

    return y

#wyznaczenie wyznaczników potrzebnych do obliczenia wartości przy użyciu ilorazu różnicowego
def coefficients(x: [], y: [], knots_number: int):
    a = y[::]
    for i in range(knots_number - 1):
        for j in range(knots_number - 1, i, -1):
            a[j] = (a[j] - a[j-1]) / (x[j] - x[j-i-1])

    return a

#obliczanie wartości wielomianu w postaci Newtona w danym punkcie
def newton(a: [], x: [], point: float):
    result = 0
    for i in range(len(x)):
        if a[i] != 0:
            multiplier = a[i]
            for j in range(i):
                multiplier = multiplier * (point - x[j])
            result += multiplier

    return result

