import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = [r'\usepackage{sansmath}', r'\sansmath']
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'Helvetica, Avant Garde, Computer Modern Sans serif'

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
X = np.arange(0, 2, 0.01)
Y = np.arange(0, 2, 0.01)
X, Y = np.meshgrid(X, Y)
Z = np.exp(np.minimum(X,Y)) - 1
surf = ax.plot_surface(X, Y, Z, cmap=cm.rainbow, linewidth=0, antialiased=False)

ax.set_xlabel(r'$t$',size=20)
ax.set_ylabel(r'$\tau$',size=20)
ax.set_zlabel(r'$S^F (t,\tau)$',size=20)
ax.grid(False)
ax.set_xticks((0, 2))
ax.set_yticks((0, 2))
ax.set_zticks(())
ax.set_xticklabels(['$0$', '$T$'], fontsize=15)
ax.set_yticklabels(['$0$', '$T$'], fontsize=15)
ax.set_zticklabels([])

fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
plt.show()
filename = 'results/surface'+'.pdf'
# fig.savefig(filename, format='pdf', bbox_inches='tight')
plt.close()

fig, ax = plt.subplots(figsize=(5,5))
two_dim_surf = ax.contour(X,Y,Z, 30, cmap=cm.rainbow)
plt.xlabel(r'$t$',size=20)
plt.ylabel(r'$\tau$',size=20)
ax.set_xticks((0, 2))
ax.set_yticks((0, 2))
ax.set_xticklabels(['$0$', '$T$'], fontsize=15)
ax.set_yticklabels(['$0$', '$T$'], fontsize=15)

plt.show()
filename = 'results/contour'+'.pdf'
# fig.savefig(filename, format='pdf',  bbox_inches='tight')
plt.close()