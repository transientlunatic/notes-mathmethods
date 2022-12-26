===============
Operator theory
===============

Linear operators can be further generalised to a wider class of
*differential operators*, :math:`{\cal L}` which act on eigenfunctions
:math:`y_i(x)` which have eigenvalues :math:`\lambda_i`, and weighted by
a weight function :math:`\rho(x)`.

[Sturm-Liouville Operator] The Sturm-Liouville operator is defined as

.. math:: {\cal L} = - \qty( p(x) \dv[2]{x} + r(x) \dv{x} + q(x) )

[Sturm-Liouville Equation] The Sturm-Liouville equation is a
differential equation of the form

.. math:: {\cal L} y = \lambda \rho(x) y

These can be simplified if :math:`r(x) = p^{\prime}(x)`, when

.. math:: {\cal L} = - \qty( \dv{x} \qty( p(x) \dv{x} ) + q(x) )

 and so

.. math:: {\cal L} y = - (py^{\prime})^{\prime} - qy

Provided we set approporiate conditions on the functions
:math:`p(x), q(x)`, and, :math:`\rho(x)`, and use appropriate boundary
conditions on a range :math:`[a,b]`, we can make a number of assertions
about the SL-equation.

[Properties of the Sturm-Liouville Operator]

[the:hermitiansloper] The Sturm-Liouville Operator is Hermitian over the
range :math:`[a,b]`

An operator is Hermitian over the range :math:`[a,b]` if

.. math::

   \int_a^b f^{*}(x) \qty[ {\cal L} g(x)] \dd{x} = \int_a^b
     \qty[{\cal L} f(x)]^{*} g(x) \dd{x}

In the case of the SL operator,

.. math:: {\cal L} y = - \qty( p y^{\prime})^{\prime} - qy

 Applying :math:`{\cal L}` to :math:`y_i`, and premultiplying by
:math:`y_i^{*}`, then integrating over :math:`[a,b]`,

.. math::

   \begin{aligned}
       \int_b^a y_i^{*} {\cal L} y_i \dd{x} &= - \int_a^b \qty( y_i^{*} (p y_j^{\prime})^{\prime} + y_i^{*} q y_j ) \dd{x} \\
   &= - \int_a^b y_i^{*} \qty(p y^{\prime}_j)^{\prime} \dd{x} - \int_a^b y_i^{*} q y_j \dd{x}
     \end{aligned}

 The first integral can be integrated by parts to yield

.. math::

   \int_a^b y_i^{*} \qty(p y^{\prime}_j)^{\prime} \dd{x} = -
     \qty[y_i^{*} p y^{\prime}_j]_a^b + \int_a^b \qty(y_i^{*})^{\prime} p
     y_j^{\prime} \dd{x}

 We set the boundary conditions to set

.. math:: \qty[y_i^{*} p y^{\prime}_j]_a^b = 0

 This leaves the integral, which can be solved by integrating again,

.. math::

   \int_a^b \qty(y_i^{*})^{\prime} p y_j^{\prime} \dd{x} =
     \qty[y_i^{*} p y^{\prime}_j]_a^b = 0 - \int_a^b \qty(
     \qty(y_i^{*})^{\prime} p )^{\prime} y_j \dd{x}

 Rearranging, and returning to the original integral,

.. math::

   \begin{aligned}
       \int_b^a y_i^{*} {\cal L} y_i \dd{x} &= - \int_a^b \qty[ y_j \qty( p (y_i^{*})^{\prime} )^{\prime} + y_j q y_i^{*}] \dd{x} \\
   \int_a^b y_i^{*} \qty( {\cal L} y_j ) \dd{x} &= \int_a^b \qty( {\cal L} y_i)^{*} y_j \dd{x}
     \end{aligned}

The eigenvalues of the Sturm-Liouville Operator are real.

q From theorem [the:hermitiansloper] the operator is known to be
Hermitian. From theorem [the:eigenvaluehermitian] we know that the
eigenvalues of a Hermitian matrix are real.

The eigenvalues of the Sturm-Liouville Operator form an ordered set
:math:`\lambda_1 < \lambda_2 < \cdots < \lambda_n`.

The eigenfunctions of the Sturm-Liouville Operator, :math:`y_i(x)` have
:math:`i-1` zeros over the range :math:`[a,b]`.

The normalised eigenfunctions, :math:`y_i(x)` of the Sturm-Liouville
operator form an orthogonal basis,

.. math:: \braket{y_i}{y_j} = \delta_{ij}


