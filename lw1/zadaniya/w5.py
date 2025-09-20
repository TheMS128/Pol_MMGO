import numpy as np
import matplotlib.pyplot as plt

n = 10

i = np.arange(1, n + 1)
j = np.arange(1, n + 1)

I, J = np.meshgrid(i, j)

A = I * (I - 2) + J * (J - 4)

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(I, J, A, cmap='viridis')

ax.set_xlabel('i')
ax.set_ylabel('j')
ax.set_zlabel('A[i,j]')
ax.set_title('Поверхность матрицы A')

plt.show()
