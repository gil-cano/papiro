Cadenas
=======


.. sourcecode:: python

    from Products.CMFPlone.utils import safe_unicode
    >>> safe_unicode('ÅÄÖrjy')
    u'\xc5\xc4\xd6rjy'
    >>> safe_unicode(u'ÅÄÖrjy')
    u'\xc3\x85\xc3\x84\xc3\x96rjy'

Normalizar
----------
.. sourcecode:: python

    >>> from plone.i18n.normalizer import filenamenormalizer
    >>> from plone.i18n.normalizer import idnormalizer
    >>> from plone.i18n.normalizer import urlnormalizer

    >>> idnormalizer.normalize(u"ÅÄÖrjy")
    'aaarjy'
    >>> idnormalizer.normalize(safe_unicode('ÅÄÖrjy'))
    'aaorjy'
    >>> idnormalizer.normalize(safe_unicode(u'ÅÄÖrjy'))
    'aaarjy'


Elimina vacios de lista

.. sourcecode:: python

    filter(None, newlist)

Directorios
===========

.. sourcecode:: python

    os.path.abspath(os.curdir)

    os.path.join()


.. sourcecode:: python

    for root, dirs, files in os.walk('/path/to/my/directory'):