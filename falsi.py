import funkcje as f


def falsiEps(x_min, x_max, dokladnosc, wyborFunkcja):
    fa = f.function(x_min,wyborFunkcja)
    fb = f.function(x_max,wyborFunkcja)
    iteracja = 0
    if fa * fb > 0:
        print("Funkcja nie spełnia założeń (fa * fb >0) ")
    else:
        guardian = True
        while guardian is True:
            iteracja += 1
            x0 = x_max - (fb * (x_max - x_min)) / (fb - fa)
            fx0 = f.function(x0, wyborFunkcja)
            if abs(fx0) < dokladnosc:
                return x0, iteracja
            if fx0 * fb < 0:
                x_min = x0
                fa = fx0
            else:
                x_max = x0
                fb = fx0
#warunek zakonczenia; WARIANT A
            if abs(x_max - x_min) < dokladnosc:
                return (x_min + x_max) / 2, iteracja

def falsiIter(a, b, N, flag):
    fa = f.function(a,flag)
    fb = f.function(b,flag)
    iter = 0
    if fa * fb > 0:
        print("Funkcja nie spełnia założeń (fa * fb >0) ")
    else:
        guardian = True
        while iter < N and guardian is True:
            iter += 1
            x0 = b - (fb * (b - a)) / (fb - fa)
            fx0 = f.function(x0, flag)
            if fx0 == 0:
                return x0
            if fx0 * fb < 0:
                a = x0
                fa = fx0
            else:
                b = x0
                fb = fx0
            if iter == N:
                print("Osiągnięto maksymalną liczbę iteracji.")
                return x0
    return x0



