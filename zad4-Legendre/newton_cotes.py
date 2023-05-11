def simpson(a, b, f, w):
    # Obliczenie szerokości przedziału całkowania
    h = (b - a) / 2
    # Zastosowanie metody Simpsona do obliczenia całki
    integral = h / 3 * ((w(a) * f(a))
                      + 4 * (w(a + b / 2) * f(a + b / 2))
                      + (w(b) * f(b)))
    # Zwrócenie wyniku całkowania
    return integral


def advanced_simpson(left, right, function, weight, epsilon):
    # Obliczenie całki metodą Simpsona na początku
    integral = simpson(left, right, function, weight)
    # Ustawienie zmiennej isNotAccurate na True, by rozpocząć pętlę while
    isNotAccurate = True
    # Ustawienie początkowej liczby podprzedziałów równą 2
    n = 2
    # Pętla while sprawdzająca dokładność obliczeń
    while isNotAccurate:
        new_integral = 0
        # Obliczenie szerokości każdego z podprzedziałów
        h = (right - left) / (2 * n)
        a = left
        b = a + 2 * h
        # Pętla for wykorzystująca metodę Simpsona do obliczenia całki w każdym podprzedziale
        for i in range(n):
            i = simpson(a, b, function, weight)
            new_integral += i
            a = b
            b += 2 * h
        # Sprawdzenie warunku dokładności obliczeń
        if abs(new_integral - integral) < epsilon:
            isNotAccurate = False
            integral = new_integral
        else:
            integral = new_integral
            n += 1
    # Zwrócenie wyniku całkowania
    return integral


def newton_cotes(function, weight, epsilon):
    # Ustawienie początkowej wartości przedziału całkowania
    a = 0
    # Ustawienie początkowego przyrostu przedziału
    delta = 1
    # Ustawienie początkowej wartości sumy całek na 0
    sum = 0
    # Ustawienie zmiennej isNotAccurate na True, by rozpocząć pętlę while
    isNotAccurate = True
    # Pętla while sprawdzająca dokładność obliczeń
    while isNotAccurate:
        # Obliczenie całki za pomocą funkcji advanced_simpson()
        integral = advanced_simpson(a, a + delta, function, weight, epsilon)
        # Dodanie wartości całki do sumy całek
        sum += integral
        # Zwiększenie wartości początkowej przedziału o przyrost
        a += delta
        # Wyświetlenie informacji o aktualnej wartości przedziału i przyroście
        print("A: " + str(a))
        print("Delta: " + str(delta))
        # Sprawdzenie warunku dokładności obliczeń
        if abs(integral) <= abs(epsilon):
            isNotAccurate = False
    return sum