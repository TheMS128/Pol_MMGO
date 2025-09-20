import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def x(a):
    return np.sin(a)

def y(a):
    return np.power(2, -0.6 * a)

A = np.arange(0, 3.5 * np.pi, 0.1)
plt.plot(A, x(A), label='$x(φ)=sin(φ)$')
plt.plot(A, y(A), label='$y(φ)=2^{0.6*φ}$')

plt.grid(True)
plt.legend(loc='best', fontsize=12)

def f(a):
    return np.sin(a) - np.power(2, -0.6 * a)
x1 = fsolve(f, 1)
print(x1)
x2 = fsolve(f, 3)
print(x2)
x3 = fsolve(f, 6.5)
print(x3)
x4 = fsolve(f, 9.3)
print(x4)
plt.show()