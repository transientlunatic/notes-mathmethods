.. _stirlings-approximation:

========================
Stirling's Approximation
========================

Stirling's approximation makes an approximation of the factorial.

.. prf:definition:: Factorial

		    The factorial of a natural number, :math:`n \in \mathbb{N}` is equal to the product of all natural numbers less than or equal to :math:`n`.
		    That is,

		    .. math::
		       \require{physics}
		       n! = 1 \times 2 \times \cdots \times (n-1) \times n

From the definition it is clear that we can define a recurrence relation for the factorial as well.

.. prf:remark:: Factorial recurrence

		The factorial of a natural number, :math:`n \in \mathbb{N}` is equal to the product of that number and the factorial of the previous natural number.
		That is,

		.. math::
		   n! = n \times (n - 1)!

The growth of the factorial is rapid, and it is clear that for large numbers we may run into situations where the ability to approximate it would be useful.
We can approach this by taking the natural logarithm of the factorial, in order to change the product into a sum.

This leads to the normal expression for the Stirling approximate.

.. math::
   \log(n!) = \sum_{x=1}^n \log(x) \approx \int_1^n \log(x) \dd{x} = n \log(n) - n + 1

.. prf:definition:: Stirling's Approximation
   :label: stirling-approximation

	   .. math::
	      \log(n!) \approx n \log(n) - n + \mathcal{O}\log(n)

==================
The Gamma Function
==================

Given the existence of the factorial for natural numbers, it is a natural extension to consider what the equivalent function looks like for the all the real (or indeed the complex) numbers.

This function is the Gamma function.

.. prf:definition:: Gamma Function

		    The Gamma function is the convergent improper integral

		    .. math::
		       \Gamma(z) = \int_0^\infty t^{z-1} e^{-t} \dd{t} \qquad \mathrm{Re}(z) > 0

		    which may be extended by analytical continuation to cover the entire complex field, except at negative integers, where the function has poles.

For natural numbers the Gamma function and the factorial are related:

.. math::
   \Gamma(n) = (n - 1)!

or, using the recurrence relation for factorials,

.. math::
   n \Gamma(n) = n!

Thus the Gamma function can be seen as an extension of the notion of a factorial over the complex field.
   
.. plot:: calculus/gamma.py

   The Gamma Function over the Complex numbers





      
