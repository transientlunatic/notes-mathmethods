from scipy.special import gamma
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import cm

def complex_plane_plot(x, y, func, ax=None):
    xx, yy = np.meshgrid(x, y)
    c = xx + 1j * yy

    z = func(c)

    alpha = z
    alpha[np.isinf(z) | np.isnan(z)] = 0
    alpha = 0.75 + np.abs(alpha)/np.abs(alpha).max()/4

    if not ax:
        f, ax = plt.subplots(1,1, dpi=300, figsize=(10,4))
    else:
        f = ax.figure

    im = ax.imshow(np.angle(z), cmap="twilight", alpha=alpha,
                   extent=[x.min(), x.max(), y.min(), y.max()])

    ax.contour(xx, yy, np.abs(z), colors="white", linewidths=0.5, levels=100)

    #ax.streamplot(x, y, z.real, z.imag, density=1.5, linewidth=0.3, color="white")
    ax.set_xlabel("Re(z)")
    ax.set_ylabel("Im(z)")
    ax.set_aspect("equal")
    ax.grid(None)

    f.tight_layout()
    
x = np.linspace(-5, 5, 501)
y = np.linspace(-2, 2, 501)

complex_plane_plot(x, y, gamma)

