import funkcje as f


def bisekcjaEps(x_min, x_max, dokladnosc, wyborFunkcja):
    fa = f.function(x_min,wyborFunkcja)
    fb = f.function(x_max,wyborFunkcja)
    iteracja = 0
    if fa * fb > 0:
        print("Funkcja nie spelnia zalozen (fa * fb >0) ")
    else:
        guardian = True
        while guardian is True:
            iteracja += 1
            x0 = (x_min + x_max) / 2
            fx0 = f.function(x0, wyborFunkcja)
#warunek zakonczenia; WARIANT A
            if abs(x_max - x_min) < dokladnosc:
                return x0, iteracja
            if fx0 * fb < 0:
                x_min = x0
            else:
                x_max = x0
                fb = fx0


def bisekcjaIter(x_min, x_max, iteracja, wyborFunkcja):
    fa = f.function(x_min,wyborFunkcja)
    fb = f.function(x_max,wyborFunkcja)
    if fa * fb > 0:
        print("Funkcja nie spelnia zalozen (fa * fb >0) ")
    else:
        while iteracja > 0:
            x0 = (x_min + x_max) / 2
            fx0 = f.function(x0, wyborFunkcja)
            if fx0 == 0:
                return x0
            if fx0 * fb < 0:
                x_min = x0
            else:
                x_max = x0
                fb = fx0
            iteracja = iteracja - 1
        return x0