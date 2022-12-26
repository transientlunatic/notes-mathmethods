

Lie Brackets
============

Any linearly independent set of vector fields can serve as a basis, but not all come from coordinate systems; all coordinate systems commute, but in general not all vector fields commute, and the commutator, 

.. math:: \comm{V}{W} = V W - W V

is a vector field with, in general, non-vanishing components.
If :math:`W` and :math:`V` are elements of a basis they cannot be expressed as derivatives with respect to any coordinates.
The commutator is the Lie Bracket of the two vector fields, and shows that the parameterisation of the integral curves of these vector fields is not that of a coordinate system.

.. prf:defintion:: Lie Bracket

		   Let :math:`X` and :math:`Y` be vector fields of class :math:`C^1`, then the Lie Bracket is a vector field, defined by the operation :math:`f \mapsto (XY - YX) f`, and is denoted :math:`\comm{X}{Y}`.

The vector :math:`\comm{V}{W}` can be viusualised as the difference in moving a distance :math:`\Delta \lambda = \epsilon` along the :math:`V` curve, then :math:`\Delta \mu = \epsilon` along a :math:`W` curve, ending at a point :math:`A`.
Going in the opposite order we end at a point :math:`B`.
The vector between these two points is :math:`\epsilon^2 \comm{V}{W}`.

A Lie Algebra of vector fields on a region :math:`U` of :math:`M` is a set :math:`A` of vector fields on :math:`U` which is a vector space under addition, which is closed under the Lie Bracket operation.

For a basis to be a coordinate basis the fields of the basis must commute.

..
   .. tikz:: A geometrical interpretation of the commutator.
	     In the top diagram are two commuting vector fields, but in the lower diagram the two fields do not commute.
	     Moving a distance :math:`\epsilon` along :math:`V` then :math:`\epsilon` along :math:`W` does not take us to the same place as moving :math:`\epsilon` along :math:`W` and then :math:`\epsilon` along :math:`V`, so the paths do not meet, with a gap equal to :math:`\epsilon^2\comm{V}{W}` separating their end points.
      :include: figures/commutation.pgf

