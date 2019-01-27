Papiro
=======

This repository is a work in progress

.. contents:: :local:

Introduction
------------

This package provides the source for documentation of some tools used for Plone development.

To read the documentation (formatted) in your web browser, please head to `??? <http://localhost>`_.

To learn how to update and manage this documentation and its tools, read `??? <http://localhost>`_.


Building The Documentation
--------------------------

Con pipenv

.. code:: bash

    $ git clone https://github.com/gil-cano/papiro.git
    $ cd papiro
    $ pipenv install
    $ pipenv run make html

con pip y virtualenv

.. code:: bash

    $ git clone https://github.com/gil-cano/papiro.git
    $ cd papiro
    $ virtualenv-3.6 .
    $ source bin/activate
    (papiro)$ pip install -r requirements.txt
    (papiro)$ make html



At the end of a successful build, you will see the location of the
resulting HTML pages.


Link Testing
------------

.. code:: bash

    $ pipenv run make linkcheck


License
-------

Copyright © 2011-2018 Gildardo Bautista.
