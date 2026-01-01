.. _set-theory:

Sets
====

Sets are collections of objects of some sort or another.
Those objects can be numbers, vectors, houses, or even other sets.
However, the sets encountered most frequently are sets of numbers.

The foundations of almost all of mathematics is now built upon sets.

.. prf:definition:: Set
   :label: def:set

	   :math:`\def\set#1{\mathcal{#1}}`
	   A set, :math:`\set{A}` is a mathematical object which is defined by a binary relationship, :math:`\in`, between the :math:`\set{A}` and any other object :math:`o`.

	   + If the object :math:`o` is an element in the set (a member of the set) then :math:`o \in \set{A}`.

.. _subset:
Subsets
-------

The notion of a set in its own right does not provide us with many useful tools for understanding it or its structure.

We can introduce the concept of a "subset" to try and build this.

.. prf:definition:: Subset
		    :label: subset

		    + Let :math:`\set{A}` and :math:`\set{B}` be sets.
		    + Let :math:`b \in \set{B}` be some element from :math:`\set{B}`.

		    If :math:`b \in \set{A}` for every element :math:`b \in \set{B}` then :math:`\set{B}` is a subset of :math:`\set{A}`.

		    We can write this as :math:`\set{B} \subset \set{A}`.

.. _set-operations:
Set operations
--------------

With sets and subsets defined, it is possible to start considering operations which might exist between two sets.

.. prf:definition:: Set Union
		    
		    + Let :math:`\set{A}` and :math:`\set{B}` be sets.

		    The **union**, :math:`\set{A} \cup \set{B}`, of the sets is the set which contains all of the elements contained in both :math:`\set{A}` and :math:`\set{B}`.
		    

.. prf:definition:: Set intersection

.. prf:definition:: Set difference

.. prf:definition:: Power set
		    
.. _order:
Ordering
--------

Ordering is a property which can apply to a set to provide the intuitive quality of a sequence to the elements of a set.

Ordering is defined by a relationship on the elements of a set which dictate that order, and describe the concepts of greater and lesser than elements of a set.

.. prf:definition:: Partial order
		    :label: partial-order

		    A binary relation, :math:`\leq`, on a set, :math:`\set{A}` is called a partial order if and only if:

		    + :math:`\leq` is reflective
		      (:math:`x \leq x \forall x \in \set{A}`)

		    + :math:`\leq` is symmetrical
		      (if :math:`x \leq y` and :math:`y \leq x` then :math:`x = y` for all :math:`x,y \in \set{A}`).

		    + :math:`\leq` is transitive
		      (if :math:`x \leq y` and :math:`y \leq z` then :math:`x \leq z` for :math:`x, y, z \in \set{A}`).

With the notion of ordering defined we can extend the definition of a set with it.
		      
.. prf:definition:: Partially-ordered set
		    :label: poset
			    
		    A set which has a partial ordering relationship defined on it is called a partially-ordered set.


Bounds
------

.. prf:definition:: Bounding

		    A partially-ordered set :math:`A \subset B` is **bounded above** if there is a number :math:`b \in B` such that :math:`a \leq b` for all :math:`a \in A`.
		    The number :math:`b` is the **upper bound** for :math:`A`.
		    
		    A partially-ordered set :math:`A \subset B` is **bounded below** if there is a number :math:`b \in B` such that :math:`a \geq b` for all :math:`a \in A`.
		    The number :math:`b` is the **lower bound** for :math:`A`.


.. prf:definition:: Supremum

		    The supremum, or least upper bound, of a partially-ordered set :math:`A \subset B` is the number :math:`s` which meets the criteria:

		    #. :math:`s` is an upper bound of :math:`A`
		    #. if :math:`b` is any upper bound for :math:`A` then :math:`s \leq b`.
