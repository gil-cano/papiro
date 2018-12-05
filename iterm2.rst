.. _iterm2:

iTerm2
======

`iTerm2 <http://www.iterm2.com/>`_ es un remplazo de la Terminal de Apple.

Instalación
-----------

Descarga la aplicación y arrastrala a la carpeta :file:`Applications`

======  =========================================================
⌘ D     divide la terminal verticalmente
⌘ ⇧ D   divide la terminal horizontalmente
⌘ ⌥ UP  cambia de terminal
⌘ /      resalta la posición del cursos
======  =========================================================

Python, Plone
-------------

Cuando iniciamos una instancia de Plone marca el error

.. code-block:: shell

    ValueError: unknown locale: UTF-8

Hay dos maneras de solucionar esto:

- agregar al archivo :file:`.bash_profile` o en el archivo :file:`.zshrc`

.. code-block:: shell

    # iTerm2 fix
    export LC_ALL=en_US.UTF-8
    export LANG=en_US.UTF-8

O en :menuselection:`Preferencias --> Perfil --> Terminal`  solicitar que no se asigne la variable de localización de manera automática (ver imagen) 


.. image:: _static/item2_locale.png
   :alt: iTerm2 (Locale)
   :width: 80%


Ventanas y Pestañas
-------------------

En `iTerm2 <http://www.iterm2.com/>`_ podemos configurar en que directorio se abriran las nuevas ventanas o pestañas. 


.. image:: _static/working_directory.png
   :alt: iTerm2 (Locale)
   :width: 80%


.. image:: _static/working_directory_tabs_windows.png
   :alt: iTerm2 (Locale)
   :width: 80%

Módificaciones al PATH
----------------------

gettetx
~~~~~~~

Para agregar :command:`gettext` al path modificamos el archivo :file:`.zshrc`

.. code-block:: shell

    export PATH=/usr/local/opt/gettext/bin:$PATH

latex
~~~~~

.. code-block:: shell

   export PATH=$PATH:/Library/TeX/texbin/


Zsh
===

Cambiamos a `Zsh <https://www.zsh.org>`_ como shell default

.. code-block:: shell

   $ echo $SHELL
   $ chsh -s $(which zsh)

Salir de sesión y volver a entrar.

.. code-block:: shell

   $ echo $SHELL

Si queremos usar una version mas reciente de `Zsh <https://www.zsh.org>`_ podemos instalarla con :ref:`brew`


.. code-block:: shell

   $ brew install zsh

Usamos la versión Zsh de Homebrew

.. code-block:: shell

   $ chsh -s /usrl/local/bin/zsh


.. warning::

   En macOS Mojave no cambia y manda el siguiente mensaje: ``chsh: /usr/local/bin/zsh: non-standard shell``

oh-my-zsh
=========

Instalamos `Oh My ZSH! <https://ohmyz.sh/>`_

.. code-block:: shell

    $ sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"


editamos el .zshrc para escoger el tema

.. code-block:: shell

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

* `What is ZSH, and Why Should You Use It Instead of Bash? <https://www.howtogeek.com/362409/what-is-zsh-and-why-should-you-use-it-instead-of-bash/>`_
* `Oh-My-ZSH <http://ohmyz.sh/>`_
* `You’re Missing Out on a Better Mac Terminal Experience <https://medium.com/@caulfieldOwen/youre-missing-out-on-a-better-mac-terminal-experience-d73647abf6d7>`_
* `Use Homebrew zsh Instead of the OS X Default <https://rick.cogley.info/post/use-homebrew-zsh-instead-of-the-osx-default/>`_
* `zsh <https://sourabhbajaj.com/mac-setup/iTerm/zsh.html>`_
* `Become A Command-Line Power User With Oh-My-ZSH And Z <https://www.smashingmagazine.com/2015/07/become-command-line-power-user-oh-my-zsh-z/>`_
* `Cobalt2 for iTerm2 and ZSH <https://github.com/wesbos/Cobalt2-iterm>`_
* `How to Customize your Terminal with ZSH <https://hackernoon.com/how-to-trick-out-terminal-287c0e93fce0>`_
* `Jazz Up Your ZSH Terminal In Seven Steps <https://medium.freecodecamp.org/jazz-up-your-zsh-terminal-in-seven-steps-a-visual-guide-e81a8fd59a38>`_
* `Faster and enjoyable ZSH (maybe) <https://htr3n.github.io/2018/07/faster-zsh/>`_
