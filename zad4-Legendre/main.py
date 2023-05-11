import functions as f
from newton_cotes import newton_cotes
import numpy as np

if __name__ == '__main__':
    funcs = {
        "1": f.f1,
        "2": f.f2,
        "3": f.f3,
        "4": f.f4,
        "5": f.f5
    }

    print("Funkcje do wyboru:")

    func = input("\n 1. f(x) = |2x - 3|"
                 "\n 2. f(x) = sin(x)"
                 "\n 3. f(x) = cos(2x)"
                 "\n 4. f(x) = x^2"
                 "\n 5. f(x) = cos(sin(x))\n"
                 "\nWybierz funkcję: ")

    epsilon = input("Podaj epsilon [Newton - Simpson]: ")
    print("Wyniki:")
    print("\n--------------------\nNewton - Simpson: ")
    print(newton_cotes(funcs.get(func), f.w, np.double(epsilon)))
