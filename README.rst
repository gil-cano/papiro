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

0. Clone and bootstrap

   .. code:: bash

      $ git clone git://github.com/gil-cano/papiro.git
      $ cd papiro

      $ python bootstrap.py
      $ bin/buildout

At the end of a successful build, you will see the location of the
resulting HTML pages.


Continous Integration
---------------------

This code base uses Travis CI continuous integration to check the integrity of the source files.

Failed manual complies will be reported

See ``.travis.yml`` file for continuous integration settings.

* `Travis build page <http://travis-ci.org/#!/collective/collective.developermanual>`_

License
-------

Copyright © 2011-2014 Gildardo Bautista.

https://github.com/collective/collective.developermanual/blob/master/README.rst

https://github.com/cewing/templer.manual
