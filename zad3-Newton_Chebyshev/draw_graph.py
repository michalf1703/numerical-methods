import matplotlib.pyplot as mplot
import numpy as np
import Newton_Chebyshev as nk
from sklearn import metrics


def draw_functions(lower_range: float, upper_range: float, function, a: [], c_x: [], c_y: []):
    axes = mplot.figure().subplots()
    x = np.linspace(lower_range, upper_range, 100)
    y = []
    newton_y = []
    for i in x:
        y.append(function(i))
        newton_y.append(nk.newton(a, c_x, i))

    axes.plot(x, y, "r", label="Oryginalna funkcja")
    axes.plot(x, newton_y, "b", label="Funkcja interpolowana")
    axes.plot(c_x, c_y, ".", label = "Węzły interpolacji")
    r2 = round(100 * metrics.r2_score(y, newton_y), 3)
    mplot.title("Dokładność interpolacji: " + str(r2))
    axes.set_xlabel('X')
    axes.set_ylabel('Y')
    mplot.legend()
    mplot.show()

