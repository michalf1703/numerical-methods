import falsi
import bisekcja
import wykres
from numpy import double


def main():

    funkcja = input("Wybierz rodzaj funkcji:\n"
                    " 1) Wielomian: 2x^3 + 3x^2 + 4x - 1 \n"
                    " 2) Wielomian: x^4 + 2x - 3, \n"
                    " 3) Wielomian: 2x^2 - 3x - 5 \n"
                    " 4) Funkcja trygonometryczna: 3sin(x) - cos(x) \n"
                    " 5) Funkcja trygonometryczna: cos(x) + 2sin(x) \n"
                    " 6) Funkcja wykladnicza: 7^x - 4\n"
                    " 7) Funkcja wykladnicza: 10^x - 2\n"
                    " 8) Funkcja zlozona: x^3 + 5^x - sin(x) \n"
                    " 9) Funkcja zlozona: 2x^4 + 2^x - cos(x) \n")

#wybieramy przedzial na którym poszukiwane bedzie miejsce zerowe
    check = False
    while not check:
        x_min = double(input("Wartosc lewego przedzialu: "))
        x_max = double(input("Wartosc prawego przedzialu: "))
        if x_min <= x_max:
             check = True
        if not check:
           print("Wartosc lewego przedzialu musi byc mniejsza niz wartosc prawego przedzialu!\n")

#wybieramy kryterium zatrzymania algorytmu
    zatrzymanie = input("Wybierz kryterium zatrzymania algorytmu:\n"
                            " 1) Spelnienie warunku nalozonego na dokladnosc,\n"
                            " 2) Zadana liczba iteracji\n")
    if zatrzymanie == '1':
         dokladnosc = double(input("Podaj wartosc dokladnosci: "))
         print("\n\nWynik dla bisekcji:\n")
         print(str(bisekcja.bisekcjaEps(x_min, x_max, dokladnosc, funkcja)[0]) + "\nIlosc iteracji: " +
               str(bisekcja.bisekcjaEps(x_min, x_max, dokladnosc, funkcja)[1]))
         print("\n\nWynik dla Reguly Falsi:\n")
         print(str(falsi.falsiEps(x_min, x_max, dokladnosc, funkcja)[0]) + "\nIlosc iteracji: " +
               str(falsi.falsiEps(x_min, x_max, dokladnosc, funkcja)[1]))
         wykres.wykresPrawdziwy(x_min,x_max,funkcja)
         wykres.wykres(x_min,x_max,bisekcja.bisekcjaEps(x_min,x_max,dokladnosc,funkcja)[0],falsi.falsiEps(x_min,x_max,dokladnosc,funkcja)[0],funkcja)

    if zatrzymanie == '2':
        iteracja = int(input("Podaj ilosc iteracji jaka ma sie wykonac:"))
        print("\n\nWynik dla bisekcji:\n\n")
        print(str(bisekcja.bisekcjaIter(x_min, x_max, iteracja, funkcja)))
        print("\n\nWynik dla Reguly Falsi:\n\n")
        print(str(falsi.falsiIter(x_min, x_max, iteracja, funkcja)))
        wykres.wykresPrawdziwy(x_min, x_max, funkcja)
        wykres.wykres(x_min,x_max,bisekcja.bisekcjaIter(x_min,x_max,iteracja,funkcja),falsi.falsiIter(x_min,x_max,iteracja,funkcja),funkcja)

if __name__ == '__main__':
    main()