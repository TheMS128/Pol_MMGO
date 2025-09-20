import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(6, 4))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)

ax.axis('off')

fig.patch.set_facecolor('#ADD8E6')

surname = 'Полуэктов'
group = 'при123'

ax.text(5, 4.5, surname, fontsize=24, fontweight='bold', color='navy', ha='center')
ax.text(5, 3.5, group, fontsize=20, fontweight='normal', color='darkred', ha='center')

square = patches.Rectangle((0.15, 0.15), 0.9, 0.9, color='pink', ec='black')
ax.add_patch(square)

ax.text(0.5, 0.5, 'P', fontsize=80, family='Brush Script MT', ha='center', va='center', color='darkred')

plt.savefig('logo.png', bbox_inches='tight', dpi=300)
plt.show()
