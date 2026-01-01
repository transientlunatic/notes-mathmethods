One-forms
=========

Consider :math:`T_P`, the tangent space of vectors at a point :math:`P`.
A one-form, :math:`\of{\omega}` at :math:`P` associates a vector
:math:`\vec{V}` at P to a real number, :math:`\of{\omega}(\vec{V})`.

This function is linear; for vectors :math:`\vec{V}` and
:math:`\vec{W}`, and real numbers :math:`a` and :math:`b`,

.. math::

   \label{eq:8}
    \of{\omega}( a \vec{V} + b \vec{W} ) = a \of{\omega}(\vec{V}) + b
   \of{\omega}(\vec{W})

can be multiplied by scalars,

.. math::

   \label{eq:9}
     (a \of{\omega})(\vec{V}) = a [ \of{\omega}(\vec{V})]

and have the property

.. math::

   \label{eq:10}
     (\of{\omega} + \of{\sigma}) (\vec{V}) + \of{\omega}(\vec{V}) + \of{\sigma}(\vec{V})

They satisfy the axioms of a vector space, and are indeed the duals of
vectors, and have a tangent vector space :math:`T^{*}_P`.

A field of one-forms can represent the gradient of a function :math:`f`; such a field is denoted :math:`\dd{f}`,

.. math:: \of{\dd{}}f (\dv*{\lambda}) = \dv{f}{\lambda}

In the vector space :math:`T^{*}_P` any :math:`n` linearly independent one-forms can constitute a basis, however selecting a set of basis vectors, :math:`\set{\vec{e}_i}` in :math:`T_P` induces a preferred basis on :math:`T^{*}_P`, the dual basis :math:`\set{\of{\omega}^i}`.

These have the property

.. math:: \of{\omega}^i(\vec{e}_j) = \delta^i_j
