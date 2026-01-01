Vector Spaces
=============

.. prf:definition:: Vector space

		    :math:`\def\vs#1{\mathsf{#1}}`
		    A vector space over a field (:prf:ref:`field<field>`) :math:`F` is a set, :math:`\vs{V}` of elements called vectors on which addition,
		    :math:`\vec{u}+\vec{v}` of vectors :math:`\vec{u}` and :math:`\vec{v}`, is defined,
		    scalar multiplication, :math:`\lambda \vec{u}` of a vector :math:`\vec{u}` by a scalar :math:`\lambda` from :math:`F` is defined
		    and the following axioms hold:

		    .. prf:axiom:: Vector addition

				   .. math::         \vec{u}+\vec{v} \in \vs{V} 

		    .. prf:axiom:: Assosciativity of addition

				   .. math::         (\vec{u} + \vec{v}) + \vec{w} = \vec{u}+(\vec{v}+\vec{w})

		    .. prf:axiom:: Commutativity of addition

				   .. math::         \vec{u}+\vec{v} = \vec{v}+\vec{u}

		    .. prf:axiom:: Existence of a zero vector

				   .. math::         \exists \vec{0} \in \vs{V}  \mid \vec{u}+\vec{0} = \vec{u}=\vec{0}+\vec{u}

		    .. prf:axiom:: Existence of an additive inverse

				   .. math::         \forall \vec{u} \in \vs{V} \exists - \vec{u}\in \vs{V}  \mid \vec{u}+(-\vec{u}) = \vec{0} = (-\vec{u})+\vec{u}

		    .. prf:axiom:: Existence of the scalar product

				   .. math::         \lambda \vec{u} \in \vs{V} \forall \lambda \in F

		    .. prf:axiom:: Distributivity of the scalar product

				   .. math::          \forall \vec{u}, \vec{v} \in \vs{V} , \forall \lambda, \mu \in F,  \lambda(\vec{u}+\vec{v}) = \lambda \vec{u}+\lambda \vec{v}

The most common types of vectors encountered in physics, for example, are Euclidean vectors, which can be represented as tuples of (often real) scalars.
However, the notion of a vector space generalises this to any object which happens to satisfy the multiplication and addition requirements of the vector space.
						      
.. prf:definition:: Vector Subspace
						      
		    A non-empty subset, :math:`w`, of a vector space :math:`\vs{V}` over :math:`F`, such that

		    .. math::

		       \label{eq:subspaceaddclose}
		       \vec{w}_1 + \vec{w}_2 \in w \qquad \forall \vec{w}_{1,2} \in w
		       
		    .. math::

		       \label{eq:scalarmultsubsclose}
		       \lambda \vec{w} \in w \qquad \forall \vec{w} \in w, \forall \lambda \in F

[Vector space sum] Let :math:`\vs{U}_1` and :math:`\vs{U}_2` be
subspaces of a vector space :math:`\vs{V}`, then the sum,
:math:`\vs{U}_1 + \vs{U}_2` is defined,

.. math::

   \label{eq:vectorspacesum}
       \vs{U}_1 + \vs{U}_2 = \left\{ \vec{u}_1 + \vec{u}_2 \in \vs{V} \mid \vec{u}_1 \in \vs{U}_1 \wedge \vec{u}_2 \in \vs{U}_2 \right\}

 i.e. \ :math:`\vs{U}_1 + \vs{U}_2` is the set of vectors in
:math:`\vs{V}`, that, expressed as a vector in :math:`\vs{U}_1` added to
a vector in :math:`\vs{U}_2`.

[Vector Direct Sum] A sum :math:`\vs{U}_1 + \vs{U}_2` in which every
element can be expressed uniquely in the form
:math:`\vec{u}_1 + \vec{u}_2`, with :math:`\vec{u}_1 \in \vs{U}_1`, and
:math:`\vec{u}_2 \in \vs{U}_2` is called a direct sum, and is denoted

.. math:: \vs{U}_1 \oplus \vs{U}_2

The sum :math:`\vec{u}_1 + \vec{u}_2` is the direct sum,
:math:`\vec{u}_1 \oplus \vec{u}_2` iff
:math:`\vec{u}_1 \cap \vec{u}_2 = \{\vec{0}\}`

[Linear Combination] Let :math:`\vec{u}_1, \vec{u}_2, \dots, \vec{u}_n`
be vectors in the vector space :math:`\vs{V}` over the field :math:`F`.
A linear combination of these vectors is a vector of the form

.. math:: \lambda_1 \vec{u}_1 + \lambda_2 \vec{u}_2 + \cdots + \lambda_n \vec{u}_n

 with :math:`\lambda_1, \lambda_2, \dots, \lambda_n \in F`.

[Span of a vector space] Let
:math:`\vec{u}_1, \vec{u}_2, \dots, \vec{u}_n` be vectors in the vector
space :math:`\vs{V}` over the field :math:`F`, then the subspace of
:math:`\vs{V}` spanned by these vectors is denoted

.. math:: {\rm sp}(\vec{u}_1, \vec{u}_2, \dots, \vec{u}_n)

 and is defined by

.. math::

   \left\{ \lambda_1 \vec{u}_1 + \lambda_2 \vec{u}_2 + \cdots +
     \lambda_n \vec{u}_n \mid \lambda_1, \lambda_2, \dots, \lambda_n \in
     F \right\}

 So the supspace spanned by this sequence of vectors is the set of all
linear combinations which may be formed from the sequence.

[Finite Dimensional Vector Space] A finite dimensional vector space is
one which is spanned by a finite sequence of vectors.

[Linearly Independent Sequence] A sequence of vectors
:math:`\vec{u}_1, \vec{u}_2, \dots, \vec{u}_n \in
  \vs{V}` is called a linearly independent sequence iff

.. math::

   \lambda_1 \vec{u}_1 + \lambda_2 \vec{u}_2 + dots + \lambda_n
     \vec{u}_n = \vec{0}

is only possible when

.. math:: \lambda_1 + \lambda_2 + \cdots +\lambda_n = 0

 with :math:`\lambda_1,
  \lambda_2, \dots , \lambda_n \in F`.

If :math:`\vs{W}` is a subspace of :math:`\vs{V}` such that it is
spanned by :math:`\vec{u}_1, \vec{u}_2, \dots, \vec{u}_n`, then there is
a subspace of this sequence which is linearly independent and still
spans :math:`\vs{W}`.

Bases
=====

.. prf:definition:: Basis

		    A basis is a linearly independent sequence of vectors which is a span of a vector space.

		    
Suppose :math:`\vec{u}_1, \vec{u}_2, \dots, \vec{u}_n` is a basis of a vector space :math:`\vs{V}`.
Then every element can be uniquely expressed as a linear combination of the sequence.

The unique scalar multiples of each are the *components* of the element :math:`\vec{x} \in \vs{V}`.

Suppose :math:`\vs{V}` has a basis :math:`\vec{u}_1, \vec{u}_2 \dots \vec{u}_n`.
Then any sequence of vectors :math:`\vec{w}_1, \vec{w}_2, \dots \vec{w}_m \in \vs{V}` with :math:`m > n` is linearly dependent.

It is often common to encounter the bases of a vector space defining a coordinate system for the vector space.

.. prf:definition:: Dimension of a vector space

		    Suppose :math:`\vs{V}` is finite dimensional.
		    Then the dimension of :math:`\vs{V}`, denoted :math:`\dim(\vs{V})`, is the number of vectors in any basis of :math:`\vs{V}`.

.. prf:criterion:: Conditions for a basis
		    
		   A sequence of vectors in :math:`\vs{V}` is a basis provided it possesses any two of the following conditions,

		   #. the sequence spans :math:`\vs{V}`
		   #. the sequence is linearly independent
		   #. :math:`n = \dim(\vs{V})`

.. prf:property:: Properties of a vector subspace

		  Suppose :math:`\vs{V}` is finite dimensional; let :math:`\vs{W}` be a subspace of :math:`\vs{V}`, then,
		  
		  #. :math:`\vs{W}` is finite dimensional
		  #. :math:`\dim(\vs{W}) \leq \dim(\vs{V})`
		  #. If :math:`\vs{W} \neq \vs{V}` then :math:`\dim(\vs{W}) < \dim(\vs{V})`
		  #. Any basis of :math:`\vs{W}` can be extended to be a basis of :math:`\vs{V}`.

