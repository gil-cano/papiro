=====================
Basic Python Patterns
=====================

Comparaciones
-------------

..
   In Python you compare for equality with == but for identity with is
   So how do you compare with None in Python? You use:
   and if you want to check whether something is not None the idiom is

En Python comparamos por igualdan con ``==`` y por identidad con ``is``

Por ejemplo para comparar ``None`` en Python usamos:

.. code-block:: python

   value is None

y si queremos comparar si algo no es ``None``:

.. code-block:: python

   value is not None

Type check
-----------

.. code-block:: python

   if type(start_date) == date:

o:

.. code-block:: python

   if isinstance(start_date, date):


Exercise 1
^^^^^^^^^^

Your mission, should you choose to accept it...

..  admonition:: Solution
    :class: toggle

    To save the world with only seconds to spare do the following:

    .. code-block:: python

        from plone import api
