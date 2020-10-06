Node.js
=======

Primero instalamos un manejador de versiones de node (`node version manager <https://github.com/nvm-sh/nvm>`_).

.. code-block:: shell

    $ curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.36.0/install.sh | bash
    => Downloading nvm from git to '/Users/gil/.nvm'
    => Cloning into '/Users/gil/.nvm'...
    => Appending nvm source string to /Users/gil/.zshrc
    => Appending bash_completion source string to /Users/gil/.zshrc
    => Close and reopen your terminal to start using nvm or run the following to use it now:

    export NVM_DIR="$HOME/.nvm"
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
    [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion


Instlamos la ultima version de node

.. code-block:: shell

    $ nvm install node

la versión de soprte a largo plazo - long term support (LTS)

.. code-block:: shell

    $ nvm install --lts

o una versión en particular

.. code-block:: shell

    $ nvm install 12.18.4


Instalamos el manejador de paquetes  `yarn <https://yarnpkg.com/>`_

.. code-block:: shell

    $ curl -o- -L https://yarnpkg.com/install.sh | bash
    > Extracting to ~/.yarn...
    > Adding to $PATH...
    > We've added the following to your /Users/gil/.zshrc
    > If this isn't the profile of your current shell then please add the following to your correct profile:

    export PATH="$HOME/.yarn/bin:$HOME/.config/yarn/global/node_modules/.bin:$PATH"

ver `React <https://training.plone.org/5/react/bootstrap.html>`_

Instalación
-----------

Instalamos `node.js <http://nodejs.org/>`_ (v10.16.3)

.. code-block:: console

    Node was installed at

       /usr/local/bin/node

    npm was installed at

       /usr/local/bin/npm

    Make sure that /usr/local/bin is in your $PATH.

npm
---

Node comes with `npm <https://www.npmjs.com/>`_ installed so you should have a version of npm. However, npm gets updated more frequently than Node does, so you'll want to make sure it's the latest version.

.. code-block:: console

    $ sudo npm install npm -g
      Password:
      /usr/local/bin/npm -> /usr/local/lib/node_modules/npm/bin/npm-cli.js
      npm@3.10.9 /usr/local/lib/node_modules/npm

Test: Run npm -v. The version should be higher than 2.1.8.


Para instalar un paquete de manera global (/usr/local/lib/node_modules) usamos el argumento  -g

.. code-block:: console

    $ sudo npm install -g jshint
    /usr/local/bin/jshint -> /usr/local/lib/node_modules/jshint/bin/jshint
    $ sudo npm install -g csslint
    /usr/local/bin/csslint -> /usr/local/lib/node_modules/csslint/cli.js


Para instalar un paquete de manera local

.. code-block:: console

    $ npm install <package_name>

This will create the node_modules directory in your current directory(if one doesn't exist yet), and will download the package to that directory.

Ejemplo:

.. code-block:: console

    $ npm install d3@next

grunt-cli
---------

.. code-block:: console

    $ npm install -g grunt-cli


Manejo de paquetes
------------------

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

`How to install Node.js <https://nodejs.dev/learn/how-to-install-nodejs>`_

`Creating Node.js modules <https://docs.npmjs.com/getting-started/creating-node-modules>`_

`Setting up a Node development environment <https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs/development_environment>`_

