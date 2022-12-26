Inner Product Spaces
--------------------
:math:`\def\vs#1{\mathsf{#1}}`      
In this section, let :math:`\vs{V}` denote a vector space over the field :math:`\mathbb{R}`, let :math:`\vec{u}, \vec{v},` and :math:`\vec{w}` be vectors from :math:`\vs{V}`, and :math:`a, b, c,` and :math:`d` be scalars from the field :math:`\mathbb{R}`.

.. prf:definition:: Real inner product

		    Suppose to each pair of vectors :math:`\vec{u},\vec{v} \in \vs{V}` there is assigned a real number, denoted :math:`\langle \vec{u}, \vec{v}    \rangle`, which is called the real inner product on :math:`\vs{V}` if it satisfies the axioms

		    .. prf:axiom:: Linearity

				   .. math::

				      \langle a \vec{u}_1 + b \vec{u}_2 , \vec{v} \rangle = a \langle \vec{u}_1, v \rangle + b \langle \vec{u}_2, \vec{v} \rangle

		    .. prf:axiom:: Symmetry

				   .. math::

				      \langle \vec{u}, \vec{v} \rangle = \langle \vec{v}, \vec{u} \rangle

		    .. prf:axiom:: Positive-definiteness

				   .. math::

				      \langle \vec{u}, \vec{u} \rangle \geq 0 \text{ and } \langle \vec{u}, \vec{u} \rangle = 0 \text{ iff } \vec{u} = 0.

.. prf:definition:: Real Inner Product Space

		    A vector space, :math:`\vs{V}` on which a real inner product is defined is called a real inner product space.

.. prf:definition:: Vector norm
		    
		    The third axiom of the inner product requires that it always be positive.
		    This allows the definition of the norm,

		    .. math:: ||\vec{u}|| = \sqrt{ \langle \vec{u}, \vec{u} \rangle }

		    which is a measure of the length of the vector.

There are numerous examples of inner product spaces, from Euclidean :math:`n`-spaces (perhaps the most day-to-day example), function and polynomial space, matrix space, and Hilbert space.

.. prf:definition:: Cauchy-Schwarz Inequality

		    For any vectors :math:`\vec{u}` and :math:`\vec{v}` in an inner product space :math:`\vs{V}`,

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
