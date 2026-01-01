Fields of Scalars
=================

A field is an algebraic structure with notions of addition, subtraction, multiplication, and division, satisfying certain axioms.
The principle examples are :math:`\mathbb{Q}`, :math:`\mathbb{R}`, and :math:`\mathbb{C}`.

.. prf:definition:: Field
   :label: field
			    
		    A field consists of a set, :math:`F`, whose elements are called scalars, together with two algebraic operations: addition and multiplication, for combining every pair of scalars, :math:`x, y \in F` to form the new scalars :math:`(x+y) \in F` and :math:`(x \times y) \in F`.

		    These operations must satisfy the field axioms:


		    .. prf:axiom:: Associativity

				   For :math:`x,y,z \in F`,
				   
				   .. math::

				      \begin{aligned}
				         (x+y)+ z            &= x+(y+z) \\
				         (x\times y)\times z &= x \times (y \times z)
				      \end{aligned}

		    .. prf:axiom:: Distributivity

				   .. math::

				      \begin{aligned}
 				        (x+y) \times z   &= x \times z + y \times z \\
				        z \times (x + y) &= z \times x + z \times y
				      \end{aligned}

		    .. prf:axiom:: Commutativity

				   .. math::

				      \begin{aligned}
				        x + y      &= y + x \\
				        x \times y &= y \times x
				      \end{aligned}

		    .. prf:axiom:: Zero and Unity

				   There are unique and distinct elements, :math:`0, 1 \in F`, such that

				   .. math::
      
				      \begin{aligned}
				               x+0 &= x = 0 + x \\
					x \times 1 &= x = 1 \times x
				      \end{aligned}

		    .. prf:axiom:: Existence of Additive and multiplicative inverses

				   For :math:`x \in F` there exists a unique element :math:`-x \in F`, for which

				   .. math:: x + (-x) = 0 = (-x)+x

				   For each non-zero :math:`y \in F` there is a unique element, :math:`y^{-1} \in F`, the multiplicative inverse, for which

				   .. math:: y \times (y^{-1}) = 1 = (y^{-1})\times y
