Sublime Text 3
==============

Linea de comandos en OS X
-------------------------

Sublime Text 3 incluye el comando, *subl*, para abrir archivos desde una terminal.

.. code-block:: bash

   $ ln -s "/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl" /usr/local/bin/subl

Agregamos el directorio /usr/local/bin a nuestro path en el archivo .bash_profile

.. code-block:: console

   export PATH=/usr/local/bin/:$PATH

User Settings
-------------

Configura tus preferencias abriendo *Preferences* -> *Settings - User*.

.. code-block:: json

    {
        "font_face": "Source Code Pro",
        "font_size": 15,
        "ignored_packages":
        [
            "Vintage"
        ],
        "rulers":
        [
            72,
            79,
            100,
        ],
        "tab_size": 4,
        "translate_tabs_to_spaces": true,
        "use_tab_stops": true,
    }


* 72, // docstrings
* 79, // optimum code line length
* 100  // maximum allowable length

En este aso estamos usando el tipo de letra `Source Code Pro <https://github.com/adobe-fonts/source-code-pro>`_

Package Control
---------------

La instalación de `Package Control <https://sublime.wbond.net/installation>`_ es atravez de la consola de Sublime Text (ctrl + \`). Una vez abierta pegamos lo siguiente (Es mejor tomarlo de la pagina original):

.. code-block:: console

   import urllib.request,os,hashlib; h = '7183a2d3e96f11eeadd761d777e62404' + 'e330c659d4bb41d3bdf022e94cab3cd0'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://sublime.wbond.net/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)

Este comando descarga el paquete *Control.sublime-package*.

Para instalar nuevos plugins abrimos la paleta de comandos con *shift + ⌘ + P*. Cuando se habra la paleta escribimos *install* y buscamos el comando *Package Control: Install Package*.


Autocompletar python
--------------------

`SublimeJedi <https://github.com/srusskih/SublimeJEDI>`_

.. note::

    Comparar con `Anaconda <http://damnwidget.github.io/anaconda/#>`_


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
            "python_interpreter_path": "/usr/local/bin/python2.7",

            "python_package_paths": [
                "/Users/user/projects/plone/matem-buildout/parts/omelette"
            ]
        }
    }

Para ir a la definición de un simbolo usamos *ctrl + shift + G*.

Para buscar otros lugares donde se use el simbolo usamos *⌥ + shift + F*.



Lint (flake8, pep257)
---------------------

Muestra errores que cometiste en el código.

Primero creamos un ambiente virtual y lo activamos

.. code-block:: console

    $ cd /Users/myuser/buildout.python
    $ virtualenv-3.5 python-3-sublenv
    New python executable in python-3-sublenv/bin/python3.5
    Also creating executable in python-3-sublenv/bin/python
    Installing setuptools, pip...done.
    $ source python-3-sublenv/bin/activate
    (python-3-sublenv)$

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
    (sublenv)$ pip install pep257
    Downloading/unpacking pep257
    Downloading pep257-0.3.2.tar.gz
    [...]
    Successfully installed pep257
    Cleaning up...
    (sublenv)$

Instalamos `SublimeLinter <http://sublimelinter.readthedocs.org/en/latest/>`_ , despues `SublimeLinter-flake8 <https://github.com/SublimeLinter/SublimeLinter-flake8>`_ y `SublimeLinter-pep257 <https://github.com/SublimeLinter/SublimeLinter-pep257>`_ usando el Package Control.

Agregamos la siguiente configuración en *Preferences -> Package Settings -> SublimeLinter -> Settings - User*:

.. code-block:: json

    {
        "user": {
            "linters": {
                 "flake8": {
                    "@disable": false,
                    "args": [],
                    "builtins": "",
                    "excludes": [],
                    "ignore": "",
                    "jobs": "1",
                    "max-complexity": 10,
                    "max-line-length": null,
                    "select": "",
                    "show-code": false
                },
                "pep257": {
                    "@disable": false,
                    "args": [],
                    "excludes": [],
                    "ignore": ""
                }
            },
            "paths": {
                "linux": [],
                "osx": [
                    "/Users/user/buildout.python/python-3-sublenv/bin"
                ],
                "windows": []
            },
            "python_paths": {
                "linux": [],
                "osx": [
                    "/Users/user/buildout.python/python-3-sublenv/bin"
                ],
                "windows": []
            },
        }
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

Instalamos `jshint <http://www.jshint.com/>`_ y `csslint <http://csslint.net/>`_

.. code-block:: console

    $ sudo npm install -g jshint
    $ sudo npm install -g csslint

En sublimetext instalamos `sublimelinter-jshint <https://github.com/SublimeLinter/SublimeLinter-jshint>`_ y `sublimelinter-csslint <https://github.com/SublimeLinter/SublimeLinter-csslint>`_.

Agregamos la siguiente configuración en *Preferences -> Package Settings -> SublimeLinter -> Settings - User*:

.. code-block:: json

    {
        "user": {
            "linters": {
                "csslint": {
                    "@disable": false,
                    "args": [],
                    "errors": "",
                    "excludes": [],
                    "ignore": "",
                    "warnings": ""
                },
                "jshint": {
                    "@disable": false,
                    "args": [],
                    "excludes": []
                },
            },
            "paths": {
                "osx": [
                    "/usr/local/bin"
                ],
            },
        }
    }


Manejo de espacios
------------------

Para eliminart espacios en blanco al final de una linea o en lineas vacias usamos `TrailingSpaces <https://github.com/SublimeText/TrailingSpaces>`_

La siguiente configuración nos permite eliminar los espacios en blanco al momento se salvar un archivo, pero solo en lineas de codigo que hemos modificado.

El archivo a modificar es *Preferences -> Package Settings -> Trailing Spaces -> Settings User*

.. code-block:: json

    {
        "trailing_spaces_modified_lines_only": true,
        "trailing_spaces_trim_on_save": true,
    }


EditorConfig
------------

`EditorConfig <https://github.com/sindresorhus/editorconfig-sublime>`_ ayuda a mantener estilos de codigo consistentes entre distintos editores.


GitGutter
---------

`GitGutter <https://github.com/jisaacks/GitGutter>`_ muestra un icono en el area de "gutter"
indicando si la linea ha sido insertada, modificada o borrada.


ST3 snippet para insertar un breakpoint
-----------------------------------------

Para poder poner un break point con solo escribir pdb y completar con tab,
debemos poner la siguiente configuración en:
"~/Library/Application Support/Sublime Text 3/Packages/User/pdb.sublime-snippet".
o en *Tools -> New Snippet ...*

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


Iluminación de archivos buildout.cfg
------------------------------------

Usamos los paquetes de TextMate modificados por Martin Aspeli.
Copiamos el directorio `Buildout <https://github.com/optilude/SublimeTextMisc/tree/master/Packages>`_  en ``Sublime Text -> Preferences -> Brows Pakages ...``


Theme
-----

`Soda Theme <http://buymeasoda.github.io/soda-theme/>`_

Abrimios el archivo de preferencias globales de Sublime Text 3 (Sublime Text -> Preferences -> Settings - User)

.. code-block:: json

    {
        "soda_classic_tabs": true,
        "theme": "Soda Dark 3.sublime-theme",
    }



* Descargar `colour-schemes.zip <http://buymeasoda.github.com/soda-theme/extras/colour-schemes.zip>`_.
* Descomprimir y mover los archivos **tmttheme** en el folder Pakages/User.
* Abilitar el esquema de colores via:

*Preferences -> Color Scheme -> User -> Monokai Soda*


Color Scheme (opcional)
-----------------------

`Monokai Extended <https://github.com/jonschlinkert/sublime-monokai-extended>`_

*Preferences -> Color Scheme -> Monokai Extended -> Monokai Extended*


OmniMarkupPreviewer
-------------------

Plugin para mostrar rst files en el navegador.

.. sourcecode:: sh

    ⌘ + ⌥ + O: Muestra el archivo en el navegador.


HTML
----

Soporte para CSS en sublime Text 3: `CSS3 <https://github.com/y0ssar1an/CSS3>`_

It's strongly recommended that you disable the default CSS package, as its completions will interfere with the improved CSS3 completions.

.. sourcecode:: sh

    Mac:      shift + ⌘ + P  -> Package Control: Disable Package -> CSS

Coloracion de sintaxis para .less: `Less <https://github.com/danro/LESS-sublime>`_


JavaScript
----------

`JavaScriptNext <https://github.com/Benvie/JavaScriptNext.tmLanguage>`_
es  una mejor definicion de JavaScript para SublimeText.

Para seleccionarlo como default para JavaScript, abre un archivo javascript, selecciona
View -> Syntax -> Open all with current extension as... -> JavascriptNext.

Referencias
-----------

`OS X Command Line <http://www.sublimetext.com/docs/3/osx_command_line.html>`_

`Reverting to a Freshly Installed State <http://www.sublimetext.com/docs/3/revert.html>`_

`Turning Sublime Text Into a Lightweight Python IDE <http://cewing.github.io/training.codefellows/assignments/day01/sublime_as_ide.html>`_

`Sublime Text 3 for Python JavaScript and web developers <http://opensourcehacker.com/2014/03/10/sublime-text-3-for-python-javascript-and-web-developers>`_

`Sublime Text for Front End Developers <https://css-tricks.com/sublime-text-front-end-developers/>`_

`Emmet LiveStyle <http://livestyle.emmet.io/>`_
