import math
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np


def my_cos(x: float, e: float) -> float:
    n = 0
    f = 0
    while (abs(math.pow(x, 2 * n) / math.factorial(2 * n))) >= (e / 6.6):
        n += 1
    for i in range(n, -1, -1):
        f += math.pow(-1, i) * math.pow(x, 2 * i) / math.factorial(2 * i)
    return f


def my_atan(x: float, e: float) -> float:
    p = 0
    f = 0
    while (abs(math.pow(x, -(2 * p + 1)) / (2 * p + 1))) >= (e / 2.1):
        p += 1
    for i in range(p, -1, -1):
        f += math.pow(-1, i) * math.pow(x, -(2 * i + 1)) / (2 * i + 1)
    return math.pi / 2 - f


def my_heron(x: float, k: int) -> float:
    if k != 0:
        w = my_heron(x, k - 1)
        return (1 / 2) * (w + x / w)
    else:
        return math.ceil(math.sqrt(x))


def my_sqrt(x: float, e: float) -> float:
    k = 1
    c = my_cos(math.pi / 2 - (2 * 0.01 + 1.05), e)
    while (abs(my_heron(x, k) - my_heron(x, k - 1)) / c) >= (e / 3):
        k += 1
    f = my_heron(x, k)
    return f


print("Write down point quantity: ")
n = int(input())
print("Write down power of exp: ")
e = pow(10, int(input()))
x = np.arange(0.01, 0.06 + (0.06 - 0.01) / n, (0.06 - 0.01) / n)
my_f = np.array([my_sqrt(1 + my_atan(6.4 * a + 1.1, e), e) / my_cos(math.pi / 2 - (2 * a + 1.05), e) for a in x])
builtin_f = np.array([math.sqrt(1 + math.atan(6.4 * a + 1.1)) / math.cos(math.pi / 2 - (2 * a + 1.05)) for a in x])
ln_f = np.array([-1 * math.log(abs(my_f[i] - builtin_f[i]), 10) for i in range(len(x))])
plt.figure("Functions")
plt.plot(x, my_f, label="My function interpretation")
plt.plot(x, builtin_f, label="Built-in function interpretation")
plt.scatter(x, my_f)
plt.scatter(x, builtin_f)
plt.legend()
plt.figure("Logarithm")
plt.plot(x, ln_f, label="Logarithm")
plt.scatter(x, ln_f)
plt.legend()
plt.show()
