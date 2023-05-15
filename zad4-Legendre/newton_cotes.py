import functions as f

# Definicja funkcji Simpsona
def simpson_formula(a: float, b: float, flag: str) -> float:
    quotient = (b - a) / 6.  # Obliczenie współczynnika
    return quotient * (f.function_value(a, flag) + 4 * f.function_value((a + b) / 2, flag) + f.function_value(b, flag))


# Definicja funkcji obliczającej całkę metodą Newtona-Cotesa
def newton_cotes_quadrature(a: float, b: float, flag: str, n: int) -> float:
    result = 0  # Inicjalizacja zmiennej wynikowej
    for i in range(n):
        h = (b - a) / n  # Obliczenie szerokości przedziału podcałkowego
        result += simpson_formula(a + i * h, a + h * (i + 1), flag)  # Dodanie wyniku z podprzedziału do zmiennej wynikowej
    return result  # Zwrócenie wyniku całkowania
