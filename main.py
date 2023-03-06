import falsi
import bisekcja
import wykres
from numpy import double


def main():

#wybor rodzaju funkcji
    funkcja = input("Wybierz rodzaj funkcji:\n"
                    " 1) Wielomian,\n"
                    " 2) Funkcja trygonometryczna,\n"
                    " 3) Funkcja wykladnicza,\n"
                    " 4) Funkcja zlozona\n")

#wybieramy przedzial
    check = False
    while not check:
        x_min = double(input("Wartosc lewego przedzialu: "))
        x_max = double(input("Wartosc prawego przedzialu: "))
        if x_min <= x_max:
             check = True
        if not check:
           print("Wartosc lewego przedzialu musi byc mniejsza niz wartosc prawego przedzialu!\n")
#
    zatrzymanie = input("Wybierz kryterium zatrzymania algorytmu:\n"
                            " 1) Spelnienie warunku nalozonego na dokladnosc,\n"
                            " 2) Zadana liczba iteracji\n")
    if zatrzymanie == '1':
         dokladnosc = double(input("Podaj wartosc dokladnosci: "))
         print("\n\nWynik dla bisekcji:\n")
         print(str(bisekcja.bisekcjaEps(x_min, x_max, dokladnosc, funkcja)[0]) + "\nIlosc iteracji: " +
               str(bisekcja.bisekcjaEps(x_min, x_max, dokladnosc, funkcja)[1]))
         wykres.wykresB(x_min,x_max,bisekcja.bisekcjaEps(x_min,x_max,dokladnosc,funkcja)[0],funkcja)
         print("\n\nWynik dla Reguly Falsi:\n")
         print(str(falsi.falsi(x_min, x_max, dokladnosc, funkcja)[0]) + "\nIlosc iteracji: " +
               str(falsi.falsi(x_min, x_max, dokladnosc, funkcja)[1]))
         wykres.wykresF(x_min, x_max, falsi.falsi(x_min, x_max, dokladnosc, funkcja)[0], funkcja)

    if zatrzymanie == '2':
        iteracja = int(input("Podaj ilosc iteracji jaka ma sie wykonac:"))
        print("\n\nWynik dla bisekcji:\n\n")
        print(str(bisekcja.bisekcjaIter(x_min, x_max, iteracja, funkcja)))
        wykres.wykresB(x_min, x_max, bisekcja.bisekcjaIter(x_min, x_max, iteracja, funkcja), funkcja)
        print("\n\nWynik dla Reguly Falsi:\n\n")
        print(str(falsi.falsiIter(x_min, x_max, iteracja, funkcja)))
        wykres.wykresF(x_min, x_max, bisekcja.bisekcjaIter(x_min, x_max, iteracja, funkcja), funkcja)

if __name__ == '__main__':
    main()