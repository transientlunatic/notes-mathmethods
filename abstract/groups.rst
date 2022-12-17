Group Theory
============

Basic Concepts
--------------

.. prf:definition:: Group
   :label: def:group
		    A group is an abstract mathematical entity which is composed of a set, :math:`G`, with an associated binary operation, :math:`*`.
		    In order to be a group, the pair :math:`(G, *)` must satisfy the follwing axioms,

   .. prf:axiom:: Closure
      :label: ax:group:closure
	      
	      For all :math:`a,b \in G`, :math:`a*b \in G`.

   .. prf:axiom:: Assosciativity
      :label: ax:group:assosciativity
	      
	      For all :math:`a,b,c, \in G`, :math:`(a*b)*c = a*(b*c)`. [itm:groupassoc]

   .. prf:axiom:: Identity
      :label: ax:group:identity
	      
	      There exists :math:`e \in G`, such that, for every :math:`a \in G`, :math:`a*e = e*a = a` holds.

   .. prf:axiom:: Inverse
      :label: ax:group:inverse
	      
	      For each :math:`a \in G` there exists a :math:`b \in G` such that :math:`a*b = b*a = e`.

.. prf:definition:: Group Order

		    The order of a group is the number of elements it contains.
		    If the group has finite order the group is described as a finite group; if it has an infinite number of elements it is an infinite group.

.. prf:example:: A Clock Face
		 
		 The hours on a clock represent a group, with a set :math:`H =   \{1,2,3,4,5,6,7,8,9,10,11,12\}`,
		 and an operation, addition :math:`\mod 12`.
		 The order of this group is 12, as it contains 12 elements.

.. prf:definition:: Homomorphism
		    
		    Given two groups, :math:`(G,*)` and :math:`(H, \cdot)`, a group homomorphism from :math:`(G,*)` to :math:`(H, \cdot)` is a function :math:`h|G \to H`, such that, for all :math:`u` and :math:`v` in :math:`G` it holds

		    .. math:: h(u * v) = h(u)\cdot h(v)

.. prf:definition:: Isomophism

		    A group isomorphism is a function between two groups which sets up a bijection between the elements of the groups in a way which respects the given group operations.
		    
Given two groups, :math:`(G,*)` and :math:`(H, \cdot)`, a group   isomorphism from :math:`(G,*)` to :math:`(H,\cdot)` is a bijective group homomorphism from :math:`G` to :math:`H`, that is, an isomorphism is a bijective function :math:`f : G \to H`, such that, for all :math:`u,v \in G`, it holds

  .. math::

     f(u*v) = f(u) \cdot
       f(v)

  If such a function exists we can write

  .. math:: (G,*) \cong (H,\cdot)

The group of real numbers under addition, and the group of real numbers
under multiplication are isomorphic under the bijection

.. math:: f(x) = e^x

[Abelian Group] A group, :math:`(G,*)` is called Abelian, if, in
addition to the axioms for a group, it also satisfies a commutative
property;

5. For all :math:`a,b \in G`, :math:`a*b = b*a`.

[Subgroup] A set :math:`H` which is a subset of :math:`G`, where
:math:`(G,*)` is a group, is called a subgroup iff :math:`(H,*)` is a
group, and

.. math:: H \le G

A subgroup, :math:`H`, is a *trivial* subgroup if the group, :math:`G`,
has only the identity element. Otherwise, if :math:`H \neq G` then
:math:`H` is a *proper* subgroup.

[Generating Set] The generating set of a group is a subset such that,
any element of the group can be expressed as the combination of finitely
many elements of the subset and their inverses.

[Cayley Diagram] Suppose that :math:`G` is a group, and :math:`S` is a
generating set for :math:`G`. They Cayley diagram,
:math:`\Gamma = \Gamma(G,S)` is a coloured directed graph with the
construction:

-  each element :math:`g\in G` is assigned a vertex. The vertex set
   :math:`V(\Gamma)` of :math:`\Gamma` is thus identified with
   :math:`G`.

-  each generator is assigned a colour, :math:`c_s`

-  For any :math:`g\in G, s \in S`, the vertices corresponding to the
   elements :math:`g` and :math:`gs` are joined by a directed edge of
   colour :math:`c_s`, and thus the edge set, :math:`E(\Gamma)` is
   composed of the pairs of form :math:`(g,gs)`, with :math:`s\in S`
   providing the colour.

For simplicity, the identity element is omitted, leaving a normal graph
without loops.

Finite Groups
-------------

Cyclic Groups
~~~~~~~~~~~~~

[Cyclic Group] A group, :math:`G`, is called cyclic if there exists an
element :math:`g` from :math:`G` such that every element in :math:`G`
can be obtained by repeatedly applying the group operation to :math:`g`
or its inverse.

The cyclic groups are an important simple group, and describe the
rotational symmetries of regular polyhedra.

Symmetric Groups
~~~~~~~~~~~~~~~~

[Symmetric Group] A symmetric group on a finite set, :math:`X` is a
group whose elements are all bijective functions from :math:`X` to
:math:`X`, and with the operation of function composition.

Dihedral Groups
~~~~~~~~~~~~~~~

[Dihedral Groups] A regular polygon with :math:`n` sides has :math:`2n`
symmetries; :math:`n` rotational, and :math:`n` reflective symmetries.
The rotations and reflections which preserve these symmetries compose
the elements of the dihedral group of order :math:`n`,
:math:`{\rm D}_n`.

Continuous Groups
-----------------

The continuous, or *Lie* groups, are groups which are composed of an
infinite set equipped with a binary operation. Lie groups are also
differentiable manifolds, with the property that the group operation is
compatible with the smooth structure of the manifold. They are named
after Sophus Lie, who laid the foundations for their study. Of
particular interest to physics are the *classical groups*, all of which
are closely related to symmetry in Euclidean spaces. There are seven
classical groups;

-  general linear—GL(\ :math:`n`)

-  special linear—SL(\ :math:`n`)

-  orthogonal—O(\ :math:`n`)

-  special orthogonal—SO(\ :math:`n`)

-  unitary—U(\ :math:`n`)

-  special unitary—SU(\ :math:`n`)

-  symplectic—Sp(\ :math:`n`)

GL(\ :math:`n`)—The General Linear Group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:math:`{\rm GL}(n)`, *The General linear group of degree :math:`n`*, are
the set of :math:`n\times n` invertible matrices, equipped with the
operation of matrix multiplication.

SU(\ :math:`n`)—The Special Unitary Group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| :math:`{\rm SU}(n)`, the *Special unitary group of degree :math:`n`*,
  are composed of the set of :math:`n\times n` unitary (i.e.
  :math:`UU* = U*U = I`) matrices with determinant 1, equipped with the
  operation of matrix multiplication.
| These are important in physics, as they do not affect the norm of the
  vector quantity on which they operate.

SU(2)
^^^^^

The generators of SU(2) are the Pauli matrices,

.. math::

   \begin{matrix}
       \sigma_1 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} &
       \sigma_2 = \begin{pmatrix}  0 & -i \\ i & 0 \end{pmatrix} &
       \sigma_3 = \begin{pmatrix}  1 & 0 \\ 0 & -1 \end{pmatrix}
     \end{matrix}

 These matrices act on the *spinors*,

.. math::

   \begin{matrix}
       u = \begin{pmatrix} 1 \\ 0 \end{pmatrix} &
       d = \begin{pmatrix} 0 \\ 1 \end{pmatrix}
     \end{matrix}

 which represent the spin up and spin down states. Then, the quantum
mechanical spin operator can be related to these via

.. math::

   \label{eq:spinoperator}
     \hat{S}_i = \frac{\hbar}{2} \sigma_i

SU(3)
^^^^^

The generators of SU(3) are the *Gell-Mann* matrices,
:math:`\lambda_{1,\dots,8}`.

.. math::

   \begin{matrix}
       \lambda_1 = \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 0  \end{pmatrix} &
       \lambda_2 = \begin{pmatrix} 0 & -i &0 \\ i & 0 & 0 \\ 0 & 0 & 0  \end{pmatrix} \\
       \lambda_3 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 0 \end{pmatrix} &
       \lambda_4 = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 0  \end{pmatrix} \\
       \lambda_5 = \begin{pmatrix} 0 & 0 &-i \\ 0 & 0 & 0 \\ i & 0 & 0  \end{pmatrix} &
       \lambda_6 = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0  \end{pmatrix} \\
       \lambda_7 = \begin{pmatrix} 0 & 0 & 0 \\0 & 0 & -i \\ 0 & i & 0  \end{pmatrix} &
       \lambda_8 = \frac{1}{\sqrt{3}} \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & -2 \end{pmatrix}
     \end{matrix}

 These obey the relations

.. math::

   \label{eq:gellmanncommutator}
     [T_a , T_b ] = i f_{abc} T_c

.. math::

   \label{eq:gellmannanticomm}
     \{T_a, T_b \} = \frac{1}{3} \delta_{ab} + d_{abc} T_c

| where :math:`T_a = \frac{\lambda_a}{2}`, and :math:`f_{abc}, d_{abc}`
  are the structure constant tensors.
| The Pauli matrices act on the spinors

  .. math::

     \begin{matrix}
         u = \begin{pmatrix}  1 \\ 0  \\ 0  \end{pmatrix} &
         d = \begin{pmatrix}  0 \\ 1 \\ 0   \end{pmatrix} &
         s = \begin{pmatrix}  0 \\ 0 \\ 1   \end{pmatrix}
       \end{matrix}

   representing the up, down, and strange states, and the isospin
  raising and lowering operators can be defined,

  .. math::

     \label{eq:isospinraise}
       \hat{I}_{\pm} = \half (\lambda_1 \pm i \lambda_2)

   and the isospin projection operator, :math:`I_3`,

  .. math::

     \label{eq:isospinprojoperator}
       \hat{I}_3 = \half \lambda_3

   Similarly, the operators

.. math::

   \label{eq:ushift}
       \hat{U}_{\pm} = \half (\lambda_6 \pm i \lambda_7)

.. math::

   \label{eq:vshift}
       \hat{V}_{\pm} = \half ( \lambda_4 \mp i \lambda_5)

Both of these, combined with their respective projection operators,
:math:`\hat{U}_3` and :math:`\hat{V}_3`,

.. math::

   \label{eq:uproj}
       \hat{U}_3 = - \frac{1}{4} \lambda_3 + \frac{\sqrt{3}}{4} \lambda_8

.. math::

   \label{eq:vproj}
       \hat{V}_3 = - \frac{1}{4} \lambda_3 - \frac{\sqrt{3}}{4} \lambda_8

define two different SU(2) subgroup representations of SU(3).
