Vector Calculus
===============

:math:`\require{physics}`

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

clearly we need :math:`\nabla \cdot \vec{e_{q_j}}` to continue; from equation ([eq:dirgradcurvi]),

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

Considering that :math:`\curl(\grad) = 0`,

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
