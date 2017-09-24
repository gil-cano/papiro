Nginx
=====

Descripcion de Nginx .....
high performance web server nginx [engine x] is an HTTP and reverse proxy server,
as well as a mail proxy server.

Instalación
-----------

Para instalar `nginx <http://nginx.org/>`_ 1.8.0-1~jessie en Debian GNU/Linux 8.2 (jessie)

.. code-block:: bash

    $ wget http://nginx.org/keys/nginx_signing.key
    $ apt-key add nginx_signing.key
    $ echo "deb http://nginx.org/packages/debian/ jessie nginx" >> /etc/apt/sources.list
    $ echo "deb-src http://nginx.org/packages/debian/ jessie nginx" >> /etc/apt/sources.list
    $ apt-get update
    $ apt-get install nginx

Verificamos que se instalo bien

.. code-block:: bash

    $ nginx -V
    nginx version: nginx/1.8.0
    built by gcc 4.9.2 (Debian 4.9.2-10)
    built with OpenSSL 1.0.1k 8 Jan 2015
    TLS SNI support enabled
    configure arguments:



Iniciar / Detener / Recargar configuración
------------------------------------------

Para detener los processos de nginx hasta que terminen de responder las peticiones actuales.
(Debe ser ejecutado por el mismo usuario que inicio nginx)

.. code-block:: bash

    $ nginx -s quit

Para recargar la configuración

.. code-block:: bash

    $ nginx -s reload

Para obtener la lista de los processos que se están ejecutando

.. code-block:: bash

    $ ps -ax | grep nginx


Configuración
-------------

El archivo de configuración se llama *nginx.conf* y encuentra en */etc/nginx/nginx.conf*

Para verificar que el archivo de configuración es valido, ejecutamos

.. code-block:: bash

    $ nginx -t

nginx consiste de modulos que son controlados por directivas

Una directiva simple consiste en el nombre y parametros separados por espacios y terminan con punto y coma(;)

.. literalinclude:: nginx.conf
    :language: bash
    :lines: 1-5

Una directiva de bloque tiene la misma estructura que una directiva simple, pero en vez del punto y coma termina con un conjunto adicional de instrucciones entre corchetes ({ }).

.. literalinclude:: nginx.conf
    :language: bash
    :lines: 7-14, 25-28, 58


Contenido estatico
~~~~~~~~~~~~~~~~~~

.. literalinclude:: nginx.conf
    :language: bash
    :lines: 29-37

Plone
~~~~~

.. literalinclude:: nginx.conf
    :language: bash
    :lines: 39-57


Sublime Text 3
--------------
`<https://github.com/brandonwamboldt/sublime-nginx>`_