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

# Versiones

Plone usa las siguinets [versiones](https://6.docs.plone.org/volto/contributing/version-policy.html#plone-python-and-plone-rest-api-compatibility) de Volto

| Plone | Python       | Volto            |
| ----- | ------------ | ---------------- |
| 6.2   | 3.10-3.14    | 19.0.0           |
| 6.1   | 3.10-3.13    | 18.0.0           |

Volto usa las siguientes [versiones](https://6.docs.plone.org/volto/contributing/version-policy.html#node-js|) de Node.js


| Node.js | Volto       |
| ------- | ----------- |
| 22, 24  | Volto 19    |
| 20, 22  | Volto 18    |



## Instalación

### nvm

Primero instalamos un manejador de versiones de node [node version manager](https://github.com/nvm-sh/nvm)`.

```shell
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.4/install.sh | bash
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

Instalar la version necesaria de node [Volto node supports](https://6.docs.plone.org/volto/contributing/version-policy.html)

```shell
nvm install 22.22.2
```

Instalamos la ultima versión de soporte a largo plazo - long term support (LTS)

```shell
nvm install --lts
```

verificar la versión de node

```shell
node -v
```

```console
v24.16.0
```

o
```shell
nvm version
```

```console
v24.16.0
```

Cambiar versión de node

```shell
nvm use 22.22.2
```

## corepack

Habilitamos corepack para que Node.js instale `pnpm` como manejador de paquetes.

```shell
npm i -g corepack@latest && corepack enable
```

## pnpm

Descarga e instala pnpm (Performant npm)

```shell
corepack prepare pnpm@latest --activate
```

verificamos la versión.

```shell
pnpm -v
```

```console
11.5.0
```

## Volto

```shell
uvx cookieplone
```

ver [Mastering Plone 6 Developmnet](https://training.plone.org/5/mastering-plone/installation.html#installing-plone-frontend)


[Setting up a Node development environment](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs/development_environment)

[Node.js](https://6.docs.plone.org/volto/contributing/version-policy.html#node-js)

[Version policy]
