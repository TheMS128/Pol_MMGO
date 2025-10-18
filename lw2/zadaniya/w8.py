import matplotlib.pyplot as plt
import numpy as np

def intersec_point(p1, p2, p3, p4):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4
    q = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if q == 0:
        return np.array([np.nan, np.nan])
    d1 = x1 * y2 - y1 * x2
    d2 = x3 * y4 - y3 * x4
    x = (d1 * (x3 - x4) - (x1 - x2) * d2) / q
    y = (d1 * (y3 - y4) - (y1 - y2) * d2) / q
    return np.array([x, y])

x_coords = np.array([9, 1, 9, 11, 8])
y_coords = np.array([17, 10, 18, 5, 8])
point_names = ['p1', 'p2', 'p3', 'p4', 'p5']

P2 = (x_coords[1], y_coords[1])
P3 = (x_coords[2], y_coords[2])
P4 = (x_coords[3], y_coords[3])
P5 = (x_coords[4], y_coords[4])

P6_coords = intersec_point(P2, P3, P4, P5)
P6x, P6y = P6_coords[0], P6_coords[1]

polygon_x = np.append(x_coords, x_coords[0])
polygon_y = np.append(y_coords, y_coords[0])

fig, ax = plt.subplots(figsize=(10, 10))

ax.plot(polygon_x, polygon_y, 'b-', linewidth=2, zorder=1)
ax.plot(x_coords, y_coords, 'ro', markersize=6, zorder=2)

for i, name in enumerate(point_names):
    ax.text(x_coords[i] + 0.3, y_coords[i] + 0.3, name, fontsize=12, color='k', weight='bold', zorder=3)

ax.plot(P6x, P6y, 'ks', markersize=8, zorder=4)
ax.text(P6x + 0.3, P6y + 0.3, 'p6', fontsize=12, color='k', weight='bold', zorder=5)
ax.plot([P6x, P3[0]], [P6y, P3[1]], 'g-', linewidth=2, zorder=3)
ax.plot([P6x, P5[0]], [P6y, P5[1]], 'g-', linewidth=2, zorder=3)
ax.text(P6x + 0.5, P6y - 0.5, '90°', fontsize=10, color='g', weight='bold')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.margins(0.1)
ax.grid(True)
ax.axis('equal')
plt.show()