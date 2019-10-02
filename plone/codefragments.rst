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


Interfaces dinamicas
--------------------

Se declara la interfaz en zcml.

.. code-block:: xml

    <interface interface="mfabrik.app.interfaces.promotion.IPromotionsPage" />

Se define la interfaz en un .py

En el ZMI se posiciona en el objeto y en el tab de Interfaces se seleccíona la nueva.

* `Dynamic marker interfaces <https://docs.plone.org/develop/addons/components/interfaces.html#dynamic-marker-interfaces>`_


Obtener el path del archivo
---------------------------

.. code-block:: python

    # Augment known mime-types.
    here = os.path.dirname(os.path.abspath(__file__))
    add_files([os.path.join(here, 'mime.types')])



.. code-block:: xml

    <interface interface="mfabrik.app.interfaces.promotion.IPromotionsPage" />


* `Expressions <https://docs.plone.org/develop/plone/functionality/expressions.html>`_
* `Static resources <https://docs.plone.org/external/plone.app.dexterity/docs/advanced/static-resources.html>`_
* `CSS <https://docs.plone.org/adapt-and-extend/theming/templates_css/css.html>`_
