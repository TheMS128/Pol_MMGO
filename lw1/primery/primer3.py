import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

fig = plt.figure()
ax1 = fig.add_subplot(1, 3, 1, projection='3d')
ax2 = fig.add_subplot(1, 3, 2, projection='3d')
ax3 = fig.add_subplot(1, 3, 3, projection='3d')
u, v = np.mgrid[0:2*np.pi:25j, 0:np.pi:25j]
R = 1
x = R * np.cos(u) * np.sin(v)
y = R * np.sin(u) * np.sin(v)
z = R * np.cos(v)
norm = plt.Normalize(z.min(), z.max())
colors = cm.viridis(norm(z))
ax1.plot_wireframe(x, y, z, color='black')
surf = ax2.plot_surface(x, y, z, facecolors=colors)
surf.set_facecolor((0, 0, 0, 0))
ax3.plot_surface(x, y, z, cmap='viridis')
plt.show()
