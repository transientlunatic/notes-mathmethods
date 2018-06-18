from mayavi import mlab
import numpy as np
from scipy.special import sph_harm

# Create a sphere
r = 0.3
pi = np.pi
cos = np.cos
sin = np.sin
phi, theta = np.mgrid[0:pi:101j, 0:2*pi:101j]

x = r*sin(phi)*cos(theta)
y = r*sin(phi)*sin(theta)
z = r*cos(phi)

sph = mlab.figure(1, bgcolor=(1, 1, 1), fgcolor=(0, 0, 0), size=(400, 300))
mlab.clf()
# Represent spherical harmonics on the surface of the sphere
for n in range(1, 6):
    for m in range(n):
        s = sph_harm(m, n, theta, phi).real

        #mlab.mesh(x-(0.7*m), y-(0.7*n), z, scalars=s, colormap='jet')

        s[s<0] *= 0.97

        s /= s.max()
        mlab.mesh(s*x-(0.6*m), s*y-(0.6*n), s*z+1.3, scalars=s, colormap='Spectral')

mlab.view(90, 0, 6.2, (-1.3, -1.6, 1.25))
print mlab.view()
#mlab.show()
mlab.savefig('../figures/spharmonics2.png', figure=sph, magnification=5)
