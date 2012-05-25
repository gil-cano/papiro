Introduction
============

This package provides the source for documentation of some tools used for Plone development.

To read the documentation (formatted) in your web browser, please head to `??? <>`_.

To learn how to update and manage this documentation and its tools, read `??? <>`_.


Building The Documentation
--------------------------

After cloning this package from the repository, do the following::

  $ cd templer.maual  # the location of your local copy
  $ python bootstrap.py  # must be Python 2.6 or 2.7
  $ ../bin/buildout
  $ ../bin/sphinx

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

Copyright © 2011-2012 Gildardo Bautista.
