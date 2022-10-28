Instalar [brew](https://brew.sh/)
# Instalación de brew

ver https://brew.sh/

# Git
```sh
brew install git
```

# Configurando Git por primera vez
https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Configurando-Git-por-primera-vez

https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup

Lo primero que deberás hacer cuando instales Git es establecer tu nombre de usuario y dirección de correo electrónico.

```sh
git config --global user.name "John Doe"
git config --global user.email "johndoe@example.com"
```

## Configuración básica del cliente
https://git-scm.com/book/es/v2/Personalizaci%C3%B3n-de-Git-Configuraci%C3%B3n-de-Git

https://git-scm.com/book/sv/v2/Customizing-Git-Git-Configuration

puedes elegir el editor de texto por defecto que se utilizará cuando Git necesite que introduzcas un mensaje
```sh
git config --global core.editor nano
```

## Git Alias
https://git-scm.com/book/es/v2/Fundamentos-de-Git-Alias-de-Git

https://git-scm.com/book/en/v2/Git-Basics-Git-Aliases

Si no quieres teclear el nombre completo de cada comando de Git, puedes establecer fácilmente un alias
```sh
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.ci commit
```

## Comprobando tu Configuración

Si quieres comprobar tu configuración, puedes usar el comando git config --list para mostrar todas las propiedades que Git ha configurado:

```sh
git config --list 
```

# Python
Antes de installar python debemos instalar varios modulos si queremos tenerlos disponibles.

En brew las dependencias de python son: gdbm ✔, mpdecimal ✘, openssl@1.1 ✘, readline ✔, sqlite ✔, xz ✔

## gdbm
gdbm es necesario para usar el profiler de Zope (Control_Panel/DebugInfo)

```sh
brew install gdbm
```

## readline
readline es una biblioteca para edición de linea de comandos

```sh
brew install readline
```
```sh
==> Caveats
readline is keg-only, which means it was not symlinked into /usr/local,
because macOS provides BSD libedit.

For compilers to find readline you may need to set:
  export LDFLAGS="-L/usr/local/opt/readline/lib"
  export CPPFLAGS="-I/usr/local/opt/readline/include"
```

## sqlite
Interface para SQLite
```sh
brew install sqlite
```
```sh
==> Caveats
sqlite is keg-only, which means it was not symlinked into /usr/local,
because macOS already provides this software and installing another version in
parallel can cause all kinds of trouble.

If you need to have sqlite first in your PATH, run:
  echo 'export PATH="/usr/local/opt/sqlite/bin:$PATH"' >> ~/.zshrc

For compilers to find sqlite you may need to set:
  export LDFLAGS="-L/usr/local/opt/sqlite/lib"
  export CPPFLAGS="-I/usr/local/opt/sqlite/include"
```

## xz
xz es una biblioteca de compresssion de datos en particular nos interesa liblzma.

```sh
brew install xz
```

## yaml
parser de YAML

```sh
brew info libyaml
```

## bzip2

```sh
brew install bzip2
```
```sh
==> Caveats
bzip2 is keg-only, which means it was not symlinked into /usr/local,
because macOS already provides this software and installing another version in
parallel can cause all kinds of trouble.

If you need to have bzip2 first in your PATH, run:
  echo 'export PATH="/usr/local/opt/bzip2/bin:$PATH"' >> ~/.zshrc

For compilers to find bzip2 you may need to set:
  export LDFLAGS="-L/usr/local/opt/bzip2/lib"
  export CPPFLAGS="-I/usr/local/opt/bzip2/include"
```

## Pillow

* jpeg biblioteca para manejo de imagenes JPEG
* libpng biblioteca para manejo de imagenes PNG
* libtiff provee funcionalidad de compresión TIFF
* little-cms2 provee manejo de color
* openjpeg biblioteca para manejo de imagenes JPEG-2000 
* webp formato de compresssion sin perdidad para imagenes web
* zlib provee acceso a PNGs comprimidos
* libxcb provee soporte para X11

```sh
brew install jpeg libpng libtiff little-cms2 webp zlib
```

```sh
==> Caveats
==> jpeg
jpeg is keg-only, which means it was not symlinked into /usr/local,
because it conflicts with `jpeg-turbo`.

If you need to have jpeg first in your PATH, run:
  echo 'export PATH="/usr/local/opt/jpeg/bin:$PATH"' >> ~/.zshrc

For compilers to find jpeg you may need to set:
  export LDFLAGS="-L/usr/local/opt/jpeg/lib"
  export CPPFLAGS="-I/usr/local/opt/jpeg/include"

==> zlib
zlib is keg-only, which means it was not symlinked into /usr/local,
because macOS already provides this software and installing another version in
parallel can cause all kinds of trouble.

For compilers to find zlib you may need to set:
  export LDFLAGS="-L/usr/local/opt/zlib/lib"
  export CPPFLAGS="-I/usr/local/opt/zlib/include"
```
## pyenv
==> Dependencies
Required: autoconf ✘, openssl@1.1 ✘, pkg-config ✘, readline ✔

```sh
brew install pyenv
brew install pyenv-virtualenv
```
```sh
==> Caveats
To enable auto-activation add to your profile:
  if which pyenv-virtualenv-init > /dev/null; then eval "$(pyenv virtualenv-init -)"; fi
```

agregamos eso a nuestro .zshrc

```sh
if which pyenv-virtualenv-init > /dev/null; then 
  eval "$(pyenv virtualenv-init -)"; 
fi
```

```sh
pyenv install 2.7.18
pyenv install 3.7.14
pyenv install 3.10.7
pyenv global 3.10.7 2.7.18
pyenv versions
```

# Plone
Creamos en el home un directorio .buildout

```sh
mkdir -p .buildout/eggs
mkdir -p .buildout/downloads
mkdir -p .buildout/extends
touch .buildout/default.cfg
```
El archivo default.cfg debe contener algo como lo siguiente:

```sh
[buildout]
eggs-directory = /Users/username/.buildout/eggs
download-cache = /Users/username/.buildout/downloads
extends-cache = /Users/username/.buildout/extends

index = https://pypi.python.org/simple
socket-timeout = 3
```

## wv
wv permite el acceso a archivos de tipo Microsoft Word

```sh
brew install wv
```
## clone

```sh
git clone plone-project
cd  plone-project
pyenv virtualenv 2.7.18 plone4.3
pyenv local plone4.3

```

# VSCode

Para agregar el comando code al PATH, abrimos vscode y escribimos *shell command* para encontrar el comando *Shell Command: Install 'code' command in PATH*

```
⌘ + ⇧ + P  # paleta de comandos
```

Reiniciamos la terminal para que el nuevo PATH tome efecto.

## Extenciones

* Github Theme

# Referencias
[The Arctic Ice Studio Markdown Code Style.](https://arcticicestudio.github.io/styleguide-markdown/)