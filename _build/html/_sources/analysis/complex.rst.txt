Complex analysis is the study of functions of complex variables.

Complex Functions
=================

.. prf:definition:: Complex function

		    A complex function is a function which maps a complex number to another complex number.

Any complex function, like a complex number, can be split into real and imaginary components, so, a function :math:`w: \mathbb{C} \to
\mathbb{C}` can be composed of two functions, :math:`u: \mathbb{R} \to \mathbb{R}`, and :math:`v: \mathbb{R} \to \mathbb{R}`, so

.. math::
   \require{physics}
   w(z) = u(x,y) + i v(x,y)

.. prf:definition:: Multi-valued Function

		    A multi-valued function is a left-total relation, such that each member in the domain of the relation corresponds to at least one member in the co-domain.

The name “function” for these objects is a misnomer, and they are in fact relations, since functions must always map to only a single value.

The relation :math:`w^2 = z` is multi-valued, because, for example, both :math:`w=\pm 1` map to the same value; in fact every output value greater than 0 is mapped to by two numbers.

Dealing with multi-valued functions requires a new framework compared to normal functions.
One approach is to consider the *branching* of a function.

.. prf:definition:: Branch Point

		    The branch points of a multi-valued function are the points in the complex plane where the complex argument can be mapped from a single point in the domain to multiple points in the range of the relation.

.. prf:definition:: Winding Number

		    The winding number for a closed curve on a plane around a point is an integer which represents the number of closed circuits the curve makes around the point.

Let :math:`w(\theta) = z(\theta)^{\half}`, with :math:`z \in \mathbb{C}`, such that :math:`z = e^{i \theta}`.
Taking the value of :math:`w` at two points, :math:`0`, and :math:`2 \pi`, we find

.. math:: w(0) = e^0 = 1

and

.. math:: w(2\pi) = e^{2 \pi i} ( \neq 1)

 each corresponds to the same point in the domain, but to different
points in the range.

.. math:: w(4 \pi) = 1

 so the function returns to its original value after two circuits about
the complex plane, so this point has a winding number of two.

The existence of branch points splits multi-valued functions into
“sheets” in which the function is single valued. It can be useful, in
order to work with these functions, to consider a multi-valued function
as the “glueing together” of such single value functions. These gluings
happen along “branch cuts.”

[Branch Cut] A branch cut is a curve in the complex plane, such that a
multi-valued function could be represented as a single valued function
as a branch minus the curve.

Returning to the example of :math:`w = z^{\half}`, a branch cut would
exist as the line where :math:`\theta = 2 \pi`. All the values on the
branch below this are single valued.

There is an alternative way of considering multi-valued functions, and
one which is easier to visualise. The different “sheets” of a
multivalued function can be considered as being superimposed ontop of
each other. If we were able to seperate the two superimposed sheets, we
would need to leave them somehow connected along the branch cuts. The
resulting surface is a Riemann Surface.

Again, in the case :math:`w = z^{\half}`, the Riemann surface consists
of two surfaces. The lower surface is joined to the upper surface at
:math:`\theta=2 \pi`, and the upper surface is joined back to the lower
surface along :math:`\theta=4 \pi` and :math:`\theta=0`.

Limits and Continuity
=====================

[Limit (Complex)] Let :math:`f` be a function of a complex variable,
:math:`z`, which is defined and single-valued in a neighbourhood about a
point :math:`z=z_0` in the complex plane, with the possible exception of
:math:`z = z_0`, thus a deleted neighbourhood of :math:`z_0`. The number
:math:`l` is the limit of :math:`f(z)` as :math:`z` approaches
:math:`z_0`, if, for any small positive number :math:`\epsilon` there
exists a :math:`\delta`, such that

.. math::

   | f(z) - l | <
     \epsilon \qquad \text{when} \qquad 0 < |z - z_0 | <
     \delta

Then

.. math:: \lim_{z \to z_0} f(z) = l

[Continuity] Let :math:`f` be a function of a complex variable,
:math:`z`, which is single-valued in the neighbourhood of :math:`z=z_0`
and at the point :math:`z=z_0`. The function :math:`f` is continuous at
:math:`z=z_0` if :math:`\lim_{z \to
    z_0} f(z) = f(z_0)`. This implies three conditions,

-  :math:`\lim_{z \to z_0} f(z) = l` must exist

-  :math:`f(z_0)` must exist

-  :math:`l = f(z_0)`

[Continuity over a region] A function is said to be continuous over a
region if it is continuous at all points in that region.

[Uniform Continuity] Let :math:`f` be a function of a complex variable
which is continuous in a region. At each point, :math:`z_0` of the
region, and for any :math:`\epsilon
  >0` there is a :math:`\delta >0` such that
:math:`|f(z) - f(z_0)| < \epsilon` when :math:`|z - z_0| < \delta`. If
there is a :math:`\delta` depending on :math:`\epsilon` but not on
:math:`z_0` :math:`f(z)` is uniformly continuous in the region.

Complex Differentiation
=======================

[Differentiation] Let :math:`f` be a function of a complex variable,
:math:`z`, which is single-valued over some region :math:`{\cal R}` of
the :math:`z` plane, then the derivative of :math:`f` is

.. math::

   \dv{f}{z} = \lim_{\Delta z \to 0} \frac{f(z + \Delta z) -
       f(z)}{\Delta z}

provided that the limit exists independent of the way in which
:math:`\Delta z \to 0`. In such a case :math:`f` is differentiable at
:math:`z`.

[Holomorphic Function] Let :math:`f` be a function of a complex variable
:math:`z` which has a derivative, :math:`f^{\prime}`, which exists at
every point in a region :math:`{\cal R}`, the :math:`f` is a holomorphic
function in :math:`{\cal R}`.

The function :math:`f(z) = \bar{z}` is not holomorphic, because
approaching :math:`0` from different directions, the limit in the
definition of the complex derivative is different.

The condition that a function is holomorphic is given by the
Cauchy-Riemann equations.

[Cauchy-Riemann Equations] Consider a function, :math:`f` of a complex
variable, :math:`z`, such that

.. math:: w = f(z) = u(x,y) + i v(x,y)

for :math:`x,y \in \mathbb{R}`. If the function satisfies the relations

.. math:: \pdv{u}{x} = \pdv{u}{y}

 and

.. math:: \pdv{u}{y} = - \pdv{v}{x}

 which are the *Cauchy-Riemann equations*, the function is holomorphic.

An important property of holomorphic functions relates to the existence
of higher derivatives.

[Higher Derivatives] Suppose :math:`f` is a holomorphic function over a
region :math:`{\cal R}`. The derivatives
:math:`f^{\prime}, f^{\prime \prime}, \dots` are all holomorphic over
:math:`{\cal R}`.

It is possible for functions to have points where they fail to be
analytic.

| [Singularity] A singularity is a point where a function on the complex
  plane ceases to be analytic.
| **Isolated singularities** exist at a point :math:`z=z_0` where it is
  possible to find a circle :math:`|z-z_0|=\delta` for :math:`\delta>0`
  encloses no singular point other than :math:`z_0`. If no such
  :math:`\delta` exists the singularity is non-isolated.
| **Poles** are isolated singularities where there exists an integer
  :math:`n` such that
  :math:`\lim_{z \to z_0} (z -z_0)^n f(z) = A \neq 0`; such a pole is of
  order :math:`n`. If :math:`n=1` the pole is a simple pole.
| **Branch Points** are non-isolated singular points since a
  multi-valued function is not continuous, and thus is not holomorphic
  in the deleted neighbourhood of the branch point.
| **Removable Singularities** are isolated singular points, :math:`z_0`
  where :math:`\lim_{z \to z_0} f(z)` exists. Defining
  :math:`z_0 = \lim_{z \to
      z_0} f(z)` the function becomes continuous and holomorphic at
  :math:`z_0`.
| **Essential Singularities** are singularities which are neither poles
  nor removable singularities.

Complex Integration
===================

[Complex Line Integral] Let :math:`f(z)` be a function of a complex
variable which is continuous at all points of a curve, :math:`C`, which
has a finite length. The line integral along the curve can be found by
dividing the curve into :math:`n` sections by means of the points
:math:`z_1, z_2, \dots, z_{n-1}` which are chosen arbitrarily. Let
:math:`a = z_0` and :math:`b=z_n` be the beginning and end points
respectively of the curve. On each arc joining points :math:`z_{k-1}` to
:math:`z_k`, for :math:`k = 1, 2, \dots, n`, choose a point
:math:`\xi_k`. A sum can then be formed, letting
:math:`\Delta z_k = z_k - z_{k-1}`,

.. math::

   S_n = \Delta z_1 f(\xi_1) + \Delta z_2 f(\xi_2) + \cdots + \Delta
     z_n f(\xi_n)

As :math:`|\Delta z_k| \to 0`, we have the integral,

.. math:: \int_a^b f(z) \dd{z} = \int_C f(z)

[Simply and Mulitply Connected Regions] A region :math:`{\cal R}` can be
described as simply connected if any closed curve which lies in
:math:`{\cal R}` can be shrunk to a point without leaving
:math:`{\cal R}`. Otherwise the region is multiply connected.

[Jordan Curve] A curve :math:`C` is a Jordan curve if it is continuous,
closed, and does not intersect itself.

[Jordan Curve Theorem] A Jordan curve on the complex plane divides the
plane into two regions, having the curve as a common boundary. The
region which is bounded (where points do not lie on the boundary) is the
interior of the curve, while the other region os the exterior of the
curve.

Infinite, Taylor, and Laurent Series
====================================

It is possible to extend the concept of sequences and series of
constants to functions. The concepts of limits can then be extended to
them as well.

| [Convergence of a sequence of functions] Let
  :math:`u_1(z), u_2(z), \dots, u_n(z)`, in short, :math:`\{ u_n(z) \}`
  be a sequence of functions of :math:`z \in \mathbb{C}`, which are all
  defined and single-valued in some region of the :math:`z`-plane. Let
  :math:`U(z)` be the limit of :math:`u_n(z)` as :math:`u \to \infty`,
  such that, :math:`\lim_{n \to \infty}
    u_n(z) = U(z)`. If, given any positive number :math:`\epsilon`,
  there exists an :math:`N` (which in general depends on
  :math:`\epsilon` and :math:`z`) such that

  .. math:: | u_n (z) - U(z) | < \epsilon \qquad \forall n > N

  In such a case the sequence converges to :math:`U(z)`.
| If such a sequnce converges for all the points in a region,
  :math:`{\cal R}`, then :math:`{\cal
      R}` is a region of convergence of the sequence.
| If the sequence is not convergent at a point, :math:`z`, it is
  described as being divergent at that point.

[Series of Functions] Let :math:`\{ u_n(z) \}` be a sequence of
functions of :math:`z \in \mathbb{C}`. Let :math:`\{ S_n(z) \}` be a new
sequence which is defined by

.. math:: S_n(z) = \sum_{k=1}^n u_n(z)

Then :math:`S_n(z)` is the :math:`n`\ th partial sum. The sequence
:math:`\{ S_n(z) \}` is an infinite series. If
:math:`\lim_{n \to \infty} S_n(z) = S(z)` the series is convergent, and
:math:`S(z)` is the sum of the series. Otherwise it is divergent.

Laurent’s Theorem
-----------------

.. prf:theorem:: Laurent's Theorem
		 
		 Let :math:`C_1` and :math:`C_2` be concentric circles of radii :math:`R_1` and :math:`R_2` respectively, which are centred on a point :math:`a`.
		 Suppose :math:`f(z)` is single-valued and analytic on both circles, and in the annulus, :math:`{\cal R}`, bounded by each.
		 Let :math:`a+h` be any point in :math:`{\cal R}`, then

		 .. math::
		    
		    f(a+h) = a_0 + a_1 h + a_2 h^2 + \cdots + \frac{a_{-1}}{h} +
		    \frac{a_{-2}}{h^2} + \cdots

		 with

		 .. math::

		    a_n = \frac{1}{2 \pi i}
		    \oint_{C_1} \frac{f(z)}{(z-a)^{n+1}} \dd{z} \quad n=0,1,2, \dots

		 .. math::

		    a_{-n} = \frac{1}{2 \pi i} \oint_{C_1} (z-a)^{n-1} f(z) \dd{z}
		    \quad n = 1,2, 3,\dots

		 If circles :math:`C_1` and :math:`C_2` represent the same circle, :math:`C`, we can write

		 .. math::

		    a_n = \frac{1}{2 \pi i} \oint_C \frac{f(z)}{(z-a)^{n+1}} \dd{z}
		    \quad n = 0, \pm 1, \pm 2,\dots

		 With a change of notation,

		 .. math::

		    f(z) = a_0 + a_1(z-a) + a_2 (z-a)^2 + \cdots + \frac{a_{-1}}{z-a}
		    + \frac{a_{-2}}{(z-a)^2} + \cdots

		 where

		 .. math::

		    a_n = \frac{1}{2 \pi i} \oint_C \frac{f(\zeta)}{(\zeta -
		    a)^{n+1}} \dd{\zeta} \quad n = 0, \pm 1, \pm 2, \dots

		 This is Laurent’s theorem, and the sequence :math:`\{ a_n \}` is a Laurent series expansion of :math:`f`.
		 
		 The positive subscript components of the series form the analytic part of the series, while the rest is the principle part.

Residues
========

.. prf:definition:: Residue

		    Let :math:`f(z)` be a single-valued function of :math:`z \in \mathbb{C}` which is analytic in and on a circle, :math:`C`, except at the point :math:`z=a` at the centre of :math:`C`.
		    Then, the Laurent series of :math:`f(z)` is

		    .. math:: f(z) = \sum_{n= - \infty}^{\infty} a_n (z-a)^n

		    with

		    .. math::

		       a_n =
			 \frac{1}{2 \pi i} \oint_C \frac{f(z)}{(z-a)^{n+1}} \dd{z} \quad n =
			 0, \pm 1, \pm 2, \dots

		    In the case :math:`n=-1`,

		    .. math:: \oint_C f(z) \dd{z} = 2 \pi i a_{-1}

		    This can be obtained by integrating the Laurent series term by term.
		    In the case of :math:`n=-1` only :math:`a_1` is involved, so :math:`a_1` is called the residue of :math:`f(z)` at :math:`z=a`.
