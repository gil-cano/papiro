Solución de algunos errores
===========================

.. code-block:: rst

    ConfigurationError: ('Unknown directive', u'http://namespaces.plone.org/plone', u'service')

To use the :command:`plone:service` directive you must include the :file:`meta.zcml`.

You must do :code:`<include package="plone.rest" file="meta.zcml"/>` before you can use the :command:`plone:service` directive.

So: add the line :code:`<include package="plone.rest" file="meta.zcml"/>` before the usage of :command:`plone:service`.

* `How to resolve ConfigurationError error 'Unknown directive' in Plone? <https://stackoverflow.com/questions/23533465/how-to-resolve-configurationerror-error-unknown-directive-in-plone>`_
