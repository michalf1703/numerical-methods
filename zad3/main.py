

def draw_menu():
    #while true:  --> to pozniej do petli
        print("Wybierz rownanie: \n")
        print("1.   4x + 3\n")
        print("2.   |x|\n")
        print("3.   2x^3 + 2x^2 + 4x - 1\n")
        print("4.   sin(x)\n")
        print("5.   4x * |x|\n")
        print("6.   sin(x) + 2x^3 + 2x^2 + 4x - 1 \n")
        choice = int(input("Wybór funkcji : "))

def choose_range():
    print("Wybierz przedział: ")
    lower_range = float(input("Dolny przedział: "))
    upper_range = float(input("Górny przedział: "))
    if lower_range > upper_range:
        return upper_range, lower_range
    return lower_range, upper_range

def choose_number_of_knots():
    return int(input("Podaj liczbę węzłów Czebyszewa: "))


if __name__ == '__main__':
    draw_menu()




