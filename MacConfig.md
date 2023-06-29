Instalar [brew](https://brew.sh/)
# Instalación de brew

ver https://brew.sh/

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
==> Checking for `sudo` access (which may request your password)...
Password:
==> This script will install:
/usr/local/bin/brew
/usr/local/share/doc/homebrew
/usr/local/share/man/man1/brew.1
/usr/local/share/zsh/site-functions/_brew
/usr/local/etc/bash_completion.d/brew
/usr/local/Homebrew
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
```

# Make

```sh
brew install make
==> Caveats
GNU "make" has been installed as "gmake".
If you need to use it as "make", you can add a "gnubin" directory
to your PATH from your bashrc like:

    PATH="/usr/local/opt/make/libexec/gnubin:$PATH"
```

Agregar en el ~/.zshrc


# Git
```sh
brew install git
```

## Configurando Git por primera vez
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

# GitHub

## Revisar las llaves SSH existentes

Lista los archivos en tu directorio .ssh

```sh
ls -la ~/.ssh
```

## Genera una nueva llave SSH

Genereamos la nueva llave.

```sh
$ ssh-keygen -t ed25519 -C "your_email@example.com"
Generating public/private ed25519 key pair.
Enter file in which to save the key (/Users/you/.ssh/id_ed25519):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /Users/you/.ssh/id_ed25519
Your public key has been saved in /Users/you/.ssh/id_ed25519.pub
```

Inicia el ssh-agente en segundo plano

```sh
$ eval "$(ssh-agent -s)"
Agent pid 10815
```

Modificamos el archivo ~/.ssh/config para cargar las llaves de manera automatica al ssh-agent y almancenar las frases de contraseñas en el llavero.

Si no exte el archivo lo creamos

```sh
$ touch ~/.ssh/config
```

Modificamos el archivo con las siguientes lineas:

```sh
Host github.com
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ed25519
```

Agregamos nuestra llave privada al ssh-agent y guardamos la frases de contraseñas en el llavero.

```sh
$ ssh-add --apple-use-keychain ~/.ssh/id_ed25519
Enter passphrase for /Users/you/.ssh/id_ed25519:
Identity added: /Users/you/.ssh/id_ed25519 (your_email@example.com)
```

Agregamos la llave publica a GitHub 

Copiamos la llave publica

```sh
pbcopy < ~/.ssh/id_ed25519.pub
```

agregamos una llave nueva en https://github.com/settings/keys y pegamos la llave publica.

Probamos la conección y verificamos que la huella coincida con alguna de las [huellas de github](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints)

```sh
ssh -T git@github.com
The authenticity of host 'github.com (IP)' can't be established.
ED25519 key fingerprint is SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
```

## GitHub CLI
```sh
brew install gh
```

```sh
gh auth login
? What account do you want to log into? GitHub.com
? What is your preferred protocol for Git operations? HTTPS
? Authenticate Git with your GitHub credentials? Yes
? How would you like to authenticate GitHub CLI? Paste an authentication token
Tip: you can generate a Personal Access Token here https://github.com/settings/tokens
The minimum required scopes are 'repo', 'read:org', 'workflow'.
? Paste your authentication token: ****************************************
- gh config set -h github.com git_protocol https
✓ Configured git protocol
✓ Logged in as login-name
```

```sh
gh auth logout
gh auth login --with-token < mytoken.txt
gh auth status
```

https://cli.github.com/manual/



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

## openssh@1.1

```sh
brew install openssl@1.1
```

```sh
==> Caveats
==> openssl@1.1
A CA file has been bootstrapped using certificates from the system
keychain. To add additional certificates, place .pem files in
  /usr/local/etc/openssl@1.1/certs

and run
  /usr/local/opt/openssl@1.1/bin/c_rehash

openssl@1.1 is keg-only, which means it was not symlinked into /usr/local,
because macOS provides LibreSSL.

If you need to have openssl@1.1 first in your PATH, run:
  echo 'export PATH="/usr/local/opt/openssl@1.1/bin:$PATH"' >> ~/.zshrc

For compilers to find openssl@1.1 you may need to set:
  export LDFLAGS="-L/usr/local/opt/openssl@1.1/lib"
  export CPPFLAGS="-I/usr/local/opt/openssl@1.1/include"

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
brew install libxcb
brew install libx11
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
# pyenv configuration for Zsh
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

# Enable auto-activation of virtualenvs 
if which pyenv-virtualenv-init > /dev/null; then 
  eval "$(pyenv virtualenv-init -)";
fi
```

```sh
pyenv install 2.7.18
pyenv install 3.9.16
pyenv install 3.11.1
pyenv global 3.11.1 2.7.18
pyenv versions

pyenv virtualenv 3.9.16 proj1-env
pyenv local proj1-env
pyenv virtualenv-delete proj1-env
pyenv uninstall 3.9.16
```

## pipx
```sh
brew install pipx
pipx install httpie
pipx install pls
pipx install bpytop
pipx list
pipx ensurepath
pipx reinstall-all
```
```sh
# Created by `pipx` on 2022-12-06 15:32:16
export PATH="$PATH:/Users/gil/.local/bin"

alias ls='pls --multi-cols'
```

# Buildout
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
## Plone 4, 5

```sh
gh repo clone useer-name/plone-project
```

```sh
git clone plone-project
cd  plone-project
pyenv virtualenv 2.7.18 plone4.3
pyenv local plone4.3
pip install -r requirements.txt 
buildout
```


# Plone 6

```sh
mkdir my_project
cd my_project
pyenv virtualenv 3.10.10 plone6.0
```


```sh
pipx install cookiecutter
pipx install plonecli
pipx inject plonecli bobtemplates.plone
```

```sh
pipx install zpretty
```

# Tools

A cat(1) clone with wings.

```sh
brew install bat
```

Linux/OSX/FreeBSD resource monitor 

```sh
pipx install bpytop
```


# VSCode

Para agregar el comando code al PATH, abrimos vscode y escribimos *shell command* para encontrar el comando *Shell Command: Install 'code' command in PATH*

```
⌘ + ⇧ + P  # paleta de comandos
```

Reiniciamos la terminal para que el nuevo PATH tome efecto.

## Extenciones

* [Github Theme](https://marketplace.visualstudio.com/items?itemName=GitHub.github-vscode-theme) 
* [MyST-Markdown](https://marketplace.visualstudio.com/items?itemName=ExecutableBookProject.myst-highlight)
* [Rainbow CSV](https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv)
* [ZCML language configuration](https://marketplace.visualstudio.com/items?itemName=erral.erral-zcmlLanguageConfiguration)
requiere zpretty
  ```shell
  pipx install zpretty
  ```

# Referencias
* [The Arctic Ice Studio Markdown Code Style.](https://arcticicestudio.github.io/styleguide-markdown/)
* [Connect with SSH.](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
