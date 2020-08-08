Einstein Summation Convention
=============================

Consider a three-dimensional vector space, :math:`\mathsf{V}`, over the
field of real numbers, :math:`\mathbb{R}`. Any point in the space can be
described by an ordered set of three numbers, :math:`(x_1, x_2, x_3)`,
known as coordinates, such that

.. math::

   \vec{A} = (x_1, x_2, x_3) \cdot
   \begin{pmatrix} \vec{e_1} \\ \vec {e_2} \\ \vec{e_3}
   \end{pmatrix}

 where :math:`\vec{A}` is any vector in :math:`\mathsf{V}`, and
:math:`\vec{e_1}`, :math:`\vec
{e_2}`, and :math:`\vec{e_3}` constitute a basis for :math:`\mathsf{V}`.

This can be expressed in a more compact form by adopting the *Einstein
summation convention*. In this system the summation sign, :math:`\sum`,
is omitted, and replaced with repeated indices, viz.

.. math:: \vec{A} = A_i \vec{e_i} = \sum_{i=1}^3 A_i\vec{e_i}

here :math:`i` is a repeated index, and so the summation over it is
implicit. This allows the definition of a number of vector calculus
operations in a more compact way.

Operations
----------

Dot Product
~~~~~~~~~~~

.. math::

   \label{eq:dotprod}
     \vec{a} \cdot \vec{b} = a_\theta b_\theta

Total Differential
~~~~~~~~~~~~~~~~~~

.. math::

   \label{eq:totaldifferential}
     \dif{f} = \frac{\partial f}{\partial x_\theta} \dif{x_\theta}

Matrix Multiplication
~~~~~~~~~~~~~~~~~~~~~

.. math::

   \label{eq:matmult}
     a_{ij} = b_{i \theta} c_{\theta j}

Cross Product
~~~~~~~~~~~~~

.. math::

   \label{eq:crossprod1}
     [ \vec a \times \vec b]_i = \epsilon_{i \theta \phi} a_{\theta} b_{\phi}

.. math::

   \label{eq:crossprod2}
     \vec{a} \times \vec{b} = \epsilon_{i \theta \phi} a_{\theta} b_{\phi} \vec{e_{i}}

Here :math:`\epsilon_{i \theta \phi}` is the Levi-Civita tensor, and
takes values

.. math::

   \label{eq:levitcivita}
     \epsilon_{i \theta \phi} = \left\{ 
       \begin{array}{rl}
         0 & \text{if any indices are repeated.} \\
         1 & \text{if indices are a cyclic permutation of } (1,2,3). \\
         -1 & \text{if indices are a cyclic permutation of } (1,3,2). 
       \end{array}\right.

There is a simple relationship between this tensor and the Kronecker
delta,

.. math::

   \label{eq:deltalevi}
     \epsilon_{\theta j k } \epsilon_{\theta l m} = \delta_{jl} \delta_{k m} - \delta_{j m} \delta_{l k}

Del Operators
-------------

The gradient is now expressed:

.. math::

   \label{eq:grad}
     \nabla = \vec e_i \frac{\partial }{\partial x_i}

 The divergence:

.. math::

   \label{eq:divergence}
     \nabla \cdot \vec{A}(\vec{r}) = \frac{\partial A_i(\vec{r})}{\partial x_i}

 and the curl:

.. math::

   \label{eq:curl}
     \nabla \times \vec{A}(\vec{r}) = \epsilon_{ijk} \frac{\partial A_j(\vec{r})}{\partial x_i} \vec{e_k}

Consider

.. math:: \left[ \vec{a} \times ( \vec{b} \times \vec{c} ) \right]_m

 using the summation convention,

.. math::

   \begin{aligned}
    \left[ \vec{a} \times ( \vec{b} \times \vec{c} )
       \right]_m
       &= \epsilon_{m \alpha \beta} a_{\alpha} \epsilon_{\beta \gamma \delta} b_{\gamma} c_{\delta} \\
       &= \epsilon_{\beta m \alpha} \epsilon_{\beta \gamma \delta} a_{\alpha} b_{\gamma} c_{\delta} \\
       &= (\delta_{m \delta}\delta_{\alpha \delta} - \delta_{m \delta} \delta_{a \gamma}) a_{\alpha} b_{\gamma} c_{\delta}\\
       &=  (a_{\alpha}c_{\alpha}) b_m - (a_{\alpha}b_{\alpha}) c_m \\
       &= \left[ (\vec a \cdot \vec c) \vec b - (\vec a \cdot \vec b)
         \vec c \right]_{m}
     \end{aligned}

Note,

.. math:: \delta_{i\theta} a_{\theta} = a_i

.. math::

   \begin{aligned}
       \nabla \times ( \nabla \phi ) &= \epsilon_{m\alpha \beta} \frac{\partial }{\partial x_a} \frac{\partial \phi}{\partial x_{\beta}}\\
       &= 0
     \end{aligned}

This arises because the Levi-Civita tensor is anti-symmetric, but the
two partial derivatives are symmetric.

.. math::

   \begin{aligned}
       \vec A \cdot \vec B \times \vec C &= A_{\alpha}\epsilon_{\alpha \beta \gamma} B_{\beta} C_{\gamma} \\
       &= C_{\gamma} \epsilon_{\gamma \alpha \beta} A_{\alpha} B_{\beta} \\
       &= C_{\gamma} [\vec A \times \vec B]_{\gamma} \\
       &= C \cdot [ \vec A \times \vec B]
     \end{aligned}

Curvilinear coordinates
=======================

A curvilinear coordinate system is a coordinate system over a space in
which the coordinate lines may be curved, and are related to a Cartesian
coordinate system by a bijection. In physics, laws are independent of
reference frame and of coordinate system, which allows the use of the
most appropriate coordinate system for a specific situation—for example,
if a problem has spherical symmetry it is likely to be easiest to solve
in spherical polar coordinates.

Spherical Polar Coordinates
---------------------------

[!]

[!]0.45

(0,0) – (0,2.5); (0,0) – (-1, -1.5); (0,0) – (3,0);

(0,0) – (2,2); (2,2) – (2, -1); (0,0) – (2,-1) node [below,] :math:`r`;

(0,0.7) arc (45:0:0.7) node [yshift=8pt,above]:math:`\theta`; (.5, -.3)
arc (300:255:1) node [yshift=-2pt, below] :math:`\phi`;

[!]0.45 They are related to Cartesian coordinates by the
transformations:

.. math::

   \begin{aligned}
         x &= r \sin \theta \cos \phi \label{eq:sph1}\\
         y &= r \sin \theta \sin \phi \label{eq:sph2}\\
         z &= r \cos \theta \label{eq:sph3}
       \end{aligned}

Cylindrical Polar Coordinates
-----------------------------

[!]

[!]0.45

(0,0) – (0,2.5); (0,0) – (-1, -1.5); (0,0) – (3,0);

(0,2) – (2,1.5); (2,1.5) – (2, -1); (0,0) – (2,-1) node [below,]
:math:`r`; (-.1,0) – (-.1,2) node [left] :math:`z`; (.5, -.3) arc
(300:255:1) node [yshift=-2pt, below] :math:`\phi`;

[!]0.45 They are related to Cartesian coordinates by the
transformations:

.. math::

   \begin{aligned}
         x &= r \cos \theta \label{eq:cyl1}\\
         y &= r \sin \theta \label{eq:cyl2}\\
         z &= z \label{eq:cyl3}
       \end{aligned}

Unit vectors and scale factors
------------------------------

In any coordinate system there is a concept of distance, which is
independent of the choice of coordinate system. In Cartesian coordinates
this is

.. math::

   \dif{s}^2 = \dif{x}^2 + \dif{y}^2 + \dif{z}^2 = \dif{r}\cdot
   \dif{r}

where :math:`\dif{r}` is the inifinitessimal line element.

Consider a general coordinate system described by :math:`q_i`, related
to Cartesian coordinates via

.. math:: x_i = f_i (q_1, q_2, q_3)

As :math:`q_i` is changed the position vector :math:`\vec r` will move:

.. math:: \frac{\partial \vec r}{\partial q_i} = h_{q_i} \vec{e}_{q_i}

 The magnitude of :math:`\frac{\partial \vec r}{\partial q_i}` is the
scale factor, :math:`h_{q_i}`, and the basis vector is the unit vector
in the direction of :math:`\frac{\partial \vec r}{\partial q_i}`. We can
then define the infinitessimal line element,

.. math::

   \label{eq:infinitessimalcurve}
     \dif{s}^2 = \sum_{i, j} g_{ij} \dif{q_i} \dif{q_j}

 Where :math:`g_{ij}` is the metric for the geometry we are considering.
The volume element is then

.. math::

   \label{eq:volumecurvi}
     \dif{V} = \dif{s}_{1} + \dif{s}_2 + \dif{s}_3 = h_{q_1}h_{q_2}h_{q_3} \dif{q_1} \dif{q_2} \dif{q_3}

[Spherical Polar Coordinates] From the relations in equations
([eq:sph1]) to ([eq:sph3]), and considering that

.. math:: \vec{r} = x \vec{e_x} + y \vec{e_y} + z \vec{e_{z}}

Then,

.. math::

   \begin{aligned}
       \frac{\partial \vec r}{\partial r}
       &= \frac{\partial x}{\partial r} \vec{e_x} + \frac{\partial y}{\partial r} \vec{e_y} + \frac{\partial z}{\partial r} \vec{e_z} \\
       &= \sin \theta \cos \phi \vec{e_{x}} + \sin\theta \sin \phi \vec{e_y} + \cos \theta \vec{e_z} = h_r\vec{e_r} \\
       \frac{\partial \vec r}{\partial \theta}
       &= \frac{\partial x}{\partial \theta} \vec{e_x} + \frac{\partial y}{\partial \theta} \vec{e_y} + \frac{\partial z}{\partial \theta} \vec{e_z} \\
       &= r \cos \theta \cos \phi \vec{e_x} + r \cos \theta \sin \phi \vec{e_y} - r \sin \theta \vec{e_z} = h_{\theta}\vec{e_{\theta}} \\
       \frac{\partial \vec r}{\partial \phi}
       &= \frac{\partial x}{\partial \phi} \vec{e_x} + \frac{\partial y}{\partial \phi} \vec{e_y} + \frac{\partial z}{\partial \phi} \vec{e_z} \\
       &= - \sin \theta \sin \phi \vec{e_{x}} + r \sin\theta \cos \phi \vec{e_y} = h_{\phi}\vec{e_{\phi}} \\
     \end{aligned}

 Then the scale factors are

.. math::

   \begin{aligned}
       h_r &= \left| \frac{\partial \vec r}{\partial r} \right| = 1\\
       h_{\theta} &= \left| \frac{\partial \vec r}{\partial \theta} \right| = r\\
       h_{\phi} &= \left|  \frac{\partial \vec r}{\partial \phi} \right| = r \sin \theta\\
     \end{aligned}

 Also, the volume element,

.. math:: \dif{V} = r^2 \sin \theta \dif{r} \dif{\theta} \dif{\phi}

 and the square of the infinitessimal line element,

.. math::

   \dif{s}^2 = \dif{r}^2 + r^2 \dif{\theta}^2 + r^2 \sin^2 \theta
     \dif{\phi^2}

Del Operators
-------------

Gradient
~~~~~~~~

The gradient in the direction of :math:`\vec{e_{q_1}}` is

.. math::

   \label{eq:dirgradcurvi} \nabla_{q_i} =
     \frac{\partial}{\partial s_i} = \frac{1}{h_{q_i}}
     \frac{\partial}{\partial q_i}

 thus, the total gradient operator is

.. math::

   \label{eq:gradincurvi}
     \nabla = \sum_i \vec{e_{q_i}} \frac{\partial}{\partial s_i} = \sum_i \vec{e_{q_i}} \frac{1}{h_{q_i}} \frac{\partial}{\partial q_i}

Divergence
~~~~~~~~~~

We can define the divergence from the gradient, since

.. math::

   \nabla \cdot \vec{A} = \nabla \cdot \left( \sum_j A_j \vec{e_{q_j}}
   \right)

clearly we need :math:`\nabla \cdot \vec{e_{q_j}}` to continue; from
equation ([eq:dirgradcurvi]),

.. math::

   \nabla \cdot q_j = \sum_i \frac{1}{h_{q_i}} \frac{\partial
     q_j}{\partial q_i} = \sum_i \vec{e_{q_i}} \frac{1}{h_{q_i}}
   \delta_{ij} = \vec{e_{q_j}} \frac{1}{h_{q_j}}

 Thus,

.. math:: \vec{e_{q_j}} = h_{q_j} \nabla q_j

 The basis vectors form a right-handed set, so,

.. math:: e_{q_1} \times e_{q_2} = e_{q_3}

 and

.. math::

   \nabla q_1 \times \nabla q_2 =
   \frac{\vec{e_{q_3}}}{h_{q_1}h_{q_2}}

 Considering that :math:`\curl(\grad)
= 0`,

.. math::

   \begin{aligned}
    \nabla \cdot (\nabla_{q_1} \times \nabla_{q_2}) &=
     \nabla q_2 \cdot (\nabla \times \nabla q_1) - \nabla q_1 \cdot (
     \nabla \times \nabla q_2) \\ &= 0\end{aligned}

 So

.. math::

   \nabla \cdot \left( \frac{\vec{e_{q_3}}}{h_{q_1} h_{q_2}} \right) =
   0

 and the same argument applies for cyclic permutations,

.. math::

   \nabla \cdot \left( \frac{\vec{e_{q_3}}}{h_{q_1} h_{q_2}} \right) =
   \nabla \cdot \left( \frac{\vec{e_{q_1}}}{h_{q_2} h_{q_3}} \right) =
   \nabla \cdot \left( \frac{\vec{e_{q_2}}}{h_{q_3} h_{q_1}} \right) =
   0

 Then returning to

.. math::

   \begin{aligned}
     \nabla \cdot \vec{A} &= \nabla \cdot \left( \sum_j A_j \vec{e_{q_j}} \right) &\\
     &= \nabla \cdot \left\{ [h_{q_1}h_{q_2}A_1] \left[
         \frac{\vec{e_{q_1}}}{h_{q_2} h_{q_3}} \right] \right.
     &+& [h_{q_3}h_{q_1}A_2] \left[ \frac{\vec{e_{q_2}}}{h_{q_3} h_{q_1}} \right] \\
     &&+&\left.[h_{q_1} h_{q_2}A_3]  \left[ \frac{\vec{e_{q_3}}}{h_{q_1} h_{q_2}} \right]  \right\} \\
     &= \left[ \frac{\vec{e_{q_1}}}{h_{q_2} h_{q_3}} \right] \cdot \nabla
     [h_{q_1}h_{q_2}A_1]
     &+&\left[ \frac{\vec{e_{q_2}}}{h_{q_3} h_{q_1}} \right] \cdot \nabla [h_{q_3}h_{q_1}A_2]\\
     &&+&\left[ \frac{\vec{e_{q_3}}}{h_{q_1} h_{q_2}} \right]\cdot \nabla
     [h_{q_1}h_{q_2}A_3]\end{aligned}

 Since

.. math::

   \vec{e_{q_i}} \cdot \nabla = \frac{1}{h_{q_i}}
   \frac{\partial}{\partial q_i}

,

.. math::

   \label{eq:divincurvi}
     \begin{split}
       \nabla \cdot \vec{A} = \frac{1}{h_{q_1}h_{q_2}h_{q_3}} \left( \frac{\partial}{\partial q_1} (h_{q_2} h_{q_3} A_1) \right. \\
       + \left. \frac{\partial}{\partial q_2} (h_{q_3} h_{q_1} A_2) +
         \frac{\partial}{\partial q_3} (h_{q_2} h_{q_1} A_3) \right)
     \end{split}

Curl
~~~~

The curl can be derived from earlier results,

.. math::

   \begin{aligned}
     \nabla \times \vec{A} &=&& \nabla \times \left( \sum_j A_j \vec{e_{q_j}} \right) \\
     &=&& \nabla \times \left(
       \begin{matrix}
         [h_{q_1}A_1] \qty[\frac{\vec{e_{q_1}}}{h_{q_1}} ] &+
         [h_{q_2}A_2] \qty[ \frac{\vec{e_{q_2}}}{h_{q_2}} ] \\ &+
         [h_{q_3}A_3] \qty[ \frac{\vec{e_{q_3}}}{h_{q_3}} ]
       \end{matrix}
     \right) \\
     &= && - \left[ \frac{\vec{e_{q_1}}}{h_{q_1}} \right] \times \nabla
     (h_{q_1}A_1)
     - \left[ \frac{\vec{e_{q_2}}}{h_{q_2}} \right] \times \nabla (h_{q_2}A_2) \\
     &&& - \left[ \frac{\vec{e_{q_3}}}{h_{q_3}} \right] \times \nabla
     (h_{q_3}A_3)\end{aligned}

 so,

.. math::

   \label{eq:curlincurvi}
     \nabla \times \vec{A} = 
     \frac{1}{h_{q_1}h_{q_2}h_{q_3}}
     \begin{vmatrix}
       h_{q_1} \vec{e_1}              & h_{q_2} \vec{e_2}              & h_{q_3} \vec{e_{3}}             \\
       \frac{\partial}{\partial q_1} & \frac{\partial}{\partial q_2} & \frac{\partial}{\partial q_3} \\
       h_{q_1} A_1 & h_{q_2} A_2 & h_{q_3} A_3
     \end{vmatrix}

Laplacian
~~~~~~~~~

.. math::

   \label{eq:laplacianincurvi}
     \begin{split}
       \nabla^2 = \frac{1}{h_{q_1}h_{q_2}h_{q_3}} 
       \bigg( \pdv{q_1} \qty[ \frac{h_{q_2}h_{q_3}}{h_{q_1}} \pdv{q_1} ] 
       +  \pdv{q_2} \qty[ \frac{h_{q_3}h_{q_1}}{h_{q_2}} \pdv{q_2} ] \\
       +  \pdv{q_3} \qty[ \frac{h_{q_2}h_{q_1}}{h_{q_1}} \pdv{q_3} ] \bigg) 
     \end{split}

Partial Differential Equations in Curvlinear Coordinate Systems
===============================================================

Common Partial Differential Equations
-------------------------------------

There are a number of common PDEs which it is useful to know.

Laplace’s Equation
~~~~~~~~~~~~~~~~~~

.. math::

   \label{eq:laplace}
     \nabla^2 \phi(\vec{r}) = 0

This equation is used in electromagnetism, gravitation, hydrodynamics,
and heat flow in situations where no sources or sinks exist.

Poisson’s Equation
~~~~~~~~~~~~~~~~~~

.. math::

   \label{eq:poisson}
     \nabla^2 \phi(\vec{r}) = f(\vec{r})

This is used in the same situations as Laplace’s equation,
([eq:laplace]), only when there *are* sources or sinks, described by the
scalar field :math:`f`.

One of Maxwell’s equations is

.. math:: \nabla \cdot \vec{E} = \frac{\rho(\vec{r})}{\epsilon_{0}}

with electric field :math:`\vec E`, charge density :math:`\rho(\vec r)`,
and the permittivity of free space, :math:`\epsilon_0`. Since
:math:`\vec{E} = - \nabla
  \phi`, we have

.. math:: \nabla^2 \phi(\vec{r}) = - \frac{\rho(\vec{r})}{\epsilon_0}

Diffusion Equation
~~~~~~~~~~~~~~~~~~

.. math::

   \label{eq:diffusion}
     \nabla^2 \phi(\vec{r}, t) = \frac{1}{\alpha} \frac{\partial \phi(\vec{r}, t}{\partial t}

The diffusion equation describes the time and space evolution of fields
where there is no source; :math:`\phi` would describe the distribution
of temperature in a conductive heat flow situation, for example.

Consider heat flowing into a metal, with the temperature a scalar field,
represented by a function of position, :math:`\vec{r}`, and time,
:math:`t`, so :math:`T(\vec{r}, t)`. Then the heat in a small volume,
:math:`V`, is

.. math:: Q = \int_V \rho c_{\rm p} T(\vec{r}, t) \difp{3}{\vec{r}}

The rate at which heat transfers from one volume to another depends on
the temperature gradient, the area of the contact, and the metal’s
thermal conductivity. For a boundary of area :math:`A`,

.. math::

   \frac{\dif{Q}}{\dif{t}} = \int_A k \dif{\vec{\sigma}} \cdot
     \nabla T(\vec{r}, t)

 with :math:`\dif{\vec{\sigma}}` the normal vector to the area,
:math:`\dif{A}`. Applying the divergence theorem,

.. math::

   \begin{aligned}
       \frac{\dif{Q}}{\dif{t}} &= \int_V \nabla \cdot [k \nabla
       T(\vec{r}, t)] \difp{3}{\vec{r}} \\
       &= \int_V k \nabla^2 T(\vec{r}, t) \difp{3}{\vec{r}}
     \end{aligned}

 Then equating the expressions for :math:`\frac{\dif{Q}}{\dif{t}}`, and
assuming :math:`\rho` and :math:`c_{\rm p}` are constant,

.. math::

   \begin{aligned}
       \frac{\dif{Q}}{\dif{t}} &= \int_V \nabla \cdot [k \nabla
       T(\vec{r}, t) ] \difp{3}{\vec{r}} \\ &= \int_{V} k \nabla^2
       T(\vec{r}, t) \difp{3}{\vec{r}} \\ \nabla^2 T(\vec{r}, t) &=
       \frac{\rho c_{\rm p}}{k} \frac{\partial T(\vec{r},t)}{\partial t}
     \end{aligned}

Wave Equation
~~~~~~~~~~~~~

.. math::

   \label{eq:wave}
     \nabla^2 \phi(\vec{r}, t) = \frac{1}{v^2} \frac{\partial^2 \phi(\vec{r}, t)}{\partial t^2}

The wave equation describes the progression of vibrations through media.
It occurs frequently in physics, and an operator is defined for it, the
d’Alembertian operator,

.. math::

   \Box^2 \equiv \frac{1}{v^2}
     \frac{\partial^2 \phi(\vec{r}, t)}{\partial t^2}

Helmholtz Equation
~~~~~~~~~~~~~~~~~~

.. math::

   \label{eq:helmholtz}
     \nabla^2 \phi + k^2 \phi = 0

This appears where the time dependence of the diffusion equation is
removed by the separation of variables.

Schrodinger Equation
~~~~~~~~~~~~~~~~~~~~

Time-independent:

.. math::

   \label{eq:tindyschrodinger}
     - \frac{\hbar^2}{2m} \nabla^2 \psi + V \psi = E \psi

 Time-dependent:

.. math::

   \label{eq:tdschrodinger}
     - \frac{\hbar^2}{2m} \nabla^2 \psi + V \psi = i \hbar \frac{\partial \psi}{\partial t}

Method of Separation of Variables
---------------------------------

Consider the diffusion equation, ([eq:diffusion]), and look for
solutions with the form

.. math:: \phi(\vec{r}, t) = \Phi(\vec{r}) T(t)

 Solutions of this form exist for these equations because they are
linear and have no cross-terms. So we now have

.. math:: \frac{1}{\Phi (\vec{r}) } \nabla^2 \Phi(\vec{r}) = \frac{1}{\alpha} \frac{1}{T(t)} \dv{T(t)}{t}  = -k^2

 since both sides must be equal, they are also both equal to a constant.
So now we have

.. math::

   \begin{aligned}
     \frac{\dif{T}}{\dif{t}} &= -\alpha k^2 T \\
     \nabla^2 \Phi(\vec{r}) &= -k^2 \Phi(\vec{r})\end{aligned}

 For examples, see MM1 notes.

Separation of Variables in spherical and cylindrical coordinate systems
-----------------------------------------------------------------------

We can decompose Laplace’s equation, equation ([eq:laplace]), into three
equations. In spherical coordinates Laplace’s equation becomes

.. math::

   \begin{split}
       \frac{1}{r^2 \sin \theta} 
       \bigg( \pdv{r}      \left[r^2 \sin \theta \pdv{\psi(r, \theta, \phi)}{r} \right] \\ 
            + \pdv{\theta} \left[\sin \theta \pdv{\psi(r, \theta, \phi)}{\theta}\right] \\ 
            + \pdv{\phi}   \left[\frac{1}{\sin \theta} \pdv{\psi(r,\theta, \phi)}{\psi } \right] \bigg)\\ =0
       \end{split}

 Then, rewriting :math:`\psi` as a product of three functions,

.. math:: \psi(r, \theta, \phi) = R(r)\Theta(\theta)\Phi(\phi)

 and dividing by this,

.. math::

   \begin{split}
         \frac{1}{R \Theta \Phi} 
         \bigg( \Theta \Phi \frac{\partial}{\partial r} \left[r^2 \sin \theta \frac{\partial \psi(r, \theta, \phi)}{\partial r} \right] \\
              + R \Phi \frac{\partial}{\partial \theta} \left[ \sin \theta \frac{\partial \psi(r, \theta, \phi)}{\partial \theta}\right] \\ 
              + R \Theta \frac{\partial}{\partial \phi} \left[ \frac{1}{\sin \theta} \frac{\partial \psi(r, \theta, \phi)}{\partial \psi }\right]
         \bigg) \\=0
         \end{split}

.. math::

   \begin{split}
           \frac{1}{R} \frac{\partial}{\partial r} \left[r^2 \sin \theta
             \frac{\partial \psi(r, \theta, \phi)}{\partial r} \right] \\
           + \frac{1}{\Theta} \frac{\partial}{\partial \theta} \left[
             \sin \theta \frac{\partial \psi(r, \theta, \phi)}{\partial
               \theta}\right] \\ + \frac{1}{\Phi}
           \frac{\partial}{\partial \phi} \left[ \frac{1}{\sin \theta}
             \frac{\partial \psi(r, \theta, \phi)}{\partial \psi }\right]
           \left.\vphantom{\frac{1}{2}}\right) \\=0
         \end{split}

| Then

  .. math::

     \sin^2\theta \frac{1}{R} \frac{\partial}{\partial r} \left[ r^2 \frac{\partial R}{\partial r} \right]
           +\sin \theta \frac{1}{\Theta} \frac{\partial}{\partial \theta} \left[ \sin \theta \frac{\partial \Theta}{\partial \theta}\right] 
           = - \frac{1}{\Phi} \frac{\difp{2}{\Phi}}{\dif \Phi^2}

   Each side must be constant, so

  .. math::

     \begin{aligned}
           \frac{1}{\Phi} \dv[2]{\Phi}{\phi} &= -m^2 \\
           \sin^2(\theta) \frac{1}{R} \dv{r} \qty[r^2 \dv{R}{r}] +
           \sin(\theta) \frac{1}{\Theta} \dv{\theta} \qty[\sin(\theta)
           \dv{\Theta}{\theta}] &= m^2
         \end{aligned}

   and these can themselves be made equal to a constant,

  .. math::

     \begin{aligned}
           \frac{1}{R} \dv{r} \qty[r^2 \dv{R}{r}] &= -
           \frac{1}{\sin(\theta)} \frac{1}{\Theta} \dv{\theta}
           \qty[\sin(\theta) \dv{\Theta}{\theta}] +
           \frac{m^2}{\sin^2(\theta)} = k
         \end{aligned}

   *The :math:`R(r)` equation:*
| 

  .. math::

     \begin{aligned}
           \dv{r} \qty[r^2 \dv{R(r)}{r}] - kR(r) &= 0 \\
           r^2 \dv[2]{R(r)}{r} + 2r \dv{R(r)}{r} - kR(r) &=0
         \end{aligned}

   The coefficients are polynomials of :math:`r`, so we try a solution
  of the form :math:`R(r) = r^n`,

  .. math::

     \begin{aligned}
           r^2n(n-1) r^{n-2} + 2r nr^{n-1} - kr^n &= 0 \\
           n(n-1)r^n + 2nr^n - kr^n &= 0 \\
           n(n+1) - k &= 0
         \end{aligned}

   and now let :math:`k = l(l+1)`, so :math:`n(n+1) = l(l+1)`, thus
  :math:`n=l` or :math:`n =
      -l-1` making the general solution

  .. math::

     \label{eq:generalsolr}
           R(r) = A r^l + B r^{-l-1}

   *The equation for :math:`\Phi(\phi)`*
| 

  .. math:: \dv[2]{\Phi(\phi)}{\phi}= -m^2 \Phi(\phi)

  The solution must have the form :math:`\Phi(\phi) = e^{\alpha \phi}`,
  so

  .. math:: \alpha^2 \Phi(\phi) = -m^2 \Phi(\phi)

   so :math:`\alpha = \pm
      e^{\alpha \phi}` . Thus, the general solution is

  .. math::

     \label{eq:generalsolphi}
           \Phi(\phi) = A^{\prime} \sin(m \phi) + B^{\prime} \cos(m \phi)

   for constants :math:`A^{\prime}`, and B\ :math:`^{\prime}`, and
  :math:`m \in
      \mathbb{N}`, since :math:`\Phi(\phi + 2 \pi) = \Phi(\phi)`.

| *The equation for :math:`\Theta(\theta)`*
| 

  .. math::

     \sin(\theta) \dv{\theta} \qty[ \sin(\theta)
         \dv{\Theta(\theta)}{\theta}] - m^2 \Theta(\theta) + l(l+1)
         \sin^2(\theta) \Theta(\theta) = 0

  which has the form of the Associate Legendre Differential equation,
  equation ([eq:assoclegendrede]), and the solution is therefore an
  Associate Legendre polynomial, with a general solution of the form

  .. math:: \Theta(\theta) = A P_l^m \qty( \cos(\theta) )

   Thus, the general solution of

  .. math:: \nabla^2 \psi(r, \theta, \phi) = 0

   is

  .. math::

     \label{eq:solutionpdesphere}
           \psi(r, \theta, \phi) = \sum_{l=0}^{\infty} \sum_{m=0}^l (A_{lm}r^l + B_{lm}r^{-l-1}) P_l^m \qty( \cos \theta) e^{\pm i m \phi}

   :math:`A`, and :math:`B` are constants determined by the boundary
  conditions of the problem. The functions

  .. math::

     \label{eq:sphericalharm}
           Y_l^m(\theta, \phi) = N e^{im\phi} P_l^m (\cos(\theta))

   with :math:`l \ge 0`, and :math:`|m| \le l`, are *Spherical
  Harmonics*.

| The surface of a metal sphere of radius :math:`r_0` is held at an
  electrostatic potential of :math:`V_0 \cos(\theta)`, with
  :math:`\theta` the polar angle. What is the electrostatic potential
  inside and outside the sphere, assuming no other sources of charge?
  There are no sources other than the sphere, so outside the sphere the
  potential obeys Laplace’s equation. The problem has spherical
  symmetry.
| *Inside the sphere*
| :math:`R(r) \propto r^{-l-1}` would give an infinity at :math:`r=0` ,
  so :math:`B_{lm}=0`. Thus,

  .. math::

     \psi(r, \theta, \phi) = \sum_{l=0}^{\infty} \sum_{m=0}^l A_{lm}r^l
       P_l^m \qty( \cos \theta) e^{\pm i m \phi}

   and we have the boundary condition that

  .. math:: \psi(r_0, \theta, \phi) = \phi_0 \cos(\theta)

   which has no :math:`\phi` dependence, implying :math:`m=0`. Then,

  .. math::

     \psi(r, \theta, \phi) = \sum_{l=0}^{\infty} A_{l}r^l P_l \qty(
       \cos \theta) = \phi_0 \cos(\theta)

   so only :math:`l=1` can satisfy this equation, and thus the potential
  is

  .. math:: \psi(r, \theta, \phi) = \psi_0 \frac{r}{r_0} \cos(\theta)

   *Outside the sphere*
| The same arrguments apply outside the sphere as did inside, so,

  .. math:: R(r) \propto r^l

  would give an infinity as :math:`r \to
    \infty`. Thus :math:`A_{lm}=0`. The same arguments for angular
  depenence also apply, so,

  .. math:: \psi(r, \theta, \phi) = \psi_0 \qty( \frac{r_0}{r})^2 \cos(\theta)
