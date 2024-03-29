*********
Manifolds
*********

:math:`\require{physics}\def\rn{\mathbb{R}}`

A manifold is a space which resembles flat Euclidean space at a local level.
The surface of a sphere is an example of a manifold.

Differentiable manifolds are a specific type of manifold where the local Euclidean-like regions can be attached together in such a way that calculus can be performed across the manifold.

Definitions
===========

In order to define a manifold we need to have some means of extending a set with some notion of proximity.
This is achieved through the definition of a :term:`neighbourhood`.

:math:`\rn` is the set of all :math:`n`-tuples of real numbers.

.. prf:definition:: Manifold

		    A set :math:`M` is called a manifold if each element of :math:`M` has an open :term:`neighbourhood` with a continuous bijection onto an open set of :math:`\rn` for some :math:`n`.

This mathematical object is rather degenerate, and hasn’t got, for example, a notion of distance, and what structure is defined is only at a local level, and there is no defined way of moving from one neighbourhood to another.

.. prf:definition:: Coordinates

		    The elements, :math:`P` of :math:`M` have a unique :math:`n`-tuple, which are the co-ordinates of :math:`P`:  :math:`\left( x_1(P), x_2(P), \dots, x_n(P) \right)`.

In order to move between locally flat neighbourhoods we need to consider a function which will map one to the other.
      
Let :math:`f:U(P) \to \rn` be a function from a neighbourhood :math:`U` around :math:`P\in M` of :math:`M` onto an open set :math:`f(U) \in \rn`.
The pair, :math:`(U,f)` are a chart.

If all points of :math:`M` are to be included in at least one open :term:`neighbourhood` they must overlap, and so these overlaps give an additional characterisation of the manifold.

Suppose :math:`V` is a neighbourhood which overlaps with :math:`U`, and :math:`V` has a map :math:`g` onto an open region of :math:`\rn`.
This region may be completely disjoint from the equivalent region for :math:`U`.

The open intersection of :math:`U` and :math:`V` is described by two coordinate systems, so there should be an expression connecting the two.
Such an equation is a *coordinate transformation*.

.. prf:definition:: Chart

		    A chart :math:`(U, f_U)` of a manifold is an open set :math:`U` together with a mapping :math:`f_U: U \to \rn`.

.. prf:definition:: Coordinates
		    
		    The coordinates :math:`(x^1, \cdots, x^n)` of the image :math:`f_U(x) \in \rn` are the coordinates of :math:`x` in the chart :math:`(U, f_U)`; the local coordinate system.

.. prf:definition:: Atlas
		    
		    If a whole system of charts, an atlas, can be constructed such that every point in :math:`M` is in at least one neighbourhood, and every chart is :math:`C^k`-related to every overlapping neighbour the manifold is :math:`C^k`.

Any such manifold for :math:`C^1` or greater is a differentiable manifold.

Many mathematical spaces can be considered as manifolds, for example the space of Lorentz boosts, mechanical phase space, solution spaces for functions, and vector spaces.
Groups also have representations as manifolds; a Lie group, e.g. the group of rotations of a rigid object in space is also a :math:`C^{\infty}` manifold.

.. glossary::

orientability
   Let :math:`M^n` be a differentiable :math:`n`-dimensional manifold equipped with an atlas :math:`\set{\phi_a}`, and suppose that for any two charts of the atlas, :math:`\phi_{\alpha}`, and :math:`\phi_{\beta}` the Jacobian of the transition function :math:`\phi_{\beta \alpha} = \phi_{\beta} \circ \phi_{\alpha}^{-1}` is positive at all points in the domain, then :math:`M` is an orientable manifold.
   A Jacobian which is negative will reverse the orientation of a coordinate system.


Examples
--------

.. include:: examples/manifold-circle.rst
.. include:: examples/manifold-sphere.rst

   
Global Properties
=================

At a local level all manifolds look like :math:`\rn`, but on a global level this is not the case. For example a sphere, :math:`S^2` and a crayon are both two-dimensional manifolds, and neither has a single map to :math:`\mathbb{R}^2`, but there is a continuous map from one to the other.

If there is an infinitely-smooth (:math:`C^{\infty}`) bijective map from one :math:`C^{\infty}` manifold to another, then the two map is a *diffeomorphism* from one manifold to the other.


Curves and Functions on Manifolds
=================================

A curve is a differentiable mapping from an open set of :math:`\mathbb{R}^1` into :math:`M`, so each point :math:`\lambda` on the real line is associated with a point in :math:`M`.

A function on :math:`M` is a rule assigning a real number to each point of :math:`M`.
When a region of :math:`M` is mapped to :math:`\rn` the function becomes a function of :math:`\rn`.
If this is differentiable on :math:`\rn` it is defined as being differentiable on :math:`M`.

So we have a function :math:`g` which maps a point :math:`P \in M` to :math:`\rn`.

.. math:: g(P \in M) = g(x_1(P), \dots, x_n(P)) = g(x_1, \dots x_n)

Now, consider a curve, :math:`c`, which passes through :math:`P \in M`, which is described by :math:`x^i = x^i(\lambda)` for :math:`i \in \set{1, \dots, n}`, and a differentiable function
:math:`g(x^i)` on :math:`M`. :math:`g` has a value at each point along the curve, so there is a differentiable function, :math:`g(\lambda)` along the curve which gives the value of  :math:`c` at the point with a parameter value :math:`\lambda`,

..
   .. tikz:: A curve on a manifold.
      :include: figures/manifold.pgf

.. prf:example:: A hill path

		 When walking along the path on a hill each step along the path indexes the path.
		 The number of steps is the parameter :math:`\lambda`.

		 The path represents a curve over the manifold, which is the hill.
		 The actual distance along the curve that each step represents changes, so to find the elevation (the value of the curve) after a given number of steps, we need a mapping from the number of steps to the point on the manifold.

		 To do this we consider that,

		 .. math::

		    g(\lambda) = g(x^1(\lambda), \dots, x^n(\lambda) ) = g(x^i(\lambda))

		 Then differentiate, and apply the chain rule, which gives
		 
		 .. math::

		    \frac{\dd g}{\dd \lambda} = \frac{\dd x^i}{\dd \lambda} \frac{\dd g}{\dd x^i}

		 using Einstein notation.

In Euclidean space the set :math:`\set{\dd x^i / \dd \lambda }` would be components of a vector tangent to the curve :math:`x_i(\lambda)`, and would be the tangent to an infinite number of curves through :math:`P`.

Manifolds do not necessarily have a notion of distance between points, so vectors must be defined in terms only of infinitessimal neighbourhoods of the points of :math:`M`.

Vectors on a manifold
=====================

.. prf:definition:: Tangent vector space

Suppose :math:`a` and :math:`b` are two numbers and :math:`x^i = x^i(\mu)` is a curve which passes through :math:`P`, then at :math:`P`,

.. math:: \dv{\mu} = \ddv{x^i}{\mu} \pdv{x^i}

and

.. math:: a \dv{\lambda} + b\dv{\mu} = \left( a \dv{x^i}{\lambda} + b \dv{x^i}{\mu} \right) \pdv{x^i}

The numbers inside the bracket are the components of a new vector, tangent to a curve at :math:`P`, so a curve must exist, with parameter :math:`\phi` such that at :math:`P`,

.. math:: \dv{\phi} = \left( a \dv{x^i}{\lambda} + b \dv{x^i}{\mu} \right) \pdv{x^i}

collecting this, at :math:`P`, 

.. math:: a \dv{\lambda} + b \dv{\mu} = \dv{\phi}

forming a vector space.

In any given coordinate system there are special curves, the coordinate
lines. The derivations along them are :math:`\pdv{x^i}`, and
:math:`\dv{\lambda}` has components on the basis, showing that
:math:`\set{\ddv{x^i}{\lambda}}` are a basis for a vector space.

Basis Vectors and basis vector fields
=====================================

At any point :math:`P` the space :math:`T_P` is a vector space with the
same dimension :math:`n` as the manifold, and is the tangent space. Any
collection of linearly independent vectors can form a basis, and if
there is a coordinate system :math:`\set{x^i}` in a neighbourhood
:math:`U` of :math:`P` then these coordinate define a coordinate basis
at all points in :math:`U`.

.. glossary::

tangent vector
   Let :math:`M^m` be a differential manifold, :math:`p` a point on it, and :math:`U` be an open neighbourhood of :math:`M`.
   Let :math:`\epsilon>0`, and :math:`\gamma :   (-\epsilon, \epsilon) \to U` be a differentiable curve on :math:`M` such that :math:`\gamma(0) = p`.

   For any differentiable function :math:`f:U \subset M \to \mathbb{R}` the directional derivative of :math:`f` along :math:`\gamma` to be the number

   .. math:: D_{\gamma}(f) = \left. \frac{\dd}{\dd t}  f \left(\gamma(t)\right)  \right|_{t=0}

   The operator :math:`D_{\gamma}` is called the tangent vector to :math:`\gamma` at :math:`p`.

tangent space
   The tangent space of :math:`M` at :math:`p`, :math:`T_p` is a vector space with the same dimension as the manifold composed of all of the tangent vectors to the manifold at :math:`p`. If :math:`x` is a coordinate system which contains :math:`p`, then the set of :math:`\pdv{x}` are the basis of the tangent space; and this is a coordinate basis.

At any point :math:`P` an arbitrary vector :math:`\vec{V}` is

.. math:: \vec{V} = V^i \pdv{x^i} = V^j \bar{e}_j = V^j \partial_j

for an arbitrary basis :math:`\set{\vec{e}_i}`. Thus :math:`\set{V^i}`
are the components of :math:`\vec{V}` in :math:`\set{ \pdv{x^i}}`, and
:math:`\set{V^j}` the components in :math:`\vec{e}_j`, where a useful
notation, :math:`\partial_i \equiv \pdv{x^i}` is introduced.

Differential of a map
=====================

.. glossary::
   differential
      Let :math:`\phi: M^m \to N^n` be a differentiable map between differentiable manifolds. We define the differential of :math:`\phi` at :math:`p \in M` as the linear transformation between vector spaces

.. Check this...

.. math::
      
   \begin{aligned}
       \ddv{\phi_p}{t} : T_pM & \to T_{\phi(p)N} \\ 
   D_{\gamma} &\mapsto D_{\phi \circ \gamma}
     \end{aligned}

Fibre bundles
=============

.. glossary::
   
   homeomorphism
      A homeomorphism is an bijection from one space to the other which is continuous, and its inverse is continuous.

   fibre bundle
      A fibre bundle is a space, :math:`E`, which has a base manifold :math:`B`, a projection :math:`\pi: E \to B`, a typical fibre :math:`F` a structure group :math:`G` of homeomorphisms of :math:`F` onto iteself, and a family :math:`\set{U_j}` of open sets which cover :math:`B`, which satisfy

     #. Locally the bundle is trivial: the bundle over any set :math:`U_j` which is just :math:`\pi^{-1}(U_j)` has a homeomorphism onto :math:`U_j \times F`.
      Part of this is a homeomorphism from each fibre, say :math:`\pi^{-1}(x)`, :math:`x\in B` onto :math:`F`.
      Call this map :math:`h_j(x)` labelled both by :math:`x` defining the fibre, but also by :math:`j` indexing the set :math:`U_j` which contains :math:`x`.

     #. When two sets :math:`U_j` and :math:`U_k` overlap a point :math:`x` in their intersection has two homeomorphisms, :math:`h_j(x)` and :math:`h_k(x)` from the fibre onto :math:`F`.
      Thus :math:`h_j(x) \circ h_k^{-1}(x)` is a homeomorphism of :math:`F` onto :math:`F`. This must be an element of :math:`G`.


In two overlapping neighbourhoods there are homeomorphisms :math:`h_j(x)` and :math:`h_k(x)` which map :math:`\vec{v}` to :math:`\alpha_{(j)}` and to :math:`\alpha_{(k)}`, and so the
homeomorphism :math:`h_j(x) \circ h_k^{-1}(x): F \to F` maps :math:`\alpha_{(k)} \to \alpha_{(j)}`, which is equivalent to multiplication by a real number :math:`r_{jk} = \alpha_{(j)}/a_{(k)}`, which must be a non-zero real number.

Thus the structure group is :math:`\mathbb{R}^1 - \set{0}`, which is a Lie group under multiplication.

The difference between two bundles over a base space is the bundles’ *structure group*.

If the coordinates :math:`\lambda_j` can be arranged in such a way that :math:`\lambda_j` and :math:`\lambda_k` increase in the same direction in :math:`S^1` in the overlap region, then :math:`S^1` is orientable.
In such an overlap all :math:`r_{jk}` are positive, so the structure group becomes :math:`\mathbb{R}^+`, and by scaling the coordinates so that :math:`\dv*{\lambda_j}{\lambda_k} = 1` in every overlap the group reduces to the identity element, thus the structure group is trivial and we have a bundle structure.

Consider the combination of a manifold :math:`M` with all of its tangent spaces :math:`T_P`.
This is equivalent to the set of all vectors at all points in the manifold, and can be defined as a new manifold :math:`TM`; a *fibre bundle*, with the fibres the spaces :math:`T_P`, and has dimension :math:`m+n`, with :math:`m` the dimension of each fibre, and :math:`n` of the base manifold.
An example of a fibre bundle is the structure of space and time in the Newtonian world view, where the base space is :math:`\mathbb{R}^1`, with :math:`\mathbb{R}^3` fibres, that is a base of time with fibres of space.
This follows, as there is no absolute concept of space in Newtonian physics, and so there is no connection between points on each fibre.

.. glossary::

   cartesian product space
      A Cartesian product space of two spaces :math:`M` and :math:`N`, denoted :math:`M \times N` is the set of all ordered pairs :math:`(a,b)` for :math:`a \in M` and :math:`b \in
N`, and if :math:`M` and :math:`N` are manifolds then :math:`M \times N` is also a manifold; the set of coordinates :math:`\set{x^i}` of an open set :math:`U` of :math:`M` taken with :math:`\set{y^i}` of an open set :math:`V` of :math:`N` form a set of :math:`m+n` coordiates for the open set :math:`(U,V)` of :math:`M \times N`.

Fiber bundles are locally product spaces; they are locally trivial, as
they look like product spaces, but not usually globally trivial. For
example, :math:`TS^2` is the tangent bundle of a 2-sphere; were it
globally tivial there would be a diffeomorphism of :math:`TS^2` onto
:math:`S^2 \times
\mathbb{R}^2`. Consider the set :math:`(P, \bar{V})` in the product
space; the invserse map gives a nowhere-zero cross-section of
:math:`TS^2`, but a vector field must always have a zero, and so
:math:`TS^2` has no global product structure. A tangent bundle
:math:`TS^1` *is* identical to :math:`S^1
\times \mathbb{R}`, but if the circle is cut at a point :math:`P`, and a
twist is introduced, making a Möbius strip, the resulting bundle is not
a product space, as no bijection exists from one bundle onto all of the
other.

[Tangent Bundle] Let :math:`M^n` be a differentiable manifold. The
disjoint union of all tangent planes to :math:`M`,

.. math:: \coprod_{p \in M} T_p M

is a vector bundle with the fibre :math:`\rn` over :math:`M`, called the
tangent bundle to :math:`M`, denoted :math:`TM`.

Integral Curves
===============

For a :math:`C^1` vector field there is always a curve which has the
field as a tangent at each of its points; these are its integral curves.

Let the components of the field be :math:`V^i(P) = v^i(x^j)` in a
coordinate system :math:`\set{x^i}` The statement that this is a tangent
vector to a curve parameterised by :math:`\lambda` is

.. math::

   \label{eq:7}
     \dv{x^i}{\lambda} = v^i(x^j)

which is a set of first-order ODEs for :math:`x^i(\lambda)`, which always has a unique solution in a neighbourood of :math:`P`.

	     

Tensors
=======

Consider a point :math:`P` in a manifold :math:`M`, a *tensor* of type
:math:`{N \choose N'}` at :math:`P` is a linear function with :math:`N`
one-form arguments, and :math:`N'` vector arguments, which has a real
scalar value. Tensors are linear on every argument.

A :math:`{N \choose N'}` tensor field is a rule which assigns a
:math:`{N \choose N'}` tensor to each point in a space, and are
functions on :math:`M`.

It is possible to construct higher-order tensors out of lower order ones
with the tensor (outer) product operation; for two vectors :math:`V` and
:math:`W` the tensor product is defined such that

.. math::

   \label{eq:11}
     V \otimes W (\of{p}, \of{q}) := V(\of{p}) W(\of{q})

If the basis vectors and one-forms are given as arguments to the tensor
the components of the tensor are returned.

It is also possible to reduce the dimensionality of a tensor by a
process called *contraction* whereby an entire argument is removed from
the tensor by constructing an inner product of those parts of the tensor
with either a one form or a vector.

Basis Transformations
=====================

Consider a point :math:`P` in a manifold :math:`M`, where a vector basis
:math:`\set{e_i}` is defined, but we want to switch to a description in
another basis, :math:`\set{e_{j'}}`, then in :math:`T_P` there is a
linear transformation, :math:`\Lambda` between the old and the new
basis,

.. math::

   \label{eq:12}
     e_{j'} = \Lambda^i_{j'} e_i

where :math:`\Lambda` is non-singular, but arbitrary.
It is not a tensor, since its indices refer to different bases.
The transformation matrix has an inverse, :math:`\Lambda^{k'}_j` such that

.. math:: \Lambda^{k'}_j \Lambda^j_i = \delta^{k'}_{i'}

We require the inverse transformation for basis one-forms, as is evident from the relation

.. math::

   \of{\omega}^i e_{j'} = \delta^{i}_{k} \Lambda^k_{j'} =
   \Lambda^i_{j'}

The general expression for the change of coordinates of a tensor takes the form

.. math::

   \label{eq:71}
     {A'}^{u_1\dots u_l}{}_{r_1 \dots r_m} = \Lambda_{t_1}^{u_1} \cdots \Lambda_{t_l}^{u_l} \Lambda_{r_1}^{q_1} \cdots \Lambda_{r_m}^{q_m} A^{t_1 \dots t_l}{}_{q_1 \dots q_m}

The Metric Tensor
=================

The metric tensor is a linear function defining the inner product of two vectors, such that

.. math::

   \label{eq:13}
     g(V,U) = g(U,V) := U \vdot V

where :math:`g` is the symmetric non-singular metric tensor, with components in the basis :math:`\set{e_i}` being

.. math::

   \label{eq:14}
     g_{ij} = e_i \vdot e_j

The Euclidean metric is defined such that

.. math:: g_{ij} = \delta_{ij}

We can always form a metric, given transformations of the Cartesian
basis,

.. math:: g_{i' j'} = \Lambda^k_{i'} g_{kl} \Lambda^l_{j'}

This can be reduced to an equation of the form

.. math:: g' = D O^{-1} g OD

thanks to the existance of a theorem allowing us to express any matrix as a product of an orthogonal matrix, :math:`O` and a diagonal one, :math:`D`.

From this we can see that orthogonal matrices compose the set of transformations between arbitrary Cartesian bases; they form a continuous group, :math:`O(n)`, which is the Euclidean symmetry group. 

The Minkowski metric, with :math:`g = \diag(-1, 1, 1, 1)`, also has transformation matrices which form the Lorentz group, :math:`L(n)`.
Some additional properties of the metric tensor are:

.. math::

   \label{eq:15}
     {g}^{ij} g_{jk} = \delta^i_k

and since :math:`g^{ki} V_i = g^{ki} g_{ij} V^j = \delta^k_j V^j = V^k`,

.. math::

   \label{eq:16}
       V_i = g_{ij} V^j

.. math::

   \label{eq:17}
       v^j = g^{jk} V_k

allowing the metric tensor to act as an index raising and lowering operator.

Defining a :math:`{0 \choose 2}` tensor on a manifold :math:`M` provides a rich structure, and allow definitions of quantities such as distance and curvature.
