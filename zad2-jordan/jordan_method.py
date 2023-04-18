import numpy as np

#Funkcja pobiera macierz (matrix) w postaci numpy array i najpierw sprawdza,
# czy element diagonalny na pozycji (i, i) jest zerem. Jeśli tak, zamienia wiersz
# z wierszem poniżej, który ma niezerowy element na tej pozycji.
#Funkcja pobiera macierz (matrix) w postaci numpy array i najpierw sprawdza, czy element diagonalny na pozycji (i, i) jest zerem.
# Jeśli tak, zamienia wiersz z wierszem poniżej, który ma niezerowy element na tej pozycji.
#Następnie funkcja wykonuje kroki eliminacji Gaussa-Jordana, aby przekształcić macierz wejściową w macierz trójkątną górną.
# W każdym kroku iteracji, elementy w kolumnie poniżej diagonalnego są wyzerowane poprzez odejmowanie wielokrotności wiersza diagonalnego.
#W końcowej fazie funkcja sprawdza, czy układ równań jest oznaczony, nieoznaczony lub sprzeczny, a następnie oblicza rozwiązanie dla każdej zmiennej i zwraca wektor wynikowy.

def jordan(matrix):
    rows = matrix.shape[0]
    result = np.zeros(rows, dtype = 'double')
    e = 1.0 / (10**10)

    for i in range(rows):
        if matrix[i][i] == 0:
            counter = 1
            while (i + counter) < rows and matrix[i + counter][i] == 0:
                counter += 1

            if i + counter == rows:
                break

            for k in range(rows + 1):
                temp = matrix[i][k]
                matrix[i][k] = matrix[i + counter][k]
                matrix[i + counter][k] = temp

        for j in range(rows):
            if i != j:
                ratio = matrix[j][i] / matrix[i][i]

                for k in range(rows + 1):
                    matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]

    for i in range(rows):
        if abs(matrix[i][i]) <= e and abs(matrix[i][rows]) <= e:
            result = "\nUkład nieoznaczony."
        elif abs(matrix[i][i]) <= e <= abs(matrix[i][rows]):
            result = "\nUkład sprzeczny."
        else:
            result[i] = matrix[i][rows] / matrix[i][i]
    print(matrix)

    return result