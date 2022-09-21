=====
Nginx
=====

Descripcion de Nginx .....
high performance web server nginx [engine x] is an HTTP and reverse proxy server,
as well as a mail proxy server.

Instalación
===========

Para instalar `nginx <http://nginx.org/>`_ 1.14.2 en Debian GNU/Linux 8.11 (jessie)

.. code-block:: shell

    $ wget http://nginx.org/keys/nginx_signing.key
    $ sudo apt-key add nginx_signing.key
    $ sudo bash -c 'echo "deb http://nginx.org/packages/debian/ jessie nginx" >> /etc/apt/sources.list.d/nginx.list'
    $ sudo bash -c 'echo "deb-src http://nginx.org/packages/debian/ jessie nginx" >> /etc/apt/sources.list.d/nginx.list'
    $ sudo apt-get update
    $ sudo apt-get install nginx

Verificamos que se instalo bien

.. code-block:: shell

    $ nginx -V
    nginx version: nginx/1.14.2
    built by gcc 4.9.2 (Debian 4.9.2-10)
    built with OpenSSL 1.0.1k 8 Jan 2015
    TLS SNI support enabled
    configure arguments:



Iniciar / Detener / Recargar configuración
------------------------------------------

Para detener los processos de nginx hasta que terminen de responder las peticiones actuales.
(Debe ser ejecutado por el mismo usuario que inicio nginx)

.. code-block:: shell

    $ nginx -s quit

Para recargar la configuración

.. code-block:: shell

    $ nginx -s reload

Para obtener la lista de los processos que se están ejecutando

.. code-block:: shell

    $ ps -ax | grep nginx


Configuración
-------------

El archivo de configuración se llama *nginx.conf* y encuentra en */etc/nginx/nginx.conf*

Para verificar que el archivo de configuración es valido, ejecutamos

.. code-block:: shell

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



Github webHooks
===============

Agregamos la siguiente configuración en nginx

.. code-block:: nginx

   server {
     listen 80;
     server_name example.org;
     access_log  /var/log/nginx/example.log;

    location /rog-one {
        root /var/www;
    }

     location /rog-update {
         proxy_pass http://127.0.0.1:4000;

         proxy_set_header Host $host;
         proxy_set_header X-Real-IP $remote_addr;
         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
     }
   }


preparamos una instancia de python 2.7 con lo sigiente

.. code-block:: shell

   $ /python2.7_webpy/bin/pip install web.py flup GitPython gunicorn


.. code-block:: shell

   $ cd /var/www/
   $ sudo mkdir [site_dir]
   $ sudo chown -R www-data:www-data /var/www/[site_dir]
   $ sudo su - -s /bin/bash www-data
   $ git clone https://github.com/poryect.git [site_dir]/
   $ cd [site_dir]
   $ touch yourapp.py


.. code-block:: python

    #! /usr/bin/env /python2.7_webpy/bin/python
    import git
    import web

    urls = ("/.*", "update")
    app = web.application(urls, globals())
    wsgiapp = app.wsgifunc()

    class update:
        def POST(self):
            g = git.cmd.Git('/var/www/[site_dir]')
            g.pull()
            rval = g.ls_files()
            return rval

    if __name__ == "__main__":
        app.run()


.. code-block:: shell

   $ sudo -u www-data /python2.7_webpy/bin/gunicorn -b 127.0.0.1:4000 yourapp:wsgiapp


.httpasswd
----------

.. code-block:: shell

   $ sudo htpasswd -c /etc/nginx/.htpasswd sammy
   $ sudo htpasswd /etc/nginx/.htpasswd another_user


html path
----------

.. code-block:: shell

   $ cd /usr/share/nginx/html

References
----------

* `JHow To Set Up Password Authentication with Nginx on Ubuntu 14.04 <https://www.digitalocean.com/community/tutorials/how-to-set-up-password-authentication-with-nginx-on-ubuntu-14-04>`_

* `fail2ban <https://easyengine.io/tutorials/nginx/fail2ban>`_

* `Pitfalls and Common Mistakes <https://www.nginx.com/resources/wiki/start/topics/tutorials/config_pitfalls/>`_

* `Understanding Nginx Server and Location Block Selection Algorithms <https://www.digitalocean.com/community/tutorials/understanding-nginx-server-and-location-block-selection-algorithms>`_

* `Configuring NGINX Plus as a Web Server <https://docs.nginx.com/nginx/admin-guide/web-server/web-server/>`_
