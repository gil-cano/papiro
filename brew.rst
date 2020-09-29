.. _brew:

========
Homebrew
========

.. topic:: Description

   This text will go to Plone's pages description field.

`Homebrew <https://brew.sh>`_


Instalación
-----------


instalar paquete::

   $ brew install <formula>


Listar paquetes::

   $ brew list

Detalles del paquete::

   $ brew list zsh

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

MacOS Mojave (10.14.6)

Necesitamos instalar Command_Line_Tools (para compilar python2.4 la version 10.14_for_Xcode_10.3) 

En macOS necesitasmos instalar algunas dependencias con Homebrew:

.. code-block:: shell

   $ brew install openssl@1.1
   ==> Pouring openssl@1.1-1.1.1d.mojave.bottle.tar.gz
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

Para Python 2.4

.. code-block:: shell

   $ brew install openssl
   If you need to have openssl first in your PATH run:
     echo 'export PATH="/usr/local/opt/openssl/bin:$PATH"' >> ~/.bash_profile

   For compilers to find openssl you may need to set:
     export LDFLAGS="-L/usr/local/opt/openssl/lib"
     export CPPFLAGS="-I/usr/local/opt/openssl/include"


Antes de compilar python debemos instalar ``gdbm`` para tener disponible ese modulo.

``gdbm`` es necesario para usar el profiler de Zope (Control_Panel/DebugInfo)

.. code-block:: shell

   $ brew install gdbm

``xz`` para tener liblzma

.. code-block:: shell

   $ brew install xz



.. code-block:: shell

   $ brew install zlib readline jpeg libpng libyaml


   ==> Pouring zlib-1.2.11.mojave.bottle.tar.gz

   For compilers to find this software you may need to set:
       export LDFLAGS="-L/usr/local/opt/zlib/lib"
       export CPPFLAGS="-I/usr/local/opt/zlib/include"

   ==> Pouring readline-8.0.1.mojave.bottle.tar.gz

   For compilers to find this software you may need to set:
       export LDFLAGS="-L/usr/local/opt/readline/lib"
       export CPPFLAGS="-I/usr/local/opt/readline/include"

.. code-block:: shell

   $ brew install gettext little-cms2

Para ``pdftotext``

.. code-block:: shell

   $ brew install poppler

   ==> Pouring gettext-0.20.1.mojave.bottle.tar.gz
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


Instalamos Command Line Tools

Para python 2.4 necesitas zlib en /usr/include

.. code-block:: shell

    $ sudo installer -pkg /Library/Developer/CommandLineTools/Packages/macOS_SDK_headers_for_macOS_10.14.pkg -target /

.. warning:
  
  Para catlina y zlib problem ver https://akrabat.com/installing-pillow-on-macos-10-15-calatalina/

.. code-block:: shell

    $ git clone https://github.com/collective/buildout.python.git
    $ cd buildout.python
    $ /usr/bin/python bootstrap.py
    $ ./bin/buildout -c local.cfg

Si hay probelmas con bootstrap.py cambiar linea 74 por  

.. code-block:: python
    
    exec urllib2.urlopen('http://132.248.17.205/listas/ez_setup.py'


El archivo local.cfg queda como sigue:

.. code-block:: shell

    [buildout]
    index = https://pypi.org/simple/
    extends =
      buildout.cfg
      src/pdbsublimetext.cfg

    parts =
        ${buildout:base-parts}
        ${buildout:readline-parts}
        ${buildout:zlib-parts}
        ${buildout:python24-parts}
        ${buildout:python27-parts}
        ${buildout:python37-parts}
        ${buildout:python38-parts}
        ${buildout:links-parts}
    #    python-2.7-pdbsublimetext


    [python-2.7-build:default]
    environment =
        LDFLAGS=-L/usr/local/opt/zlib/lib -L/usr/local/opt/readline/lib
        CPPFLAGS=-I/usr/local/opt/zlib/include -I/usr/local/opt/readline/include

    [python-3.7-build:default]
    environment =
        LDFLAGS=-L/usr/local/opt/zlib/lib -L/usr/local/opt/readline/lib
        CPPFLAGS=-I/usr/local/opt/zlib/include -I/usr/local/opt/readline/include

    [python-3.8-build:default]
    environment =
        LDFLAGS=-L/usr/local/opt/openssl@1.1/lib -L/usr/local/opt/zlib/lib -L/usr/local/opt/readline/lib
        CPPFLAGS=-I/usr/local/opt/openssl@1.1/include -I/usr/local/opt/zlib/include -I/usr/local/opt/readline/include

    [install-links]
    prefix = /Users/gil/local


Para Python 2.4 modificamos el archivo src/python24.cfg

.. code-block:: shell

    [python-2.4]
    recipe = plone.recipe.command
    location = ${buildout:directory}/python-2.4
    executable = ${python-2.4-build:executable}
    easy_install = ${opt:location}/bin/easy_install-2.4
    command =
        ${:executable} ${buildout:python-buildout-root}/ez_setup-1.x.py
        ${:easy_install} pip==1.1
        ${python-2.4-virtualenv:output} --system-site-packages ${:location}
        ${:location}/bin/pip install --pypi-url=https://pypi.python.org/simple docutils==0.15.2
        ${:location}/bin/pip install --pypi-url=https://pypi.python.org/simple collective.dist
    update-command = ${:command}
    stop-on-error = yes

Plone 2.1.4
~~~~~~~~~~~

.. code-block:: shell

    cd plone2.1.4
    /Users/user/buildout.python3.8/bin/virtualenv-2.4 .
    bin/pip install -r requirements.txt --pypi-url=https://pypi.python.org/simple
    bin/pip install --pypi-url=https://pypi.python.org/simple zc.buildout==1.4.2


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
