import numpy as np
import matplotlib.pyplot as plt

R = np.arange(5, 10.1, 0.5)
def S(R):
    return np.pi * np.power(R, 2)

ax1 = plt.subplot(2, 2, 1)
ax2 = plt.subplot(2, 2, 2)
ax3 = plt.subplot(2, 1, 2)
ax1.plot(R, S(R), label='S(R)')
ax1.legend(loc='best', fontsize=12)
ax2.plot(R, S(R), label='S(R)')
ax2.legend(loc='best', fontsize=12)
ax2.grid(linewidth=2)
ax2.set_xticks(np.linspace(5, 10, 5))
ax2.set_yticks(np.linspace(0, 400, 5))
ax2.set_xlim(5, 10)
ax3.plot(R, S(R), label='S(R)')
ax3.legend(loc='best', fontsize=12)
ax3.grid(linewidth=2)
ax3.set_xticks(np.linspace(5, 10, 5))
ax3.set_yticks(np.linspace(0, 400, 5))
ax3.set_xlim(5, 10)
_, xlim = ax3.get_xlim()
_, ylim = ax3.get_ylim()
ax3.set_aspect(0.5 / ((ylim / xlim) * 2))
plt.tight_layout()
plt.show()