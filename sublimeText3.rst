.. _sublimetext:

Sublime Text 3
==============

Línea de comandos en Mac OS X
-----------------------------

`Sublime Text 3 <https://www.sublimetext.com/3>`_ incluye el comando :command:`subl`, para abrir archivos desde una terminal.

Para poder usarlo hacemos un enlace simbólico:

.. code-block:: shell

   $ ln -s "/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl" /usr/local/bin/subl

Debemos asegurarnos que el directorio ``/usr/local/bin`` se encuntra en nuestro ``$PATH``, de no ser así podemos agregarlo en el archivo :file:`.bash_profile`

.. code-block:: shell

   export PATH=/usr/local/bin/:$PATH

.. seealso::

    `OS X Command Line - Sublime Text 3 Documentation <http://www.sublimetext.com/docs/3/osx_command_line.html>`_

Configuración de Usuario
------------------------

El archivo de configuración de usurio se abre desde el menú :menuselection:`Sublime Text --> Preferences --> Settings`.

.. code-block:: json

    {
        "color_scheme": "Monokai.sublime-color-scheme",
        "font_face": "Source Code Pro",
        "font_size": 13,

        "theme": "Default.sublime-theme",
        "bold_folder_labels": true,
        "git_diff_target": "index",
        "mini_diff": "auto",
        "show_encoding": true,

        "auto_complete_commit_on_tab": false,
        "ensure_newline_at_eof_on_save": true,
        "highlight_modified_tabs": true,
        "ignored_packages": ["Vintage"],
        "indent_to_bracket": true,
        "scroll_past_end": false,
        "tab_size": 4,
        "translate_tabs_to_spaces": true,
    }

Para configuración de archivos python abrimos un archivo :file:`.py` y desde esa ventana :menuselection:`Sublime Text --> Preferences --> Settings - Syntax Specific`.

.. code-block:: json

    {
        // "font_face": "Fira Code Medium",
        // "font_options": ["subpixel_antialias"],
        // "font_face": "SauceCodePro Nerd Font",
        "font_face": "Source Code Pro",
        "font_size": 13,
        "rulers": [79],
        "tab_size": 4,
        "translate_tabs_to_spaces": true,
        "use_tab_stops": true,

        "auto_indent": true,
        "smart_indent": true,
        "trim_automatic_white_space": true,
        "word_wrap": false,

        "draw_white_space": "selection"
    }

Salvamos el archivo como :file:`Python.sublime-settings`

Sublime Text mostrará un margen en las columnas:

    *  72 docstrings
    *  79 longitud optima de linea de codigo
    * 100 longitud maxima permitida

En este caso estamos usando el tipo de letra `Source Code Pro <https://github.com/adobe-fonts/source-code-pro>`_


Code Snippets
-------------

Para agregar un fragmento de código lo hacemos en :menuselection:`Tools --> Developer --> New Snippet ...` o en
:file:`~/Library/Application Support/Sublime Text 3/Packages/User/pdb.sublime-snippet`.

Ejemplo

.. code-block:: xml

    <snippet>
        <content><![CDATA[import pdb; pdb.set_trace()]]></content>
        <tabTrigger>pdb</tabTrigger>
        <scope>source.python</scope>
        <description>pdb debug tool</description>
    </snippet>

El ejemplo anterior agrega un break point con solo escribir ``pdb + <tab>``


Iluminación de archivos zcml
----------------------------

Abrimos un archivo :file:`.zcml` y seleccionamos :menuselection:`View --> Syntax --> Open all with current extension as... --> XML`


Iluminación de archivos buildout.cfg
------------------------------------

Usamos los paquetes de TextMate modificados por Martin Aspeli.
Copiamos el directorio `Buildout <https://github.com/optilude/SublimeTextMisc/tree/master/Packages>`_  en :menuselection:`Sublime Text --> Preferences --> Browse Pakages ...`

Abrimos un archivo :file:`buildout.cfg` y seleccionamos :menuselection:`View --> Syntax --> Open all with current extension as... --> Buildout config`


Control de paquetes
-------------------

Instalamos `Package Control <https://sublime.wbond.net/installation>`_ con:

:menuselection:`Tools --> Install Package Control...`

.. warning::

    Antes la instalación era atravez de la consola de Sublime Text (``ctrl + ```). En la consola ejecutabamos el texto tomado de la pagina.

Para instalar nuevos plugins abrimos la paleta de comandos con ``⌘ + ⇧ + P``, escribimos *install* y buscamos el comando ``Package Control: Install Package``.

.. note::

    ========  =============================================
    ctrl `    muestra la consola
    ⌘ ⇧ P     paleta de comandos
    ========  =============================================


GitGutter
---------

`GitGutter <https://github.com/jisaacks/GitGutter>`_ muestra información, en el area de ``gutter``, sobre archivos que estan bajo control de versiones con :command:`git`.

* Iconos en el area de ``gutter`` indicando modificaciónes y lineas nuevas o borradas
* Una ventana emergente con información de las lineas modificadas.
* Información en la barra de estado

.. seealso::

   Sublime 3.2 introdujo `Incremental Diff <https://www.sublimetext.com/docs/3/incremental_diff.html>`_ que implementa varias  funciones para identificar cambios en los archivos editados.

    ========  =============================================
    ctrl .    brinca al siguiente cambio
    ctrl ,    brinca al cambio anterior
    ========  =============================================

Para desactivar Incremental Diff y usar GitGutter en :menuselection:`Sublime Text --> Preferences --> Settings` agregamos lo siguiente:

.. code-block:: json

    {
        "mini_diff": false,
        "show_git_status": true
    }

La configuracíon de GitGutter se realiza en :menuselection:`Sublime Text --> Preferences --> Package Settings --> GitGutter --> Settings`

.. code-block:: json

    {
        "git_binary": "/usr/local/bin/git",
    }


Resaltar bloques
----------------

`BracketHighlighter <https://github.com/facelessuser/BracketHighlighter>`_ muestra alcance de bloques.


Diferencias
-----------

`FileDiffs <https://github.com/colinta/SublimeFileDiffs>`_ muestra diferencias entre el archivo actual y otro.

INI files
---------

`INI <https://github.com/clintberry/sublime-text-2-ini>`_ Colorea archivos INI.

Mejoras a la barra lateral
--------------------------
`SideBarEnhancements <https://github.com/titoBouzout/SideBarEnhancements>`_

`SyncedSideBar <https://github.com/TheSpyder/SyncedSideBar>`_


Autocompletar código python
---------------------------

`SublimeJedi <https://github.com/srusskih/SublimeJEDI>`_


    * Abrimos la paleta de comandos (``⌘ + ⇧ + P``)
    * Escribimos ``package control install`` y seleccionamos el comando ``Package Control: Install Package``
    * Escribimos ``Jedi`` y seleccionamos ``Jedi - Python autocompletion``

.. seealso::

    `Anaconda <http://damnwidget.github.io/anaconda/#>`_


.. code-block:: pycon

    >>> sys.path
    ['/Applications/Sublime Text.app/Contents/MacOS',
    '/Applications/Sublime Text.app/Contents/MacOS/python3.3.zip',
    '/Users/gil/Library/Application Support/Sublime Text 3/Lib/python3.3',
    '/Users/gil/Library/Application Support/Sublime Text 3/Packages']

Creamos un ambiente virtual para los paquetes que usamos en sublime

.. code-block:: shell

    $ cd /Users/myuser/buildout.python
    $ virtualenv- python-3.7-sublenv
    New python executable in python-3.7-sublenv/bin/python3.7
    Also creating executable in python-3.7-sublenv/bin/python
    Installing setuptools, pip, wheel...done.
    $ source python-3.7-sublenv/bin/activate
    (python-3.7-sublenv)$ pip install jedi

Para solo usar el autocomplete de jedi editamos :menuselection:`Sublime Text --> Preferences --> Packages Settings --> Jedi --> Settings - User`

.. code-block:: json

    {
        "python_virtualenv": "/Users/myuser/buildout.python/python-3.7-sublenv",
        "sublime_completions_visibility": "jedi",
        "auto_complete_function_params": "required"
    }


Usamos la siguiente configuración para definir el interprete de python que usaremos en nuestro proyecto.

.. code-block:: json

    {
        "folders":
        [
            {
                "path": ".",
                "folder_exclude_patterns": [
                    "src-git",
                    "Extensions",
                    "parts",
                ],
            },
            {
                "path": "src-git",
                "folder_exclude_patterns": ["*.egg-info"],
            },
            {
                "path": "Extensions",
                "folder_exclude_patterns": ["mathscinet*"],
                "file_exclude_patterns": ["*.xlsx", "*.json"],
            },
            {
                "path": "parts/omelette",
                "folder_exclude_patterns": ["math*", "UNAM*"],
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

Para crear un proyecto :menuselection:`Project --> save Project as`

Para editarlo :menuselection:`Project --> Edit Project`

Ejemplo de plone.recipe.sublimetext:

.. code-block:: json

    {
        "SublimeLinter":{
            "linters":{
                "pylint":{
                    "disable":false,
                    "paths":[
                        "/Users/myuser/.buildout/eggs/ZODB3-3.11.0-py2.7.egg",
                        "/Users/myuser/.buildout/eggs/Products.CMFCore-2.2.12-py2.7.egg",
                        "/Users/myuser/.buildout/eggs/Plone-5.1.2-py2.7.egg",
                        "/Users/myuser/.buildout/eggs/Acquisition-4.4.2-py2.7-macosx-10.4-x86_64.egg"
                    ]
                }
            }
        },
        "folders":[
            {
                "folder_exclude_patterns":[
                    "bin",
                    "develop-eggs",
                    "eggs",
                    "include",
                    "lib",
                    "local",
                    "parts",
                    "var",
                    ".sass-cache",
                    ".yolk"
                ],
                "follow_symlinks":"true",
                "path":"."
            },
            {
                "follow_symlinks":"true",
                "path":"parts/omelette"
            }
        ],
        "settings":{
            "python_interpreter":"/Users/myuser/projects/plone/sites/sublime-buildout/bin/python2.7",
            "python_package_paths":[
                "/Users/myuser/.buildout/eggs/Zope2-2.13.27-py2.7.egg",
                "/Users/myuser/.buildout/eggs/ZODB3-3.11.0-py2.7.egg",
                "/Users/myuser/.buildout/eggs/Plone-5.1.2-py2.7.egg",
                "/Users/myuser/.buildout/eggs/Acquisition-4.4.2-py2.7-macosx-10.4-x86_64.egg"
            ],
            "sublimelinter":true
        }
    }


.. note::

    ========  =========================================================
    ctrl ⇧ G  Encuentra la definición de una función, variable o clase
    ⌥ ⇧ F     Encuentra donde se usa el metodo, varibale o clase
    ctrl ⌥ D  Muestra la documentación como tooltip
    ========  =========================================================


SublimeLinter
-------------

Instalamos `SublimeLinter <http://sublimelinter.readthedocs.org/en/latest/>`_ usando el Package Control.

Editamos el archivo de configuración de SublimeLinter :menuselection:`Sublime Text --> Preferences --> Package Settings --> SublimeLinter --> Settings`

.. code-block:: json

    {
        "debug": false,
        "delay": 0.25,
        "gutter_theme": "Default",
        "lint_mode": "background",
        "linters": {},
        "no_column_highlights_line": false,
        "paths": {
            "linux": [],
            "osx": [],
            "windows": []
        },
        "show_marks_in_minimap": true,
    }


SublimeLinter-flake8
~~~~~~~~~~~~~~~~~~~~

`Flake8 <https://pypi.python.org/pypi/flake8>`_ reporta errores en el código,
haciendo uso de las herramientas `PyFlakes <https://pypi.python.org/pypi/pyflakes>`_, `pep8 <https://pypi.python.org/pypi/pep8>`_ y `mccabe <https://pypi.python.org/pypi/mccabe>`_

Primero creamos un ambiente virtual y lo activamos

.. code-block:: console

    $ virtualenv- python-3.7-sublenv
    New python executable in python-3.7-sublenv/bin/python3.7
    Also creating executable in python-3.7-sublenv/bin/python
    Installing setuptools, pip, wheel...done.
    $ source python-3.7-sublenv/bin/activate
    (python-3.7-sublenv)$

Instalamos los paquetes necesarios (`flake8 <https://pypi.python.org/pypi/flake8>`_)

.. code-block:: console

    (python-3.7-sublenv)$ pip install flake8
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
    (python-3-sublenv)$ pip install flake8-commas
    // (python-3-sublenv)$ pip install flake8-debugger
    (python-3-sublenv)$ pip install flake8-deprecated
    (python-3-sublenv)$ pip install flake8-isort
    (python-3-sublenv)$ pip install flake8-pep3101
    (python-3-sublenv)$ pip install flake8-plone-api
    // (python-3-sublenv)$ pip install flake8-print
    (python-3-sublenv)$ pip install flake8-quotes
    (python-3-sublenv)$ pip install flake8-string-format
    (python-3-sublenv)$ pip install flake8-todo

Si queremos usar un archivo requirements.txt debe contener los siguiente

.. code-block:: text

    entrypoints==0.3
    flake8==3.7.7
    flake8-blind-except==0.1.1
    flake8-coding==1.3.1
    flake8-commas==2.0.0
    flake8-deprecated==1.3
    flake8-isort==2.7.0
    flake8-pep3101==1.2.1
    flake8-plone-api==1.4
    flake8-plone-hasattr==0.2.post0
    flake8-quotes==2.0.1
    flake8-string-format==0.2.3
    flake8-todo==0.7
    isort==4.3.20
    mccabe==0.6.1
    pycodestyle==2.5.0
    pyflakes==2.1.1
    testfixtures==6.8.2


Agregamos lo siguiente:

.. code-block:: json

    {
        "linters": {
            "flake8": {
                "disable": false,
                "args": "--ignore E501,D100",
                "excludes": [],
                "max-complexity": 10,
                "max-line-length": null,
                "select": "",
                "show-code": true,
                "python": 3.7,
            }
        },
        "paths": {
            "linux": [],
            "osx": ["~/buildout.python/python-3.7-sublenv/bin"],
            "windows": []
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

Agregamos la siguiente configuración en ``Sublime Text -> Preferences -> Package Settings -> SublimeLinter -> Settings``:

.. code-block:: json

    {
        "linters": {
            "csslint": {
                "disable": false,
                "args": [],
                "errors": "",
                "excludes": [],
                "ignore": "",
                "warnings": ""
            },
            "jshint": {
                "disable": false,
                "args": [],
                "excludes": []
            },
        },
        "paths": {
            "osx": [
                "/usr/local/bin"
            ],
        }
    }

sublimelinter-json
~~~~~~~~~~~~~~~~~~

En sublimetext instalamos `sublimelinter-json <https://github.com/SublimeLinter/SublimeLinter-json>`_

.. code-block:: json

    {
        "linters": {
            "json": {
                "strict": false
            }
        }
    }


SublimeLinter--contrib-yamllint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: console

    (python-3-sublenv)$ pip install yamllint


En sublimetext instalamos `sublimelinter-contrib-yamllint <https://github.com/thomasmeeus/SublimeLinter-contrib-yamllint>`_

.. code-block:: json

    {
        "linters": {
            "pyyaml": {
            }
        }
    }


Manejo de espacios
------------------

Para eliminart espacios en blanco al final de una linea o en lineas vacias usamos `TrailingSpaces <https://github.com/SublimeText/TrailingSpaces>`_

La siguiente configuración nos permite eliminar los espacios en blanco al momento se salvar un archivo, pero solo en lineas de codigo que hemos modificado.

El archivo a modificar es :menuselection:`Preferences --> Package Settings --> Trailing Spaces --> Settings User`

.. code-block:: json

    {
        "trailing_spaces_modified_lines_only": true,
        "trailing_spaces_trim_on_save": true,
    }


EditorConfig
------------

`EditorConfig <https://github.com/sindresorhus/editorconfig-sublime>`_ ayuda a mantener estilos de codigo consistentes entre distintos editores.


Debug de Sesión
---------------
`PDBSublimeTextSupport <https://pypi.python.org/pypi/PdbSublimeTextSupport>`_

.. code-block:: console

    (projectenv)$ pip install PDBSublimeTextSupport


Theme
-----

`Flatland <https://github.com/thinkpixellab/flatland>`_

Lo instalamos usando Package Control:

* Abrimos la paleta de comandos (``⌘ + ⇧ + P``) y  seleccionammos ``Package Control: Install Package``.
* Buscamos la opción ``Theme - Flatland``


Abrimios el archivo de preferencias globales de Sublime Text 3: :menuselection:`Sublime Text --> Preferences --> Settings - User`

.. code-block:: json

    {
        "theme": "Flatland Dark.sublime-theme",
        "color_scheme": "Packages/Theme - Flatland/Flatland Monokai.tmTheme",
    }

`Soda Theme <http://buymeasoda.github.io/soda-theme/>`_

Abrimos el archivo de preferencias globales de Sublime Text 3: :menuselection:`Sublime Text --> Preferences --> Settings - User`

.. code-block:: json

    {
        "soda_classic_tabs": true,
        "theme": "Soda Dark 3.sublime-theme",
    }

* Descargar `colour-schemes.zip <http://buymeasoda.github.com/soda-theme/extras/colour-schemes.zip>`_.
* Descomprimir y mover los archivos **tmttheme** en el folder ``Pakages/User``.
* Abilitar el esquema de colores via:

:menuselection:`Sublime Text --> Preferences --> Color Scheme --> User --> Monokai Soda`


`Material Theme <http://equinusocio.github.io/material-theme/>`_


Color Scheme (opcional)
-----------------------

`Monokai Extended <https://github.com/jonschlinkert/sublime-monokai-extended>`_

:menuselection:`Sublime Text --> Preferences --> Color Scheme --> User --> Monokai Extended`

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

Abrimios el archivo :menuselection:`Sublime Text --> Preferences --> Key Bindings` y agregamos

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

Instalamos MacTeX

Instalamos Skim para abrir los pdfs.

.. code-block:: shell

   $ brew install imagemagick

Para ortografia instalamos el paquete `Dictionaries <https://github.com/titoBouzout/Dictionaries>`_
Lo colocamos en el folder de paquetes :menuselection:`Sublime Text --> Preferences --> Browse Packages`

Para seleccionar el idioma :menuselection:`View --> Dictionary --> Dictionaries --> English (American)`

Verificar que la ortografia este correcta (:menuselection:`View --> Spell Check` / F6)


.. note::

    =========  =========================================================
    ⌘ b         Compila latex
    ⇧ ⌘ b      Selecciona que usar Latex/PdfLatex/XeLatex
    ⌘ l + ⌫    Borra archivos temporales
    ⇧ ⌘ clic   Lleva de skim a sublimetext
    =========  =========================================================

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
    ctrl ⌥ D    Muestra la documentación como tooltip
    ctrl ⌘ j     Da formato a un archivo json
    ctrl ⌘ m     Minimiza archivo json (remueve espacios extras y saltos de linea)
    ctrl ⇧ ⌘ j   Consola de comandos de jq
    ⌘ ⌥ O       muestra un archivo rst en el navegador
    ctrl ⌥ d    muestra panel para comparar archivos
    ⌘ ⇧ L       selecciona lineas multiples
    ctrl ⌘ G    selecciona todas las apariciones
    ctrl G      ir a linea
    ==========  =========================================================


.. code-block:: shell


    >>> sublime.windows()[0].project_data()
    >>> sublime.windows()[0].extract_variables()


pipenvRun
---------

Creamos un "Build system"

.. code-block:: json

   {
       "encoding": "UTF-8",
       "working_dir": "$file_path",
       "cmd": ["pipenv" ,"run" ,"python3" ,"$file_name"],
       "selector": "source.python",
       "env": {"LANG": "en_US.UTF-8"}
   }


Otros
------
`RESTer <https://github.com/pjdietz/rester-sublime-http-client>`_ - HTTP client for Sublime Text

`restview <https://documentation-plone5.readthedocs.io/en/latest/about/helper_tools.html>`_

`<https://medium.com/@john.m.smalley/update-sublime-text-3-to-python-3-on-mac-ce57989bdbf3>`_

`<http://www.rmworking.com/blog/2018/02/11/sublime-text3-pipenv/>`_


Bibliografía
------------

* `Reverting to a freshly installed state - Sublime Text 3 Documentation <http://www.sublimetext.com/docs/3/revert.html>`_

* `Setting Up Sublime Text 3 for Full Stack Python Development <https://realpython.com/setting-up-sublime-text-3-for-full-stack-python-development/#markdown-preview>`_

* `How to set up Sublime Text 3 for Python development <http://premgkumar.com/2019/03/16/sublimetext-for-python>`_

* `Turning Sublime Text Into a Lightweight Python IDE <http://cewing.github.io/training.codefellows/assignments/day01/sublime_as_ide.html>`_

* `Sublime Text for Front End Developers <https://css-tricks.com/sublime-text-front-end-developers/>`_

* `My Sublime Text 3 setup <https://fredrikaverpil.github.io/2016/05/20/my-sublime-3-setup/>`_

* `Sublime 3 xml_pp (xmltwig) based xml auto formatter <https://gist.github.com/jensens/4fc631616f5ef9ac4c6b>`_

* `<https://www.shopify.com/partners/blog/sublime-text-plugins-2018>`_

* `Sublime Text Umofficial Documentation <http://docs.sublimetext.info/en/latest/basic_concepts.html?highlight=python>`_
