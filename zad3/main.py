import draw_graph as df
import Newton_Chebyshev as nk
import functions as func

def main():
    #function, lower_range, upper_range, knots_number
    options = menu()
    x = nk.knots_x(options[3], options[1], options[2])
    y = nk.knots_y(x, options[0])
    a = nk.coefficients(x, y, options[3])
    print(nk.newton(a, x, 1.8))
    df.draw_functions(options[1], options[2], options[0], a, x, y)
def menu():
    function = choose_func()
    lower_range, upper_range = choose_range()
    knots_number = number_of_knots()
    return function, lower_range, upper_range, knots_number

def choose_func():
    while True:
        print("Wybierz funkcje: "
              "\n1. 4x+3"
              "\n2. |x|"
              "\n3. 2x^3 + 2x^2 + 4x - 1"
              "\n4. sin(x)"
              "\n5. 4x * |x|"
              "\n6. sin(x) + 2x^3 + 2x^2 + 4x - 1")
        choice = int(input("Wybrana funkcja: "))
        if choice == 1:
            return func.linear
        elif choice == 2:
            return func.absolute_x
        elif choice == 3:
            return func.polynomial
        elif choice == 4:
            return func.trigonometric
        elif choice == 5:
            return func.composite_1
        elif choice == 6:
            return func.composite_2
        print("Wybierz prawidłową liczbę (od 1 do 6)")


def choose_range():
    print("Wybierz przedział: ")
    lower_range = float(input("Dolny przedział: "))
    upper_range = float(input("Górny przedział: "))
    if lower_range > upper_range:
        return upper_range, lower_range
    return lower_range, upper_range


def number_of_knots():
    return int(input("Podaj ilość węzłów Czebyszewa: "))


if __name__ == '__main__':
    main()

