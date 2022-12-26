Multilinear Algebra and Tensors
===============================

:math:`\require{physics}\def\vs#1{\mathsf{#1}}`

.. prf:definition:: Covector
		    
		    A covector (linear form, one-form, or linear functional) is a linear map from a vector space to its field of scalars.

.. prf:definition:: Dual vector space
		    
		    The set of all covectors which map a vector space :math:`\vs{V}` to its field :math:`F` form a vector space over :math:`F`, which is called the dual space of :math:`\vs{V}`, and denoted :math:`\vs{V^{*}}`.

Suppose that vectors in the real vector space :math:`\mathbb{R}^n` are represented as column matrices,

.. math::

   \vec{x} = 
   \begin{pmatrix}
     x_1 \\ x_2 \\ \vdots \\ x_n 
   \end{pmatrix}

Then any linear functional can be written in these coordinates as the sum

.. math:: f(\vec{x}) = a_1 \vec{x}_1 + \cdots + a_n \vec{x}_n

can also be represented as a row matrix,

.. math::

   f =
   \begin{pmatrix}
     a_1, & a_2, & \cdots, & a_n 
   \end{pmatrix}

.. prf:definition:: Contravariant tensor
   
		    Suppose :math:`n` quantities in a basis :math:`\vec{x}^{1}, \dots, \vec{x}^n` are related to another :math:`n` quantities, :math:`A^{\prime}^1, \dots,
  A^{\prime}^n` in a coordinate system :math:`x^{\prime}^1, \dots, x^{\prime}^n` by a set of transformations 

		    .. math:: A^{\prime}^p = \pdv{x^{\prime p}}{x^{\prime q}} A^q

		    Then :math:`A^1, \dots, A^n` are the components of a first rank contravariant tensor.

.. prf:definition:: Covariant tensor
		    
		    Suppose :math:`n` quantities in a basis :math:`\vec{x}_{1}, \dots, \vec{x}_n` are related to another :math:`n` quantities, :math:`A^{\prime}_1, \dots,
  A^{\prime}_n` in a coordinate system :math:`x^{\prime}_1, \dots, x^{\prime}_n` by a set of transformations

		    .. math:: A^{\prime}_p = \pdv{x^{\prime p}}{x^{\prime q}} A_q

		    Then :math:`A_1, \dots, A_n` are the components of a first rank covariant tensor.

		    An intuitive introduction to tensors is via *dyads*, which were historically the precursors of tensors.

.. prf:definition:: Dyadic product
		    
		    Consider two vectors, :math:`\vec{u}, \vec{v} \in \vs{V}`, then their dyadic product, denoted :math:`\dyad{uv}`, can be represented by the sum

		    .. math::

			      \begin{aligned}
				  \label{eq:dyadicproduct}
				     \dyad{ab} =           & a_1 b_1 \dyad{ii} + a_2 b_1 \dyad{ij} + a_1 b_3 \dyad{ik} \\ 
				     +                     & a_2 b_1 \dyad{ji} + a_2 b_2 \dyad{jj} + a_2 b_3 \dyad{jk} \\ 
				     +                     & a_3 b_1 \dyad{ki} + a_3 b_2 \dyad{kj} + a_3 b_3 \dyad{kk}
				\end{aligned}

				
		    with the standard basis Dyads being of the form

		    .. math::

		       \begin{matrix}
		       \dyad{ii} =\begin{pmatrix} 1 & 0 & 0                                                     \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} & 
		       \dyad{ij} =\begin{pmatrix} 0 & 1 & 0                                                     \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} & 
		       \dyad{ik} =\begin{pmatrix} 0 & 0 & 1                                                     \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} \\
		       \dyad{ji} =\begin{pmatrix} 0 & 0 & 0                                                     \\ 1 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} & 
		       \dyad{jj} =\begin{pmatrix} 0 & 0 & 0                                                     \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{pmatrix} & 
		       \dyad{jk} =\begin{pmatrix} 0 & 0 & 0                                                     \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix} \\
		       \dyad{ki} =\begin{pmatrix} 0 & 0 & 0                                                     \\ 0 & 0 & 0 \\ 1 & 0 & 0 \end{pmatrix} & 
		       \dyad{kj} =\begin{pmatrix} 0 & 0 & 0                                                     \\ 0 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix} & 
		       \dyad{kk} =\begin{pmatrix} 0 & 0 & 0                                                     \\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}
		       \end{matrix}


In terms of dyads, both the outer product, :math:`\vec{a} \vec{b}^{\rm T}` and the tensor product, :math:`\vec{a} \otimes \vec{b}` are the same quantity.

.. prf:definition:: Tensor
 
		    A tensor of type :math:`(n, m-n)` is an assignment of a multi-dimensional array,
		    
		    .. math:: T_{i_{n+1} \cdots i_m}^{i_1 \cdots i_n} \qty[\vec{f}]

		    to each basis :math:`\vec{f} = (\vec{e}_1, \dots \vec{e}_n)`, such that, if a change of basis is applied,

		    .. math:: \vec{f} \to R \vec{f} = (R^i_1 \vec{e}_1, \dots, R^i_n \vec{e}_n )

		    then the array obeys the transform law

		    .. math:: T_{i_{n+1} \cdots i_m}^{i_1 \cdots i_n} \qty[ \vec{f} \cdot R] = (R^{-1})^{i_1}_{j_1}  R^{j_{n+1}}_{i_{n+1}}  \cdots R^{j_m}_{i_m} T_{j_{n+1}, \dots, j_m}^{j_1 \dots j_n} \qty[\vec{f}]

.. prf:example:: The Stress Tensor
			      
		 The Stress Tensor is a quantity which involves forces acting on a three-dimensional object.
		 There are three forces, one acting on a plane perpendicular to each plane in the object, and each force having three spatial components.
		 The components of the force on the plane for which :math:`x` is the normal are :math:`f_{xx}, f_{xy}, f_{xz}`, so the overall force on the body is

		 .. math::

		    \begin{pmatrix}
		    f_{xx} & f_{xy} & f_{xz} \\ f_{yx} & f_{yy} & f_{yz} \\ f_{zx} & f_{zy} & f_{zz}
		    \end{pmatrix}

		 and converting to stress, by dividing through by the area of each plane,

		 .. math::

		    \begin{pmatrix}
		    \sigma_{xx} & \sigma_{xy} & \sigma_{xz} \\ \sigma_{yx} & \sigma_{yy} & \sigma_{yz} \\ \sigma_{zx} & \sigma_{zy} & \sigma_{zz}
		    \end{pmatrix}

		 The elements of the leading diagonal are three orthogonal normal, or compressive stresses.
		 The six off-diagonal elements are orthogonal sheer stresses, so an alternative notation of the tensor is

		 .. math::

		    \begin{pmatrix}
		    \sigma_x & \tau_{xy} & \tau_{xz} \\
		    \tau_{yx} & \sigma_y & \tau_{yz} \\
		    \tau_{xz} & \tau_{yz} & \sigma_z
		    \end{pmatrix}

Tensor Rotations
================

Rotation tensors are an important quantity in physics, allowing the
transformation between coordinate systems. Let :math:`(x,y,z)` be a
coordinate system, and a second coordinate system, :math:`(x^{\prime},
y^{\prime}, z^{\prime})` is rotated relative to it. The rotation can be
described by a tensor of the form

.. math::

   \label{eq:1}
     \begin{pmatrix}
       x^{\prime} \\ y^{\prime} \\ z^{\prime}
     \end{pmatrix} = 
     \begin{pmatrix}
       \cos(\theta_{xx^{\prime}}) & \cos(\theta_{yx^{\prime}}) & \cos(\theta_{zx^{\prime}})\\
       \cos(\theta_{xy^{\prime}}) & \cos(\theta_{yy^{\prime}}) & \cos(\theta_{zy^{\prime}})\\
       \cos(\theta_{xz^{\prime}}) & \cos(\theta_{yz^{\prime}}) & \cos(\theta_{zz^{\prime}})
     \end{pmatrix}
     \begin{pmatrix}
       x \\ y \\ z
     \end{pmatrix}

Using the summation convention, and letting the rotation matrix from
equation ([eq:1]) be :math:`a_{ij}`, we can rewrite the rotation
operation as

.. math:: x_j^{\prime} = a_{ij} x_j

where :math:`a_{ij} = \hat{e}_i^{\prime}
\cdot \hat{e}_j`. The rotation is orthonormal, so
:math:`A^{-1} = A^{\rm T}`, and so

.. math:: x_i = a_{ji} x_j^{\prime}

Extensions of Rotations to rank-2 Tensors
=========================================

A tensor can be produced from the outer product of two vectors,

.. prf:definition:: Vector outer product

		    Let :math:`\vec{u}` and :math:`\vec{v}` be vectors, then

		    .. math:: \vec{u} \otimes \vec{v} = \vec{u} \vec{v}^{\rm T}

		    is the outer product of the two vectors, and is a rank-2 tensor.

Now, suppose the vectors :math:`\vec{u}`, and :math:`\vec{v}` are rotated to become

.. math::

   \begin{aligned}
     u_i^{\prime} &= a_{ik} u_k \\
     v_j^{\prime} &= a_{jl} v_l
   \end{aligned}

and we construct a tensor by taking the outer product, :math:`t^{\prime} = \vec{u}^{\prime} \otimes \vec{v}^{\prime}` then

.. math::

   t^{\prime} = u_i^{\prime} v_j^{\prime} = (a_{ik} u_k)(a_{jl} v_l) = a_{ik} a_{jl} u_k v_l = a_{ik} a_{jl} t_{kl}

and the inverse relation is then

.. math:: t_{ij} = a_{kl} a_{lj} t^{\prime}_{kl}

This principle can be continued for higher and higher order tensors.

Physical examples
-----------------

.. _moment-of-inertia-tensor:

.. prf:example:: The moment of intertia tensor
   :label: moment-of-inertia-tensor
	   
		 Rotational motion of a rigid body depends both on the axis and the moment of inertia with respect to the axis, with the moment of inertia, which, for a body composed of masses, :math:`\set{m_i}` which are at a distance :math:`r_i` from the axis can be described

		 .. math::

		    I = \sum_i m_i r_i^2 = \int \rho r^2 \dd{V}

		 In order to have a means of calculating the moment of inertia along any axis we need a tensor.
		 In order to find the form of this tensor we turn to angular momentum.
		 The total angular momentum, :math:`\vec{J}`, of a body is the sum of all the angular momenta of its constituent parts,

		 .. math::

		    \vec{J} = \sum_i \vec{L}_i = \sum_i \vec{r}_i \times m_i \vec{v}_i = \sum_i m_i \qty[ \vec{r}_i \times (\omega \times \vec{r}_i)]

		 We assume the body to be rigid, so that :math:`\vec{\omega}` is constant for all its constituent particles.
		 Then

		 .. math::

		     \begin{aligned}
		     \vec{J}                        & = \sum_i m_i \qty[ (\vec{r} \cdot \vec{r}) \vec{\omega} - (\vec{r}_i \cdot \vec{\omega} ) \vec{r}_i] \\
                                                    & = \sum_i m_i 
			\begin{pmatrix}
			  \omega_x (y_i^2 + z_i^2 ) & - \omega_y x_i y_i       & - \omega_z x_i z_i                                                        \\
			  - \omega_x y_i x_i        & \omega_y (z_i^2 + x_i^2) & - \omega_z y_i z_i                                                        \\
			  - \omega_x z_i x_i        & - \omega_y z_i y_i       & \omega_z (x_i^2 + y_i^2)
			\end{pmatrix}                                                                                                                      \\
                                                    & =
                        \begin{pmatrix}
                          \sum_i m_i  (y_i^2 + z_i^2)  & - \sum_i m_i  x_i y_i         & - \sum_i m_i  x_i z_i \\
		        - \sum_i m_i  y_i x_i          &   \sum_i m_i  (z_i^2 + x_i^2) & - \sum_i m_i  y_i z_i \\
		        - \sum_i m_i z_i x_i           & - \sum_i m_i  z_i y_i         &   \sum_i m_i  (x_i^2 + y_i^2)
		     \end{pmatrix}
		     \begin{pmatrix}
		       \omega_x    \\
                       \omega_y                             \\
		       \omega_z
		     \end{pmatrix}   \\ & = {\cal I} \vec{\omega}\end{aligned}

Hence

.. prf:definition:: Moment of intertia tensor

		    .. math::

		       {\cal I} =
		       \begin{pmatrix}
		          \sum_i m_i  (y_i^2 + z_i^2 ) & - \sum_i m_i  x_i y_i & - \sum_i m_i  x_i z_i \\
		        - \sum_i m_i  y_i x_i & \sum_i m_i  (z_i^2 + x_i^2) & - \sum_i m_i  y_i z_i \\
			- \sum_i m_i z_i x_i & - \sum_i m_i  z_i y_i & \sum_i m_i  (x_i^2 + y_i^2)
		       \end{pmatrix}

The on-diagonal components of the moment of inertia tensor are the moments of inertia, while the off-diagonal elements are the products of inertia.
We can find the three moments of inertia,

.. math::

   \begin{aligned}
     I_{xx} &= \sum m(y^2 + z^2)   = ma^2 \qty( 4 \times \frac{3}{16} )                        = \frac{3 ma^2}{4}\\
     I_{yy} &= \sum m( x^2 + z^2 ) = ma^2 \qty( 2 \times\frac{9}{16} + 2 \times \frac{1}{16} ) = \frac{5 ma^2}{4} \\
     I_{zz} &= \sum m(x^2 + y^2 )  = \frac{8 ma^2}{4}
   \end{aligned}

The products of inertia are straightforward, as :math:`z=0` causes :math:`I_{xy} = I_{yz} = 0`, so

.. math::

   \begin{aligned}
     I_{xy} &= - \sum m x y = - ma^2 \qty( 2 \times \frac{3}{4} \frac{\sqrt{3}}{4} - 2 \times \frac{1}{4} \frac{\sqrt{3}}{4} ) \\
            &= - \frac{\sqrt{3}m a^2}{4}
   \end{aligned}

So

.. math::

   {\cal I} = \frac{ma^2}{4}
   \begin{pmatrix}
             3  & - \sqrt{3} & 0 \\
     - \sqrt{3} & 5          & 0 \\
             0  & 0          & 8
   \end{pmatrix}

By diagonalising the matrix we can find the principle moments of inertia.
From the characteristic equation of :math:`{\cal I}`,

.. math::

   \begin{aligned}
     \chi_{{\cal I}}(\mu) &= \qty( (3-\mu)(5-\mu)-3 ) = 0 \\ &= (2-\mu)(6-\mu) = 0\end{aligned}

so :math:`\mu = \set{2,6,8}`. Thus

.. math::

   {\cal I} = \frac{ma^2}{4}
   \begin{pmatrix}
     2 & 0 & 0 \\ 0 & 6 & 0 \\ 0 & 0 & 8
   \end{pmatrix}

So the body’s principle moments of inertia are

.. math:: I_{\rm prin} = \set{ \half ma^2, \frac{3}{2} ma^2, 2 ma^2}

Finally, to find the principle axes we need the corresponding eigenvectors to the eigenvalues, so :math:`\mu=2`,

.. math::

   \begin{aligned}
     (3-2) x - \sqrt{3} y &= 0 \\
   y &= \frac{1}{\sqrt{3}} x\end{aligned}

:math:`\mu=8`,

.. math::

   \begin{aligned}
     (3-8)x - \sqrt{3} y &= 0 \\
   5x + \sqrt{3} y &= 0 \\
   y &= \frac{-5}{\sqrt{3}} x\end{aligned}

:math:`\mu=6`,

.. math::

   \begin{aligned}
     (3-6) x - \sqrt{3} y &= 0 \\
   y &= \frac{-3}{\sqrt{3}} x = - \sqrt{3} x\end{aligned}

The Parallel Axis Theorem
-------------------------

Let :math:`{\cal I}_G` be the inertia tensor with respect to the centre of mass, :math:`G` of a rigid body, and :math:`{\cal I}_O` be the tensor with respect to a different point :math:`O` in the same coordinate frame.
Let :math:`\vec{r} = GO`.
From the definition of the moment of inertia tensor,

.. math::

   {\cal I}_O = {\cal I}_G + M 
   \begin{pmatrix}
     r_y^2 + r_z^2 & -r_x r_y & - r_x r_z \\
   - r_y r_x & r_z^2 + r_x^2 & - r_y r_z \\
   - r_z r_x & - r_z r_y & r_x^2 + r_y^2
   \end{pmatrix}

which gives the parallel axis theorem.

.. _einstein-summation-convention:
Einstein Summation Convention
-----------------------------

Consider a three-dimensional vector space, :math:`\mathsf{V}`, over the field of real numbers, :math:`\mathbb{R}`.
Any point in the space can be described by an ordered set of three numbers, :math:`(x_1, x_2, x_3)`, known as coordinates, such that

.. math::

   \vec{A} = (x_1, x_2, x_3) \cdot
             \begin{pmatrix} \vec{e_1} \\ \vec {e_2} \\ \vec{e_3} \end{pmatrix}

where :math:`\vec{A}` is any vector in :math:`\mathsf{V}`, and :math:`\vec{e_1}`, :math:`\vec{e_2}`, and :math:`\vec{e_3}` constitute a basis for :math:`\mathsf{V}`.

This can be expressed in a more compact form by adopting the *Einstein summation convention*.
In this system the summation sign, :math:`\sum`, is omitted, and replaced with repeated indices, viz:

.. math:: \vec{A} = A_i \vec{e_i} = \sum_{i=1}^3 A_i\vec{e_i}

here :math:`i` is a repeated index, and so the summation over it is implicit.
This allows the definition of a number of vector calculus operations in a more compact way.
