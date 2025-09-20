import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
R = 10
c1 = 4
c2 = 4
A = 0.5
B = -3
v = np.linspace(0, 2 * np.pi, 100)
x = c1 + R * np.cos(v)
y = c2 + R * np.sin(v)
ax.plot(x, y)

def f(x, A, B):
    return A * x + B

xline = np.arange(-10, 20, 0.1)
yline = f(xline, A, B)
line, = ax.plot(xline, yline)

def get_touch_coefs(a, c1, c2, r):
    m = (a ** 2 * r ** 2 + r ** 2) ** (1 / 2)
    return [
        -a * c1 + c2 + m,
        -a * c1 + c2 - m
    ]

b1, b2 = get_touch_coefs(A, c1, c2, R)

def update(frame):
    yline = f(xline, A, frame)
    line.set_data(xline, yline)
    return line

ani = FuncAnimation(fig, func=update, frames=np.linspace(b2 - 2, b1 + 2,
60), interval=30)
ax.set_xticks(np.linspace(-25, 25, 5))
ax.set_yticks(np.linspace(-25, 25, 5))
ax.grid(True)

plt.show()