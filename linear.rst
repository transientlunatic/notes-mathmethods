Fields of Scalars
=================

A field is an algebraic structure with notions of addition, subtraction,
multiplication, and division, satisfying certain axioms. The principle
examples are :math:`\mathbb{Q}`, :math:`\mathbb{R}`, and
:math:`\mathbb{C}`.

[Field of Scalars] A field of scalars consists of a set, :math:`F`,
whose elements are called scalars, together with two algebraic
operations—addition and multiplication—for combining every pair of
scalars, :math:`x, y \in F` to form the new scalars :math:`(x+y) \in
   F` and :math:`(x \times y) \in F`. These operations must satisfy the
field axioms:

#. *Associativity*: For :math:`x,y,z \in F`,

   .. math::

      \begin{aligned}
            (x+y)+ z &= x+(y+z) \\
            (x\times y)\times z &= x \times (y \times z)
          \end{aligned}

#. *Distributivity*:

   .. math::

      \begin{aligned}
            (x+y) \times z &= x \times z + y \times z \\
            z \times (x + y) &= z \times x + z \times y
          \end{aligned}

#. *Commutativity*:

   .. math::

      \begin{aligned}
            x + y &= y + x \\
            x \times y &= y \times x
          \end{aligned}

#. *Zero and Unity*: There are unique and distinct elements,
   :math:`0, 1 \in F`, such that

   .. math::

      \begin{aligned}
            x+0 &= x = 0 + x \\
            x \times 1 &= x = 1 \times x
          \end{aligned}

#. *Additive and multiplicative inverses*: For :math:`x \in F` there
   exists a unique element :math:`-x \in F`, for which

   .. math:: x + (-x) = 0 = (-x)+x

   For each non-zero :math:`y \in F` there is a unique element
   :math:`y^{-1} \in F` for which

   .. math::

      y \times
          (y^{-1}) = 1 = (y^{-1})\times y

Vector Spaces
=============

| [Vector Space] A vector space over :math:`F` is a set, :math:`\vs{V}`
  of elements called vectors on which addition, :math:`\vec{u}+\vec{v}`
  of vectors :math:`\vec{u}` and :math:`\vec{v}`, is defined, scalar
  multiplication, :math:`\lambda \vec{u}` of a vector :math:`\vec{u}` by
  a scalar :math:`\lambda` from :math:`F` is defined and the following
  axioms hold:

.. math::

   \begin{aligned}
        \vec{u}+\vec{v} &\in \vs{V} \\
        (\vec{u} + \vec{v}) + \vec{w} &= \vec{u}+(\vec{v}+\vec{w}) \\
        \vec{u}+\vec{v} &= \vec{v}+\vec{u} \\
        \exists \vec{0} \in \vs{V} & \mid \vec{u}+\vec{0} = \vec{u}=\vec{0}+\vec{u} \\
        \forall \vec{u} \in \vs{V} \exists - \vec{u}\in \vs{V} & \mid \vec{u}+(-\vec{u}) = \vec{0} = (-\vec{u})+\vec{u} \\
        \lambda \vec{u} \in \vs{V} \\
        \forall \vec{u}, \vec{v} \in \vs{V} , \forall \lambda, \mu \in F, & \lambda(\vec{u}+\vec{v}) = \lambda \vec{u}+\lambda \vec{v}
     \end{aligned}

[Vector Subspace] A non-empty subset, :math:`w`, of a vector space
:math:`\mathsf{V}` over :math:`F`, such that

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

[Basis] A basis is a linearly independent sequence of vectors which is a
span of a vector space.

[Expressing elements in a vector space] Suppose
:math:`\vec{u}_1, \vec{u}_2, \dots, \vec{u}_n` is a basis of . Then
every element can be uniquely expressed as a linear combination of the
sequence. The unique scalar multiples of each are the *components* of
the element :math:`\vec{x} \in \vs{V}`.

Suppose :math:`\vs{V}` has a basis :math:`\vec{u}_1, \vec{u}_2 \dots
  \vec{u}_n`. Then any sequence of vectors :math:`\vec{w}_1, \vec{w}_2,
  \dots \vec{w}_m \in \vs{V}` with :math:`m > n` is linearly dependent.

[Dimension of a vector space] Suppose :math:`\vs{V}` is finite
dimensional. Then the dimension of :math:`\vs{V}`, denoted
:math:`\dim(\vs{V})`, is the number of vectors in any basis of
:math:`\vs{V}`.

[Conditions for a basis] A sequence of vectors in :math:`\vs{V}` is a
basis provided it possesses any two of the following conditions,

#. the sequence spans :math:`\vs{V}`

#. the sequence is linearly independent

#. :math:`n = \dim(\vs{V})`

[Properties of a vector subspace] Suppose :math:`\vs{V}` is finite
dimensional; let :math:`\vs{W}` be a subspace of :math:`\vs{V}`, then,

#. :math:`\vs{W}` is finite dimensional

#. :math:`\dim(\vs{W}) \leq \dim(\vs{V})`

#. If :math:`\vs{W} \neq \vs{V}` then
   :math:`\dim(\vs{W}) < \dim(\vs{V})`

#. Any basis of :math:`\vs{W}` can be extended to be a basis of
   :math:`\vs{V}`.

Inner Product Spaces
--------------------

In this section, let :math:`\vs{V}` denote a vector space over the field
:math:`\mathbb{R}`, let :math:`\vec{u}, \vec{v},` and :math:`\vec{w}` be
vectors from :math:`\vs{V}`, and :math:`a, b, c,` and :math:`d` be
scalars from the field :math:`\mathbb{R}`.

[Real Inner Product] Suppose to each pair of vectors
:math:`\vec{u},\vec{v} \in \vs{V}` there is assigned a real number,
denoted :math:`\langle \vec{u}, \vec{v}
  \rangle`, which is called the real inner product on :math:`\vs{V}` if
it satisfies the axioms

#. (Linearity)

   .. math::

      \langle a \vec{u}_1 + b \vec{u}_2 , \vec{v} \rangle = a \langle
          \vec{u}_1, v \rangle + b \langle \vec{u}_2, \vec{v} \rangle

#. (Symmetry)

   .. math::

      \langle \vec{u}, \vec{v} \rangle = \langle \vec{v}, \vec{u}
          \rangle

#. (positive definite)

   .. math::

      \langle \vec{u}, \vec{u} \rangle \geq 0 \text{ and }
             \langle \vec{u}, \vec{u} \rangle = 0 \text{ iff } \vec{u} = 0.

[Real Inner Product Space] A vector space, :math:`\vs{V}` on which a
real inner product is defined is called a real inner product space.

[Norm of a vector] The third axiom of the inner product requires that it
always be positive. This allows the definition of the norm,

.. math:: ||\vec{u}|| = \sqrt{ \langle \vec{u}, \vec{u} \rangle }

which is a measure of the length of the vector.

There are numerous examples of inner product spaces, from Euclidean
:math:`n`-spaces (perhaps the most day-to-day example), function and
polynomial space, matrix space, and Hilbert space.

[Cauchy-Schwarz Inequality] For any vectors :math:`\vec{u}` and
:math:`\vec{v}` in an inner product space :math:`\vs{V}`,

.. math::

   \langle \vec{u}, \vec{v} \rangle^2 \leq \langle \vec{u}, \vec{u}
     \rangle \langle \vec{v}, \vec{v} \rangle \quad \text{or} \quad |
     \langle \vec{u}, \vec{v} \rangle \leq ||\vec{u}|| ||\vec{v}||

[Properties of the Norm] Let :math:`\vs{V}` be an inner product space.
Then the norm in :math:`\vs{V}` satisfies the following properties

#. :math:`||\vec{v}|| \geq 0` and :math:`||\vec{v}||=0` if and only if
   :math:`\vec{v}=0`.

#. :math:`||k \vec{v}|| = |k| ||\vec{v}||`

#. :math:`||\vec{u} + \vec{v}|| \leq ||\vec{u}|| + ||\vec{v}||`

[Orthogonal Vectors] Two vectors, :math:`\vec{u}, \vec{v} \in \vs{V}`
are orthogonal iff

.. math:: \langle \vec{u}, \vec{v} \rangle = 0

[Orthonormal Vectors] Two vectors, :math:`\vec{u}, \vec{v} \in \vs{V}`
are orthonormal iff

.. math::

   \langle \vec{u}_i, \vec{u}_j \rangle =
     \begin{cases}
       0 & \vec{u} \neq \vec{v} \\
       1 & \vec{u} = \vec{v}
     \end{cases}

It follows that a sequence of orthogonal or orthonormal vectors is
linearly independent, and so can form a basis. In order to orthogonalise
a basis use the Gram-Schmidt Process. Let :math:`\vec{u}_1,
\vec{u}_2` be linearly independent vectors with an angle :math:`\theta`
between them. Then

.. math::

   \theta = \frac{\langle \vec{u}_1, \vec{u}_2 \rangle}{||\vec{u}_1||
     || \vec{u}_2||}

so :math:`\vec{u}_2` can be expressed as the sum of two vectors in the
direction of :math:`\vec{v}_2` (a new, vector orthogonal to
:math:`\vec{u}_1`, and :math:`\vec{u}_1`. For convenience, let
:math:`\vec{v}_1 = \vec{u}_1`.

[Gram-Schmidt Process] For a sequence of non-orthonormal, linearly
independent vectors :math:`\vec{u}_1, \vec{u}_2, \dots, \vec{u}_n`, in
order to produce an orthonormal sequence,
:math:`\vec{v}_1, \vec{v}_2, \dots, \vec{v}_n`,

#. Let :math:`\vec{v}_1`

#. Set

   .. math:: \vec{v}_k = \vec{u}_k - \sum_{i=1}^{k-1} \frac{\langle \vec{v}_i, \vec{u}_k \rangle}{\langle \vec{v}_i, \vec{u}_i \rangle} \cdot \vec{v}_i

    :math:`\forall k \in \{ 1, ..., n \}`.

#. Normalise each vector by

   .. math:: \hat{v}_i = \frac{\vec{v}_i}{||\vec{v}_i||}

[Complex inner product spaces] Let :math:`\vs{V}` be a vector space over
:math:`\mathbb{C}`. Suppose each pair of vectors

Matrices
========

[Matrix] A matrix, :math:`A` over a field :math:`K` is a rectangular,
:math:`n \times m`, array of scalars, which is usually represented in
the form

.. math::

   A =
   \begin{pmatrix}
     a_{11} & a_{12} & \cdots & a_{1n} \\
     a_{21} & a_{22} & \cdots & a_{2n} \\
     \vdots & \vdots & \ddots & \vdots \\
     a_{m1} & a_{m2} & \cdots & a_{mn}
   \end{pmatrix}

 Both the operations of addition and multiplication are defined for
matrices.

[Main Diagonal] The main diagonal of a matrix are the entries
:math:`a_{ij}` where :math:`j=i`.

[Square Matrix] A matrix is called a square matrix if it is of shape
:math:`(n \times n)`.

[Upper and Lower Triangular Matrices] If a square matrix has only zeros
below every entry in the main diagonal it is an upper triangular matrix.
If the matrix has only zeros above every entry in the main diagonal it
is lower triangular.

[Diagonal Matrix] A matrix is called diagonal if all of the entries
lying off the main diagonal are zero. A diagonal matrix may also be
written as

.. math:: \operatorname{diag}(a_{11}, a_{22}, \cdots, a_{nn})

It should be noted that a diagonal matrix is both upper and lower
triangular.

[Cofactors of a Matrix] The cofactors, :math:`A^{ij}` of an
:math:`n \times n` matrix :math:`A` is the :math:`(n-1) \times (n-1)`
matrix containing the elements of :math:`A` excluding those in the
:math:`i^{\rm th}` row and the :math:`j^{\rm th}` column.

[Cofactor Matrix] A cofactor matrix is a matrix whose elements are all
cofactors, and has the form

.. math::

   C = 
   \begin{pmatrix}
     C_{11} & C_{12} & \cdots & C_{1n} \\
     C_{21} & C_{22} & \cdots & C_{2n} \\
     \vdots & \vdots & \ddots & \vdots \\
     C_{n1} & C_{n2} & \cdots & C_{nn}
   \end{pmatrix}

Matrix Operations
~~~~~~~~~~~~~~~~~

[Matrix Transpose] The transpose of a square matrix :math:`A` is defined

.. math:: \qty[\trans{A}]_{ij} = \qty[A]_{ji}

that is, the transpose of a matrix is the original matrix reflected
about its main diagonal.

[Matrix Trace] The trace of a square matrix, :math:`A` is the sum of the
elements in its main diagonal, ie.

.. math:: \trace(A) = \sum^n_{i=1} a_{ii}

where :math:`a_{ij}` are the elements of :math:`A`.

[Complex Conjugate] The complex conjugate, :math:`\conj(A)` of a matrix
:math:`A` over :math:`\mathbb{C}` is the matrix in which every element
is the complex conjugate of the corresponding element of :math:`A`.

.. math:: \qty[\conj(A)]_{ij} = \qty( \qty[A]_{ij} )^{*}

[Hermitian Conjugate] The hermitian conjugate, :math:`A^{\dagger}` of a
matrix :math:`A` is the matrix

.. math:: A^{\dagger} = \conj(\trans{A}) = \trans{\conj(A)}

[Matrix Determinant] Let :math:`A` be a square matrix, and
:math:`a_{i,j}` be the elements of :math:`A`, then, the determinant of
the matrix, denoted :math:`\det(A)` or :math:`|A|`, is defined

.. math::

   \det(A) = \sum_{i_1, i_2, \dots, i_n = 1}^n \epsilon_{i_1 \cdots
       i_n} a_{1,i_1} \cdots a_{n,i_n}

[Properties of the Determinant] For :math:`n \times n` matrices,
:math:`A,B`, a triangular matrix, :math:`D`, and scalar :math:`c`,

#. :math:`\det(I_n) = 1`

#. :math:`\det(A^{\rm T}) = \det(A)`

#. :math:`\det(A^{-1}) = \det^{-1}(A)`

#. :math:`\det(AB) = \det(A) \det(B)`

#. :math:`\det{cA} = c^n \det{A}`

#. :math:`\det{D} = \prod_{i=1}^n d_{i,i}` (for :math:`d_{i,j} \in D`)

[Determinant of a triangular matrix] The determinant of any triangular
matrix is the product of the entries on its main diagonal.

Let :math:`E(\Theta)` be an elementary matrix for an elementary row
operation :math:`\Theta`, and :math:`B = E(\Theta)A` for matrices
:math:`A` and :math:`B`. Then,

.. math::

   \det(B) = 
     \begin{cases}
       - \det(A) & \text{ if } \Theta \text{ is } R_i \leftrightarrow R_j \\
       \lambda \det(A) & \text{ if } \Theta \text { is } R_i \to R_j \\
       + \det(A) & \text{ if } \Theta \text{ is } R_i \to R_i + \lambda R_j
     \end{cases}

[Invertible Matrix] An :math:`n \times n` matrix :math:`A` is called
invertible if there exists an :math:`n \times n` matrix :math:`B` such
that

.. math:: AB = BA = I

 with :math:`I` the identity matrix.

There are a number of techniques for identifying the inverse of a
matrix, one of which is Cramer’s rule, and the other is Eigenvalue
decomposition.

[Adjugate Matrix] The adjugate matrix is the transpose of the cofactor
matrix.

[Cramer’s Rule] Cramer’s rule is a process for inverting a square
matrix. Let :math:`A` be a square matrix, with :math:`\det(A) \neq 0`.
Then

.. math:: A^{-1} = \frac{1}{|A|} \trans{C}

where :math:`\trans{C}` is the adjugate matrix of :math:`A`. This
process is highly inefficient for large matrices.

Special Matrices
~~~~~~~~~~~~~~~~

[Identity Matrix] The matrix :math:`I` is called the identity matrix and
has the form

.. math:: \operatorname{diag}(1,1,\dots, 1)

[Symmetric Matrix] A matrix :math:`A` over :math:`\mathbb{R}` is a
symmetric matrix if :math:`A^{\rm T} = A`.

[Eigenvectors and Eigenvectors of Symmetric Matrices] Let :math:`A` be a
real, :math:`n \times n` symmetric matrix. The eigenvalues are all real,
and each has a corresponding real unit eigenvector. Further, any
eigenvectors corresponding to distinct eigenvalues are orthogonal.

[Hermitian Matrix] A matrix :math:`A` over :math:`\mathbb{C}` is a
hermitian matrix if :math:`A^\dagger = A`.

[Orthogonal Matrix] A matrix :math:`Q` over :math:`\mathbb{R}` is called
*Orthogonal* if :math:`Q^{\rm T} = Q^{-1}`.

[Inverse of an orthogonal matrix] An orthogonal matrix :math:`P` is
invertible, and :math:`P^{-1} = \trans{P}`.

[Unitary Matrix] A matrix :math:`U` over :math:`\mathbb{C}` is called
*Unitary* if the Hermitian conjugate of :math:`U`,
:math:`U^{\dagger} = U^{-1}`.

[Markov Matrix] A markov matrix is a square matrix in which every
element is non-negative, and in ehich all of the entries in each column
sum to 1.

Every Markov matrix defines a difference equation

.. math::

   X_{n+1} = M
   X_n

for Markov matrix :math:`M`, and non-negative columns :math:`X_n`.

Eigenquantities
~~~~~~~~~~~~~~~

[Eigenvectors & Eigenvalues] Let :math:`A` be an :math:`n \times n`
matrix with entries from :math:`F`. A non-zero vector
:math:`\vec{x} \in F^n`, such that

.. math:: A \vec{x} = \lambda \vec{x}

 for some scalar :math:`\lambda \in F`. Then :math:`\vec{x}` is an
*eigenvector* of :math:`A`, and :math:`\lambda` is the corresponding
eigenvalue.

Let :math:`A` be a square matrix over :math:`\mathbb{R}`, with an
eigenvalue, :math:`\lambda` in :math:`\mathbb{R}`. Then :math:`A` has a
real eigenvector which corresponds to :math:`\lambda`.

[Characteristic Polynomial] Let :math:`A` be an :math:`n \times n`
matrix. The characteristic polynomial :math:`\chi_A (t)` of :math:`A` is
defined

.. math:: \chi_A (t) = \det (t I - A)

with :math:`I` the identity matrix.

For an :math:`n \times n` matrix :math:`A` the polynomial
:math:`\chi_A (t)` is of degree :math:`n` and is monic (i.e. the
coefficient of :math:`t^n` is 1). Suppose that
:math:`\chi_A (t) = t^n + c_{n-1} t^{n-1} + \cdots + c_1
  t + c_0`, then

.. math:: c_{n-1} = - \tr(A) \qquad c_0 = (-1)^n \det(A)

Let :math:`A, B` be :math:`n \times n` matrices, with :math:`B` being
invertible, then,

.. math:: \chi_{BAB^{-1}}(t)  = \chi_A (t)

[Matrix Polynomial] Consider a polynomial

.. math:: p(t) = a_k t^k + a_{k-1} t^{k-1} + \cdots + a_1 t + a_0

with coefficients drawn from a field :math:`F`. The :math:`n \times n`
matrix :math:`A` is said to satisfy the polynomial :math:`p(t)` if

.. math:: p(A) = a_k A^k + a_{k-1} A^{k-1} + \cdots + a_1 A + a_0 I = 0

 with the right hand side being the zero matrix.

[Cayley-Hamilton Theorem] Let :math:`A` be an :math:`n \times n` matrix,
then

.. math:: \chi_A(A) = 0

For an :math:`n \times n` matrix :math:`A`, if :math:`\det(A) \neq 0`
then :math:`A` is invertible.

Let :math:`A` be a complex square matrix. Since :math:`\chi_A(t)` has
degree :math:`n`, :math:`A` has :math:`n` complex eigenvalues (which may
have multiplicity).

Let :math:`\lambda_1, \lambda_2, \dots `\ l\ :math:`_n` be the
eigenvalues of an :math:`n
  \times n` matrix over :math:`\mathbb{C}`. Then

.. math:: \sum_{i=1}^n \lambda_i = \trace(A)

and

.. math::

   \prod_{i=1}^n
     \lambda_i = \det(A)

[Eigenvalues of a Hermitian Matrix] [the:eigenvaluehermitian] The
eigenvalues of a Hermitian matrix are real.

Let :math:`A` be a Hermitian matrix; by definition
:math:`A = A^\dagger`. Let :math:`\lambda` be an eigenvector of
:math:`A`. Let :math:`\vec{v}` be an eigenvector corresponding to the
eigenvalue :math:`\lambda`. Let :math:`\braket{\cdot}` be the inner
product on :math:`\mathbb{C}`, using braket notation, so,

.. math::

   \begin{aligned}
         \lambda \braket{\vec{v}} &= \braket{\lambda \vec{v}}{\vec{v}} \\
         &= \braket{A \vec{v}}{\vec{v}} \\
         &= \braket{\vec{v}}{A^{\dagger}\vec{v}} \\
         &= \braket{\vec{v}}{A\vec{v}}\\
         &= \braket{\vec{v}}{\lambda \vec{v}} \\
         &= \lambda^{*} \braket{\vec{v}}
       \end{aligned}

 Since :math:`\braket{v} \neq 0` it follows that
:math:`\lambda = \lambda^{*}`, and so must be real.

Roots of Polynomials
~~~~~~~~~~~~~~~~~~~~

Any polynomial :math:`p(t) \in \mathbb{C}[t]` of positive degree
:math:`n` can be factored into :math:`n` linear factors

.. math:: p(t) = c(t-\alpha_1)(t-\alpha_2)\cdots (t-\alpha_n)

where :math:`c
\neq 0`, and the roots :math:`\alpha_1, \alpha_2, \dots \alpha_n` are
uniquely determined from their order. Then gathering repeated factors,

.. math::

   p(t) = c(t-\beta_1)^{r_1} (t-\beta_2)^{r_2} \cdots
   (t-\beta_m)^{r_m}

 where :math:`\beta_1, \beta_2, \dots \beta_m` are the distinct complex
roots of :math:`p(t)`, and each :math:`r_k \ge 1` which is the algebraic
multiplicity of :math:`\beta_k`.

Let

.. math:: p(t) = t^n + a_{n-1}t^{n-1} + \cdots + a_1 t + a_0

be a monic polynomial which can be factored

.. math::

   p(t) =
     (t-\alpha_1)(t-\alpha_2)\cdots (t-\alpha_n)

 where :math:`\alpha_1,
  \dots \alpha_n` are complex roots, then

.. math::

   \sum_{i=1}^n \alpha_i = - a_{n-1} \qquad \prod_{i=1}^n = (-1)^n
     a_0

Diagonalisation
~~~~~~~~~~~~~~~

[Similarity] Let :math:`A,B` be square matrices with entries from
:math:`F`. Then :math:`A` is similar to :math:`B` if

.. math:: B = P^{-1} A P

for some invertible square matrix :math:`P` with entries from :math:`F`.

[Properties of similar matrices]

#. Any square matrix :math:`A` is similar to itself.

#. If :math:`A` is similar to :math:`B`, then :math:`B` is similar to
   :math:`A`.

#. If :math:`A` is similar to :math:`B`, and :math:`B` is similar to
   :math:`C`, then :math:`A` is similar to :math:`C`.

[Characteristic Polynomial of similar matrices] Let :math:`A, B` be
similar square matrices. Then :math:`A` and :math:`B` have the same
characteristic polynomial, and hence the same trace, determinant, and
eigenvalues.

[Diagonalisability] Let :math:`A` be a square matrix over :math:`F`. If
:math:`A` is similar to a diagonal matrix over :math:`F` then A is
diagonalisable over :math:`F`.

Let :math:`A` be a square matrix over :math:`F`. :math:`A` is
diagonalisable over :math:`F` iff there exists an invertible matrix
:math:`P` over :math:`F` whose columns are the eigenvectors of
:math:`A`. That is

.. math:: P^{-1} A P = D

for :math:`D` a diagonal matrix, :math:`D =
  \diag(\lambda_1, \dots, \lambda_n)` for distinct eigenvalues
:math:`\lambda_1, \dots, \lambda_n`.

[Jordan-normal Form] A matrix is said to be in Jordan-normal form if all
of the non-zero entries off the main diagonal are immediately above an
element on the main diagonal, and have identical diagonal elements to
the left and below them.

Not all matrices are diagonalisable, but over :math:`\mathbb{C}` it is
always possible to find a matrix :math:`P` such that

.. math:: P^{-1} A P = J

 for a matrix :math:`J` which is in Jordan-normal form.

Linear Mappings
===============

Let :math:`X,Y,Z` denote sets.

[Mapping] A mapping :math:`f:X \to Y` is a rule associating every
element in :math:`X` with a unique member of :math:`Y`. :math:`X` is the
domain, :math:`Y` is the codomain.

[Function Composition] Given two mappings :math:`f:X \to Y` and
:math:`g:Y \to Z`, the composition, :math:`g
  \circ f: X \to Z` is the mapping

.. math:: (g \circ f)(x) = g(f(x)) \qquad \forall x \in X

[Identity Mapping] The identity mapping

.. math:: \idmap_X : X \to X

is defined by

.. math:: \idmap_X(x) = x \quad \forall x \in X

[Zero Mapping] Provided :math:`Y` contains a zero element :math:`0`, the
zero mapping, :math:`0_x:X
  \to Y` is defined

.. math:: 0_x(x) = 0 \quad \forall x \in X

| [Injective, surjective, and bijective mappings] A mapping
  :math:`f:X \to Y` is injective if for all :math:`x_1, x_2 \in X`,

  .. math:: f(x_1) = f(x_2) \implies x_1 = x_2

  A mapping :math:`f: X \to Y` is called surjective if, for every
  :math:`y \in Y` there exists at least one :math:`x \in X` for which
  :math:`y = f(x)`.
| A mapping is bijective if it is both injective and surjective.

A mapping :math:`f:X \to Y` is bijective iff there is an inverse mapping

.. math:: h: Y \to X

such that

.. math::

   h \circ f = \idmap_X \quad
     \text{and} \quad f \circ h = \idmap_Y

[Linear Mapping] Let :math:`\vs{V}, \vs{W}` be vector spaces over a
field :math:`F`. A linear mapping (or linear transformation) from
:math:`\vs{V}` to :math:`\vs{W}` is a mapping

.. math:: f: \vs{V} \to \vs{W}

such that

.. math:: f(\alpha \vec{u} + \beta \vec{v}) = \alpha f(\vec{u}) + \beta f(\vec{v})

 :math:`\forall \alpha, \beta \in F` and
:math:`\vec{u}, \vec{v} \in \vs{V}`.

Examples of linear mappings are linear functions, and the linear
differential operator.

[Matrix of a linear mapping with respect to a given basis] Let
:math:`f:\vs{V} \to \vs{W}` be a mapping between two vector spaces
:math:`\vs{V}` and :math:`\vs{W}` over :math:`F`. Suppose
:math:`S_1: \vec{v}_1, \vec{v}_2,
  \dots, \vec{v}_n` is a basis for :math:`\vs{V}`, and
:math:`S_2: \vec{w}_1,
  \vec{w}_2, \cdots \vec{w}_m` is a basis for :math:`\vs{W}`. Then, for
:math:`j
  = 1,2, \dots, n`,

.. math::

   f(\vec{v}_j) = a_{1j} \vec{w}_1 + a_{2j} \vec{w}_2 + \cdots +
     a_{mj} \vec{w}_m

for scalars :math:`a_{ij}`, with :math:`i = 1,2, \dots, m`,
:math:`j=1,2, \dots, n`, then the matrix

.. math:: A = \qty[a_{ij}]

 is the matrix of :math:`f` with respect to the bases :math:`S_1` and
:math:`S_2`.

Let :math:`f:\vs{V} \to \vs{W}` and :math:`g:\vs{V}\to \vs{W}` be linear
mappings of vector spaces over :math:`F`, and let
:math:`\gamma , \delta \in
  F`. Then the mapping :math:`\gamma f + \delta g : \vs{V} \to \vs{W}`
defined by the rule

.. math::

   (\gamma f + \delta g)(\vec{v}) = \gamma f(\vec{v}) + \delta
     g(\vec{v}) \qquad (\vec{v} \in \vs{V})

is a linear mapping.

[Kernel of a linear mapping] Let :math:`f:\vs{V} \to \vs{W}` be a linear
mapping between the vecotr spaces :math:`\vs{V}` and :math:`\vs{W}` over
:math:`F`. The kernel of :math:`f` is the set of vectors from the domain
of :math:`f` which are mapped to the zero vector of the codomain
:math:`\vs{W}`. That is,

.. math::

   \ker(f) = \{ \vec{v}
     \in \vs{V} : f(\vec{v}) = \vec{0} \}

[Image of a linear mapping] Let :math:`f:\vs{v} \to \vs{W}` be a linear
mapping of vector spaces over :math:`F`. The image is

.. math::

   \img(f) = \{ f(\vec{v}) : \vec{v} \in \vs{V}
     \}

the set of vectors in the codomain, :math:`\vs{W}`, which are mapped to
by at least one vector from :math:`\vs{V}`.

Let :math:`f: \vs{V} \to \vs{W}` be a linear mapping of vector spaces
over :math:`F`, then

-  :math:`\ker(f)` is a subspace of :math:`\vs{V}`.

-  :math:`\img(f)` is a subspace of :math:`\vs{W}`.

Let :math:`f: \vs{V} \to \vs{W}` be a linear mapping of vector spaces
then,

#. :math:`f` is injective iff :math:`\ker(f) = \{ \emptyset \}`

#. :math:`f` is surjective iff :math:`\img(f) = \vs{W}`

#. :math:`f` is bijective iff :math:`\ker(f) = \{ \emptyset \}` and
   :math:`\img(f) = \vs{W}`

| [Rank and Nullity] Let :math:`f: \vs{V} \to \vs{W}` be a linear
  mapping of vector spaces over :math:`F`.
| The rank of :math:`f`, denoted :math:`\rank(f)` is defined

  .. math::

     \rank(f) =
       \dim(\img(f))

  and the nullity of :math:`f` is denoted :math:`\nullity(n)`, and is
  defined

  .. math:: \nullity(f) = \dim(\ker(f))

Let :math:`f: \vs{V} \to \vs{W}` be a linear mapping between finite
dimensional vector spaces over :math:`F`, then

#. :math:`f` is injective iff :math:`\nullity(f)=0`

#. :math:`f` is surjective iff :math:`\rank(f) = \dim(\vs{W})`

#. :math:`f` is bijective iff :math:`\nullity(f) = 0` and
   :math:`\rank(f) =
       \dim(\vs{W})`

[Rank-nullity Theorem] Let :math:`f: \vs{V} \to \vs{W}` be a linear
mapping between vector spaces over :math:`F`, where :math:`\vs{V}` is
finite-dimensional, then

.. math:: \dim(\vs{V}) = \rank(f) + \nullity(f)

Let :math:` \vec{y} = A \vec{x}` be a representation of a vector with
respect to a basis :math:`\vec{v}^{\prime}`, and
:math:`\vec{z} = B \vec{x}` be a represetation of the vector with
respect to a basis :math:`\vec{w}^{\prime}` The matrix of a linear
mapping :math:`f` with respect to the bases :math:`\vec{v}^{\prime}` and
:math:`\vec{w}^{\prime}` will be :math:`B^{-1} F A` for :math:`F` the
matrix of :math:`f`.

| Suppose :math:`\vs{U}, \vs{V}, \vs{W}` are finite dimensional vector
  spaces, and that :math:`f:\vs{U} \to \vs{W}` and
  :math:`g:\vs{V} \to \vs{W}` are linear mappings. Suppose
  :math:`\vec{u}_1, \dots, \vec{u}_m`, :math:`\vec{v}_1,
    \dots, \vec{v}_n`, and :math:`\vec{w}_1, \dots, \vec{w}_n` are bases
  of each vector space. Let :math:`F, G` respectively represent the
  matrices of :math:`f, g`.
| Then the composition :math:`g \circ f: \vs{U} \to \vs{W}` with respect
  to these bases is :math:`GF`.

[Row Rank] Let :math:`F` be a field, and :math:`A \in M_{m \times n}(F)`
be an :math:`m \times n` matrix over :math:`F`. The row rank of
:math:`A` is the number of non-zero rows in the reduced echelon matrix
row equivalent of :math:`A`.

[Column Rank] Let :math:`F` be a field, and
:math:`A \in M_{m \times n}(F)` be an :math:`m \times n` matrix over
:math:`F`. The column rank of :math:`A` is the number of non-zero
columns in the reduced echelon matrix column equivalent of :math:`A`.

For any :math:`m \times n` matrix, :math:`A`, the row rank and the
column rank are equal.

[Rank of a Matrix] The rank of a matrix, :math:`A`, is

.. math::

   \rank(A) = \rank(f) =
     \dim(\img(f))

Let :math:`A` be a complex :math:`m \times n` matrix, and let
:math:`\lambda \in
  \mathbb{C}` be an eigenvalue of :math:`A`. Then

.. math::

   S = \{ \vec{x} \in \mathbb{C}^n : A \vec{x} = \lambda \vec{x}
     \}

is a subspace of :math:`\mathbb{C}^n`.

[Eigenspace] Let :math:`A` be an :math:`n \times n` complex matrix, and
let :math:`\lambda \in
  \mathbb{C}` be an eigenvalue of :math:`A`. Then the
:math:`\lambda`-eigenspace of :math:`A` is

.. math::

   \Eig_A(\lambda) = \{ \vec{x} \in \mathbb{C}^n : A
     \vec{x} = \lambda \vec{x} \}

Let :math:`A` be an :math:`n \times n` complex matrix, and let
:math:`\lambda \in
  \mathbb{C}` be an eigenvalue of :math:`A`. The geometric multiplicity
of :math:`\lambda` is :math:`\dim \Eig_A(\lambda)`, and the dimension of
the :math:`\lambda`-eigenspace of :math:`A`.

The geometric multiplicity of an eigenvalue :math:`\lambda` is less than
or equal to the algebraic multiplicity of :math:`\lambda` in the
characteristic polynomial of :math:`A`.

Let :math:`A` be an :math:`n \times n` matrix over :math:`\mathbb{C}`.
Suppose :math:`\lambda_1, \dots, \lambda_k` are distinct eigenvalues of
:math:`A`, with associated eigenvectors
:math:`\vec{v}_1, \dots, \vec{v}_k`. Then,

-  The eigenvectors are linearly independent.

-  The sum of the eigenspaces :math:`\Eig_A(\lambda_1) + \cdots +
       \Eig_A(\lambda_k)` is a direct sum, i.e. 

   .. math::

      \Eig_A(\lambda_1) + \cdots + \Eig_A(\lambda_k) \equiv
          \Eig_A(\lambda_1) \oplus \cdots \oplus \Eig_A(\lambda_k)

Lagrange’s equations for oscillating systems
============================================

Equations of motion in generalised coordinates, :math:`q_i`, can be
expressed in terms of the Lagrangian, :math:`{\cal L}`, of the system.
Each generalised coordinate has an associated generalised force,
:math:`\pdv{{\cal L}}{q_i}`, and a generalised momentum,
:math:`\dot{q} =
  \pdv{q_i}{t}`. This allows the equations of motion of the system to be
expressed as

.. math:: \dv{t} \qty( \pdv{{\cal L}}{\dot{q}_i} ) = \pdv{{\cal L}}{q_i}

 these can be treated as a matrix formulation. In an oscillating system
the kinetic energy is quadratic with respect to the generalised momenta,
and potential is quadratic with respect to the generalised coordinates.
We thus have,

.. math::

   {\cal L} = \half m \dot{q}^{\rm T} T \dot{q} - \half k q^{\rm T}
     V q

 with :math:`T` and :math:`V` being matrices for kinetic and potential
energies respectively.

| *The characteristic frequencies of a system of springs.*

=[thick,decorate,decoration=zigzag,pre length=0.1cm,post
length=0.1cm,segment length=5]

[node distance=2cm] (wall) ;

(mass1) :math:`m`; (mass2) :math:`m`;

(wall2) ;

(wall) – (mass1) node [midway, above] :math:`k`; (mass1) – (mass2) node
[midway, above] :math:`k`; (mass2) – (wall2) node [midway, above]
:math:`k`;

; ;

| 
| Here :math:`x` and :math:`y` are generalised coordinates for the
  system. The kinetic energy is

  .. math:: T = \half m \qty( \dot{x}^2 + \dot{y}^2 )

  and the potential is

  .. math::

     V = \half k x^2 + \half k y^2 + \half k (x-y)^2 = \half k
         \qty(2 x^2 + 2y^2 - 2xy )

   In matrix form this is

  .. math::

     \begin{aligned}
           T &= \half m
           \begin{pmatrix}
             \dot{x} & \dot{y}
           \end{pmatrix}
           \begin{pmatrix}
             1 & 0 \\ 0 & 1
           \end{pmatrix}
           \begin{pmatrix}
             \dot{x} \\ \dot{y}
           \end{pmatrix} \\
           V &= \half k
           \begin{pmatrix}
             x & y
           \end{pmatrix}
           \begin{pmatrix}
             2 & -1 \\ -1 & 2
           \end{pmatrix}
           \begin{pmatrix}
             x \\ y
           \end{pmatrix} \\
         \end{aligned}

   This can be solved by diagonalising the matrix

  .. math::

     \begin{aligned}
       \begin{pmatrix}
         2 & -1 \\ -1 & 2
       \end{pmatrix}\end{aligned}

   In order to do this we find the eigenvectors of :math:`V`; the
  characteristic equation is

  .. math::

     \begin{aligned}
       \qty|
       \begin{matrix}
         2 - \mu & -1 \\ -1 & 2 - \mu
       \end{matrix} | &= 0 \\
       (2 - \mu)(2-\mu)-1 &=0 \\
     \mu^2 - 4 \mu + 3 &=0 \\
     (\mu - 1)(\mu - 3) &= 0 \\
     \mu &= 1 \quad \text{ or } \quad 3\end{aligned}

   We have,

  .. math::

     \begin{aligned}
       \begin{pmatrix} x \\ y \end{pmatrix} =C \begin{pmatrix} x^{\prime}
         \\ y^{\prime}\end{pmatrix}\end{aligned}

   a change of variables gives

  .. math::

     \begin{aligned}
       D = \begin{pmatrix} 1 & 0 \\ 0 & 3 \end{pmatrix}\end{aligned}

   for :math:`C^{-1}M C = D`, where

  .. math:: V = \half k^{\prime} \qty( x^{\prime 2} + 3 y^{\prime 2} )

   :math:`\dot{x}` and :math:`\dot{y}` transform in the same way as
  :math:`x` and :math:`y`, so we have :math:`T=I`, so

  .. math:: C^{-1} T C = C^{-1} I C = C^{-1} C = I

   is unchanged, and so

  .. math::

     T
     = \half m^{\prime} \qty( \dot{x}^{\prime 2} + \dot{y}^{\prime 2} )

   and

  .. math:: {\cal L} = T - V = \half m^{\prime} \qty( \dot{x}^{\prime 2} + y^{\prime 2} ) - \half k^{\prime} \qty( x^{\prime 2} + 3 y^{\prime 2})

| The two Lagrange equations are uncoupled (there are no :math:`xy`
  cross terms), so they can be solved seperately,

  .. math::

     \begin{aligned}
       \dv{t} \qty( \pdv{{\cal L}}{\dot{x}^{\prime}} ) - \pdv{{\cal L}}{x^{\prime}} &= 0 \\
     \dv{t} \qty( \half m \cdot 2 \dot{x}^{\prime} ) - \qty( - \half k \cdot 2 x^{\prime} ) &= 0 \\
     m \ddot{x}^{\prime} + k x^{\prime} &= 0 \\
     x^{\prime} &= A \sin(\omega_x t + \alpha) \\
     \omega_x &= \sqrt{\frac{k}{m}}\end{aligned}

  .. math::

     \begin{aligned}
       \dv{t} \qty( \pdv{{\cal L}}{\dot{y}^{\prime}} ) - \pdv{{\cal L}}{y^{\prime}} &= 0 \\
     \dv{t} \qty( \half m \cdot 2 \dot{y}^{\prime} ) - \qty( - \half k \cdot 6 y^{\prime} ) &= 0 \\
     m \ddot{y}^{\prime} + k \cdot 3y{\prime} &= 0 \\
     x^{\prime} &= B \sin(\omega_y t + \beta) \\
     \omega_y &= \sqrt{\frac{3k}{m}}\end{aligned}

   These normal modes then correspond to,
| (:math:`\mu=1`),

  .. math::

     \begin{aligned}
       \begin{pmatrix}    2 & -1 \\ -1 & 2  \end{pmatrix}
       \begin{pmatrix} x \\ y \end{pmatrix}
       &= \mu
       \begin{pmatrix} x \\ y \end{pmatrix} 
       =
       \begin{pmatrix} x \\ y \end{pmatrix} \\
       2x - y &= x \\
       y &= x\end{aligned}

   (:math:`\mu=3`),

  .. math::

     \begin{aligned}
       \begin{pmatrix}2 & -1 \\ -1 & 2 \end{pmatrix}
       \begin{pmatrix}  x \\ y         \end{pmatrix}
       &= 3
       \begin{pmatrix} x \\ y \end{pmatrix} \\
       2x - y &= 3x \\
       y &= -x\end{aligned}
