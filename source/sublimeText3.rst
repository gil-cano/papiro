Sublime Text 3
==============

.. _chapter_content:

Linea de comandos en OS X
-------------------------

Sublime Text 3 incluye el comando, *subl*, para abrir archivos desde una terminal.

.. code-block:: bash

   $ ln -s "/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl" /opt/local/bin/subl

Agregamos el directorio /opt/local/bin a nuestro path en el archivo .bash_profile

.. code-block:: console

   export PATH=/opt/local/bin/:$PATH

User Settings
-------------

Configura tus preferencias abriendo *Preferences* -> *Settings - User*.

.. code-block:: json

    {
        "ignored_packages":
        [
            "Vintage"
        ],
        "rulers":
        [
            // set text rulers so I can judge line length for pep8
            72, // docstrings
            79, // optimum code line length
            100  // maximum allowable length
        ],
        "tab_size": 4,
        "translate_tabs_to_spaces": true,
        // "trim_trailing_white_space_on_save": true,
        "use_tab_stops": true,
    }

Package Control
---------------

La instalación de `Package Control <https://sublime.wbond.net/installation>`_ es atravez de la consola de Sublime Text (ctrl + \`). Una vez abierta pegamos lo siguiente (Es mejor tomarlo de la pagina original):

.. code-block:: console

   import urllib.request,os,hashlib; h = '7183a2d3e96f11eeadd761d777e62404' + 'e330c659d4bb41d3bdf022e94cab3cd0'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://sublime.wbond.net/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)

Este comando descarga el paquete *Control.sublime-package*.

Para instalar nuevos plugins abrimos la paleta de comandos con *shift + command + p*. Cuando se habra la paleta escribimos *install* y buscamos el comando *Package Control: Install Package*.


Autocompletar
-------------

`SublimeJedi <https://github.com/srusskih/SublimeJEDI>`_

Usamos la siguiente configuración para definir el interprete de python usado en el proyecto. Por default el archivo de un proyecto es *<project name>.sublime-project*

(para crear un proyecto abrir los archivos son sublimetext y despues *Project -> save Project as*)

(para editarlo *Project -> Edit Project*)

.. code-block:: json

    {
        "folders":
        [
            {
                "follow_symlinks": true,
                "path": "src-git"
            }
        ],
        "settings": {
            // ...
            "python_interpreter_path": "/opt/local/bin/python2.7",

            "python_package_paths": [
                "/Users/gil/projects/plone/matem-buildout/parts/omelette"
            ]
        }
    }

Para ir a la definición de un simbolo usamos *ctrl + shift + g*.

Para buscar otros lugares donde se use el simbolo usamos *alt + shift + f*.

Lint (flake8)
-------------

Muestra errores que cometiste en el código.

Primero creamos un ambiente virtual y lo activamos

.. code-block:: console

    $ cd /Users/gil/buildout.python
    $ virtualenv-2.7 sublenv
    New python executable in sublenv/bin/python2.7
    Installing setuptools, pip...done.
    $ source sublenv/bin/activate
    (sublenv)$

Instalamos los paquetes necesarios (`flake8 <https://pypi.python.org/pypi/flake8>`_)

.. code-block:: console

    (sublenv)$ pip install flake8
    Downloading/unpacking flake8
    [...]
    Downloading/unpacking pyflakes>=0.7.3 (from flake8)
    [...]
    Downloading/unpacking pep8>=1.4.6 (from flake8)
    [...]
    Downloading/unpacking mccabe>=0.2.1 (from flake8)
    [...]
    Installing collected packages: flake8, pyflakes, pep8, mccabe
    [...]
    Successfully installed flake8 pyflakes pep8 mccabe
    Cleaning up...
    (sublenv)$

Instalamos `SublimeLinter <http://sublimelinter.readthedocs.org/en/latest/>`_ y despues `SublimeLinter-flake8 <https://github.com/SublimeLinter/SublimeLinter-flake8>`_ usando el Package Control.

Agregamos la siguiente configuración en *Preferences -> Package Settings -> SublimeLinter -> Settings - User*:

.. code-block:: json

    {
        //...
        "linters": {
            "flake8": {
                "@disable": false,
                "args": [],
                "builtins": "",
                "excludes": [],
                "ignore": "",
                "max-complexity": 10,
                "max-line-length": null,
                "select": ""
            }
        },
        //...
        "paths": {
            "linux": [],
            "osx": [
                "/Users/gil/buildout.python/sublenv/bin"
            ],
            "windows": []
        },
        "python_paths": {
            "linux": [],
            "osx": [
                "/Users/gil/buildout.python/sublenv/bin"
            ],
            "windows": []
        },
        //...
    }

Lints (jshint / csslit)
-----------------------

Instalamos `node.js <http://nodejs.org/>`_ (v0.10.26)

.. code-block:: console

    Node was installed at

       /usr/local/bin/node

    npm was installed at

       /usr/local/bin/npm

    Make sure that /usr/local/bin is in your $PATH.

Instalamos `jslint <http://www.jshint.com/>`_ y `csslint <http://csslint.net/>`_

.. code-block:: console

    $ sudo npm install -g jslint
    $ sudo npm install -g csslint

En sublimetext instalamos `sublimelinter-jshint <https://github.com/SublimeLinter/SublimeLinter-jshint>`_ y `sublimelinter-csslint <https://github.com/SublimeLinter/SublimeLinter-csslint>`_.

Agregamos la siguiente configuración en *Preferences -> Package Settings -> SublimeLinter -> Settings - User*:

.. code-block:: json

    {
        //...
        "linters": {
            "csslint": {
                "@disable": false,
                "args": [],
                "errors": "",
                "excludes": [],
                "ignore": "",
                "warnings": ""
            },
            //...
            "jshint": {
                "@disable": false,
                "args": [],
                "excludes": []
            },
        },
        //...
        "paths": {
            "linux": [],
            "osx": [
                //...,
                "/usr/local/bin"
            ],
            "windows": []
        },
        //...
    }


sublimelinter-pep257 (python docstrings conventions)

HTML
----

`Emmet <http://docs.emmet.io/>`_


Manejo de espacios
------------------

Para eliminart espacios en blanco al final de una linea o en lineas vacias usamos `TrailingSpaces <https://github.com/SublimeText/TrailingSpaces>`_

La siguiente configuración nos permite eliminar los espacios en blanco al momento se salvar un archivo, pero solo en lineas de codigo que hemos modificado.

El archivo a modificar es *Preferences -> Package Settings -> Trailing Spaces -> Settings User*

.. code-block:: json

    {
        //...
        "trailing_spaces_modified_lines_only": true,
        "trailing_spaces_trim_on_save": true,
        // ...
    }

ST3 snippet para insertar un breakpoint
-----------------------------------------

Para poder poner un break point con solo escribir pdb y completar con tab,
debemos poner la siguiente configuración en:
"~/Library/Application Support/Sublime Text 3/Packages/User/pdb.sublime-snippet"

.. code-block:: xml

    <snippet>
        <content><![CDATA[import pdb; pdb.set_trace()]]></content>
        <tabTrigger>pdb</tabTrigger>
        <scope>source.python</scope>
        <description>pdb debug tool</description>
    </snippet>


Debug de Sesión
---------------
`PDBSublimeTextSupport <https://pypi.python.org/pypi/PdbSublimeTextSupport>`_

.. code-block:: console

    (projectenv)$ pip install PDBSublimeTextSupport


Referencias
-----------

`OS X Command Line <http://www.sublimetext.com/docs/3/osx_command_line.html>`_

`Reverting to a Freshly Installed State <http://www.sublimetext.com/docs/3/revert.html>`_

`Turning Sublime Text Into a Lightweight Python IDE <http://cewing.github.io/training.codefellows/assignments/day01/sublime_as_ide.html>`_

`Sublime Text 3 for Python JavaScript and web developers <http://opensourcehacker.com/2014/03/10/sublime-text-3-for-python-javascript-and-web-developers>`_

`Jenkins buildout fro Plone projects <https://buildoutjenkins.readthedocs.org/en/latest/index.html>`_
