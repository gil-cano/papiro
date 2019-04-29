.. _about:

===================================
Lineaminetos generales de escritura
===================================


.. topic:: Descripción

   Esta página explica los lineamientos de escritura reST para la ducumentación de este proyecto.


Está basada en los lineamientos de la documentación del CMS `Plone <https://docs.plone.org/about/contributing/documentation_styleguide.html>`_.


Enlaces
-------

.. code-block:: rst

   `Example <https://example.com>`_

`Example <https://example.com>`_

Italicas
--------

.. code-block:: rst

   This *word* is italics.

This *word* is italics.


Negritas
--------

.. code-block:: rst

   This **word** is in bold text.


This **word** is in bold text.

Comandos
--------

.. code-block:: rst

   :command:`gettext`

:command:`gettext`

Código en linea
---------------

.. code-block:: rst

   This is :func:`aFunction`, this is the :mod:`some.module` that contains the :class:`some.module.MyClass`

This is :func:`aFunction`, this is the :mod:`some.module` that contains the :class:`some.module.MyClass`

Resaltar nombres de archivos o cadenas
--------------------------------------

.. code-block:: rst

   :file:`index.rst` note la extension ``.rst``


:file:`index.rst` note la extension ``.rst``

Rutas en menus
--------------

.. code-block:: rst

   :menuselection:`Preferencias --> Perfil --> Terminal`

:menuselection:`Preferencias --> Perfil --> Terminal`

Lista
-----

.. code-block:: rst

   * primer elemento
   * segundo elemento
   * tercer elemento

* primer elemento
* segundo elemento
* tercer elemento


Etiquetas de página
-------------------

.. code-block:: rst

   .. _about:

.. code-block:: rst

   :ref:`about`


:ref:`about`


Tablas en lista
---------------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Shapes
     - Description
   * - Square
     - Four sides of equal length, 90 degree angles
   * - Rectangle
     - Four sides, 90 degree angles


Advertencia
-----------

.. code-block:: rst

   .. warning::

      This is a warning box

.. warning::

   This is a warning box

Error
-----

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

Json
----

.. code-block:: rst

   .. code-block:: json

      {
        "font_face": "Source Code Pro",
        "font_size": 15,
        "ignored_packages":
        [
            "Vintage",
        ],
        "rulers":
        [
            72,
            79,
            100,
        ],
        "tab_size": 4,
        "translate_tabs_to_spaces": true,
        "use_tab_stops": true,
      }



Imagenes
--------

.. code-block:: rst

   .. image:: ../_static/plone_donut.png
      :alt: Picture of Plone Donut

Bibliografía
============

* `Plone Documentation Styleguide <https://docs.plone.org/about/contributing/documentation_styleguide.html>`_
* `General Writing Guidelines <https://docs.plone.org/about/contributing/rst-styleguide.html>`_
* `Sphinx Syntax reStructuredText <http://udig.refractions.net/files/docs/latest/user/docguide/sphinxSyntax.html>`_
* `Sphinx/Rest Memo <https://rest-sphinx-memo.readthedocs.io/en/latest/ReST.html>`_
* `Programming Notes <https://aert-notes-dev.readthedocs.io/en/latest/content/rest/#structural-elements>`_
