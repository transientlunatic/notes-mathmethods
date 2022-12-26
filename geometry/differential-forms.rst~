******************
Differential forms
******************

The concept of a manifold does not come along with the definition of a metric, although such a definition is possible. While avoiding making a choice of metric it is still possible to define volumes on a manifold.
We can do this by considering a volume as the area described by the paralleloid described by a set of vectors. For example, if we have two of these vectors describing a parallelogram, then by doubling the length of the vectors we would expect to double the area of the parallelogram.
The area is unaffected by moving one of the vectors along the straight line it defines, and so the area is in fact a tensor. By swapping the order of the vectors we get a negative value for the tensor, so it is antisymmetric.

Antisymmetric Tensors
=====================

An antisymmetric tensor changes sign upon an interchange of its arguments:

.. math:: \of{\omega}(U,V) = - \of{\omega}(V,U)

A tensor of order 3 or greater is commpletely antisymmetric if this sign change occurs for an interchange of any combination of arguments.

It is possible to find the antisymmetric parts for any tensor,
:math:`S`, of dimension :math:`p` :

.. math::

   \label{eq:antisymmetrisation-tensor}
     S_{[a_1 ,a_p]} = \frac{1}{p!} \epsilon_{a_1 \dots a_p}\epsilon^{b_1 \dots b_p} S_{b_1\dots b_p}


for :math:`\epsilon` the Levi-Civita symbol. The indices which are
antisymetric are contained within square brackets, and interchange of
these will result in a sign change. An antisymmetric tensor can also be
denoted as

:math:`{\of{\ten{a}}}`.

Differential Forms
==================

A :math:`p`-form is a completely antisymmetric tensor of type
:math:`(0,p)`. A :math:`(0,1)`-tensor is a one-form. In the same way
that vectors can be combined to form a tensor using the tensor product,
:math:`\otimes`, one-forms can be combined using the wedge product,
:math:`\wedge`,

.. math::

   \label{eq:34}
     \of{a} \wedge \of{b} = \of{p} \otimes \of{q} - \of{q} \otimes \of{p}


The set of all forms of arbitrary degree equipped with the anticommutative wedge operator form a *Grassmann algebra*.

Forms have a commutation rule; for a :math:`p`-form, :math:`{\of{\ten{p}}}`, and a :math:`q`-form :math:`{\of{\ten{q}}}`, then

.. math::

   \label{eq:35}
     {\of{\ten{p}}} \wedge {\of{\ten{q}}} = (-1)^{pq} {\of{\ten{q}}} \wedge {\of{\ten{p}}}


A form can be contracted with a tensor,

.. math::

   \label{eq:36}
     {\of{\ten{\alpha}}}(\vec{\xi}) \equiv {\of{\ten{\alpha}}}(\xi,\ , \ , \dots), \quad [{\of{\ten{\alpha}}}(\vec{\xi}) ]_{j\dots k} = \alpha_{ij \dots k} \vec{\xi}^i

     
Tensor densities
================

On three dimensional Euclidean manifolds there are three defined
three-forms: one has an integral giving the volume of a region, one has
an integral giving the mass of the region, and the final one has an
integral giving a conserved quantity, e.g. vorticity.

Considering a coordinate-dependent :math:`n`-form, with components
:math:`\epsilon_{ijk}`, then a one-form :math:`\of{\omega}` can be
written

.. math::

   \label{eq:38}
     \omega_{ij\dots k} = \mathfrak{w} \epsilon_{ij\dots k}

     
with :math:`\mathfrak{w}` the scalar density, which, under a change of
coordinates supplied by a Jacobian :math:`J`, transforms as

.. math:: \mathfrak{w}^{'} = J \mathfrak{w}


In the case that the density quantity is a tensor, :math:`\ten{T}`, then

.. math:: T^{ij}_{k \dots l} = \mathfrak{I}^{ij} \epsilon_{k \dots l}

	  
and :math:`\mathfrak{I}` transforms as

.. math:: \mathfrak{I}^{i' j'} = J \Lambda^{i'}_k \Lambda^{j'}_l \mathfrak{I}^{kl}

The generalised delta
=====================

When arrangements of the form :math:`\epsilon^{ij \dots k} \epsilon_{il\dots m}` occur we end up with combinations of Kronecker deltas,

.. math::

   \label{eq:39}
     \epsilon_{ij \dots k} \epsilon^{lm \dots r} =n! \delta^l_{[i} \delta^m_j \cdots \delta^r_{k]} = \delta^{lm \dots r}_{ij \dots k}

     
Defining the :math:`p`-delta as

.. math::

   \label{eq:40}
   \delta^{i \dots j}_{k \dots l} = p! \delta^i_{[k}\dots \delta^j_{l]}


where the sets of upper and lower indices each have :math:`p` elements.

The exterior derivative
=======================

Let :math:`\omega = \sum_I a_I \dd{x}^I` be a smooth differential :math:`r`-form over :math:`U`.
The exterior differential of :math:`\omega` is the :math:`(r+1)`-form,
:math:`\dd{\omega}`, defined by

.. math::

   \dd{\omega} = \sum_{I \in \mathcal{X}}
     (\dd{a}_I) \wedge \dd{x}^I

with :math:`\mathcal{X}` the set of all vector fields defined on the
manifold.

Let :math:`f` be a smooth, real-valued function on :math:`\rn`, then

.. math:: \dd{f} = \pdv{f}{x^i} \dd{x^i}

 which is the gradient; a covector field.

Let
:math:`\eta^j = (-1)^{j-1} \dd{x^1} \wedge \dd{x^n} : 1 \leq j \leq n`
be an :math:`(n-1)`-form, then any :math:`(n-1)`-form can be written
:math:`\of{\omega} = a_i \eta^i`

.. math::

   \dd{\omega} = \pdv{a_i}{x^j} \dd{x^j} \wedge \eta^i = \partial_i
   a^i \dd{x^1} \wedge \dots \dd{x^n}

For the case of :math:`(n-1)`-forms the exterior differential behaves
like the divergence operator on a vector field in :math:`\rn`.

Integration on oriented manifolds
=================================

Integration is essentially the act of multiplying a function by a small
coordinate element, and then summing the values, so,

.. math::

   \label{eq:37}
     \int \of{\omega} \equiv \int f(x^1, \dots, f^n) \dd{x^1} \dots \dd{x^n}


The basis of integration on a smooth manifold relies on relating it to integration on :math:`\rn`. Given that a manifold is only locally homeomorphic to :math:`\rn` however, integration may only be performed directly in coordinate patches, and so there is some extra work to produce an overall theory of integration for a manifold.


Stokes Theorem
--------------
There is a version of Stokes Theorem for an arbitrary :math:`(n-1)`-form, :math:`\of{\alpha}` on :math:`M`.

.. math:: \int_U \dd{\of{\alpha}} = \int_{\partial U} \of{\alpha}


Divergence Theorem
------------------

And, taking :math:`(\div_{\of{\omega}} \xi) \of{\omega} \equiv \dd{[\of{\omega}(\xi)]}`, then

.. sidebar:: Sidebar test

	     This is a quick test of the sidebar functionality.
   

.. math::

   \label{eq:60}
       \int_U (\div_{\of{\omega}} \xi) \of{\omega} = \int_{\partial U} \of{n}(\xi) \of{\alpha}


Lie Derivatives of Forms
========================

The Lie derivative of a form :math:`\omega` with respect to a vector
field :math:`V` is

.. math::

   \label{eq:57}
     \ld{V}{\of{\omega}} = \dd{d}[\of{\omega}(V)] + (\dd{\of{\omega}})(V)


An important consequence of this is that Lie and exterior differentiation commute, so we also have

.. math::

   \label{eq:58}
     \ld{V}{\dd{\of{\omega}}} = \dd{(\ld{V}{\of{\omega}})}


