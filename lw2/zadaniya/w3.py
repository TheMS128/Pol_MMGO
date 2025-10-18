import matplotlib.pyplot as plt
import numpy as np

x_coords = [9, 1, 9, 11, 8]
y_coords = [17, 10, 18, 5, 8]
point_names = ['p1', 'p2', 'p3', 'p4', 'p5']

polygon_x = x_coords + [x_coords[0]]
polygon_y = y_coords + [y_coords[0]]
mid_p1p2_x = (x_coords[0] + x_coords[1]) / 2
mid_p1p2_y = (y_coords[0] + y_coords[1]) / 2
mid_p3p4_x = (x_coords[2] + x_coords[3]) / 2
mid_p3p4_y = (y_coords[2] + y_coords[3]) / 2
mid_p5p1_x = (x_coords[4] + x_coords[0]) / 2
mid_p5p1_y = (y_coords[4] + y_coords[0]) / 2

triangle_x_coords = [mid_p1p2_x, mid_p3p4_x, mid_p5p1_x]
triangle_y_coords = [mid_p1p2_y, mid_p3p4_y, mid_p5p1_y]
triangle_point_names = ['m1', 'm2', 'm3']
triangle_polygon_x = triangle_x_coords + [triangle_x_coords[0]]
triangle_polygon_y = triangle_y_coords + [triangle_y_coords[0]]

def calculate_distance(p1_x, p1_y, p2_x, p2_y):
    return np.sqrt((p2_x - p1_x)**2 + (p2_y - p1_y)**2)

side1 = calculate_distance(triangle_x_coords[0], triangle_y_coords[0],
                           triangle_x_coords[1], triangle_y_coords[1])
side2 = calculate_distance(triangle_x_coords[1], triangle_y_coords[1],
                           triangle_x_coords[2], triangle_y_coords[2])
side3 = calculate_distance(triangle_x_coords[2], triangle_y_coords[2],
                           triangle_x_coords[0], triangle_y_coords[0])

perimeter = side1 + side2 + side3

print(f"Координаты вершин треугольника: ")
print(f"  m1: ({triangle_x_coords[0]:.2f}, {triangle_y_coords[0]:.2f})")
print(f"  m2: ({triangle_x_coords[1]:.2f}, {triangle_y_coords[1]:.2f})")
print(f"  m3: ({triangle_x_coords[2]:.2f}, {triangle_y_coords[2]:.2f})")
print(f"Периметр треугольника: {perimeter:.2f}")

fig, ax = plt.subplots(figsize=(10, 10))

ax.plot(polygon_x, polygon_y, 'b-', linewidth=2, zorder=1)
ax.plot(x_coords, y_coords, 'ro', markersize=6, zorder=2)

for i, name in enumerate(point_names):
    ax.text(x_coords[i] + 0.3, y_coords[i] + 0.3, name, fontsize=12, color='k', weight='bold', zorder=3)

ax.plot(triangle_polygon_x, triangle_polygon_y, 'g--', linewidth=2, zorder=1)
ax.plot(triangle_x_coords, triangle_y_coords, 's', color='orange', markersize=8, zorder=4)

for i, name in enumerate(triangle_point_names):
    ax.text(triangle_x_coords[i] + 0.3, triangle_y_coords[i] + 0.3, name, fontsize=12, color='darkgreen', weight='bold', zorder=5)

ax.axis('equal')
ax.margins(0.1)

plt.show()