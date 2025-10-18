import matplotlib.pyplot as plt
import numpy as np

x_coords = np.array([9, 1, 9, 11, 8])
y_coords = np.array([17, 10, 18, 5, 8])
point_names = ['p1', 'p2', 'p3', 'p4', 'p5']

polygon_x = np.append(x_coords, x_coords[0])
polygon_y = np.append(y_coords, y_coords[0])

P1_vertex_x, P1_vertex_y = x_coords[0], y_coords[0]

P3x, P3y = x_coords[2], y_coords[2]
P4x, P4y = x_coords[3], y_coords[3]

vector_P3P4_x = P4x - P3x
vector_P3P4_y = P4y - P3y

half_vector_x = vector_P3P4_x / 2
half_vector_y = vector_P3P4_y / 2

Ax = P1_vertex_x - half_vector_x
Ay = P1_vertex_y - half_vector_y

Bx = P1_vertex_x + half_vector_x
By = P1_vertex_y + half_vector_y

new_segment_x = [Ax, Bx]
new_segment_y = [Ay, By]


fig, ax = plt.subplots(figsize=(8, 8))

ax.plot(polygon_x, polygon_y, 'b-', linewidth=2, zorder=1)
ax.plot(x_coords, y_coords, 'ro', markersize=6, zorder=2)

for i, name in enumerate(point_names):
    ax.text(x_coords[i] + 0.3, y_coords[i] + 0.3, name, fontsize=12, color='k', weight='bold', zorder=3)

ax.plot(new_segment_x, new_segment_y, 'g--', linewidth=3, zorder=4)
ax.plot(P1_vertex_x, P1_vertex_y, 'go', markersize=8, zorder=5)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.margins(0.1)
ax.grid(True)
ax.axis('equal')

plt.show()