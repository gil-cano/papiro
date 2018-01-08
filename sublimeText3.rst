Sublime Text 3
==============

Línea de comandos en Mac OS X
-----------------------------

`Sublime Text 3 <https://www.sublimetext.com/3>`_ incluye el comando, ``subl``, para trabajar con archivos desde una terminal.

Para poder usarlo hacemos un enlace simbólico:

.. code-block:: console

   $ ln -s "/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl" /usr/local/bin/subl

Debemos asegurarnos que el directorio ``/usr/local/bin`` se encuntra en nuestro ``$PATH``, de no ser así podemos agregarlo en el archivo ``.bash_profile``

.. code-block:: console

   export PATH=/usr/local/bin/:$PATH

.. seealso::
    `OS X Command Line - Sublime Text 3 Documentation <http://www.sublimetext.com/docs/3/osx_command_line.html>`_

Configuración de Usuario
------------------------

El archivo de configuración de usurio se abre desde el menú ``Sublime Text -> Preferences -> Settings ``.

.. code-block:: json

    {
        "font_face": "Source Code Pro",
        "font_size": 15,
        "ignored_packages":
        [
            "Vintage",
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


Sublime Text mostrará un margen en las columnas:

    -  72 docstrings
    -  79 longitud optima de linea de codigo
    - 100 longitud maxima permitida

En este caso estamos usando el tipo de letra `Source Code Pro <https://github.com/adobe-fonts/source-code-pro>`_

Control de paquetes
-------------------

Para la administración de paquetes se recomienda usar `Package Control <https://sublime.wbond.net/installation>`_. La instalación es atravez de la consola de Sublime Text (``ctrl + ```). En la consola ejecutamos lo siguiente (es mejor tomarlo de la pagina original):

.. code-block:: console

    import urllib.request,os,hashlib; h = '6f4c264a24d933ce70df5dedcf1dcaee' + 'ebe013ee18cced0ef93d5f746d80ef60'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by) 
    
Este comando descarga el paquete ``Control.sublime-package``.

Para instalar nuevos plugins abrimos la paleta de comandos con ``⇧ + ⌘ + P``, escribimos *install* y buscamos el comando ``Package Control: Install Package``.

.. note::

    ========  =============================================
    ctrl `    muestra la consola
    ⇧ ⌘ P     paleta de comandos
    ========  =============================================


Autocompletar código python
---------------------------

`SublimeJedi <https://github.com/srusskih/SublimeJEDI>`_

.. seealso::

    `Anaconda <http://damnwidget.github.io/anaconda/#>`_

Usamos la siguiente configuración para definir el interprete de python que usaremos en nuestro proyecto.

.. code-block:: json

    {
        "folders":
        [
            {
                "path": "src-git"
            },
            {
                "path": "src-git",
                "folder_exclude_patterns": ["*.egg-info"],
            },
            {
                "path": "Extensions",
                "folder_exclude_patterns": ["mathscinet*"],
                "file_exclude_patterns": ["*.xlsx", "*.json"],
            }
        ],
        "settings":
        {
            "python_interpreter": "$project_path/bin/python2.7",
            "python_package_paths": ["$project_path/parts/omelette"]
        }
    }

Por default el archivo de un proyecto es ``<project name>.sublime-project``

Para crear un proyecto ``Project -> save Project as``

Para editarlo ``Project -> Edit Project``

Para solo usar el autocomplete de jedi editamos ``Sublime Text -> Preferences -> Packages Settings -> Jedi -> Settings - User``

.. code-block:: json

    {
        "sublime_completions_visibility": "jedi"
    }

.. note::

    ========  =========================================================
    ctrl ⇧ G  Encuentra la definición de una función, variable o clase
    ⌥ ⇧ F     Encuentra donde se usa el metodo, varibale o clase
    ========  =========================================================


SublimeLinter
-------------

Instalamos `SublimeLinter <http://sublimelinter.readthedocs.org/en/latest/>`_ usando el Package Control.

Editamos el archivo de configuración de SublimeLinter ``Sublime Text -> Preferences -> Package Settings -> SublimeLinter -> Settings - User``:

.. code-block:: json

    {

    }

Salvamos y reiniciamos SublimeText. El archivo de configuración tendra la siguiente configuración:

.. code-block:: json

    {
        "user": {
            "debug": false,
            "delay": 0.25,
            "error_color": "D02000",
            "gutter_theme": "Packages/SublimeLinter/gutter-themes/Default/Default.gutter-theme",
            "gutter_theme_excludes": [],
            "lint_mode": "background",
            "linters": {},
            "mark_style": "outline",
            "no_column_highlights_line": false,
            "passive_warnings": false,
            "paths": {
                "linux": [],
                "osx": [],
                "windows": []
            },
            "python_paths": {
                "linux": [],
                "osx": [],
                "windows": []
            },
            "rc_search_limit": 3,
            "shell_timeout": 10,
            "show_errors_on_save": false,
            "show_marks_in_minimap": true,
            "syntax_map": {
                "html (django)": "html",
                "html (rails)": "html",
                "html 5": "html",
                "javascript (babel)": "javascript",
                "magicpython": "python",
                "php": "html",
                "python django": "python",
                "pythonimproved": "python"
            },
            "warning_color": "DDB700",
            "wrap_find": true
        }
    }


SublimeLinter-flake8
~~~~~~~~~~~~~~~~~~~~

`Flake8 <https://pypi.python.org/pypi/flake8>`_ reporta errores en el código,
haciendo uso de las herramientas `PyFlakes <https://pypi.python.org/pypi/pyflakes>`_, `pep8 <https://pypi.python.org/pypi/pep8>`_ y `mccabe <https://pypi.python.org/pypi/mccabe>`_

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

    (python-3-sublenv)$ pip install flake8
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
    (python-3-sublenv)$ pip install flake8-blind-except
    (python-3-sublenv)$ pip install flake8-coding
    (python-3-sublenv)$ pip install flake8-debugger
    (python-3-sublenv)$ pip install flake8-docstrings

Si queremos usar un archivo requirements.txt debe contener los siguiente

.. code-block:: text

    flake8==2.5.4
    flake8-blind-except==0.1.0
    flake8-coding==1.2.1
    flake8-debugger==1.4.0
    flake8-docstrings==0.2.7
    mccabe==0.4.0
    pep257==0.7.0
    pep8==1.7.0
    pyflakes==1.0.0


Agregamos la siguiente:

.. code-block:: json

    {
        "user": {
            "linters": {
                 "flake8": {
                    "@disable": false,
                    "args": [],
                    "builtins": "",
                    "excludes": [],
                    "ignore": "E501,D100,T000",
                    "jobs": "1",
                    "max-complexity": 10,
                    "max-line-length": null,
                    "select": "",
                    "show-code": true
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

Instalamos `SublimeLinter-flake8 <https://github.com/SublimeLinter/SublimeLinter-flake8>`_

sublimelinter-jshint / sublimelinter-csslint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

Agregamos la siguiente configuración en ``Sublime Text -> Preferences -> Package Settings -> SublimeLinter -> Settings - User``:

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

sublimelinter-json
~~~~~~~~~~~~~~~~~~

En sublimetext instalamos `sublimelinter-json <https://github.com/SublimeLinter/SublimeLinter-json>`_


Iluminación de archivos buildout.cfg
------------------------------------

Usamos los paquetes de TextMate modificados por Martin Aspeli.
Copiamos el directorio `Buildout <https://github.com/optilude/SublimeTextMisc/tree/master/Packages>`_  en ``Sublime Text -> Preferences -> Browse Pakages ...``

Abrimos un archivo ``buildout.cfg`` y seleccionamos ``View -> Syntax -> Open all with current extension as... -> Buildout config``

Iluminación de archivos zcml
----------------------------

Abrimos un archivo ``.zcml`` y seleccionamos ``View -> Syntax -> Open all with current extension as... -> XML``

Manejo de espacios
------------------

Para eliminart espacios en blanco al final de una linea o en lineas vacias usamos `TrailingSpaces <https://github.com/SublimeText/TrailingSpaces>`_

La siguiente configuración nos permite eliminar los espacios en blanco al momento se salvar un archivo, pero solo en lineas de codigo que hemos modificado.

El archivo a modificar es ``Preferences -> Package Settings -> Trailing Spaces -> Settings User``

.. code-block:: json

    {
        "trailing_spaces_modified_lines_only": true,
        "trailing_spaces_trim_on_save": true,
    }

Resaltar bloques
----------------

`BracketHighlighter <https://github.com/facelessuser/BracketHighlighter>`_ muestra alcance de bloques.


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
``~/Library/Application Support/Sublime Text 3/Packages/User/pdb.sublime-snippet``.
o en ``Tools -> New Snippet ...``

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


Mejoras a la barra lateral
--------------------------
`SideBarEnhancements <https://github.com/titoBouzout/SideBarEnhancements>`_


Theme
-----

`Material Theme <http://equinusocio.github.io/material-theme/>`_

`Material Theme - Appbar <https://github.com/equinusocio/material-theme-appbar>`_

Abrimios el archivo de preferencias globales de Sublime Text 3 ``Sublime Text -> Preferences -> Settings - User``

.. code-block:: json

    {
        "theme": "Material-Theme-Darker.sublime-theme",
        "color_scheme": "Packages/Material Theme/schemes/Material-Theme-Darker.tmTheme",
        "always_show_minimap_viewport"  : true,
        "bold_folder_labels"            : true,
        "material_theme_bold_tab"       : true,
        "material_theme_compact_sidebar": true,
        "material_theme_small_statusbar": true,
        "material_theme_small_tab"      : true,
        "overlay_scroll_bars"           : "enabled",
    }


`Soda Theme <http://buymeasoda.github.io/soda-theme/>`_

Abrimios el archivo de preferencias globales de Sublime Text 3 ``Sublime Text -> Preferences -> Settings - User``

.. code-block:: json

    {
        "soda_classic_tabs": true,
        "theme": "Soda Dark 3.sublime-theme",
    }



* Descargar `colour-schemes.zip <http://buymeasoda.github.com/soda-theme/extras/colour-schemes.zip>`_.
* Descomprimir y mover los archivos **tmttheme** en el folder ``Pakages/User``.
* Abilitar el esquema de colores via:

``Sublime Text -> Preferences -> Color Scheme -> User -> Monokai Soda``


Color Scheme (opcional)
-----------------------

`Monokai Extended <https://github.com/jonschlinkert/sublime-monokai-extended>`_

*Preferences -> Color Scheme -> Monokai Extended -> Monokai Extended*

CSS
----

Soporte para CSS en sublime Text 3: `CSS3 <https://github.com/y0ssar1an/CSS3>`_

Se recomienda desabilitar el paquete CSS desde la paleta de comandos ``Package Control: Disable Package -> CSS``

Asigna CSS3 como el lenguaje por omision para los archivos .css ``View -> Syntax -> Open all with current extension as... -> CSS3``

Coloracion de sintaxis para .less: `Less <https://github.com/danro/LESS-sublime>`_


JavaScript
----------

`JavaScriptNext <https://github.com/Benvie/JavaScriptNext.tmLanguage>`_
es  una mejor definicion de JavaScript para SublimeText.

Para seleccionarlo como default para JavaScript, abre un archivo javascript, selecciona
View -> Syntax -> Open all with current extension as... -> JavascriptNext.

Asigna JavaScriptNext como el lenguaje por omision para los archivos .js ``View -> Syntax -> Open all with current extension as... -> JavaScript Next``

Json
----

`Pretty JSON <https://github.com/dzhibas/SublimePrettyJson>`_ da formato y minimiza archivos json.

Abrimios el archivo ``Sublime Text -> Preferences -> Key Bindings - User`` y agregamos

.. code-block:: json

    { "keys": [ "ctrl+command+m" ], "command": "un_pretty_json" }

.. note::

    ========   ======================================
    ctrl ⌘ j   Da formato a un archivo json
    ctrl ⌘ m   Minimiza archivo json (remueve espacios extras y saltos de linea)
    ========   ======================================

Tambien se puede usar `jq <https://stedolan.github.io/jq/>`_

.. code-block:: console

    $ brew install jq

.. note::

    ==========   ======================================
    ctrl ⇧ ⌘ j   Consola de comandos de jq
    ==========   ======================================


OmniMarkupPreviewer
-------------------

`OmniMarkupPreviewer <https://github.com/timonwong/OmniMarkupPreviewer>`_ interpreta archivos rst en el navegador.

.. note::

    ========  =========================================================
    ⌘ ⌥ O     Muestra un archivo rst en el navegador
    ========  =========================================================


.. seealso::

    https://gist.github.com/svx/885f2d870ed6aab1b9cc


Latex
-----
`LaTeXTools <https://github.com/SublimeText/LaTeXTools>`_

Si instalamos Skim podemos generar automaticamente el pdf.

Comparar archivos
-----------------

`sublimerge <http://www.sublimerge.com>`_. Diff lado a lado

.. note::

    ========   ======================================
    ctrl ⌥ d   muestra panel para comparar archivos
    ========   ======================================


Acordeón
--------

.. note::

    ==========  =========================================================
    ctrl `      muestra la consola
    ⇧ ⌘ P       paleta de comandos
    ctrl ⇧ G    encuentra la definición de una función, variable o clase
    ⌥ ⇧ F       encuentra donde se usa el metodo, varibale o clase
    ctrl ⌘ j     Da formato a un archivo json
    ctrl ⌘ m     Minimiza archivo json (remueve espacios extras y saltos de linea)
    ctrl ⇧ ⌘ j   Consola de comandos de jq
    ⌘ ⌥ O       muestra un archivo rst en el navegador
    ctrl ⌥ d    muestra panel para comparar archivos
    ⌘ ⇧ L       selecciona lineas multiples
    ctrl ⌘ G    selecciona todas las apariciones
    ctrl G      ir a linea
    ==========  =========================================================

Bibliografía
------------

* `Reverting to a freshly installed state - Sublime Text 3 Documentation <http://www.sublimetext.com/docs/3/revert.html>`_

* `Turning Sublime Text Into a Lightweight Python IDE <http://cewing.github.io/training.codefellows/assignments/day01/sublime_as_ide.html>`_

* `Sublime Text 3 for Python JavaScript and web developers <http://opensourcehacker.com/2014/03/10/sublime-text-3-for-python-javascript-and-web-developers>`_

* `Sublime Text for Front End Developers <https://css-tricks.com/sublime-text-front-end-developers/>`_

* `My Sublime Text 3 setup <https://fredrikaverpil.github.io/2016/05/20/my-sublime-3-setup/>`_