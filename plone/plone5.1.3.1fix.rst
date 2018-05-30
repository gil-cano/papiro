==========================
Contribute to Translations
==========================

.. note::

    Plone 5.1.3.dev0 (5113)
    CMF 2.2.12
    Zope 2.13.27
    Python 2.7.14 (default, Apr 6 2018, 01:24:42) [GCC 4.2.1 Compatible Apple LLVM 7.3.0 (clang-703.0.29)]
    PIL 4.3.0 (Pillow)

`Plone translation dictionary <https://github.com/collective/plone.app.locales/blob/master/docs/terms-es.txt>`_

How to rebuild plone.app.locales POT files of Plone core?
=========================================================

* `How to rebuild plone.app.locales POT files of Plone core? <https://community.plone.org/t/how-to-rebuild-plone-app-locales-pot-files-of-plone-core/2799>`_
* `How To Contribute To Plone Core Translations <https://docs.plone.org/develop/plone/i18n/contribute_to_translations.html>`_

https://github.com/plone/mockup/blob/master/README.rst

.. code-block:: shell

    $ cd mockup
    $ make i18n-dump
    $ cp widgets.pot plone.app.locales/plone/app/locales/locales/widgets.pot


https://github.com/collective/plone.app.locales/blob/master/utils/README.txt

.. code-block:: shell

    $ cd plone5devel
    $ bin/i18n widgets



Log in popup
============

No se traduce la parte superior "log in"
Products/CMFPlone/profiles/default/actions.xml
<property name="modal" type="text">{"prependContent": ".portalMessage", "title": "Log in", "width": "26em", "actionOptions": {"redirectOnResponse": true}}</property>


Vista folder_contents
=====================

Faltán muchas etiquetas por traducir.

This only deals with the fact that some items are missing the _t('')-method.

One example:
https://github.com/plone/mockup
mockup/patterns/structure/js/views/app.js
there is no translation for "tooltip: _t('Manage selection')"



typo fix in error message