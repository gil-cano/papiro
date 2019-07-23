.. _codefragments:

Fragmentos de código
====================



Probar si un paquete esta instalado.
------------------------------------

.. code-block:: python

    try:
        import plone.app.event
        HAS_PLONE_APP_EVENT = True
    except ImportError:
        HAS_PLONE_APP_EVENT = False



Obtener la raiz del sitio en un template
----------------------------------------

En un template podemos usar varias expresiones predefinidas.

.. code-block:: xml

    string:${context/portal_url}/@@my_view_name

`Aquí <https://docs.plone.org/develop/plone/functionality/expressions.html#expression-variables>`_ puedes ver la lista completa.

`Vistas y metodos <https://docs.plone.org/4/en/old-reference-manuals/plone_3_theming/page/otherinfo.html#available-views-and-methods>`_ disponibles en templates.


* `Expressions <https://docs.plone.org/develop/plone/functionality/expressions.html>`_
* `Static resources <https://docs.plone.org/external/plone.app.dexterity/docs/advanced/static-resources.html>`_
* `CSS <https://docs.plone.org/adapt-and-extend/theming/templates_css/css.html>`_
