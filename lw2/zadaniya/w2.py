import matplotlib.pyplot as plt

x_coords = [9, 1, 9, 11, 8]
y_coords = [17, 10, 18, 5, 8]
point_names = ['p1', 'p2', 'p3', 'p4', 'p5']

polygon_x = x_coords + [x_coords[0]]
polygon_y = y_coords + [y_coords[0]]

fig, ax = plt.subplots(figsize=(8, 8))

ax.plot(polygon_x, polygon_y, 'b-', linewidth=2, zorder=1)

ax.plot(x_coords, y_coords, 'ro', markersize=6, zorder=2)

for i, name in enumerate(point_names):
    ax.text(x_coords[i] + 0.3, y_coords[i] + 0.3, name, fontsize=12, color='k', weight='bold', zorder=3)

ax.margins(0.1)

ax.legend()

plt.show()
