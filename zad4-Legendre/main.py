import newton_cotes as nc
import gaussian_legendre as gl


def main():
    # Wczytanie wybranej funkcji przez użytkownika
    chosen_function = input("Wybierz funkcje:\n"
                            "1. x^2 - 3x + 3\n"
                            "2. cos(x) * (x + 8)\n"
                            "3. 1 / (x^2)\n"
                            "4. x^4 + 2x - 3, \n"
                            "5. 3sin(x) - cos(x) \n")
    # Sprawdzenie, czy użytkownik podał prawidłowy numer funkcji
    while not (chosen_function.isdigit() or '1' <= chosen_function <= '3'):
        chosen_function = input("Niepoprawny wybor, spróbuj ponownie: ")
    # Wczytanie przedziału całkowania
    input_a = float(input("Podaj poczatek przedziału a: "))
    input_b = float(input("Podaj koniec przedzialu b: "))
    # Sprawdzenie, czy przedział jest prawidłowy
    while not (input_a < input_b):
        print("Początek przedziału musi być mniejszy niż koniec przedziału!")
        input_a = float(input("Podaj poczatek przedziału a: "))
        input_b = float(input("Podaj koniec przedzialu b: "))
    # Wczytanie dokładności obliczeń
    input_epsilon = float(input("Podaj epsilon e: "))

    # Przygotowanie do iteracyjnego obliczania całki metodą Newtona-Cotesa
    iterations = 1
    previous_result_nc = 0
    result_nc = nc.newton_cotes_quadrature(input_a, input_b, chosen_function, iterations)
    # Iteracyjne obliczenie całki metodą Newtona-Cotesa, aż do osiągnięcia zadanej dokładności
    while abs(previous_result_nc - result_nc) > input_epsilon:
        iterations += 1
        previous_result_nc = result_nc
        result_nc = nc.newton_cotes_quadrature(input_a, input_b, chosen_function, iterations)

    # Wyświetlenie wyników całkowania metodą Newtona-Cotesa
    print(f"Wynik dla Newtona Cotesa:{round(result_nc, 5)} Liczba iteracji: {iterations}")

    # Obliczenie całek metodą Gaussa-Legendre'a z użyciem różnej liczby węzłów i wyświetlenie wyników
    for i in range(2, 6):
        result_gl = gl.gaussian_legendre_quadrature(input_a, input_b, chosen_function, i)
        print(f"Wynik dla kwadratura Gaussa-Legendre'a: {round(result_gl, 5)}   Liczba węzłów: {i}")


# Wywołanie funkcji main
if __name__ == '__main__':
    main()
