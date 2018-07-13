====
Brew
====

.. topic:: Description

   This text will go to Plone's pages description field.

Instalación
-----------


instalar paquete::

   $ brew install <formula>


Listar paquetes::

   $ brew list


Actualizar lista de paquetes disponibles::

   $ brew update

listar formulas no actualizadas::

   $ brew outdated

actualizar formula::

   $ brew upgrade <formula>


información de formula::

   $ brew info <formula>

Compilar `buildout.python <https://github.com/collective/buildout.python>`_ y Plone
-----------------------------------------------------------------------------------

En macOS necesitasmos instalar algunas dependencias con Homebrew:

.. code-block:: shell

   $ brew install openssl

   If you need to have this software first in your PATH run:
     echo 'export PATH="/usr/local/opt/openssl/bin:$PATH"' >> ~/.zshrc

   For compilers to find this software you may need to set:
       LDFLAGS:  -L/usr/local/opt/openssl/lib
       CPPFLAGS: -I/usr/local/opt/openssl/include


.. code-block:: shell

   $ brew install zlib readline jpeg libpng libyaml


   ==> Pouring zlib-1.2.11.el_capitan.bottle.tar.gz

   For compilers to find this software you may need to set:
       LDFLAGS:  -L/usr/local/opt/zlib/lib
       CPPFLAGS: -I/usr/local/opt/zlib/include


   ==> Pouring readline-7.0.3_1.el_capitan.bottle.tar.gz

   For compilers to find this software you may need to set:
       LDFLAGS:  -L/usr/local/opt/readline/lib
       CPPFLAGS: -I/usr/local/opt/readline/include


Para ``pdftotext``

.. code-block:: shell

   $ brew install poppler

   ==> Pouring gettext-0.19.8.1.el_capitan.bottle.tar.gz

   For compilers to find this software you may need to set:
       LDFLAGS:  -L/usr/local/opt/gettext/lib
       CPPFLAGS: -I/usr/local/opt/gettext/include

   ==> Pouring libffi-3.2.1.el_capitan.bottle.tar.gz

   For compilers to find this software you may need to set:
       LDFLAGS:  -L/usr/local/opt/libffi/lib


``wv`` permite el acceso a archivos de tipo Microsoft Word

.. code-block:: shell

   $ brew install wv

.. code-block:: shell

   $ brew install wget pandoc gnupg

.. code-block:: shell

   $ brew info cgal
   $ brew install cgal --with-lapack --with-eigen --with-qt

   ==> Pouring qt-5.10.1.el_capitan.bottle.tar.gz

   If you need to have this software first in your PATH run:
     echo 'export PATH="/usr/local/opt/qt/bin:$PATH"' >> ~/.zshrc

   For compilers to find this software you may need to set:
       LDFLAGS:  -L/usr/local/opt/qt/lib
       CPPFLAGS: -I/usr/local/opt/qt/include

Bibliografía
------------

* `Homebrew FAQ <https://docs.brew.sh/FAQ.html>`_
