import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

fig = plt.figure()
ax1 = fig.add_subplot(1, 3, 1, projection='3d')
ax2 = fig.add_subplot(1, 3, 2, projection='3d')
ax3 = fig.add_subplot(1, 3, 3, projection='3d')

def sphere(ax, s0, s1, t0, t1):
    u = np.linspace(s0, s1, 10)
    v = np.linspace(t0, t1, 10)
    x = np.outer(np.sin(u), np.cos(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.cos(u), np.ones_like(v))
    norm = plt.Normalize(z.min(), z.max())
    colors = cm.viridis(norm(z))
    surf = ax.plot_surface(x, y, z, facecolors=colors)
    surf.set_facecolor((0, 0, 0, 0))
    ax.set(
        xticks=np.linspace(-1, 1, 5),
        yticks=np.linspace(-1, 1, 5),
        zticks=np.linspace(-1, 1, 5)
    )

sphere(ax1, 0, np.pi, 0, np.pi)
sphere(ax2, 0.5, np.pi, 0, np.pi)
sphere(ax3, 1.2, np.pi - 1.2, 0, np.pi)
plt.show()
