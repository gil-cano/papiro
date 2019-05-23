Solucion a algunos errores
==========================

ConfigurationError: ('Unknown directive', u'http://namespaces.plone.org/plone', u'service')

.. note::

    To use the plone:service directive you must include the meta.zcml.

    You must do <include package="plone.rest" file="meta.zcml"/> before you can use the plone:service directive.
    So: add the line <include package="plone.rest" file="meta.zcml"/> before the usage of plone:service.
