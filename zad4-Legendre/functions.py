from numpy import sin, cos, e

# definicja funkcji f1, która zwraca wartość bezwzględną z 2*x-3
f1 = lambda x: abs(2 * x - 3)

# definicja funkcji f2, która zwraca wartość sin(x+2)
f2 = lambda x: sin(x + 2)

# definicja funkcji f3, która zwraca wartość cos(2*x)
f3 = lambda x: cos(2*x)

# definicja funkcji f4, która zwraca wartość x^2
f4 = lambda x: x * x

# definicja funkcji f5, która zwraca wartość cos(sin(x))
f5 = lambda x: cos(sin(x))

# definicja funkcji w, która zwraca wartość e^(-x^2)
w = lambda x: e ** (- (x * x))
