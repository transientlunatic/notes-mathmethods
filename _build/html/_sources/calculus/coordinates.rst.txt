==================
Coordinate Systems
==================

Spherical Polar Coordinates
---------------------------

They are related to Cartesian coordinates by the transformations:

.. math::

   \begin{aligned}
         x &= r \sin \theta \cos \phi \label{eq:sph1}\\
         y &= r \sin \theta \sin \phi \label{eq:sph2}\\
         z &= r \cos \theta \label{eq:sph3}
       \end{aligned}

Cylindrical Polar Coordinates
-----------------------------

They are related to Cartesian coordinates by the transformations:

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



Curvilinear coordinates
=======================

A curvilinear coordinate system is a coordinate system over a space in which the coordinate lines may be curved, and are related to a Cartesian coordinate system by a bijection.
In physics, laws are independent of reference frame and of coordinate system, which allows the use of the most appropriate coordinate system for a specific situation—for example, if a problem has spherical symmetry it is likely to be easiest to solve in spherical polar coordinates.


