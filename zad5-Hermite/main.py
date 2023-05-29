import matplotlib.pyplot as plt

from Hermite import *
import functions as f

if __name__ == '__main__':
    a = np.array([2,2,2])
    print(a)
    print(a/2)
    print("\n\nMetody numeryczne - zadanie 5. Aproksymacja")
    print("Wariant 2 - wielomiany Hermite'a\n")

    funcs = {
        "1": f.f1,
        "2": f.f2,
        "3": f.f3,
        "4": f.f4,
        "5": f.f5,
        "6": f.f6
    }

    func = input("\n 1. f(x) = |2x - 3|"
                 "\n 2. f(x) = x + 2"
                 "\n 3. f(x) = cos(2x)"
                 "\n 4. f(x) = x^2"
                 "\n 5. f(x) = cos(sin(x))"
                 "\n 6. f(x) = 1/2x^3 + 3x^2 + 3x - 2\n"
                 "\n Wybierz funkcję: ")

    level = int(input("podaj stopien wielomianu aproksymujacego:"))
    left = np.double(input("podaj lewą stronę przedziału aproksymacji:"))
    right = np.double(input("podaj prawą stronę przedziału aproksymacji:"))
    nodes = int(input("podaj liczbę węzłów całkowania metodą Gaussa-Hermite'a:"))

    factors = np.zeros(level + 1)
    for i in range(level + 1):
        factors[i] = hermite_factors(funcs.get(func), nodes, i)

    xs = np.linspace(left, right, 1000, endpoint=True)
    ys = []
    for x in xs:
        yi = 0.0
        for i in range(level + 1):
            yi += factors[i] * hermite(i, x)
        ys.append(yi)

    xs2 = np.linspace(left, right, 1000, endpoint=True)
    ys2 = []
    for x in xs2:
        ys2.append(funcs.get(func)(x))

    plt.plot(xs, ys, 'r', label='aproksy')
    plt.plot(xs2, ys2, 'y', label='real')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(title='Legenda', loc='best', fontsize='xx-small')
#    plt.grid(b=True, axis='both')
    plt.show()

    meanerror = f.mean_error(ys, ys2)
    mindev = f.min_deviation(ys, ys2)
    maxdev = f.max_deviation(ys, ys2)
    meanerror = meanerror
    maxdev = maxdev

    print('Sredni blad aproksymacji: %.16f' % meanerror)
    print('Minimalne odchylenie aproksymacji: %.16f' % mindev)
    print('Maksymalne odchylenie aproksymacji: %.16f' % maxdev)