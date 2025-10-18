import matplotlib.pyplot as plt
import numpy as np

M1 = (5.0, 13.5)
M2 = (10.0, 11.5)
M3 = (8.5, 12.5)

COEFFS = {
    'M1M2': {'A': 4, 'B': 10, 'C': -155, 'P1': M1, 'P2': M2},
    'M2M3': {'A': 4, 'B': 6, 'C': -109, 'P1': M2, 'P2': M3},
    'M3M1': {'A': 4, 'B': 14, 'C': -209, 'P1': M3, 'P2': M1},
}


def y_from_implicit(A, B, C, x):
    if B == 0:
        return None
    return (-A * x - C) / B


fig, ax = plt.subplots(figsize=(8, 8))

for name, data in COEFFS.items():
    A, B, C = data['A'], data['B'], data['C']
    P1, P2 = data['P1'], data['P2']

    x_start = min(P1[0], P2[0])
    x_end = max(P1[0], P2[0])

    x_coords = np.linspace(x_start, x_end, 100)

    y_coords = y_from_implicit(A, B, C, x_coords)

    ax.plot(x_coords, y_coords, color='g', linewidth=2, linestyle='-', label=f'Сторона {name}')

vertices = [M1, M2, M3]
vertex_names = ['M1', 'M2', 'M3']
ax.plot([v[0] for v in vertices], [v[1] for v in vertices], 's', color='orange', markersize=8, zorder=5)

for i, (x, y) in enumerate(vertices):
    ax.text(x + 0.2, y + 0.2, vertex_names[i], fontsize=12, color='darkgreen', weight='bold', zorder=6)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.grid(True)
ax.axis('equal')
plt.show()