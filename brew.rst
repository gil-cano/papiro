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

   $ brew install openssl@1.1
   ==> Pouring openssl@1.1-1.1.1.mojave.bottle.tar.gz
   ==> Caveats
   A CA file has been bootstrapped using certificates from the system
   keychain. To add additional certificates, place .pem files in
     /usr/local/etc/openssl@1.1/certs

   and run
     /usr/local/opt/openssl@1.1/bin/c_rehash

   openssl@1.1 is keg-only, which means it was not symlinked into /usr/local,
   because this is an alternate version of another formula.

   If you need to have openssl@1.1 first in your PATH run:
     echo 'export PATH="/usr/local/opt/openssl@1.1/bin:$PATH"' >> ~/.zshrc

   For compilers to find openssl@1.1 you may need to set:
     export LDFLAGS="-L/usr/local/opt/openssl@1.1/lib"
     export CPPFLAGS="-I/usr/local/opt/openssl@1.1/include"

Antes de compilar python debemos instalar ``gdbm`` para tener disponible ese modulo.

``gdbm`` es necesario para usar el profiler de Zope (Control_Panel/DebugInfo)

.. code-block:: shell

   $ brew install gdbm

``xz`` para tener liblzma

.. code-block:: shell

   $ brew install xz



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

   ==> Pouring gettext-0.19.8.1.mojave.bottle.tar.gz
   ==> Caveats
   gettext is keg-only, which means it was not symlinked into /usr/local,
   because macOS provides the BSD gettext library & some software gets confused if both are in the library path.

   If you need to have gettext first in your PATH run:
     echo 'export PATH="/usr/local/opt/gettext/bin:$PATH"' >> ~/.bash_profile

   For compilers to find gettext you may need to set:
     export LDFLAGS="-L/usr/local/opt/gettext/lib"
     export CPPFLAGS="-I/usr/local/opt/gettext/include"

   ==> Pouring libffi-3.2.1.mojave.bottle.tar.gz

   For compilers to find libffi you may need to set:
       export LDFLAGS="-L/usr/local/opt/libffi/lib"
       
   ==> Pouring nss-3.40.mojave.bottle.tar.gz

   If you need to have nss first in your PATH run:
     echo 'export PATH="/usr/local/opt/nss/bin:$PATH"' >> ~/.bash_profile

   For compilers to find nss you may need to set:
     export LDFLAGS="-L/usr/local/opt/nss/lib"
     export CPPFLAGS="-I/usr/local/opt/nss/include"

Para agregar gettext al path modificamos el archivo .zshrc

.. code-block:: shell

    export PATH=/usr/local/opt/gettext/bin:$PATH


``wv`` permite el acceso a archivos de tipo Microsoft Word

.. code-block:: shell

   $ brew install wv

.. code-block:: shell

   $ brew install wget pandoc gnupg

Latex y skim ver Sublimetext3
-----------------------------

.. code-block:: shell

   $ brew install imagemagick

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
