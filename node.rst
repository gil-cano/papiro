Node.js
=======

.. _chapter_content:

Instalación
-----------

Instalamos `node.js <http://nodejs.org/>`_ (v4.6.0)

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
      npm@3.9.3 /usr/local/lib/node_modules/npm

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


Manejo de paquetes
------------------

Para crear un archivo package.json ejecutamos:


.. code-block:: console

    $ npm init
    This utility will walk you through creating a package.json file.
    ...
    name: (voronoi)
    version: (1.0.0)
    description: voronoi diagram
    entry point: (index.js)
    test command:
    git repository:
    keywords: voronoi
    license: (ISC) MIT
    About to write to /Users/gil/projects/javascript/voronoi/package.json:

    {
      "name": "voronoi",
      "version": "1.0.0",
      "description": "voronoi diagram",
      "main": "index.js",
      "scripts": {
        "test": "echo \"Error: no test specified\" && exit 1"
      },
      "keywords": [
        "voronoi"
      ],
      "author": "gilo <gil.cano@gmail.com>",
      "license": "MIT"
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
