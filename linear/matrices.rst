Matrices
========

.. prf:definition:: Matrix

		    A matrix, :math:`A` over a field :math:`K` is a rectangular, :math:`n \times m`, array of scalars, which is usually represented in the form

		    .. math::

		       A =
			   \begin{pmatrix}
			     a_{11} & a_{12} & \cdots & a_{1n} \\
			     a_{21} & a_{22} & \cdots & a_{2n} \\
			     \vdots & \vdots & \ddots & \vdots \\
			     a_{m1} & a_{m2} & \cdots & a_{mn}
			   \end{pmatrix}

Both the operations of addition and multiplication are defined for matrices.

.. prf:definition:: Main diagonal

		    The main diagonal of a matrix are the entries :math:`a_{ij}` where :math:`j=i`.

.. prf:definition:: Square Matrix

		    A matrix is called a square matrix if it is of shape :math:`(n \times n)`.

.. prf:definition:: Upper and Lower Triangular Matrices

		    If a square matrix has only zeros below every entry in the main diagonal it is an upper triangular matrix.
		    If the matrix has only zeros above every entry in the main diagonal it is lower triangular.

.. prf:definition:: Diagonal Matrix
		    
		    A matrix is called diagonal if all of the entries lying off the main diagonal are zero.
		    A diagonal matrix may also be written as

		    .. math:: \operatorname{diag}(a_{11}, a_{22}, \cdots, a_{nn})

It should be noted that a diagonal matrix is both upper and lower triangular.

.. prf:definition:: Matrix cofactors

		    The cofactors, :math:`A^{ij}` of an :math:`n \times n` matrix :math:`A` is the :math:`(n-1) \times (n-1)` matrix containing the elements of :math:`A` excluding those in the :math:`i^{\rm th}` row and the :math:`j^{\rm th}` column.

.. prf:definition:: Cofactor Matrix
		    
		    A cofactor matrix is a matrix whose elements are all cofactors, and has the form

		    .. math::

			  C = 
			  \begin{pmatrix}
			    C_{11} & C_{12} & \cdots & C_{1n} \\
			    C_{21} & C_{22} & \cdots & C_{2n} \\
			    \vdots & \vdots & \ddots & \vdots \\
			    C_{n1} & C_{n2} & \cdots & C_{nn}
			  \end{pmatrix}
			  

Matrix Operations
-----------------

.. prf:definition:: Matrix transpose

		    The transpose of a square matrix :math:`A` is defined

		    .. math:: \qty[\trans{A}]_{ij} = \qty[A]_{ji}

		    that is, the transpose of a matrix is the original matrix reflected about its main diagonal.

.. prf:definition::  Matrix Trace

		     The trace of a square matrix, :math:`A` is the sum of the elements in its main diagonal, ie.

		     .. math:: \trace(A) = \sum^n_{i=1} a_{ii}

		     where :math:`a_{ij}` are the elements of :math:`A`.

.. prf:definition:: Complex Conjugate

		    The complex conjugate, :math:`\conj(A)` of a matrix :math:`A` over :math:`\mathbb{C}` is the matrix in which every element is the complex conjugate of the corresponding element of :math:`A`.

		    .. math:: \qty[\conj(A)]_{ij} = \qty( \qty[A]_{ij} )^{*}

.. prf:definition:: Hermitian Conjugate

		    The hermitian conjugate, :math:`A^{\dagger}` of a matrix :math:`A` is the matrix

		    .. math:: A^{\dagger} = \conj(\trans{A}) = \trans{\conj(A)}

.. prf:definition:: Matrix Determinant
			      
		    Let :math:`A` be a square matrix, and :math:`a_{i,j}` be the elements of :math:`A`, then, the determinant of the matrix, denoted :math:`\det(A)` or :math:`|A|`, is defined 

		    .. math::

		       \det(A) = \sum_{i_1, i_2, \dots, i_n = 1}^n \epsilon_{i_1 \cdots i_n} a_{1,i_1} \cdots a_{n,i_n}

[Properties of the Determinant] For :math:`n \times n` matrices,
:math:`A,B`, a triangular matrix, :math:`D`, and scalar :math:`c`,

.. prf:property:: Determinant of the Identity Matrix
      
   :math:`\det(I_n) = 1`

.. prf:property:: Determinant of a Transposed Matrix
	 
   :math:`\det(A^{\rm T}) = \det(A)`

.. prf:property:: Determinant of the Inverse of a Matrix
	 
   :math:`\det(A^{-1}) = \det^{-1}(A)`

.. prf:property:: Determinant of the Product of Matrices
	 
   :math:`\det(AB) = \det(A) \det(B)`

.. prf:property:: Determinant of the Scalar Product of a Matrix
	 
   :math:`\det{cA} = c^n \det{A}`

.. prf:property:: Determinant of a Triangular Matrix
	 
   :math:`\det{D} = \prod_{i=1}^n d_{i,i}` (for :math:`d_{i,j} \in D`)

.. prf:observation:: Determinant of a triangular matrix

		  The determinant of any triangular matrix is the product of the entries on its main diagonal.

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

.. prf:definition:: Invertible Matrix
     
		    An :math:`n \times n` matrix :math:`A` is called invertible if there exists an :math:`n \times n` matrix :math:`B` such that

		    .. math:: AB = BA = I

		    with :math:`I` the identity matrix.

There are a number of techniques for identifying the inverse of a matrix, one of which is Cramer’s rule, and the other is Eigenvalue decomposition.

.. prf:definition:: Adjugate Matrix

		    The adjugate matrix is the transpose of the cofactor matrix.

.. prf:definition:: Cramer's Rule

		    Cramer’s rule is a process for inverting a square matrix.
		    Let :math:`A` be a square matrix, with :math:`\det(A) \neq 0`. 
		    Then

		    .. math:: A^{-1} = \frac{1}{|A|} \trans{C}

		    where :math:`\trans{C}` is the adjugate matrix of :math:`A`.
		    This process is highly inefficient for large matrices.


Atlas of Special Matrices
-------------------------

.. prf:definition:: Identity Matrix

		    The matrix :math:`I` is called the identity matrix and has the form

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
