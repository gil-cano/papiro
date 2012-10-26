Sublime Text 2
==============

.. _chapter_content:

Linea de comandos en OS X
-------------------------

Sublime Text 2 incluye el comando, *subl*, para abrir archivos desde una terminal.

.. code-block:: bash

   $ ln -s "/Applications/Sublime Text 2.app/Contents/SharedSupport/bin/subl" ~/local/bin/subl

Agregamos el directorio local/bin a nuestro path en el archivo .profile

.. code-block:: console

   export PATH=/Users/user/local/bin:$PATH

Sublime Package Control
-----------------------

La instalacion de `Sublime Package Control <http://wbond.net/sublime_packages/package_control>`_ es atravez de la consola de Sublime Text 2(ctrl + \`). Una vez abierta pegamos lo siguiente:

.. code-block:: console

   import urllib2,os; pf='Package Control.sublime-package'; ipp=sublime.installed_packages_path(); os.makedirs(ipp) if not os.path.exists(ipp) else None; urllib2.install_opener(urllib2.build_opener(urllib2.ProxyHandler())); open(os.path.join(ipp,pf),'wb').write(urllib2.urlopen('http://sublime.wbond.net/'+pf.replace(' ','%20')).read()); print 'Please restart Sublime Text to finish installation'

Este comando crea el folder de paquetes instalados y descarga el paquete *Control.sublime-package*.

Temas
-----

Instalamos el tema `Soda <https://github.com/buymeasoda/soda-theme/>`_ (Dark and light custom UI themes for Sublime Text 2).

⌘+shift+p combo y escribimos Install, seleccionamos “Package Control: Install Package” y damos enter. Luego escribimos "soda" y selecionamos el paquete “Theme - Soda”.

Para activar el tema:

* Abrimios el archivo de preferencias globales de Sublime Text 2 (``Sublime Text 2 -> Preferences -> Settings - User``)
* Agregamos la entrada del tema para que sea ``"theme": "Soda Dark.sublime-theme"`` o ``"theme": "Soda Light.sublime-theme"``

.. code-block:: python

   {
       "theme": "Soda Dark.sublime-theme"
   }

Esquema de Colores
------------------

Instalamos el esquema `espresso-tutti-colori.tmtheme <https://github.com/mkhl/espresso-tutti-colori.tmtheme/>`_.

* Copiamos el archivo `Espresso.tmTheme <https://github.com/optilude/SublimeTextMisc/blob/master/Espresso.tmTheme>`_ en ``Library/Application\ Support/Sublime\ Text\ 2/Packages/User``.
* Activar el esquema (``Sublime Text 2 -> Preferences -> Color Scheme -> User -> Espreso``)

SublimeCodeIntel
----------------

`SublimeCodeIntel <https://github.com/Kronuz/SublimeCodeIntel>`_


SublimeLinter
-------------
SublimeLinter is a plugin that supports "lint" programs (known as "linters").
SublimeLinter highlights lines of code the linter deems to contain (potential) errors.
It also supports highlighting special annotations (for example: TODO) so that they can be quickly located.

C/C++ - lint via cppcheck
CSS - lint via built-in csslint
HTML - lint via tidy
Java - lint via javac -Xlint
Javascript - lint via built in jshint
Python - lint via built-in pylint 

Javascript-based linters
~~~~~~~~~~~~~~~~~~~~~~~~
If you plan to edit files that use a Javascript-based linter (Javascript, CSS), your system must have a Javascript engine installed.
On Mac OS X, you must install Node.js if you plan to edit Javascript or CSS files that use non-ASCII characters in strings or comments.

instalamos node engine for javascript linters (jshint, csslint)

Node (v0.8.12) was installed at

   /usr/local/bin/node

npm was installed at

   /usr/local/bin/npm

Make sure that /usr/local/bin is in your $PATH.

c linter
~~~~~~~~
instalamos cpplint.py in local/bin for c/c++ linter


add these adjustments to the SublimeLinter User Settings file. 
Instalacion: ⌘+shift+p → “install” → ENTER → “codeintel” → ENTER → Restart ST2

change the linter language for C and C++ to c_cpplint via sublimelinter_syntax_map


configuración
~~~~~~~~~~~~~
Preferences->Package Settings->SublimeLinter->Settings - User


Sublime HTMLPrettify
--------------------
ctrl + shift + x

WordHighlight
-------------


PdbSublimeTextSupport
---------------------

Primero instalamos PdbSublimeTextSupport.

.. code-block:: console

   $ pip install PdbSublimeTextSupport

Despues agregamos lo siguiente en el archivo .pdbrc que se esta en nuestro directio raiz.

.. code-block:: python

   from PdbSublimeTextSupport import preloop, precmd
   pdb.Pdb.preloop = preloop
   pdb.Pdb.precmd = precmd

Para que esto funcione debemos tener el comando subl


Fuente
------

Usamos la fuente `Melso <https://github.com/andreberg/Meslo-Font>`_ (11pt).

En Mac OS X instalamos la fuente usando **Font Book**.

* En el **Finder** hacemos doble-clik en el icono de la fuente. Se habre **Font Book** y nos muestra como se ve.
* Damos clik en Instalar.

En Linux:

.. code-block:: sh

   # (Linux)
   $ mkdir ~/.fonts
   $ mkfontdir ~/.fonts
   $ cd Meslo\ LG\ DZ\ v1.0/
   $ cp *.ttf ~/.fonts
   $ fc-cache



Historia de comandos
--------------------

Este plug-in funciona como ``Cmd+Shift+V/Cmd+Alt+Ctrl+V`` en TextMate.
Tomado de un ejemplo de Martin Aspeli.

Para instalarlo basta con copiar el archivo `clipboradHistory.py <https://github.com/optilude/SublimeTextMisc/blob/master/clipboardHistory.py>`_ a ``Library/Application\ Support/Sublime\ Text\ 2/Packages/User``.


PEP-8 y PyFlakes
----------------

`sublimetext_python_checker  <https://github.com/vorushin/sublimetext_python_checker>`_ es un plug-in para el editor Sublime Text 2 que integra los verificadores pep8 y pyflakes.

Para instalarlo clonamos el repositorio en el directorio ``Packages``:

.. code-block:: sh

   # (Mac OS X)
   $ cd Library/Application\ Support/Sublime\ Text\ 2/Packages
   $ git clone git://github.com/vorushin/sublimetext_python_checker.git

Agregamos un archivo dentro de este directorio llamado local_settings.py con la lista de los verificadores que queremos usar:

.. code-block:: python

   CHECKERS = [('/Users/gil/python-snow/python-2.4/bin/pep8', []),
               ('/Users/gil/python-snow/python-2.4/bin/pyflakes', [])]

El primer parametro es la ruta al comando, el segundo parametro es una lista opcional de argumentos. Si queremos desabilitar la revision de la longitud de lineas de pep8, ponemos el segundo parametro a ``['--ignore=E501']``.


Iluminar ocurrencias de variable
--------------------------------

Este plugin Ilumina las ocurrencias de una varibale.

Para instalarlo basta con copiar el archivo `highlight.py <https://github.com/optilude/SublimeTextMisc/blob/master/highlight.py>`_ a ``Library/Application\ Support/Sublime\ Text\ 2/Packages/User``.


Iluminacion de sintaxis para archivos de Zope y Buildout
--------------------------------------------------------

Usamos los pauetes de TextMate modificados por Martin Aspeli.
Copiamos los directorios `Buildout <https://github.com/optilude/SublimeTextMisc/tree/master/Packages>`_ y `Zope <https://github.com/optilude/SublimeTextMisc/tree/master/Packagesy>`_ en ``Sublime Text 2 -> Preferences -> Brows Pakages ...``


Configuración
-------------

Para excluir determinados archivos de la navegación, editamos el archivo de Preferencias Globales de Usuario

.. code-block:: python

   {
       "theme": "Soda Light.sublime-theme",
       "folder_exclude_patterns": [".svn", ".git", ".hg", "CVS", ".*", "parts"]
   }

"goto anything" (Cmd+P)

Referencias
-----------

`OS X Command Line <http://www.sublimetext.com/docs/2/osx_command_line.html>`_

`Sublime Text 2 for Zope and Plone <http://www.martinaspeli.net/articles/sublime-text-2-for-zope-and-plone>`_

`Reverting to a Freshly Installed State <http://www.sublimetext.com/docs/2/revert.html>`_

`Font Book 2.0 <http://docs.info.apple.com/article.html?path=FontBook/2.0/en/fb680.html>`_

`Using Sublime Text 2 for Development <http://www.rockettheme.com/magazine/1319-using-sublime-text-2-for-development>`_

`An Editor You Will Regret You Haven’t Used Before <http://o2js.com/2011/10/29/fell-in-love-with-sublime-text-2/>`_

`Configuració del Sublime Text 2 <http://documentacio.readthedocs.org/en/latest/howto/sublimetext2.html>`_
