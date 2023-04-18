import funkcje as f

#regula Falsi - regula falszywej prostej

#metoda znajdujaca miejsca zerowe funkcji wybranej przez uzytkownika
# za pomoca Zasady Falsi z wykorzystaniem kryterium stopu poprzez osiagniecie zadanej dokladnosci obliczen
def falsiEps(a, b, eps, flag):
    # podane krance przedzialu podstawiamy do funkcji wybranej przez uzytkownika
    fa = f.function(a, flag)
    fb = f.function(b, flag)
    # zliczamy liczbe wykonanych iteracji na potrzeby sprawodzania
    iter = 0
    # sprawdzamy poprawnosc zalozenia o przeciwnych znakach funkcji na krancach badanego przedzialu
    if fa * fb > 0:
        print("Funkcja nie spełnia założeń (fa * fb >0) ")
    else:
        guardian = True
#wartosc poprzedniej iteracji
        x_prev = None
        while guardian:
            iter += 1
            x0 = b - (fb * (b - a)) / (fb - fa)
            fx0 = f.function(x0, flag)
            if fx0 * fb < 0:
                a = x0
                fa = fx0
            else:
                b = x0
                fb = fx0
            if x_prev and abs(x0 - x_prev) < eps:
                return x0, iter
            x_prev = x0

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
                return x0
    return x0




