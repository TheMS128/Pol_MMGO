import numpy as np
import matplotlib.pyplot as plt

def k(p1, p2):
    x, y = p2 - p1
    return y / x

def b(p, k):
    x, y = p
    return y - k * x

def fkp(x, k, p):
    x0, y0 = p
    return k * (x - x0) + y0

def fkb(x, k, b):
    return k * x + b

def segment_length(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def sign_point(p, text, c='orange', offset=[0.2, -0.2]):
    ax.plot(*p, 'o', color=c, zorder=3)
    ax.text(p[0] + offset[0], p[1] + offset[1], text)

p1 = np.array([-1, -1])
p2 = np.array([1, 1])
p3 = np.array([-1, 1])
k1 = k(p1, p2)
k2 = k1
b1 = b(p1, k1)
b2 = b(p3, k2)
ax = plt.subplot()
x1 = np.arange(p1[0], p2[0] + 0.01, 0.1)
ax.plot(x1, fkb(x1, k1, b1))
x2 = np.arange(p3[0], p3[0] + (p2[0] - p1[0]) + 0.01, 0.1)
ax.plot(x2, fkb(x2, k2, b2), color='green')
sign_point(p1, 'p1')
sign_point(p2, 'p2')
sign_point(p3, 'p3')

ax.set_xlim(-2, 4)
ax.set_ylim(-2, 4)
ax.set_aspect(1)
ax.axvline(x=0, color='k')
ax.axhline(y=0, color='k')
ax.grid(True)
plt.show()
