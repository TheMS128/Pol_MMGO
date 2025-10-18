import matplotlib.pyplot as plt
import numpy as np

M1 = (5.0, 13.5)
M2 = (10.0, 11.5)
M3 = (8.5, 12.5)

PARAM_EQS = {
    'M1M2': {'x1': M1[0], 'y1': M1[1], 'l': M2[0] - M1[0], 'm': M2[1] - M1[1]},
    'M2M3': {'x1': M2[0], 'y1': M2[1], 'l': M3[0] - M2[0], 'm': M3[1] - M2[1]},
    'M3M1': {'x1': M3[0], 'y1': M3[1], 'l': M1[0] - M3[0], 'm': M1[1] - M3[1]},
}

t_values = np.linspace(0, 1, 100)

fig, ax = plt.subplots(figsize=(8, 8))

for name, data in PARAM_EQS.items():
    x1, y1 = data['x1'], data['y1']
    l, m = data['l'], data['m']
    x_coords = x1 + l * t_values
    y_coords = y1 + m * t_values
    ax.plot(x_coords, y_coords, color='b', linewidth=2, linestyle='-', label=f'Сторона {name}')

vertices = [M1, M2, M3]
vertex_names = ['M1', 'M2', 'M3']
ax.plot([v[0] for v in vertices], [v[1] for v in vertices], 's', color='red', markersize=8, zorder=5)

for i, (x, y) in enumerate(vertices):
    ax.text(x + 0.2, y + 0.2, vertex_names[i], fontsize=12, color='darkred', weight='bold', zorder=6)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.grid(True)
ax.axis('equal')
plt.show()