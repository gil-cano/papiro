Visual studio Code
==================


Línea de comandos en macOS
--------------------------

`Visual Studio Code <https://code.visualstudio.com/>`_ incluye el comando :command:`code`, para abrir archivos desde una terminal.


 * Inicia VS Code.
 * Abrimos la paleta de comandos con ``F1`` o ``⌘ + ⇧ + P`` y escribimos *shell command* para encontrar el comando *Shell Command: Install 'code' command in PATH*
 * Reiniciamos la terminal para que el nuevo $PATH tome efecto.


.. note::

    ========  =============================================
    F1        paleta de comandos
    ⇧ ⌘ P     paleta de comandos
    ========  =============================================

.. image:: _static/vscode/vsc_shell.png
   :alt: shell command

`Visual Studio Code on macOS <https://code.visualstudio.com/docs/setup/mac>`_

Python en Visual Studio Code
----------------------------


`Python in Visual Studio Code <https://code.visualstudio.com/docs/languages/python>`_

Configuración
~~~~~~~~~~~~~

.. code-block:: shell

    mkdir product
    cd product
    pipenv install -python=python3.8
    code product


.. image:: _static/vscode/vsc_interpreter.png
   :alt: shell command


.. warning::

    Abrimos un archivo :file:`.py`. La extensión de Python muestra un botón en la barra de estado donde podemos seleccinar el ambiente de Python a usar. Las preferencias son salvadas en el archivo :file:`.vscode/settings.json`.


Debug
~~~~~

Selecciona la linea en el gutter y presiona ``F5``


.. image:: _static/vscode/vsc_debug.png
   :alt: shell command

La ejecusíon se detiene en la linea selecionada y aparece la barra de debug

.. image:: _static/vscode/vsc_debugtoolbar.png
   :alt: shell command


La consola de debug

.. image:: _static/vscode/vsc_debugconsole.png
   :alt: shell command


Testing
~~~~~~~
`pytest <https://code.visualstudio.com/docs/python/testing#_enable-a-test-framework>`_

.. code-block:: shell

    cd product
    pipenv install pytest

Abilitamos las pruebas con el comando Python: Configure Tests

Linters

`flake8 <https://code.visualstudio.com/docs/python/linting#_enable-linters>`_

.. code-block:: shell

    cd product
    pipenv install flake8


reStructuredText
----------------

Instalación
~~~~~~~~~~~

Instalamos la extension `reStructuredText <https://docs.restructuredtext.net>`_ .

* Vamos a la vista de extensiones dando clic en el quinto icono de la barra izquierda.
* Escribimos "restructuredtext" en la caja de búsqueda y damos enter.
* Damos clic en el botón instalar.


Configuración
~~~~~~~~~~~~~

.. code-block:: shell

    mkdir notas
    cd notas
    pipenv install -python=python3.8
    pipenv install Sphinx
    pipenv shell
    (notas) sphinx-quickstart
    (notas) code .



.. warning::

    Abrimos el archivo :file:`conf.py`. La extensión de Python muestra un botón en la barra de estado donde podemos seleccinar el ambiente de Python a usar. Las preferencias son salvadas en el archivo :file:`.vscode/settings.json`.


Linters
~~~~~~~

.. code-block:: shell

    cd notas
    pipenv install doc8
    pipenv install rstcheck

