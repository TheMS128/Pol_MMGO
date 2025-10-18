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


p1 = np.array([-1, -1])
p2 = np.array([1, 1])
p4 = np.array([5, 0])
x1, y1 = p1
x2, y2 = p2
x4, y4 = p4
k0 = k(p1, p2)
x6 = (k0 * y1 - k0 * y4 + x4 - x1) / (k0 ** 2 + 1)
y6 = k0 * (x6 - x1) + y1
p6 = np.array([x6, y6])
print('Координаты точки p6:', p6)
x = np.arange(-2, 6, 0.1)

ax = plt.subplot()
ax.plot(x, f2p(x, p1, p2))
ax.plot(x, f2p(x, p4, p6))
sign_point(p1, 'p1')
sign_point(p2, 'p2')
sign_point(p4, 'p4', c='green', offset=[-0.5, -0.3])
sign_point(p6, 'p6', c='green')
ax.axvline(x=0, color='k')
ax.axhline(y=0, color='k')
ax.set_xlim(-2, 6)
ax.set_ylim(-2, 6)
ax.set_aspect(1)
ax.grid(True)
plt.show()