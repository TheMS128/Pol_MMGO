import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)

X, Y = np.meshgrid(x, y)

Z = np.exp(2 * Y * X) + Y**2

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.set_title(r'$z = e^{2 y x} + y^2$')

ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(1, 20)

plt.show()
