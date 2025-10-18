import matplotlib.pyplot as plt
import numpy as np

x_coords = np.array([9, 1, 9, 11, 8])
y_coords = np.array([17, 10, 18, 5, 8])
point_names = ['p1', 'p2', 'p3', 'p4', 'p5']

polygon_x = np.append(x_coords, x_coords[0])
polygon_y = np.append(y_coords, y_coords[0])

P1_prime_x = 1609 / 173
P1_prime_y = 2949 / 173

Hx = 1583 / 173
Hy = 2945 / 173
P1x, P1y = x_coords[0], y_coords[0]

vector_P3P4_x = x_coords[3] - x_coords[2]
vector_P3P4_y = y_coords[3] - y_coords[2]
S1x, S1y = P1_prime_x, P1_prime_y
S2x = S1x + vector_P3P4_x
S2y = S1y + vector_P3P4_y

fig, ax = plt.subplots(figsize=(8, 8))
ax.plot(polygon_x, polygon_y, 'b-', linewidth=2, zorder=1)
ax.plot(x_coords, y_coords, 'ro', markersize=6, zorder=2)

for i, name in enumerate(point_names):
    ax.text(x_coords[i] + 0.3, y_coords[i] + 0.3, name, fontsize=12, color='k', weight='bold', zorder=3)

P3x, P3y = x_coords[2], y_coords[2]
P4x, P4y = x_coords[3], y_coords[3]
ax.plot([P3x, P4x], [P3y, P4y], 'm-', linewidth=3, zorder=1)
ax.plot([P1x, P1_prime_x], [P1y, P1_prime_y], 'r:', linewidth=1, zorder=4)
ax.plot(P1_prime_x, P1_prime_y, 'bs', markersize=8, zorder=5)
ax.text(P1_prime_x + 0.1, P1_prime_y - 0.5, "p1'", fontsize=12, color='b', weight='bold', zorder=6)
ax.plot(Hx, Hy, 'go', markersize=4, zorder=5)


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.margins(0.1)
ax.grid(True)
ax.axis('equal')

plt.show()