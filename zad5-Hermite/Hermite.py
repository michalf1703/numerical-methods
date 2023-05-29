import numpy as np
import math

roots = (
    (0.0, 1.73205080757),
    (-0.524647623275, 0.524647623275, 2.52464762327),
    (-0.958572464614, 0.0, 0.958572464614, 3.75),
    (-1.22474487139, -0.524647623275, 0.524647623275, 1.22474487139, 4.95)
)

coefficients = (
    (0.0, 2.0),
    (-0.790123462330, 0.790123462330, 0.0),
    (0.335462627902, 1.24641810996, 0.335462627902, 0.0),
    (-0.945308720482, -0.393619323152, 0.393619323152, 0.945308720482, 0.0)
)


def hermite(deg, x):
    if deg == 0:
        return 1
    elif deg == 1:
        return 2 * x
    else:
        h = np.zeros(deg + 1, dtype="double")
        h[0] = 1
        h[1] = 2 * x
        for i in range(1, deg):
            h[i + 1] = 2 * x * h[i] - 2 * i * h[i - 1]
        return h[deg]


def hermite_factors(f, quadlevel, polylevel):
    result = 0.0
    for j in range(0, quadlevel):
        result += f(roots[quadlevel - 2][j]) * coefficients[quadlevel - 2][j] * hermite(polylevel, roots[quadlevel - 2][j])

    return result / (math.factorial(polylevel) ** 2)
