Spherical Harmonics
-------------------

Spherical harmonics are a class of function related to the associated
Legendre polynomials by the expression

.. math::

   \label{eq:spharmonicdef}
     Y_{lm}(\theta, \phi) = \qty[ \frac{2l+1}{4 \pi} \frac{(l-|m|)!}{(l+|m|)!}]^{\frac{1}{2}} P_l^m (\cos(\theta)) e^{im\phi}

Spherical harmonics with a negative :math:`m` value can be related to
those with a positive :math:`m` value via


.. plot::

    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.gridspec as gridspec
    # The following import configures Matplotlib for 3D plotting.
    from mpl_toolkits.mplot3d import Axes3D
    from scipy.special import sph_harm
    plt.rc('text', usetex=True)

    # Grids of polar and azimuthal angles
    theta = np.linspace(0, np.pi, 100)
    phi = np.linspace(0, 2*np.pi, 100)
    # Create a 2-D meshgrid of (theta, phi) angles.
    theta, phi = np.meshgrid(theta, phi)
    # Calculate the Cartesian coordinates of each point in the mesh.

    xyz = np.array([np.sin(theta) * np.sin(phi),
		    np.sin(theta) * np.cos(phi),
		    np.cos(theta)])

    def plot_Y(ax, el, m): 
       # NB In SciPy's sph_harm function the azimuthal coordinate, theta,
       # comes before the polar coordinate, phi.
       Y = sph_harm(abs(m), el, phi, theta)

       # Linear combination of Y_l,m and Y_l,-m to create the real form.
       if m < 0:
	   Y = np.sqrt(2) * (-1)**m * Y.imag
       elif m > 0:
	   Y = np.sqrt(2) * (-1)**m * Y.real
       Yx, Yy, Yz = np.abs(Y) * xyz

       # Colour the plotted surface according to the sign of Y.
       cmap = plt.cm.ScalarMappable(cmap=plt.get_cmap('PRGn'))
       cmap.set_clim(-0.5, 0.5)

       ax.plot_surface(Yx, Yy, Yz,
		       facecolors=cmap.to_rgba(Y.real),
		       rstride=2, cstride=2)

       # Draw a set of x, y, z axes for reference.
       ax_lim = 0.5
       ax.plot([-ax_lim, ax_lim], [0,0], [0,0], c='0.5', lw=1, zorder=10)
       ax.plot([0,0], [-ax_lim, ax_lim], [0,0], c='0.5', lw=1, zorder=10)
       ax.plot([0,0], [0,0], [-ax_lim, ax_lim], c='0.5', lw=1, zorder=10)
       # Set the Axes limits and title, turn off the Axes frame.
       #ax.set_title(r'$Y_{{{},{}}}$'.format(el, m))
       ax_lim = 0.5
       ax.set_xlim(-ax_lim, ax_lim)
       ax.set_ylim(-ax_lim, ax_lim)
       ax.set_zlim(-ax_lim, ax_lim)
       ax.axis('off')

    fig = plt.figure(figsize=(10,6))
    el_max = 4
    spec = gridspec.GridSpec(ncols=2*el_max+1, nrows=el_max+1, figure=fig)
    for el in range(el_max+1):
      for m_el in range(-el, el+1):
        print(el, m_el)
        ax = fig.add_subplot(spec[el, m_el+el_max], projection='3d')
        plot_Y(ax, el, m_el)
    plt.tight_layout()

.. math::

   \label{eq:negativespharm}
     Y_{l, -m} (\theta, \phi) = (-1)^m Y^{*}_{lm} (\theta, \phi)

 and they are orthogonal,

.. math::

   \label{eq:spahrmorthog}
     \int \dd{\Omega} Y^{*}_{lm} (\theta, \phi) Y_{l^{\prime}m^{\prime}}(\theta, \phi) = \delta_{l l^{\prime}} \delta_{m, m^{\prime}}

 The first few spherical harmonics are

.. math:: Y_{00} = \sqrt{\frac{1}{4 \pi}}

.. math:: Y_{10}= \sqrt{\frac{3}{4 \pi}} \cos(\theta)

.. math:: Y_{1, \pm 1} = \mp \sqrt{\frac{3}{8 \pi}} \sin(\theta) e^{\pm i \phi}


Spherical Harmonics and the Schrodinger Equation
------------------------------------------------

In spherical coordinates the time-independent Schrodinger equation is

.. math::

   \label{eq:tisespherical}
     \begin{split}
     - \frac{\hbar^2}{2m} \frac{1}{r^2 \sin^2 \theta} \bigg( \pdv{r} \qty[ r^2 \sin(\theta) \pdv{\psi}{r}] 
   + \pdv{\theta} \qty[ \sin \theta  \pdv{\psi}{\theta}] \\ + \pdv{\phi} \qty[ \frac{1}{\sin \theta} \pdv{\psi}{\phi}] \bigg) 
   + (V-E)\psi = 0
   \end{split}

 Now, splitting this into the radial part and an angular part,

.. math::

   \label{eq:sepschrod}
     \psi(r, \theta, \phi) = R(r) Y(\theta, \phi)

 Then, substituting this in, and setting both sides of the equation
equal to :math:`l(l+1)` we get two independent solutions

.. math::

   \begin{aligned}
     \dv{r} \qty[r^2 \dv[2]{R}{r}] - \frac{2m}{\hbar^2} \qty(V(r)-E) r^2
     R - l(l+1) R &= 0 \\\frac{1}{\sin \theta} \pdv{\theta} \qty[ \sin
     \theta \pdv{Y}{\theta}] + \frac{1}{\sin^2(\theta)}
     \pdv[2]{Y}{\phi} +l(l+1)Y &= 0\end{aligned}

 The angular part is solved by spherical harmonics,

.. math::

   \label{eq:sphericalharmonics}
     Y_l^m(\theta, \phi) = N e^{im\phi} P_l^m (\cos \theta)
