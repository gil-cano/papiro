Debian
======

.. code-block:: bash

    $ sudo apt-get update
    $ sudo apt-get upgrade


.. code-block:: bash

    $ apt-cache policy haproxy
    haproxy:
      Installed: 1.5.14-1~bpo8+1
      Candidate: 1.6.5-1~bpo8+1
      Version table:
         1.6.5-1~bpo8+1 0
            100 http://http.debian.net/debian/ jessie-backports/main amd64 Packages
     *** 1.5.14-1~bpo8+1 0
            100 /var/lib/dpkg/status
         1.5.8-3+deb8u2 0
            500 http://mmc.geofisica.unam.mx/debian/ jessie/main amd64 Packages
         1.5.8-3+deb8u1 0
            500 http://security.debian.org/ jessie/updates/main amd64 Packages



`buildout.python <https://github.com/collective/buildout.python>`_
------------------------------------------------------------------

Trying to install PIL for python2.4

.. code-block:: bash


    fatal error: freetype/fterrors.h: No such file or directory

The version of freetype is 2, I guess it's the problem.

.. code-block:: bash

    $ cd /usr/include
    $ ln -s freetype2 freetype


Procesos muertos
----------------

.. code-block:: bash

    $ ps -ef | grep defunct
