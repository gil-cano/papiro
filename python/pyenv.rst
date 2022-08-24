Pyenv
=====

Configuración
~~~~~~~~~~~~~

.. code-block:: shell

    $ brew install pyenv
    $ brew install pyenv-virtualenv
    $ pyenv install 3.9.13
    python-build: use openssl@1.1 from homebrew
    python-build: use readline from homebrew
    Downloading Python-3.9.13.tar.xz...
    -> https://www.python.org/ftp/python/3.9.13/Python-3.9.13.tar.xz
    Installing Python-3.9.13...
    python-build: use tcl-tk from homebrew
    python-build: use readline from homebrew
    python-build: use zlib from xcode sdk
    Installed Python-3.9.13 to /Users/gil/.pyenv/versions/3.9.13

Agregamos a nuestro .zshrc

.. code-block:: shell

    if command -v pyenv 1>/dev/null 2>&1; then
      export PYENV_VIRTUALENV_DISABLE_PROMPT=1
      eval "$(pyenv init -)"
      eval "$(pyenv virtualenv-init -)"
    fi

.. code-block:: shell

    $ pyenv virtualenv 3.9.13 plonepy
    Looking in links: /var/folders/07/6qr9cd9972ggl74l4w7btjvh0000gn/T/tmpo68w9ded
    Requirement already satisfied: setuptools in /Users/gil/.pyenv/versions/3.9.13/envs/plonepy/lib/python3.9/site-packages (58.1.0)
    Requirement already satisfied: pip in /Users/gil/.pyenv/versions/3.9.13/envs/plonepy/lib/python3.9/site-packages (22.0.4)
    $ pyenv activate plonepy

.. code-block:: shell

    $ python --version
    Python 3.9.13

Ver todas las verciones disponibles de python

.. code-block:: shell

    $ pyenv install --list


Poner una version de python como default:

.. code-block:: shell

    $ pyenv global 3.9.13
    $ pyenv versions
      system
      3.9.13
      3.9.13/envs/plonepy
    * plonepy (set by PYENV_VERSION environment variable) 

