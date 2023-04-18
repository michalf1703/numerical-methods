import numpy as np
from matplotlib import pyplot as plt
from numpy import double
import funkcje as f


def wykres(x, y, x0,x02, flag):
    x_data = np.linspace(x, y, 1000)
    y_data = f.function(x_data, flag)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    if type(x0) == double:
        plt.plot(x0, 0, "o", color = 'm')
    if type(x02) == double:
        plt.plot(x02, 0, "o", color = 'yellow')
    plt.plot(x_data, y_data, 'b')
    plt.xlabel('X', loc='right')
    plt.ylabel('Y', loc='top')
    if flag == '1':
        plt.title('Wykres dla f(x)= 2x^3 + 3x^2 + 4x - 1 wraz z miejscem zerowym')
    if flag == '2':
        plt.title('Wykres dla f(x)= x^4 + 2x - 3 wraz z miejscem zerowym')
    if flag == '3':
        plt.title('Wykres dla f(x)= 2x^2 - 3x - 5 wraz z miejscem zerowym')
    if flag == '4':
        plt.title('Wykres dla f(x) = 3sin(x) - cos(x) wraz z miejscem zerowym')
    if flag == '5':
        plt.title('Wykres dla f(x) = cos(x) + 2sin(x) wraz z miejscem zerowym')
    if flag == '6':
        plt.title('Wykres dla f(x) = 7^x - 4 wraz z miejscem zerowym')
    if flag == '7':
        plt.title('Wykres dla f(x) = 10^x - 2 wraz z miejscem zerowym')
    if flag == '8':
        plt.title('Wykres dla f(x) = x^3 + 5^x - sin(x) wraz z miejscem zerowym')
    if flag == '9':
        plt.title('Wykres dla f(x) = 2x^4 + 2^x - cos(x) wraz z miejscem zerowym')
    line = plt.plot(x, y, label='bisekcja')
    plt.setp(line, color='m')
    line = plt.plot(x, y, label='falsi')
    plt.setp(line, color='yellow')
    line = plt.plot(x, y, label='wykres danej funkcji')
    plt.setp(line, color='b')
    plt.legend()
    plt.show()


def wykresPrawdziwy(x, y, flag):
    x_data = np.linspace(x, y, 1000)
    y_data = f.function(x_data, flag)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    plt.plot(x_data, y_data, 'g')
    plt.xlabel('X', loc='right')
    plt.ylabel('Y', loc='top')
    if flag == '1':
        plt.title('Wykres dla f(x)= 2x^3 + 3x^2 + 4x - 1')
    if flag == '2':
        plt.title('Wykres dla f(x)= x^4 + 2x - 3')
    if flag == '3':
        plt.title('Wykres dla f(x)= 2x^2 - 3x - 5')
    if flag == '4':
        plt.title('Wykres dla f(x)= 3sin(x) - cos(x)')
    if flag == '5':
        plt.title('Wykres dla f(x)= cos(x) + 2sin(x)')
    if flag == '6':
        plt.title('Wykres dla f(x)= 7^x - 4')
    if flag == '7':
        plt.title('Wykres dla f(x)= 10^x - 2')
    if flag == '8':
        plt.title('Wykres dla f(x)= x^3 + 5^x - sin(x)')
    if flag == '9':
        plt.title('Wykres dla f(x)= 2x^4 + 2^x - cos(x)')
    plt.show()
