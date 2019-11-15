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

Se define la interfaz en un :file:`.py`

En el ZMI se posiciona en el objeto y en el tab de Interfaces se seleccíona la nueva.

* `Dynamic marker interfaces <https://docs.plone.org/develop/addons/components/interfaces.html#dynamic-marker-interfaces>`_


Obtener el path del archivo
---------------------------

:file:`__file__` hace referecia al archivo

.. code-block:: python

    # Augment known mime-types.
    here = os.path.dirname(os.path.abspath(__file__))
    add_files([os.path.join(here, 'mime.types')])

.. code-block:: python

    client_path = os.path.abspath(os.curdir)

Buscar Missing values
---------------------

.. code-block:: python

    from BTrees.IIBTree import difference
    from BTrees.IIBTree import IISet
    from plone import api

    catalog = api.portal.get_tool(name='portal_catalog')
    date_index = catalog._catalog.getIndex('fecha_termino')
    date_referenced = IISet(date_index.referencedObjects())
    other_index = catalog._catalog.getIndex('sponsor')
    other_referenced = IISet(other_index.referencedObjects())
    missing = difference(other_referenced, date_referenced)
    paths = [catalog.getpath(cat_record) for cat_record in missing]

* `How can I look for objects with missing value or None as key? <https://stackoverflow.com/questions/11216472/how-can-i-look-for-objects-with-missing-value-or-none-as-key>`_


Operaciónes con fechas
----------------------


.. code-block:: python

    from datetime import datetime
    from datetime import timedelta

    timeout = 60 * 60 * 12

    token['time'] = time.time()

    def _valid_token(token):
        expdate = datetime.utcfromtimestamp(token['time']) + timedelta(seconds=timeout)
        return datetime.utcnow() < expdate




----

* `Expressions <https://docs.plone.org/develop/plone/functionality/expressions.html>`_
* `Static resources <https://docs.plone.org/external/plone.app.dexterity/docs/advanced/static-resources.html>`_
* `CSS <https://docs.plone.org/adapt-and-extend/theming/templates_css/css.html>`_
