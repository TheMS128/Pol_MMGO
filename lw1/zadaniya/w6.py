import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.optimize import fsolve

def f(x):
    val = x**2 - 1
    if val > 0:
        return 2 * np.log(val) + np.exp(-x)
    else:
        return np.nan

root = fsolve(f, 2)
root1 = fsolve(f, -2)
print(root)
print(root1)

x_left = np.linspace(-1.5, -1.001, 250)
x_right = np.linspace(1.001, 1.5, 250)
x = np.concatenate((x_left, x_right))

y = np.array([f(val) for val in x])

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x, y, label=r'$f(x) = 2 \ln(x^2 - 1) + e^{-x}$')
ax.axhline(0, color='gray', linestyle='--')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title('График функции')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1, 4)
ax.grid(True)
ax.legend()

point, = ax.plot([], [], 'ro')

def update(frame):
    x_val = x[frame]
    y_val = f(x_val)
    if np.isnan(y_val):
        return point,
    point.set_data([x_val], [y_val])
    return point,

ani = FuncAnimation(fig, update, frames=range(len(x)), interval=20, blit=False)
ani.save("w6.gif", writer='pillow', fps=20)
plt.show()
