===================================
Lineaminetos generales de escritura
===================================


.. topic:: Descripción

   Esta página explica los lineamientos de escritura reST para la ducumentación de este proyecto.


Está basada en los lineamientos de la documentación del CMS `Plone <https://docs.plone.org/about/contributing/documentation_styleguide.html>`_.


Enlaces
=======

.. code-block:: rst

   `Example <https://example.com>`_

*Italicas*

.. code-block:: rst

   This *word* is italics.

**Negritas**

.. code-block:: rst

   This **word** is in bold text.

Resaltado de codigo en linea

.. code-block:: rst

   This is :func:`aFunction`, this is the :mod:`some.module` that contains the :class:`some.module.MyClass`

This is :func:`aFunction`, this is the :mod:`some.module` that contains the :class:`some.module.MyClass`

Resaltar nombres de archivos o cadenas

.. code-block:: rst

   :file:`index.rst` note la extension ``.rst``


:file:`index.rst` note la extension ``.rst``


Lista

.. code-block:: rst

   * First bullet
   * Second bullet with `a link <http://opensourcehacker.com>`_

Advertencia

.. code-block:: rst

   .. warning::

      This is a warning box

.. warning::

   This is a warning box

Error

.. code-block:: rst

   .. error::

      This is an error box

.. error::

   This is an error box

Nota

.. code-block:: rst

   .. note::

      This is a note box

.. note::

   This is a note box


Por hacer

.. code-block:: rst

   .. TODO::

      This is a TODO item

.. TODO::

   This is a TODO item


Ver también

.. code-block:: rst

   .. seealso::

      This!

.. seealso::

   This!
   
Resaltado de sintaxis
=====================

Terminal UNIX
-------------

.. code-block:: rst

   .. code-block:: shell

      bin/plonectl fg

Python
------

.. code-block:: rst

   .. code-block:: python

      if "foo" == "bar":
          # This is Python code
          pass

Python interactivo
------------------

.. code-block:: rst

   .. code-block:: pycon

      >>> class Foo:
      ...     bar = 100
      ...
      >>> f = Foo()
      >>> f.bar
      100
      >>> f.bar / 0
      Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      ZeroDivisionError: integer division or modulo by zero

XML
---

.. code-block:: rst

   .. code-block:: xml

      <somesnippet>Some XML</somesnippet>

Archivos ini
------------

.. code-block:: rst

   .. code-block:: ini

      [some-part]
      # A random part in the buildout
      recipe = collective.recipe.foo
      option = value


JavaScript
----------

.. code-block:: rst

   .. code-block:: javascript

      var $el = $('<div/>');
      var value = '<script>alert("hi")</script>';
      $el.text(value);
      $('body').append($el);

Imagenes
--------

.. code-block:: rst

   .. image:: ../_static/plone_donut.png
      :alt: Picture of Plone Donut

Bibliografía
============

* `Plone Documentation Styleguide <https://docs.plone.org/about/contributing/documentation_styleguide.html>`_
* `General Writing Guidelines <https://docs.plone.org/about/contributing/rst-styleguide.html>`_
