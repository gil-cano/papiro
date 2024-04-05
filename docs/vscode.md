# Visual studio Code

## Línea de comandos en macOS

[Visual Studio Code](https://code.visualstudio.com) incluye el comando `code`, para abrir archivos desde una terminal.

* Inicia VS Code.
* Abre la paleta de comandos con <kbd>F1</kbd> o (<kbd>⌘</kbd> + <kbd>⇧</kbd> + <kbd>P</kbd>) y escribe 'shell command' para encontrar el comando:
```console
Shell Command: Install 'code' command in PATH
```

```{figure} _static/vscode/vsc_shell.png
:alt: Shell Command: Install 'code' command in PATH

Shell Command: Install 'code' command in PATH
```
 * Reinicia la terminal para que el nuevo `$PATH` tome efecto.

```{note}
| Teclas        | Descripción        |
| :---          | ---                |
| <kbd>F1</kbd> | paleta de comandos |
| <kbd>⌘</kbd> <kbd>⇧</kbd> <kbd>P</kbd>  | paleta de comandos |
```

[Visual Studio Code on macOS](https://code.visualstudio.com/docs/setup/mac)


## GitHub theme for VS Code

Instala la extension [GitHub Theme](https://github.com/primer/github-vscode-theme)

Seleccióna el tema.

```{figure} _static/vscode/github-themes.png
:alt: set color theme

Color theme
```

## Python en Visual Studio Code

Instala la extensión [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

Por default instalara un paquede de extensiones: Pylance, Python Debugger, Jupyter (E. Pack 2 Jupyter Keymap, Jupyter Notebook Renderers)

[Python in Visual Studio Code](https://code.visualstudio.com/docs/languages/python)

### Configuración

```shell
mkdir product
cd product
pipenv install -python=python3.8
code product
```

.. image:: _static/vscode/vsc_interpreter.png
   :alt: shell command


```{warning}
Abrimos un archivo :file:`.py`. La extensión de Python muestra un botón en la barra de estado donde podemos seleccinar el ambiente de Python a usar. Las preferencias son salvadas en el archivo :file:`.vscode/settings.json`.
```

### Debug

Selecciona la linea en el gutter y presiona ``F5``


.. image:: _static/vscode/vsc_debug.png
   :alt: shell command

La ejecusíon se detiene en la linea selecionada y aparece la barra de debug

.. image:: _static/vscode/vsc_debugtoolbar.png
   :alt: shell command


La consola de debug

.. image:: _static/vscode/vsc_debugconsole.png
   :alt: shell command


### Testing
`pytest <https://code.visualstudio.com/docs/python/testing#_enable-a-test-framework>`_

```shell
cd product
pipenv install pytest
```

Abilitamos las pruebas con el comando Python: Configure Tests

Linters

`flake8 <https://code.visualstudio.com/docs/python/linting#_enable-linters>`_

```shell
    cd product
    pipenv install flake8
```

## reStructuredText

### Instalación

Instalamos la extension [reStructuredText](https://docs.restructuredtext.net)

* Vamos a la vista de extensiones dando clic en el quinto icono de la barra izquierda.
* Escribimos "restructuredtext" en la caja de búsqueda y damos enter.
* Damos clic en el botón instalar.


### Configuración

.. code-block:: shell

    mkdir notas
    cd notas
    pipenv install -python=python3.8
    pipenv install Sphinx
    pipenv shell
    (notas) sphinx-quickstart
    (notas) code .



```{warning}
Abrimos el archivo :file:`conf.py`. La extensión de Python muestra un botón en la barra de estado donde podemos seleccinar el ambiente de Python a usar. Las preferencias son salvadas en el archivo :file:`.vscode/settings.json`.
```

## Linters

```shell
cd notas
pipenv install doc8
pipenv install rstcheck
```

## Uninstall

Borramos los folders de configuración del usuario:

```shell
rm $HOME/Library/Application Support/Code
rm ~/.vscode
```
movemos la app a la basura.

[Uninstall Visual Studio Code](https://code.visualstudio.com/docs/setup/uninstall)
