
======================================
Solving Partial Differential Equations
======================================

Method of Separation of Variables
---------------------------------

Consider the diffusion equation, ([eq:diffusion]), and look for
solutions with the form

.. math:: \phi(\vec{r}, t) = \Phi(\vec{r}) T(t)

 Solutions of this form exist for these equations because they are
linear and have no cross-terms. So we now have

.. math:: \frac{1}{\Phi (\vec{r}) } \nabla^2 \Phi(\vec{r}) = \frac{1}{\alpha} \frac{1}{T(t)} \dv{T(t)}{t}  = -k^2

 since both sides must be equal, they are also both equal to a constant.
So now we have

.. math::

   \begin{aligned}
     \frac{\dif{T}}{\dif{t}} &= -\alpha k^2 T \\
     \nabla^2 \Phi(\vec{r}) &= -k^2 \Phi(\vec{r})\end{aligned}

 For examples, see MM1 notes.

Separation of Variables in spherical and cylindrical coordinate systems
-----------------------------------------------------------------------

We can decompose Laplace’s equation, equation ([eq:laplace]), into three
equations. In spherical coordinates Laplace’s equation becomes

.. math::

   \begin{split}
       \frac{1}{r^2 \sin \theta} 
       \bigg( \pdv{r}      \left[r^2 \sin \theta \pdv{\psi(r, \theta, \phi)}{r} \right] \\ 
            + \pdv{\theta} \left[\sin \theta \pdv{\psi(r, \theta, \phi)}{\theta}\right] \\ 
            + \pdv{\phi}   \left[\frac{1}{\sin \theta} \pdv{\psi(r,\theta, \phi)}{\psi } \right] \bigg)\\ =0
       \end{split}

 Then, rewriting :math:`\psi` as a product of three functions,

.. math:: \psi(r, \theta, \phi) = R(r)\Theta(\theta)\Phi(\phi)

 and dividing by this,

.. math::

   \begin{split}
         \frac{1}{R \Theta \Phi} 
         \bigg( \Theta \Phi \frac{\partial}{\partial r} \left[r^2 \sin \theta \frac{\partial \psi(r, \theta, \phi)}{\partial r} \right] \\
              + R \Phi \frac{\partial}{\partial \theta} \left[ \sin \theta \frac{\partial \psi(r, \theta, \phi)}{\partial \theta}\right] \\ 
              + R \Theta \frac{\partial}{\partial \phi} \left[ \frac{1}{\sin \theta} \frac{\partial \psi(r, \theta, \phi)}{\partial \psi }\right]
         \bigg) \\=0
         \end{split}

.. math::

   \begin{split}
           \frac{1}{R} \frac{\partial}{\partial r} \left[r^2 \sin \theta
             \frac{\partial \psi(r, \theta, \phi)}{\partial r} \right] \\
           + \frac{1}{\Theta} \frac{\partial}{\partial \theta} \left[
             \sin \theta \frac{\partial \psi(r, \theta, \phi)}{\partial
               \theta}\right] \\ + \frac{1}{\Phi}
           \frac{\partial}{\partial \phi} \left[ \frac{1}{\sin \theta}
             \frac{\partial \psi(r, \theta, \phi)}{\partial \psi }\right]
           \left.\vphantom{\frac{1}{2}}\right) \\=0
         \end{split}

| Then

  .. math::

     \sin^2\theta \frac{1}{R} \frac{\partial}{\partial r} \left[ r^2 \frac{\partial R}{\partial r} \right]
           +\sin \theta \frac{1}{\Theta} \frac{\partial}{\partial \theta} \left[ \sin \theta \frac{\partial \Theta}{\partial \theta}\right] 
           = - \frac{1}{\Phi} \frac{\difp{2}{\Phi}}{\dif \Phi^2}

   Each side must be constant, so

  .. math::

     \begin{aligned}
           \frac{1}{\Phi} \dv[2]{\Phi}{\phi} &= -m^2 \\
           \sin^2(\theta) \frac{1}{R} \dv{r} \qty[r^2 \dv{R}{r}] +
           \sin(\theta) \frac{1}{\Theta} \dv{\theta} \qty[\sin(\theta)
           \dv{\Theta}{\theta}] &= m^2
         \end{aligned}

   and these can themselves be made equal to a constant,

  .. math::

     \begin{aligned}
           \frac{1}{R} \dv{r} \qty[r^2 \dv{R}{r}] &= -
           \frac{1}{\sin(\theta)} \frac{1}{\Theta} \dv{\theta}
           \qty[\sin(\theta) \dv{\Theta}{\theta}] +
           \frac{m^2}{\sin^2(\theta)} = k
         \end{aligned}

   *The :math:`R(r)` equation:*
| 

  .. math::

     \begin{aligned}
           \dv{r} \qty[r^2 \dv{R(r)}{r}] - kR(r) &= 0 \\
           r^2 \dv[2]{R(r)}{r} + 2r \dv{R(r)}{r} - kR(r) &=0
         \end{aligned}

   The coefficients are polynomials of :math:`r`, so we try a solution
  of the form :math:`R(r) = r^n`,

  .. math::

     \begin{aligned}
           r^2n(n-1) r^{n-2} + 2r nr^{n-1} - kr^n &= 0 \\
           n(n-1)r^n + 2nr^n - kr^n &= 0 \\
           n(n+1) - k &= 0
         \end{aligned}

   and now let :math:`k = l(l+1)`, so :math:`n(n+1) = l(l+1)`, thus
  :math:`n=l` or :math:`n =
      -l-1` making the general solution

  .. math::

     \label{eq:generalsolr}
           R(r) = A r^l + B r^{-l-1}

   *The equation for :math:`\Phi(\phi)`*
| 

  .. math:: \dv[2]{\Phi(\phi)}{\phi}= -m^2 \Phi(\phi)

  The solution must have the form :math:`\Phi(\phi) = e^{\alpha \phi}`,
  so

  .. math:: \alpha^2 \Phi(\phi) = -m^2 \Phi(\phi)

   so :math:`\alpha = \pm
      e^{\alpha \phi}` . Thus, the general solution is

  .. math::

     \label{eq:generalsolphi}
           \Phi(\phi) = A^{\prime} \sin(m \phi) + B^{\prime} \cos(m \phi)

   for constants :math:`A^{\prime}`, and B\ :math:`^{\prime}`, and
  :math:`m \in
      \mathbb{N}`, since :math:`\Phi(\phi + 2 \pi) = \Phi(\phi)`.

| *The equation for :math:`\Theta(\theta)`*
| 

  .. math::

     \sin(\theta) \dv{\theta} \qty[ \sin(\theta)
         \dv{\Theta(\theta)}{\theta}] - m^2 \Theta(\theta) + l(l+1)
         \sin^2(\theta) \Theta(\theta) = 0

  which has the form of the Associate Legendre Differential equation,
  equation ([eq:assoclegendrede]), and the solution is therefore an
  Associate Legendre polynomial, with a general solution of the form

  .. math:: \Theta(\theta) = A P_l^m \qty( \cos(\theta) )

   Thus, the general solution of

  .. math:: \nabla^2 \psi(r, \theta, \phi) = 0

   is

  .. math::

     \label{eq:solutionpdesphere}
           \psi(r, \theta, \phi) = \sum_{l=0}^{\infty} \sum_{m=0}^l (A_{lm}r^l + B_{lm}r^{-l-1}) P_l^m \qty( \cos \theta) e^{\pm i m \phi}

   :math:`A`, and :math:`B` are constants determined by the boundary
  conditions of the problem. The functions

  .. math::

     \label{eq:sphericalharm}
           Y_l^m(\theta, \phi) = N e^{im\phi} P_l^m (\cos(\theta))

   with :math:`l \ge 0`, and :math:`|m| \le l`, are *Spherical
  Harmonics*.

| The surface of a metal sphere of radius :math:`r_0` is held at an
  electrostatic potential of :math:`V_0 \cos(\theta)`, with
  :math:`\theta` the polar angle. What is the electrostatic potential
  inside and outside the sphere, assuming no other sources of charge?
  There are no sources other than the sphere, so outside the sphere the
  potential obeys Laplace’s equation. The problem has spherical
  symmetry.
| *Inside the sphere*
| :math:`R(r) \propto r^{-l-1}` would give an infinity at :math:`r=0` ,
  so :math:`B_{lm}=0`. Thus,

  .. math::

     \psi(r, \theta, \phi) = \sum_{l=0}^{\infty} \sum_{m=0}^l A_{lm}r^l
       P_l^m \qty( \cos \theta) e^{\pm i m \phi}

   and we have the boundary condition that

  .. math:: \psi(r_0, \theta, \phi) = \phi_0 \cos(\theta)

   which has no :math:`\phi` dependence, implying :math:`m=0`. Then,

  .. math::

     \psi(r, \theta, \phi) = \sum_{l=0}^{\infty} A_{l}r^l P_l \qty(
       \cos \theta) = \phi_0 \cos(\theta)

   so only :math:`l=1` can satisfy this equation, and thus the potential
  is

  .. math:: \psi(r, \theta, \phi) = \psi_0 \frac{r}{r_0} \cos(\theta)

   *Outside the sphere*
| The same arrguments apply outside the sphere as did inside, so,

  .. math:: R(r) \propto r^l

  would give an infinity as :math:`r \to
    \infty`. Thus :math:`A_{lm}=0`. The same arguments for angular
  depenence also apply, so,

  .. math:: \psi(r, \theta, \phi) = \psi_0 \qty( \frac{r_0}{r})^2 \cos(\theta)
