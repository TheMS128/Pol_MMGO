import numpy as np
import matplotlib.pyplot as plt

def k(p1, p2):
    x, y = p2 - p1
    return y / x

def fkp(x, k, p):
    x0, y0 = p
    return k * (x - x0) + y0

def f2p(x, p1, p2):
    k0 = k(p1, p2)
    return fkp(x, k0, p1)

def sign_point(p, text, c='orange', offset=[0.2, -0.2]):
    ax.plot(*p, 'o', color=c, zorder=3)
    ax.text(p[0] + offset[0], p[1] + offset[1], text)

def intersec_point(p1, p2, p3, p4):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4
    q = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    d1 = x1 * y2 - y1 * x2
    d2 = x3 * y4 - y3 * x4
    x = (d1 * (x3 - x4) - (x1 - x2) * d2) / q
    y = (d1 * (y3 - y4) - (y1 - y2) * d2) / q
    return np.array([x, y])

p1 = np.array([-1, -1])
p2 = np.array([1, 1])
p3 = np.array([-1, 1])
p4 = np.array([1, -2])
M = intersec_point(p1, p2, p3, p4)
print('Координаты точки M:', M)
x = np.arange(-2, 2 + 0.01, 0.1)
ax = plt.subplot()
ax.plot(x, f2p(x, p2, p1), color='green')
ax.plot(x, f2p(x, p3, p4), color='green')
sign_point(p1, 'p1')
sign_point(p2, 'p2')
sign_point(p3, 'p3')
sign_point(p4, 'p4')

sign_point(M, 'M', c='red', offset=[-0.4, -0.1])
ax.axvline(x=0, color='k')
ax.axhline(y=0, color='k')
ax.set_xlim(-2, 3)
ax.set_ylim(-3, 2)
ax.set_aspect(1)
ax.grid(True)
plt.show()
