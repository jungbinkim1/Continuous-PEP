import os
import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
import math

os.environ['KMP_DUPLICATE_LIB_OK']='True'
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = [r'\usepackage{sansmath}', r'\sansmath']
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'Helvetica, Avant Garde, Computer Modern Sans serif'

def AGM_SC_ODE(x0, h, cost, grad, mu, t_start, t_end):
    K = math.floor((t_end - t_start)/h)
    x = [x0 for i in range(K)]
    a = [(x0-x0) for i in range(K)]
    v = [(x0-x0) for i in range(K)]
    f = np.zeros((K,))
    f[0] = cost(x0)
    t = np.zeros((K,))
    t[0] = t_start
    for k in range(K - 1):
        t[k+1] = t[k] + h
        alpha = 2*mu**0.5
        beta = 1 - h*alpha
        a[k] = beta*v[k] - h*grad(x[k])
        x[k+1] = x[k]+h*a[k]
        v[k+1] = a[k]
        f[k+1] = cost(x[k+1])
    return t, x, v, f

N = 100000 # number of iterations
mu = 0.01 # strong convexity parameter

def cost(X):
    return 0.02 * X[0] ** 2 + 5e-3 * X[1] ** 2
def grad(X):
    return np.array([0.04 * X[0], 1e-2 * X[1]])

X0 = np.array([1, 1])
stepsize = 0.01
t_start = 0
t_end = 10000

t4, X4, v_raw, f4 = AGM_SC_ODE(X0, stepsize, cost, grad, mu, t_start, t_end)
f_sol = f4[-1] + 1e-10
N = t4.size
v4 = np.zeros((N,))
for i in range(N):
    if (i==0):
        v4[i] = (la.norm(v_raw[1])) ** 2
    else:
        v4[i] = (la.norm(v_raw[i])) ** 2

plt.rcParams['text.usetex'] = True
plt.rcParams["font.family"] = "serif"
fig, ax = plt.subplots(figsize=(7,5))

ax.loglog(t4, v4, label=r'AGM-SC ODE', color ='red')
ax.loglog(t4, 2*np.exp(-mu**0.5 * t4)*(f4[0]-f_sol+0.5*mu*la.norm(X0-X4[-1])**2),'--',label='$O(e^{-\sqrt{\mu}t})$',color='black')
plt.xlabel(r'$t$',size=20)
plt.ylabel(r'$\Vert \dot{X}(t) \Vert^2$',size=20)
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.grid()
ax.legend(fontsize=20)
plt.show()

filename = 'results/agm-sc_velocity_final2'+'.pdf'
# fig.savefig(filename, format='pdf',  bbox_inches='tight')