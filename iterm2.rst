iTerm2
======

Cuando iniciamos una instancia de Plone marca el error

.. code-block:: bash

    unknown locale: UTF-8

para solucionar eso hay que agregar al .bash_profile o en el .zshrc

.. code-block:: bash

    # iTerm2 fix
    export LC_ALL=en_US.UTF-8
    export LANG=en_US.UTF-8

Para dividir la terminal verticalmente ⌘+D y ⌘+⇧+D horizontal

⌘+/ resalta la posición del cursos.

Para agregar gettext agregamos en .zshrc

.. code-block:: bash

    export PATH=/usr/local/opt/gettext/bin:$PATH


oh-my-zsh
=========

Cambiamos a Zsh como shell default

.. code-block:: bash

    $ echo $SHELL
    $ chsh -s $(which zsh)
    $ echo $SHELL

Instalamos oh-my-zsh

$ sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"


editamos el .zshrc para escoger el tema

.. code-block:: bash

    ZSH_THEME="agnoster"


Step-by-step installation

* Drop the cobalt2.zsh-theme file in to the ~/.oh-my-zsh/themes/ directory.
* Open up your ZSH preferences at ~/.zshrc and change the theme variable to ZSH_THEME="cobalt2".
* In iTerm2 access the Preferences pane on the Profiles tab.
* Under the Colors tab import the cobalt2.itermcolors file via the Load Presets drop-down.
* Under the Text tab change the font for each type (Regular and Non-ASCII) to 'Inconsolata for Powerline'. (Refer to the powerline-fonts repo for help on font installation.)
* Refresh ZSH by typing source ~/.zshrc on the command line.


Bibliografía
------------

* `Oh-My-ZSH <http://ohmyz.sh/>`_
* `Become A Command-Line Power User With Oh-My-ZSH And Z <https://www.smashingmagazine.com/2015/07/become-command-line-power-user-oh-my-zsh-z/>`_
* `Cobalt2 for iTerm2 and ZSH <https://github.com/wesbos/Cobalt2-iterm>`_

