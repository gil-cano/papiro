.. _brew:

========
Homebrew
========

.. topic:: Description

   This text will go to Plone's pages description field.

`Homebrew <https://brew.sh>`_


Instalación
-----------

.. code-block:: shell
   
   ==> The following new directories will be created:
   /usr/local/bin
/usr/local/etc
/usr/local/include
/usr/local/lib
/usr/local/sbin
/usr/local/share
/usr/local/var
/usr/local/opt
/usr/local/share/zsh
/usr/local/share/zsh/site-functions
/usr/local/var/homebrew
/usr/local/var/homebrew/linked
/usr/local/Cellar
/usr/local/Caskroom
/usr/local/Frameworks
==> The Xcode Command Line Tools will be installed.




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

MacOS Catalina (10.15.7)

Necesitamos instalar Command_Line_Tools (para compilar python2.4 la version 10.14_for_Xcode_10.3) 

.. code-block:: shell

   $ xcode-select -p
   /Library/Developer/CommandLineTools


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

   For pkg-config to find openssl@1.1 you may need to set:
     export PKG_CONFIG_PATH="/usr/local/opt/openssl@1.1/lib/pkgconfig"

Python 2.4  solo soporta hasta la versión 1.0.x de OpenSSL, pero homebrew removio la formula 1.0

.. code-block:: shell

   $ brew install mjpieters/tap/openssl@1.0
   If you need to have openssl@1.0 first in your PATH, run:
     echo 'export PATH="/usr/local/opt/openssl@1.0/bin:$PATH"' >> ~/.zshrc

   For compilers to find openssl@1.0 you may need to set:
     export LDFLAGS="-L/usr/local/opt/openssl@1.0/lib"
     export CPPFLAGS="-I/usr/local/opt/openssl@1.0/include"

   For pkg-config to find openssl@1.0 you may need to set:
     export PKG_CONFIG_PATH="/usr/local/opt/openssl@1.0/lib/pkgconfig"


Antes de compilar python debemos instalar ``gdbm`` para tener disponible ese modulo.

``gdbm`` es necesario para usar el profiler de Zope (Control_Panel/DebugInfo)

.. code-block:: shell

   $ brew install gdbm

``xz`` para tener liblzma

.. code-block:: shell

   $ brew install xz

.. code-block:: shell

   $ brew install git
   $ brew link --overwrite git

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

Para agregar gettext al path modificamos el archivo ``.zshrc``

.. code-block:: shell

    export PATH=/usr/local/opt/gettext/bin:$PATH


``wv`` permite el acceso a archivos de tipo Microsoft Word

.. code-block:: shell

   $ brew install wv


Instalamos Command Line Tools

Para compilar

.. code-block:: shell

   $ git clone https://github.com/collective/buildout.python.git
   $ cd buildout.python
   $ /usr/bin/python bootstrap.py
   $ ./bin/buildout -c local.cfg


El archivo local.cfg queda como sigue:

.. code-block:: shell

    # This is here just for backward compatibility
    [buildout]
    extends =
        src/base.cfg
        src/readline.cfg
        src/zlib.cfg
        src/openssl10.cfg
        src/python24.cfg
        src/python27.cfg
        src/python37.cfg
        src/python38.cfg
        src/python39.cfg
        src/links.cfg

    parts =
        ${buildout:base-parts}
        ${buildout:readline-parts}
        ${buildout:zlib-parts}
        ${buildout:openssl10-parts}
        ${buildout:python24-parts}
        ${buildout:python27-parts}
        ${buildout:python37-parts}
        ${buildout:python38-parts}
        ${buildout:python39-parts}
        ${buildout:links-parts}

    python-buildout-root = ${buildout:directory}/src

    # we want our own eggs directory and nothing shared from a
    # ~/.buildout/default.cfg to prevent any errors and interference
    eggs-directory = eggs

    [install-links]
    prefix = /Users/gil/local


Para Python 2.4 modificamos el archivo src/python24.cfg, en la parte python-2.4 comentamos la linea que instala docutils
    
    .. code-block:: shell
    
        [python-2.4]
        recipe = plone.recipe.command
        location = ${buildout:directory}/python-2.4
        executable = ${python-2.4-build:executable}
        easy_install = ${opt:location}/bin/easy_install-2.4
        command =
            ${:executable} ${buildout:python-buildout-root}/scripts/ez_setup-1.x.py
            ${:easy_install} pip==1.1
            ${python-2.4-virtualenv:output} --system-site-packages ${:location}
            # ${:location}/bin/pip install --pypi-url=https://pypi.python.org/simple 'docutils<0.15dev' collective.dist
        
        update-command = ${:command}
        stop-on-error = yes

Instalamos docutils y collective.dist manualmente
    
    .. code-block:: shell
        
            $ python-2.4/bin/pip install ~/.buildout/downloads/dist/docutils-0.14.tar.gz
            $ python-2.4/bin/pip install ~/.buildout/downloads/dist/collective.dist-0.2.5.tar.gz
        
    

        
Si hay probelmas con bootstrap.py cambiar linea 74 por  

    .. code-block:: python
            
       exec urllib2.urlopen('http://132.248.17.205/listas/ez_setup.py'
 



Para python 2.4 necesitas zlib en /usr/include (probablemente ya no sea necesario)

.. code-block:: shell

   $ sudo installer -pkg /Library/Developer/CommandLineTools/Packages/macOS_SDK_headers_for_macOS_10.14.pkg -target /

.. warning:
   
   Para catlina y zlib problem ver https://akrabat.com/installing-pillow-on-macos-10-15-calatalina/
   
   .. code-block:: shell
   
      export CPATH=`xcrun --show-sdk-path`/usr/include
   

En caso de que no encuentre zlib o openssl

.. code-block:: shell

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


Desinstalar HomeBrew
--------------------

.. code-block:: shell

    $ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/uninstall.sh)"

Asegurate de eliminar  ``/usr/local/Homebrew/``

Bibliografía
------------

* `Homebrew FAQ <https://docs.brew.sh/FAQ.html>`_
* `Homebrew (un)installer <https://github.com/homebrew/install#uninstall-homebrew>`_
