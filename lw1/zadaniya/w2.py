import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def f(x):
    val = x**2 - 1
    if val > 0:
        return 2 * np.log(val) + np.exp(-x)
    else:
        return np.nan

root = fsolve(f, 2)
root1 = fsolve(f, -2)
print(root, root1)

x = np.linspace(-1, 1, 400)

y = np.array([f(val) for val in x])

plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r'$f(x) = 2 \ln(x^2 - 1) + e^{-x}$')
plt.axhline(0, color='gray', linestyle='--')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График функции')
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.legend()
plt.grid(True)
plt.show()
