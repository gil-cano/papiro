Pyenv
=====

Configuración
~~~~~~~~~~~~~

.. code-block:: shell

    $ brew install pyenv
    $ brew install pyenv-virtualenv

Ver todas las verciones disponibles de python

.. code-block:: shell

    $ pyenv install --list

Instalar una versión 

.. code-block:: shell

    $ pyenv install  3.10.6
    python-build: use openssl@1.1 from homebrew
    python-build: use readline from homebrew
    Downloading Python-3.10.6.tar.xz...
    -> https://www.python.org/ftp/python/3.10.6/Python-3.10.6.tar.xz
    Installing Python-3.10.6...
    python-build: use tcl-tk from homebrew
    python-build: use readline from homebrew
    python-build: use zlib from xcode sdk
    Installed Python-3.10.6 to /Users/gil/.pyenv/versions/3.10.6

Si queremos que use zlib de homebrew hay que poner algo como esto:

.. code-block:: shell

    export LDFLAGS="-L/usr/local/opt/zlib/lib"
    export CPPFLAGS="-I/usr/local/opt/zlib/include"

Agregamos a nuestro .zshrc

.. code-block:: shell

    if command -v pyenv 1>/dev/null 2>&1; then
      export PYENV_VIRTUALENV_DISABLE_PROMPT=1
      eval "$(pyenv init -)"
      eval "$(pyenv virtualenv-init -)"
    fi


Para ver que version es la default

.. code-block:: shell

    pyenv version

Para poner una version default

.. code-block:: shell

    pyenv global 3.10.6 2.7.18


.. code-block:: shell

   $ python --version
    Python 3.10.6

Para ver las versiones instaladas

.. code-block:: shell

    pyenv versions

Crean un ambiente virtual

.. code-block:: shell

    $ pyenv virtualenv 3.10.6 proj1-env
    Looking in links: /var/folders/07/6qr9cd9972ggl74l4w7btjvh0000gn/T/tmpo68w9ded
    Requirement already satisfied: setuptools in /Users/gil/.pyenv/versions/3.9.13/envs/plonepy/lib/python3.9/site-packages (58.1.0)
    Requirement already satisfied: pip in /Users/gil/.pyenv/versions/3.9.13/envs/plonepy/lib/python3.9/site-packages (22.0.4)


Se puede activar con

.. code-block:: shell

    $ pyenv activate proj1-env

O definir por directorio

.. code-block:: shell

    pyenv local proj1-env

Para desintalar o borrar ambiente

.. code-block:: shell

    pyenv virtualenv-delete plonepy

O

.. code-block:: shell

    pyenv uninstall plonepy
