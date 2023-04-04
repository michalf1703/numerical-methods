import numpy as np
import sympy
from IPython.display import display
from wspolczynniki import file_len
from jordan_method import jordan

if __name__ == "__main__":
    i = 1
    print("Metoda eliminacji Jordana\n")
    print("-------------------------------------------")

    # Aby dodać własny układ równań, należy połączyć macierz współczynników z macierzą znajdującą się po znaku równości, dodając ją jako ostatnią kolumnę. Separator dziesiętny to kropka.
    # Kolejne linijki to kolejne wiersze, a kolumny powinny być oddzielone spacją. Nazwa pliku wg wzoru: "data" + wielka litera inna niż A-J + ".txt".

    while i != 0:

        print("Wybierz podpunkt (1-10) z zadania: ")
        print("(1)")
        print("|3 3 1| |x1|   |12|")
        print("|2 5 7| |x2| = |33|")
        print("|1 2 1| |x3|   | 8|   , x1 = 1, x2 = 2, x3 = 3\n")
        print("(2)")
        print("|3    3     1| |x1|   |  1|")
        print("|2    5     7| |x2| = | 20|")
        print("|-4  -10  -14| |x3|   |-40|   , nieoznaczony\n")
        print("(3)")
        print("|3    3     1| |x1|   |  1|")
        print("|2    5     7| |x2| = | 20|")
        print("|-4  -10  -14| |x3|   |-20|   , sprzeczny\n")
        print("(4)")
        print("|    0.5    -0.0625    0.1875    0.0625| |x1|   |   1.5|")
        print("|-0.0625        0.5         0         0| |x2| = |-1.625|")
        print("| 0.1875          0     0.375     0.125| |x3|   |     1|")
        print("| 0.0625          0     0.125      0.25| |x4|   |0.4375|    , x1 = 2, x2 = -3, x3 = 1.5, x4 = 0.5\n")
        print("(5)")
        print("|3   2   1  -1| |x1|   | 0|")
        print("|5  -1   1   2| |x2| = |-4|")
        print("|1  -1   1   2| |x3|   | 4|")
        print("|7   8   1  -7| |x4|   | 6|    , sprzeczny\n")
        print("(6)")
        print("| 3  -1   2  -1| |x1|   |-13|")
        print("| 3  -1   1   1| |x2| = |  1|")
        print("| 1   2  -1   2| |x3|   | 21|")
        print("|-1   1  -2  -3| |x4|   | -5|    , x1 = 1, x2 = 3, x3 = -4, x4 = 5\n")
        print("(7)")
        print("|0  0  1| |x1|   |3|")
        print("|1  0  0| |x2| = |7|")
        print("|1  0  0| |x3|   |5|       , x1 = 7, x2 = 5, x3 = 3\n")
        print("(8)")
        print("|10  -5   1| |x1|   | 3|")
        print("|4   -7   2| |x2| = |-4|")
        print("|5    1   4| |x3|   |19|       , x1 = 1, x2 = 2, x3 = 3\n")
        print("(9)")
        print("|  6    -4     2| |x1|   |   4|")
        print("| -5     5     2| |x2| = |  11|")
        print("|0.9   0.9   3.6| |x3|   |13.5|  ,nieoznaczony\n")
        print("(10)")
        print("|   1   0.2    0.3| |x1|   |1.5|")
        print("| 0.1     1   -0.3| |x2| = |0.8|")
        print("|-0.1  -0.2      1| |x3|   |0.7|     ,x1 = 1, x2 = 1, x3 = 1\n")


        choice = "rownanie" + input().capitalize() + ".txt"

        file = open(choice, "r")
        number_of_rows = file_len(choice)
        spl = file.read().splitlines()

        matrix = []
        for i in range(number_of_rows):
            helper = spl[i].split()
            matrix.append(helper)
        mat = np.asarray(matrix, dtype = np.double)
        print("\nRozwiązanie:")
        print(jordan(mat))

        print("\nKontynuować? 0 - nie, inne - tak")
        i = input()