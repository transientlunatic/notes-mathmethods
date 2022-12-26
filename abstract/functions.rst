.. _functions:
.. _mappings:

Mappings and Functions
======================

Let :math:`X,Y,Z` denote sets.

.. prf:definition:: Mapping

		    A mapping :math:`f:X \to Y` is a rule associating every element in :math:`X` with a unique member of :math:`Y`.
		    :math:`X` is the domain, and :math:`Y` is the codomain of the mapping.

.. prf:definition:: Function Composition

		    Given two mappings :math:`f:X \to Y` and :math:`g:Y \to Z`, the composition, :math:`g \circ f: X \to Z` is the mapping 

		    .. math:: (g \circ f)(x) = g(f(x)) \qquad \forall x \in X

.. prf:definition:: Identity Mapping

		    The identity mapping

		    .. math:: \idmap_X : X \to X

		    which is defined by

		    .. math:: \idmap_X(x) = x \quad \forall x \in X

.. prf:definition:: Zero Mapping
			      
		    Provided :math:`Y` contains a zero element :math:`0`, the zero mapping, :math:`0_x:X \to Y` is defined

		    .. math:: 0_x(x) = 0 \quad \forall x \in X

.. prf:definition:: Injective, surjective, and bijective mappings
			      
		    A mapping :math:`f:X \to Y` is injective if for all :math:`x_1, x_2 \in X`,

		    .. math:: f(x_1) = f(x_2) \implies x_1 = x_2

		    A mapping :math:`f: X \to Y` is called surjective if, for every :math:`y \in Y` there exists at least one :math:`x \in X` for which :math:`y = f(x)`.

		    A mapping is bijective if it is both injective and surjective.

.. prf:observation:: Inverse mappings
		    
		     A mapping :math:`f:X \to Y` is bijective iff there is an inverse mapping

		     .. math:: h: Y \to X

		     such that

		     .. math::

			h \circ f = \idmap_X \quad
			\text{and} \quad f \circ h = \idmap_Y
