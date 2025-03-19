# NodeJS

Node.js® is a free, open-source, cross-platform JavaScript runtime environment

## Uninstall

Borramos {term}`nvm` de manera manual, ejecutamos lo siguiente:

```shell
rm -rf "$NVM_DIR"
```

```shell
rm -rf .npm
```

Editamos ~/.zshrc y borramos las lineas:


```console
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm
[[ -r $NVM_DIR/bash_completion ]] && \. $NVM_DIR/bash_completion
```

## Instalación

### nvm

Primero instalamos un manejador de versiones de node [node version manager](https://github.com/nvm-sh/nvm)`.

```shell
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.2/install.sh | bash
```
```console
=> Compressing and cleaning up git repository

=> Appending nvm source string to /Users/myuser/.zshrc
=> Appending bash_completion source string to /Users/myuser/.zshrc
=> Close and reopen your terminal to start using nvm or run the following to use it now:

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
```

To verify that nvm has been installed, do:

```shell
nvm --version
```

### Node.js

listar versiones de node disponibles de manera remota

```shell
nvm ls-remote
```

listar versiones de node instaladas de manera local

```shell
nvm ls
```

Instalar una version especificad de node

```shell
nvm install 20.19.0
```

Instalamos la ultima versión de soporte a largo plazo - long term support (LTS)

```shell
nvm install --lts
```

Cambiar version de node

```shell
nvm use 20.19.2
```

verificar la version de node

```shell
node -v
```

```console
v22.14.0
```

o
```shell
nvm version
```

```console
v22.14.0
```

## corepack

Habilitamos corepack para que Node.js instale `pnpm` como manejador de paquetes.

```shell
npm i -g corepack@latest && corepack enable
```

## Volto

```shell
pipx run cookieplone project
```

ver `Mastering Plone 6 Developmnet <https://training.plone.org/5/mastering-plone/installation.html#installing-plone-frontend>`_


## Instalación (deprecated)

## Manejo de paquetes

Para crear un nuevo paquete necesitamos un archivo :file:`package.json` ejecutamos:


.. code-block:: console

    $ npm init
    This utility will walk you through creating a package.json file.
    ...
    package name: (myapp)
    version: (1.0.0)
    description:
    entry point: (index.js)
    test command:
    git repository:
    keywords:
    author:
    license: (ISC)
    About to write to /Users/gil/projects/javascript/myapp/package.json:

    {
      "name": "myapp",
      "version": "1.0.0",
      "description": "",
      "main": "index.js",
      "scripts": {
        "test": "echo \"Error: no test specified\" && exit 1"
      },
      "author": "",
      "license": "ISC"
    }


    Is this ok? (yes)

para instalar un paquete y agregarlo al archivo package.json ejecutamos:

.. code-block:: console

    $ npm install <pkg> --save

para paquetes que solo se usaran para desarrollo se usara --save-dev

.. code-block:: console

    $ npm install <pkg> --save-dev

Si tenemos un archivo package.json y queremos instalar sus dependencias ejecutamos:

.. code-block:: console

    $ npm install

`Creating Node.js modules <https://docs.npmjs.com/getting-started/creating-node-modules>`_

`Setting up a Node development environment <https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs/development_environment>`_

Version policy [Node.js](https://6.docs.plone.org/volto/contributing/version-policy.html#node-js)
