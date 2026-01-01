Linear Mappings
===============

Linear mappings extend the concept of :ref:`mappings` to vector spaces.

.. prf:definition:: Linear Mapping
		    
		    :math:`\def\vs#1{\mathsf{#1}}\require{physics}`

		    Let :math:`\vs{V}, \vs{W}` be vector spaces over a field :math:`F`.
		    A linear mapping (or linear transformation) from :math:`\vs{V}` to :math:`\vs{W}` is a mapping
		    
		    .. math:: f: \vs{V} \to \vs{W}

		    such that

		    .. math:: f(\alpha \vec{u} + \beta \vec{v}) = \alpha f(\vec{u}) + \beta f(\vec{v})

		    :math:`\forall \alpha, \beta \in F` and :math:`\vec{u}, \vec{v} \in \vs{V}`.

Examples of linear mappings are linear functions, and the linear differential operator.
Not all mappings satisfy the requirements of a linear mapping, however.
For example, the mapping :math:`f: x \to x^2` is not linear, but is still a mapping.

.. prf:definition:: Matrix of a linear mapping with respect to a given basis

		    Let :math:`f:\vs{V} \to \vs{W}` be a mapping between two vector spaces :math:`\vs{V}` and :math:`\vs{W}` over :math:`F`.
		    Suppose :math:`S_1: \vec{v}_1, \vec{v}_2,   \dots, \vec{v}_n` is a basis for :math:`\vs{V}`, and :math:`S_2: \vec{w}_1, \vec{w}_2, \cdots \vec{w}_m` is a basis for :math:`\vs{W}`.
		    Then, for :math:`j = 1,2, \dots, n`,

		    .. math::

		       f(\vec{v}_j) = a_{1j} \vec{w}_1 + a_{2j} \vec{w}_2 + \cdots + a_{mj} \vec{w}_m

		    for scalars :math:`a_{ij}`, with :math:`i = 1,2, \dots, m`, :math:`j=1,2, \dots, n`, then the matrix

		    .. math:: A = \qty[a_{ij}]

		    is the matrix of :math:`f` with respect to the bases :math:`S_1` and :math:`S_2`.

.. prf:corollary:: Composition of linear mappings
		    
		    Let :math:`f:\vs{V} \to \vs{W}` and :math:`g:\vs{V}\to \vs{W}` be linear mappings of vector spaces over :math:`F`, and let :math:`\gamma , \delta \in F`.
		    Then the mapping :math:`\gamma f + \delta g : \vs{V} \to \vs{W}` defined by the rule

		    .. math::

		       (\gamma f + \delta g)(\vec{v}) = \gamma f(\vec{v}) + \delta g(\vec{v}) \qquad (\vec{v} \in \vs{V})

		    is a linear mapping.

.. prf:definition:: Kernel of a linear mapping

		    Let :math:`f:\vs{V} \to \vs{W}` be a linear mapping between the vector spaces :math:`\vs{V}` and :math:`\vs{W}` over :math:`F`.
		    The kernel of :math:`f` is the set of vectors from the domain of :math:`f` which are mapped to the zero vector of the codomain :math:`\vs{W}`.
		    That is,

		    .. math::

		       \ker(f) = \{ \vec{v} \in \vs{V} : f(\vec{v}) = \vec{0} \}

.. prf:definition:: Image of a linear mapping
		       
		    Let :math:`f:\vs{V} \to \vs{W}` be a linear mapping of vector spaces over :math:`F`.
		    The image is
		    
		    .. math::
		       \DeclareMathOperator{\img}{Img}
		       \img(f) = \{ f(\vec{v}) : \vec{v} \in \vs{V} \}

		    the set of vectors in the codomain, :math:`\vs{W}`, which are mapped to by at least one vector from :math:`\vs{V}`.

Let :math:`f: \vs{V} \to \vs{W}` be a linear mapping of vector spaces over :math:`F`, then
-  :math:`\ker(f)` is a subspace of :math:`\vs{V}`.
-  :math:`\img(f)` is a subspace of :math:`\vs{W}`.

Let :math:`f: \vs{V} \to \vs{W}` be a linear mapping of vector spaces then,
#. :math:`f` is injective iff :math:`\ker(f) = \{ \emptyset \}`
#. :math:`f` is surjective iff :math:`\img(f) = \vs{W}`
#. :math:`f` is bijective iff :math:`\ker(f) = \{ \emptyset \}` and :math:`\img(f) = \vs{W}`

.. prf:definition:: Rank and Nullity

		    Let :math:`f: \vs{V} \to \vs{W}` be a linear mapping of vector spaces over :math:`F`.
		    The rank of :math:`f`, denoted :math:`\rank(f)` is defined

		    .. math::
		       \DeclareMathOperator{\rank}{rank}
		       \rank(f) = \dim(\img(f))

		    and the nullity of :math:`f` is denoted :math:`\nullity(n)`, and is defined

		    .. math::
		       \DeclareMathOperator{\nullity}{nullity}
		       \nullity(f) = \dim(\ker(f))

Let :math:`f: \vs{V} \to \vs{W}` be a linear mapping between finite dimensional vector spaces over :math:`F`, then 

#. :math:`f` is injective iff :math:`\nullity(f)=0`
#. :math:`f` is surjective iff :math:`\rank(f) = \dim(\vs{W})`
#. :math:`f` is bijective iff :math:`\nullity(f) = 0` and :math:`\rank(f) = \dim(\vs{W})`


.. prf:theorem:: Rank-Nullity Theorem

		 Let :math:`f: \vs{V} \to \vs{W}` be a linear mapping between vector spaces over :math:`F`, where :math:`\vs{V}` is finite-dimensional, then

		 .. math:: \dim(\vs{V}) = \rank(f) + \nullity(f)

Composition of linear mappings
------------------------------
			   
Let :math:` \vec{y} = A \vec{x}` be a representation of a vector with respect to a basis :math:`\vec{v}^{\prime}`, and :math:`\vec{z} = B \vec{x}` be a represetation of the vector with respect to a basis :math:`\vec{w}^{\prime}`.

The matrix of a linear mapping :math:`f` with respect to the bases :math:`\vec{v}^{\prime}` and :math:`\vec{w}^{\prime}` will be :math:`B^{-1} F A` for :math:`F` the
matrix of :math:`f`.

Suppose :math:`\vs{U}, \vs{V}, \vs{W}` are finite dimensional vector spaces, and that :math:`f:\vs{U} \to \vs{W}` and :math:`g:\vs{V} \to \vs{W}` are linear mappings. Suppose :math:`\vec{u}_1, \dots, \vec{u}_m`, :math:`\vec{v}_1, \dots, \vec{v}_n`, and :math:`\vec{w}_1, \dots, \vec{w}_n` are bases of each vector space.
Let :math:`F, G` respectively represent the matrices of :math:`f, g`. 
Then the composition :math:`g \circ f: \vs{U} \to \vs{W}` with respect to these bases is :math:`GF`.

Eigenquantities
---------------

.. prf:definition:: Eigenvectors and eigenvalues

		    Let :math:`A` be a linear mapping from a vector space :math:`\vs{V}` over a field :math:`F` to itself.
		    A non-zero vector :math:`\vec{x} \in \vs{V}`, such that
		    
		    .. math:: A \vec{x} = \lambda \vec{x}

		    for some scalar :math:`\lambda \in F`.
		    
		    Then :math:`\vec{x}` is an *eigenvector* of :math:`A`, and :math:`\lambda` is the corresponding *eigenvalue*.

Let :math:`A` be a square matrix over :math:`\mathbb{R}`, with an eigenvalue, :math:`\lambda` in :math:`\mathbb{R}`.
Then :math:`A` has a real eigenvector which corresponds to :math:`\lambda`.

.. prf:example:: Eigenvectors of the Moment of Inertia

		 The moment of inertia of a rigid body is described by an object called the moment of inertia tensor :prf:ref:`moment-of-inertia-tensor`.
		 In order to find the axes about which the rigid body moves we can find its eigenvectors from its principle moments of inertia.
		 These eigenvectors are unaffected by rotation of the rigid body.

.. prf:definition:: Characteristic Polynomial

		    Let :math:`A` be an :math:`n \times n` matrix.
		    The characteristic polynomial :math:`\chi_A (t)` of :math:`A` is defined

		    .. math:: \chi_A (t) = \det (t I - A)

		    with :math:`I` the identity matrix.

For an :math:`n \times n` matrix :math:`A` the polynomial :math:`\chi_A (t)` is of degree :math:`n` and is monic (i.e. the coefficient of :math:`t^n` is 1).
Suppose that :math:`\chi_A (t) = t^n + c_{n-1} t^{n-1} + \cdots + c_1 t + c_0`, then

.. math:: c_{n-1} = - \tr(A) \qquad c_0 = (-1)^n \det(A)

Let :math:`A, B` be :math:`n \times n` matrices, with :math:`B` being invertible, then,

.. math:: \chi_{BAB^{-1}}(t)  = \chi_A (t)

.. prf:definition:: Matrix Polynomial

		    Consider a polynomial
		    
		    .. math:: p(t) = a_k t^k + a_{k-1} t^{k-1} + \cdots + a_1 t + a_0

		    with coefficients drawn from a field :math:`F`.
		    The :math:`n \times n` matrix :math:`A` is said to satisfy the polynomial :math:`p(t)` if
		    
		    .. math:: p(A) = a_k A^k + a_{k-1} A^{k-1} + \cdots + a_1 A + a_0 I = 0

		    with the right hand side being the zero matrix.

.. prf:theorem:: Cayley-Hamilton Theorem

		 Let :math:`A` be an :math:`n \times n` matrix, then

		 .. math:: \chi_A(A) = 0

		 For an :math:`n \times n` matrix :math:`A`, if :math:`\det(A) \neq 0` then :math:`A` is invertible.

.. prf:proof::
		 
               Let :math:`A` be a complex square matrix.
	       Since :math:`\chi_A(t)` has degree :math:`n`, :math:`A` has :math:`n` complex eigenvalues (which may have multiplicity).

	       Let :math:`\lambda_1, \lambda_2, \dots `\ l\ :math:`_n` be the eigenvalues of an :math:`n \times n` matrix over :math:`\mathbb{C}`.
	       Then

	       .. math:: \sum_{i=1}^n \lambda_i = \trace(A)

	       and

	       .. math:: \prod_{i=1}^n \lambda_i = \det(A)

.. prf:corollary:: Eigenvalues of a Hermitian Matrix
		   
		   The eigenvalues of a Hermitian matrix are real.

.. prf:proof::
		   
	       Let :math:`A` be a Hermitian matrix; by definition :math:`A = A^\dagger`.
	       Let :math:`\lambda` be an eigenvector of :math:`A`. Let :math:`\vec{v}` be an eigenvector corresponding to the eigenvalue :math:`\lambda`.
	       Let :math:`\braket{\cdot}` be the inner product on :math:`\mathbb{C}`, using braket notation, so,

	       .. math::

		      \begin{aligned}
			    \lambda \braket{\vec{v}} &= \braket{\lambda \vec{v}}{\vec{v}} \\
			    &= \braket{A \vec{v}}{\vec{v}} \\
			    &= \braket{\vec{v}}{A^{\dagger}\vec{v}} \\
			    &= \braket{\vec{v}}{A\vec{v}}\\
			    &= \braket{\vec{v}}{\lambda \vec{v}} \\
			    &= \lambda^{*} \braket{\vec{v}}
		      \end{aligned}

	       Since :math:`\braket{v} \neq 0` it follows that :math:`\lambda = \lambda^{*}`, and so must be real.

