Pruebas
-------

Las pruebas unitarias (*unit tests*)

Unit tests are automated tests created by the developer to ensure that the add-on product is intact in the current product configuration. Unit tests are regression tests and are designed to catch broken functionality over the code evolution.


For each test:
* The test user is logged in


.. code-block:: console

    bin/test -t TestInstallation

Bibliografía
------------

* `plone.app.testing's documentation <http://docs.plone.org/external/plone.app.testing/docs/source/README.html>`_

* `Dexterity Integration tests <http://docs.plone.org/external/plone.app.dexterity/docs/testing/integration-tests.html>`_

* `plonetraining.testing <http://plonetrainingtesting.readthedocs.io/en/latest/index.html>`_

* `collective.nitf testing <https://github.com/collective/collective.nitf/blob/master/src/collective/nitf/tests/test_views.py>`_