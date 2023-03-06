import funkcje as f


def falsiEps(a, b, eps, flag):
    fa = f.function(a,flag)
    fb = f.function(b,flag)
    iter = 0
    if fa * fb > 0:
        print("Funkcja nie spełnia założeń (fa * fb >0) ")
    else:
        guardian = True
        while guardian is True:
            iter += 1
            x0 = b - (fb * (b - a)) / (fb - fa)
            fx0 = f.function(x0, flag)
            if abs(fx0) < eps:
                return x0, iter
            if fx0 * fb < 0:
                a = x0
                fa = fx0
            else:
                b = x0
                fb = fx0
            if abs(b - a) < eps:
                return (a + b) / 2, iter

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




