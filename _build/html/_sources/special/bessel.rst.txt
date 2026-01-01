.. include:: ../macros.rst

.. _besselfunctions:
Bessel Functions
================

Bessel functions are the solutions to Bessel’s differential equation,

.. math::
   :label: eq:besselde 

     x^2 \dv[2]{y}{x} + x \dv{y}{x} + (x^2 - \alpha^2)y = 0

for :math:`x \in \mathbb{C}` and :math:`\alpha` some arbitrary complex number.

When :math:`\alpha \in \mathbb{Z}` the Bessel Functions are also Cylindrical Harmonics, representing the solutions to the Laplace equation in cylindrical coordinates.
They can then be used to model the behaviour of wave equations in cylinders, such as heat propagation through a pipe.

When :math:`\alpha` is of half-integer order the solutions represent the behaviour of functions in spherical coordinate systems.

More generally they represent a generalisation of the sine function, and can be thought of as representing the vibration of a string which has variable thickness or tension along it.

There are two families of Bessel function, which correspond to solutions to :eq:`eq:besselde` which have a finite value at the origin (functions of the first kind) and those which have a singularity there (functions of the second kind).

.. plot::
   :caption: The Bessel Functions of the first kind over the real numbers .

   import matplotlib.pyplot as plt
   import numpy as np
   from scipy.special import jv

   n = 3
   x = np.arange(0, 20, 0.01)

   for n in [0, 1, 2, 3, 4, 5]:
      plt.plot(x, jv(n, x), label=n)
   plt.legend()
   plt.tight_layout()

.. plot::
   :caption: The Bessel Functions of the second kind over the real numbers .

   import matplotlib.pyplot as plt
   import numpy as np
   from scipy.special import yn

   n = 3
   x = np.arange(0.1, 20, 0.01)

   for n in [0, 1, 2, 3, 4, 5]:
      plt.plot(x, yn(n, x), label=n)
   plt.ylim([-2, 0.6])
   plt.legend()
   plt.tight_layout()



.. plot::
   :caption: The Bessel Functions of the first kind with half-integer order over the complex number.

   from scipy.special import jv
   import numpy as np
   import matplotlib.pyplot as plt
   import matplotlib as mpl
   from matplotlib import cm

   x = np.linspace(-2, 2, 501)
   y = np.linspace(-2, 2, 501)
   xx, yy = np.meshgrid(x, y)
   c = xx + 1j * yy
	     
   f, axes = plt.subplots(2,2, dpi=300, figsize=(5,5))

   for i, ax in enumerate(axes.flatten()):
       z = jv(i + 0.5, c)
       #ax.imshow(z.real, cmap="cubehelix", alpha=0.5+z.imag/z.imag.max()/2,
       #         extent=[x.min(), x.max(), y.min(), y.max()])

       im = ax.imshow(np.angle(z), cmap="twilight", alpha=0.5+np.abs(z)/np.abs(z).max()/2,
		extent=[x.min(), x.max(), y.min(), y.max()])

       ax.contour(xx, yy, np.abs(z), colors="white", linewidths=0.5)
       ax.set_title(f"Order {i+0.5}")
       #ax.streamplot(x, y, z.real, z.imag, density=1.5, linewidth=0.3, color="white")
       ax.set_xlabel("Re(z)")
       ax.set_ylabel("Im(z)")
       ax.set_aspect("equal")
       ax.grid(None)

   display_axes = f.add_axes([0.45,0.45,0.1,0.1], projection='polar')
   #display_axes._direction = 2*np.pi ## This is a nasty hack - using the hidden field to 
				     ## multiply the values such that 1 become 2*pi
				     ## this field is supposed to take values 1 or -1 only!!

   norm = mpl.colors.Normalize(0.0, 2*np.pi)

   # Plot the colorbar onto the polar axis
   # note - use orientation horizontal so that the gradient goes around
   # the wheel rather than centre out
   quant_steps = 2056
   cb = mpl.colorbar.ColorbarBase(display_axes, cmap=cm.get_cmap('twilight',quant_steps),
				      norm=norm,
				      orientation='horizontal')

   # aesthetics - get rid of border and axis labels                                   
   cb.outline.set_visible(False)                                 
   display_axes.set_axis_off()

   f.tight_layout()
   
Bessel functions from the Generating Function
---------------------------------------------

The Bessel functions can be described by a generating function,

.. math::
   :label: eq:bessel-generating-function

   g(x,t) = \exp(\frac{x}{2t}(t^2-1)) = \sum_{\nu=-\infty}^{\infty} J_{\nu}(x) t^{\nu}

So, for Bessel functions of integer order we can expand this to form a series expansion,

.. math::
   :label: eq:besselseriesexp
	   
   J_n(x) = \sum^{\infty}_{s=0} \frac{(-1)^s}{s! (n+s)!} \qty( \frac{x}{2} )^{n+2s} \approx \frac{x^n}{2^n n!}

for small :math:`x`.

Bessel functions with a negative index can be found from the relation

.. math::

   \label{eq:negativebessel}
     J_{-\nu}(x) = (-1)^{\nu} J_{\nu}(x)

Recurrence Relation for Bessel Functions
----------------------------------------

The Bessel functions can be descried by a pair of recurrence relations, found by differentiating with respect to :math:`t`,

.. math::

   \label{eq:recurrencebessel}
     J_{\nu-1}(x) + J_{\nu+1}(x) = \frac{2 \nu}{x} J_{\nu}(x)

and by differentiating with respect to :math:`x`,

.. math::

   \label{eq:recurrencebessel2}
     J_{\nu-1}(x) - J_{\nu+1}(x) = 2J_{\nu}^{\prime}(x)

A number of other integral relationships also exist.

.. math::

   \begin{aligned}
     \int x^n J_{n-1}(x) \dd{x} &= x^n J_n(x) \\
     \int x^{-n} J_{n+1}(x) \dd{x} &= -x^{-n} J_n(x) \\
     \int J_1(x) \dd{x} &= -J_0(x)
   \end{aligned}

Orthogonality of the Bessel Functions
-------------------------------------

The orthogonality relations for Bessel functions are similar to those of the trigonometric functions, but they include an additional weighting factor, :math:`r`.

.. math::

   \label{eq:orthogbess}
     \int_0^a r J_p \qty( \frac{\alpha r}{a} ) J_p \qty(\frac{\beta r}{a}) \dd{r} = \delta_{\alpha \beta} \frac{a^2}{2} J_{p+1}^2(\alpha)

with

.. math::

   \begin{aligned}
     J_p(\alpha) = J_p(\beta) = 0\end{aligned}

Bessel Series
-------------

The orthogonality relations for Bessel functions allow the definition of Bessel series,

.. math::
   :label: eq:bessel-series

	   f(x) = \sum_0^{\infty} c_n J_p(k_n x)

with :math:`J_p(k_na)=0`.


Solving problems in cylindrical systems
---------------------------------------

.. prf:example:: Deriving the steady state inside an infinite cyclinder.

		 With the curved sides kept at a temperature :math:`T_0`, and the base at :math:`T_1`.

		 We know :math:`\nabla^2 T =0`, and we can use seperation of variables to give a solution of the form :math:`T = R(r)\Theta(\theta)Z(z)`.

		 Then, in cylinderical coordinates,

		 .. math:: \frac{1}{R}\frac{1}{r} \dv{r} \qty(r \dv{R}{r}) + \frac{1}{\Theta} \frac{1}{r^2} \dv[2]{\Theta}{\theta} + \frac{1}{Z} \dv[2]{Z}{z} = 0

		 We now have

		 .. math:: \frac{1}{Z} \dv[2]{Z}{z} = k^2

		 implying

		 .. math:: Z = \exp(\pm kz)

		 also,

		 .. math:: \frac{1}{R}\frac{1}{r} \dv{r} \qty(r \dv{R}{r}) + \frac{1}{\Theta} \frac{1}{r^2} \dv[2]{\Theta}{\theta} + k^2 = 0

		 which we can multiply by :math:`r^2`,

		 .. math:: \frac{r}{R} \dv{r} \qty(r \dv{R}{r}) + \frac{1}{\Theta} \dv[2]{\Theta}{\theta} + k^2 r^2 = 0

		 from which,

		 .. math:: \frac{1}{\Theta} \dv[2]{\Theta}{\theta} = -n^2

		 implying that

		 .. math:: \Theta = \{ \cos(n \theta), \sin(n \theta) \}

		 and the periodicity of :math:`\theta` will force :math:`n` to be a
		 natural number. Then

		 .. math:: \frac{r}{R} \dv{r} \qty(r \dv{R}{r}) + (k^2 r^2 - n^2) = 0

		 and letting :math:`kr = s`,

		 .. math:: s \dv{s} \qty( s \dv{R}{s} ) + (s^2 - n^2)R = 0

		 which has the form of Bessel’s differential equation, equation :eq:`eq:besselde`, and thus the solutions are Bessel functions, :math:`J_n(s)`, the complete solution is thus
		 
		 .. math:: J_n (kr) \qty( A \sin(n\theta) + B \cos(n \theta) ) e^{-kz}

		 We can ignore the Bessel functions which are infinite at :math:`r=0`, as we need a finite solution there, so the functions of the first-kind are the appropriate solutions.
		 We know that :math:`T_1 > T_0`, so :math:`T>T_0` everywhere, and so :math:`T_0` can be taken as a constant.
		 The boundary condition of the curved surface at :math:`r=a` is where :math:`J_n(ka) = 0`.
		 We now need to know the zeros of the Bessel functions, and our solution becomes

		 .. math:: T = T_0 + \sum_{m=0}^{\infty} c_m J_0 \qty(\alpha_{0m}\frac{r}{a}) \exp(-\qty(\frac{\alpha_{0m}z}{a}))

		 The boundary condition at :math:`z=0` is that :math:`T=T_0`, so

		 .. math:: T_1 - T_0 = \sum_m c_m J_0 \qty( \alpha_{0m} \frac{r}{a})

		 and using the orthogonality condition,

		 .. math:: \int_0^a (T_1 - T_0) J_0 \qty( \alpha_{0m} \frac{r}{a} ) r \dd{r} = c_m \frac{a^2}{2} J_1^2(\alpha_{0m})

		 and then, from the indefinite integral relationship :math:`\int x J_0(x) \dd{x} = x J_1(x)`,

		 .. math::

		    \begin{aligned}
		    (T_1-T_0) \frac{a}{\alpha_{0m}} \qty[ r J_1 \qty( \alpha_{0m} \frac{r}{a})]_0^a &= (T_1 - T_0) \frac{a^2}{\alpha_{0m}} J_1 (\alpha_{0m})\\
		    &= c_m \frac{a^2}{2} J_1^2 (\alpha_{0m})
		    \end{aligned}

		 with

		 .. math:: c_m = \frac{2}{\alpha_{0m}} \frac{1}{J_1(\alpha_{0m})} (T_1-T_0)

		 and the overarching solution is thus

		 .. math:: T = T_0 + \sum_m \frac{2 (T_1-T_0)}{\alpha_{0m}J_1(\alpha_{0m})} J_0 \qty( \alpha_{0m} \frac{r}{a}) \exp( - \qty(\frac{\alpha_{0m}z}{a}) )


Spherical Bessel Functions
--------------------------

The spherical Bessel functions are a class of Bessel function related to the half-integer order order Bessel functions by

.. math::
   :label: eq:spherical-bessel-functions
	   
	   j_n(x) = \sqrt{\frac{\pi}{2x}} J_{n+\frac{1}{2}}(x) = x^n \qty(- \frac{1}{x} \dv{x})^n \frac{\sin(x)}{x}

.. prf:example::  Finding energy levels of particles inside a spherical box using Schrodinger’s equation.

		  Starting at

		  .. math:: - \frac{\hbar^2}{2m} \nabla^2 \Psi = E \Psi

		  after seperating variables

		  .. math:: \pdv{r} \qty(r^2 \pdv{R}{r}) + \qty( \frac{2mEr^2}{\hbar^2} - l(l+1) )R=0

		  letting

		  .. math:: k^2 = \frac{2mE}{\hbar^2} \quad \text{and} \quad s=kr

		  .. math:: s^2 \pdv[2]{R}{s} + 2s \pdv{R}{s} + \qty(s^2 - l(l+1))R = 0

		  and letting

		  .. math:: R = \frac{Z}{s^{\frac{1}{2}}}

		  .. math:: s^2Z^{\prime \prime} + s Z^{\prime} + (s^2 - \qty(l + \frac{1}{2})^2 ) Z = 0

		  Which is Bessel’s equation of order :math:`l+\half`, so

		  .. math:: R = j_l \qty( \frac{\sqrt{2mE}}{\hbar} r)

		  which is a finite solution as :math:`r \to 0`. The lowest energy
		  state will have :math:`l=0` (so no angular variation), and to satisy
		  the boundary condition of :math:`R=0` when :math:`r=a`, we need

		  .. math:: j_0 \qty( \frac{\sqrt{2mE}}{\hbar}a)=0

		  the zeros of :math:`j_0` are the same as those of :math:`\sin(x)`,
		  since

		  .. math:: j_0(x) = \frac{\sin(x)}{x}

		  so

		  .. math:: \frac{a \sqrt{2mE_{\rm min}}}{\hbar} = \pi

		  thus

		  .. math:: E_{\rm min} = \frac{\pi^2 \hbar^2}{2ma^2}

