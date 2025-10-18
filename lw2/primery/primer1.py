import numpy as np
import matplotlib.pyplot as plt

def k(p1, p2):
    x, y = p2 - p1
    return y / x

def fkp(x, k, p):
    x0, y0 = p
    return k * (x - x0) + y0

def segment_length(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def sign_point(p, text, c='orange', offset=[0.2, -0.2]):
    ax.plot(*p, 'o', color=c, zorder=3)
    ax.text(p[0] + offset[0], p[1] + offset[1], text)

p1 = np.array([-1, -1])
p2 = np.array([1, 1])
r = segment_length(p1, p2)
print('Длина отрезка:', r)

x = np.arange(-2, 2 + 0.01, 0.1)
k0 = k(p1, p2)

ax = plt.subplot()
ax.plot(x, fkp(x, k0, p1))
sign_point(p1, 'p1')
sign_point(p2, 'p2')
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
ax.set_aspect(1)
ax.axvline(x=0, color='k')
ax.axhline(y=0, color='k')
ax.grid(True)
plt.show()
