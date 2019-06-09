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



`Expressions <https://docs.plone.org/4/en/develop/plone/functionality/expressions.html>`_
`Static resources <https://docs.plone.org/external/plone.app.dexterity/docs/advanced/static-resources.html>`_
`CSS <https://docs.plone.org/adapt-and-extend/theming/templates_css/css.html>`_
