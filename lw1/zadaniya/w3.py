import numpy as np
import matplotlib.pyplot as plt

a = 1

phi = np.linspace(0, 2 * np.pi, 1000)

r = a * np.sin(phi / 2)

plt.figure(figsize=(8, 8))
ax = plt.subplot(111, projection='polar')
ax.plot(phi, r, color='blue')
ax.set_title(r'$r = a \cdot \sin(\frac{\phi}{2})$', fontsize=14)
plt.show()
