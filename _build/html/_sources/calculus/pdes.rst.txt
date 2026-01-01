==============================
Partial Differential Equations
==============================
:math:`\require{physics}`

.. include:: ../macros.rst

Atlas of PDEs
=============

There are a number of common PDEs which it is useful to know.

------------------
Laplace’s Equation
------------------

.. math::
   :label: laplace-equation

   \nabla^2 \phi(\vec{r}) = 0

This equation is used in electromagnetism, gravitation, hydrodynamics, and heat flow in situations where no sources or sinks exist.

------------------
Poisson’s Equation
------------------

.. math::
   :label: poisson-equation

   \nabla^2 \phi(\vec{r}) = f(\vec{r})

This is used in the same situations as Laplace’s equation, (:eq:`laplace-equation`), only when there *are* sources or sinks, described by the
scalar field :math:`f`.

.. prf:example:: Maxwell's Equations

		 One of Maxwell’s equations is

		 .. math:: \nabla \cdot \vec{E} = \frac{\rho(\vec{r})}{\epsilon_{0}}

		 with electric field :math:`\vec E`,
		 charge density :math:`\rho(\vec r)`,
		 and the permittivity of free space, :math:`\epsilon_0`.
		 
		 Since :math:`\vec{E} = - \nabla   \phi`, we have

		 .. math:: \nabla^2 \phi(\vec{r}) = - \frac{\rho(\vec{r})}{\epsilon_0}

------------------
Diffusion Equation
------------------

.. math::
   :label: diffusion-equation

   \nabla^2 \phi(\vec{r}, t) = \frac{1}{\alpha} \frac{\partial \phi(\vec{r}, t)}{\partial t}

The diffusion equation describes the time and space evolution of fields where there is no source; :math:`\phi` would describe the distribution of temperature in a conductive heat flow situation.


.. prf:example:: Heat-flow in a conductor
		 
		 Consider heat flowing into a metal, with the temperature a scalar field, represented by a function of position, :math:`\vec{r}`, and time, 		 :math:`t`, so :math:`T(\vec{r}, t)`.
		 Then the heat in a small volume, :math:`V`, is

		 .. math:: Q = \int_V \rho c_{\rm p} T(\vec{r}, t) \difp{3}{\vec{r}}

		 The rate at which heat transfers from one volume to another depends on the temperature gradient, the area of the contact, and the metal’s thermal conductivity.
		 For a boundary of area :math:`A`,

		 .. math::

		    \frac{\dif{Q}}{\dif{t}} = \int_A k \dif{\vec{\sigma}} \cdot \nabla T(\vec{r}, t)

		 with :math:`\dif{\vec{\sigma}}` the normal vector to the area, :math:`\dif{A}`.
		 Applying the divergence theorem,

		 .. math::

		    \begin{aligned}
  		      \frac{\dif{Q}}{\dif{t}} &= \int_V \nabla \cdot [k \nabla T(\vec{r}, t)] \difp{3}{\vec{r}} \\
		                              &= \int_V k \nabla^2 T(\vec{r}, t) \difp{3}{\vec{r}}
		    \end{aligned}

		 Then equating the expressions for :math:`\frac{\dif{Q}}{\dif{t}}`, and assuming :math:`\rho` and :math:`c_{\rm p}` are constant,

		 .. math::

		    \begin{aligned}
		       \frac{\dif{Q}}{\dif{t}} &= \int_V \nabla \cdot [k \nabla T(\vec{r}, t) ] \difp{3}{\vec{r}} \\
					       &= \int_{V} k \nabla^2 T(\vec{r}, t) \difp{3}{\vec{r}} \\
		       \nabla^2 T(\vec{r}, t)  &= \frac{\rho c_{\rm p}}{k} \frac{\partial T(\vec{r},t)}{\partial t}
		    \end{aligned}

-------------
Wave Equation
-------------

The wave equation describes the progression of vibrations through media.

.. math::
   :label: wave-equation
	   
   \nabla^2 \phi(\vec{r}, t) = \frac{1}{v^2} \frac{\partial^2 \phi(\vec{r}, t)}{\partial t^2}

It occurs frequently in physics, and an operator is defined for it, the d’Alembertian operator,

.. prf:definition:: Box Operator

   .. math::

      \Box^2 \equiv \frac{1}{v^2} \frac{\partial^2 \phi(\vec{r}, t)}{\partial t^2}


------------------
Helmholtz Equation
------------------

.. math::
   :label: helmholtz-equation

   \nabla^2 \phi + k^2 \phi = 0

This appears where the time dependence of the diffusion equation is removed by the separation of variables.

--------------------
Schrodinger Equation
--------------------

Time-independent:

.. math::
   :label: time-independent-schrodinger-equation

   - \frac{\hbar^2}{2m} \nabla^2 \psi + V \psi = E \psi

Time-dependent:

.. math::
   :label: time-dependent-schrodinger-equation

   - \frac{\hbar^2}{2m} \nabla^2 \psi + V \psi = i \hbar \frac{\partial \psi}{\partial t}
