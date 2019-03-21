.. _varnishcache:

Varniscache
===========

.. code-block:: shell

   $ sudo apt-get install debian-archive-keyring
   $ sudo apt-get install curl gnupg apt-transport-https
   # $ curl -L https://packagecloud.io/varnishcache/varnish52/gpgkey | sudo apt-key add -
   $ curl -L https://packagecloud.io/varnishcache/varnish60lts/gpgkey | sudo apt-key add -


.. code-block:: shell

   $ sudo bash -c 'echo "deb https://packagecloud.io/varnishcache/varnish60lts/debian/ jessie main" >> /etc/apt/sources.list.d/varnishcache.list'
   $ sudo bash -c 'echo "deb-src https://packagecloud.io/varnishcache/varnish60lts/debian/ jessie main" >> /etc/apt/sources.list.d/varnishcache.list'


* `Varnish Installation instructions <https://packagecloud.io/varnishcache/varnish60lts/install#manual-deb>`_


