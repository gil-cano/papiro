Node.js
=======


Uninstall
---------

Borramos nvm de manera manual, ejecutamos lo siguiente:

.. code-block:: shell

    $ rm -rf "$NVM_DIR"

Editamos ~/.zshrc y borramos las lineas:

.. code-block:: shell

    export NVM_DIR="$HOME/.nvm"
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm
    [[ -r $NVM_DIR/bash_completion ]] && \. $NVM_DIR/bash_completion

Instalación
-----------

nvm
~~~

Primero instalamos un manejador de versiones de node (`node version manager <https://github.com/nvm-sh/nvm>`_).

.. code-block:: shell

    $ curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
    => Downloading nvm from git to '/Users/name/.nvm'
    => Cloning into '/Users/name/.nvm'...
    => Appending nvm source string to /Users/name/.zshrc
    => Appending bash_completion source string to /Users/name/.zshrc
    => Close and reopen your terminal to start using nvm or run the following to use it now:

    export NVM_DIR="$HOME/.nvm"
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
    [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion


Para ver que version de nvm:

.. code-block:: shell

    $ nvm --version
    0.39.0

    $ nvm version
    none

Listar las versiones de node

.. code-block:: shell

    $ nvm ls

node
~~~~

Instalamos la ultima versión de soprte a largo plazo - long term support (LTS)

.. code-block:: shell

    $ nvm install --lts


o podemos Instalamos la ultima version de node

.. code-block:: shell

    $ nvm install node

o una versión en particular

.. code-block:: shell

    $ nvm install 14.8.1
    $ nvm use 14.18.1

probar:

.. code-block:: shell

    $ node -v
    v16.13.0

.. code-block:: shell

    $ nvm version
    v16.13.0


Yarn
~~~~

Instalamos el manejador de paquetes  `yarn <https://yarnpkg.com/>`_

.. code-block:: shell

    $ npm install --global yarn

    /Users/name/.nvm/versions/node/v14.18.1/bin/yarn -> /Users/name/.nvm/versions/node/v14.18.1/lib/node_modules/yarn/bin/yarn.js
    /Users/name/.nvm/versions/node/v14.18.1/bin/yarnpkg -> /Users/name/.nvm/versions/node/v14.18.1/lib/node_modules/yarn/bin/yarn.js


probar:

.. code-block:: shell

    $ yarn -v
    1.22.17

Yeoman
~~~~~~

.. code-block:: shell

    $ npm install -g yo


.. code-block:: shell

    $ yo --version
    4.3.0

Volto generator
~~~~~~~~~~~~~~~

.. code-block:: shell

    $ npm install -g @plone/generator-volto
    + @plone/generator-volto@4.4.0


Volto
~~~~~

.. code-block:: shell

    $ yo @plone/volto
    Getting latest Volto version
    Using latest released Volto version: 13.15.1

    $ cd volto-project-myprojectname
    $ yarn start


ver `Volto developer documentation <https://docs.voltocms.com/getting-started/install/>`_

ver `Mastering Plone 6 Developmnet <https://training.plone.org/5/mastering-plone/installation.html#installing-plone-frontend>`_



Yeoman
------

.. code-block:: shell

    $ npm install -g yo
    $ npm install -g generator-webapp
    $ mkdir mytodo && cd mytodo
    $ yo webapp
    $ npm start
    $ npm run serve:test
    $ npm run build


Ir a la página del generador

.. code-block:: shell

    $ npm home generator-webapp


Instalación (deprecated)
------------------------

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

