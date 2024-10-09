# Visual studio Code

## Línea de comandos en macOS

[Visual Studio Code](https://code.visualstudio.com) incluye el comando `code`, para abrir archivos desde una terminal.

* Inicia VS Code.
* Abre la paleta de comandos con <kbd>F1</kbd> o (<kbd>⌘</kbd> + <kbd>⇧</kbd> + <kbd>P</kbd>) y escribe 'shell command' para encontrar el comando:

```console
Shell Command: Install 'code' command in PATH
```

```{figure} _static/vscode/vsc_shell.png
:alt: Install 'code' command in PATH

Install 'code' command in PATH
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

Por default instala las extensiones: [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) y [Python Debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy).

[Python in Visual Studio Code](https://code.visualstudio.com/docs/languages/python)

### Configuración

```shell
pyenv virtualenv 3.12.2 product
mkdir product
cd product
pyenv local product
code .
```

```{figure} _static/vscode/vsc_interpreter.png
:alt: shell command

shell command
```

```{warning}
Abrimos un archivo `.py`. La extensión de Python muestra un botón en la barra de estado donde podemos seleccinar el ambiente de Python a usar. Las preferencias son salvadas en el archivo `.vscode/settings.json`.
```

### Debug

Selecciona la linea en el gutter y presiona ``F5``

```{figure} _static/vscode/vsc_debug.png
:alt: debug

debug
```

La ejecusíon se detiene en la linea selecionada y aparece la barra de debug

```{figure} _static/vscode/vsc_debugtoolbar.png
:alt: debug

debug
```

La consola de debug

```{figure} _static/vscode/vsc_debugconsole.png
:alt: debug

debug
```

### Testing
[pytest](https://code.visualstudio.com/docs/python/testing#_enable-a-test-framework)

```shell
cd product
pip install pytest
```

Abilitamos las pruebas con el comando Python: Configure Tests

Linters

[flake8](https://code.visualstudio.com/docs/python/linting#_enable-linters)

```shell
cd product
pip install flake8
```

## Jupyter

Instala la extensión [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)

Por default instala las extensiones: 
* [Jupyter Keymap](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter-keymap)
* [Jupyter Notebook Renderers](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter-renderers)
* [Jupyter Cell Tags](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.vscode-jupyter-cell-tags)
* [Jupyter Slide Show](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.vscode-jupyter-slideshow)

## Ruff

Un linter y formateador de código python extremadamente rapido, escrito en Rust

Instala la extension [Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)

Ruff resalta errores según la regla de estilos usada, por ejemplo si importas una función que no usas.

```{figure} _static/vscode/ruff-lint.png
:alt: Install 'code' command in PATH

Install 'code' command in PATH
```

"Quick Fix" no premite corregirlo de manera automática (<kbd>⌘</kbd> + <kbd>.</kbd>)

```{figure} _static/vscode/ruff-quickfix.png
:alt: Quick fix

Quick fix
```

"Format Document"

Abre la paleta de comandos (<kbd>⌘</kbd> + <kbd>⇧</kbd> + <kbd>P</kbd>) y selecciona 'Format Document'.

"Organize Imports"

Abre la paleta de comandos (<kbd>⌘</kbd> + <kbd>⇧</kbd> + <kbd>P</kbd>) y selecciona 'Organize Imports'.


## Latex

Instala la extensión [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop)


## Extenciones

* [Github Theme](https://marketplace.visualstudio.com/items?itemName=GitHub.github-vscode-theme) 
* [MyST-Markdown](https://marketplace.visualstudio.com/items?itemName=ExecutableBookProject.myst-highlight)
* [Rainbow CSV](https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv)
* [ZCML language configuration](https://marketplace.visualstudio.com/items?itemName=erral.erral-zcmlLanguageConfiguration)
requiere zpretty

```shell
pipx install zpretty
```

## Crea tus propios snippets
Para crear o editar tus propios snippets, selecciona `Configure User Snippets` en `code > Setting...` y despues selecciona el lenguaje (python.json).

```json
{
	"Add debugger": {
		"prefix": "pdb",
		"body": [
			"import pdb; pdb.set_trace()",
			"$0"
		],
		"description": "break into the debugger"
	}
}
```

## Excluye archivos de la navegación
En `code > Setting... > Setting` buscar la sección `Files: excludes`. Agregar los patrones 

```
**/*.mo
**/*.pyc
**/*.pyo
```

## Font

```console
'VictorMono Nerd Font'
```

## Uninstall

Borra los folders de configuración de usuario:

```shell
rm -rf $HOME/Library/Application Support/Code
rm -rf ~/.vscode
```
mueve la app a la basura.

[Uninstall Visual Studio Code](https://code.visualstudio.com/docs/setup/uninstall)




## reStructuredText

### Instalación

Instalamos la extension [reStructuredText](https://docs.restructuredtext.net)

* Vamos a la vista de extensiones dando clic en el quinto icono de la barra izquierda.
* Escribimos "restructuredtext" en la caja de búsqueda y damos enter.
* Damos clic en el botón instalar.


### Configuración

```shell
mkdir notas
cd notas
pipenv install -python=python3.8
pipenv install Sphinx
pipenv shell
(notas) sphinx-quickstart
(notas) code .
```


```{warning}
Abrimos el archivo :file:`conf.py`. La extensión de Python muestra un botón en la barra de estado donde podemos seleccinar el ambiente de Python a usar. Las preferencias son salvadas en el archivo :file:`.vscode/settings.json`.
```

## Linters

```shell
cd notas
pipenv install doc8
pipenv install rstcheck
```


## OLD
* Markdown Preview Mermaid Support
* Rainbow CSV

```console
code --list-extensions
bierner.markdown-mermaid
erral.erral-zcmllanguageconfiguration
executablebookproject.myst-highlight
github.github-vscode-theme
james-yu.latex-workshop
mechatroner.rainbow-csv
mrorz.language-gettext
ms-python.debugpy
ms-python.isort
ms-python.python
ms-python.vscode-pylance
ms-toolsai.jupyter
ms-toolsai.jupyter-keymap
ms-toolsai.jupyter-renderers
ms-toolsai.vscode-jupyter-cell-tags
ms-toolsai.vscode-jupyter-slideshow
ms-vscode.makefile-tools
yy0931.vscode-sqlite3-editor
```

https://training.plone.org/effective-volto/development/vscode.html


Friday

```console
code --list-extensions
charliermarsh.ruff
davidanson.vscode-markdownlint
dbaeumer.vscode-eslint
emmanuelbeziat.vscode-great-icons
erral.erral-zcmllanguageconfiguration
executablebookproject.myst-highlight
github.github-vscode-theme
james-yu.latex-workshop
mrorz.language-gettext
ms-python.debugpy
ms-python.python
ms-python.vscode-pylance
ms-toolsai.jupyter
ms-toolsai.jupyter-keymap
ms-toolsai.jupyter-renderers
ms-toolsai.vscode-jupyter-cell-tags
ms-toolsai.vscode-jupyter-slideshow
wesbos.theme-cobalt2
```

# Files Excludes

Settings

**/*.pyc
