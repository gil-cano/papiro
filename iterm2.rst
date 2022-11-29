iTerm2
======

`iTerm2 <http://www.iterm2.com/>`_ es un remplazo de la Terminal de Apple.

Instalación
-----------

Descarga la aplicación y arrastrala a la carpeta :file:`Applications`

======  =====================================
⌘ ⏎     pantalla completa
⌘ D     divide la terminal verticalmente
⌘ ⇧ D   divide la terminal horizontalmente
⌘ ⌥ UP  cambia de terminal
⌘ /      resalta la posición del cursos
======  =====================================


Ventanas y Pestañas
-------------------

En `iTerm2 <http://www.iterm2.com/>`_ podemos configurar en que directorio se abriran las nuevas ventanas o pestañas.

.. image:: _static/working_directory.png
   :alt: iTerm2 (Locale)
   :width: 80%

.. image:: _static/working_directory_tabs_windows.png
   :alt: iTerm2 (Locale)
   :width: 80%


Tipo de letra
-------------

Source Code Pro
~~~~~~~~~~~~~~~

`Source Code Pro <https://github.com/adobe-fonts/source-code-pro>`_ es un tipo de letra para programadores. Este tipo de letra tambien se usa en :ref:`sublimetext`

Se instala con brew

.. code-block:: shell

   $ brew tap homebrew/cask-fonts
   $ brew install font-source-code-pro
   $ brew install font-jetbrains-mono
   $ brew install font-monoid-nerd-font
   $ brew list
   $ brew uninstall font-monoid-nerd-font

En iTerm2 :menuselection:`Preferences --> Profiles --> Text` seleccionamos el tipo de letra.

.. image:: _static/iterm2font.png
   :alt: Font for iTerm2
   :width: 80%

Para probar algunos caracteres en la terminal:

.. code-block:: shell

   $ echo "\ue0b0 \u00b1 \ue0a0 \u27a6 \u2718 \u26a1 \u2699"

Nerd Fonts
~~~~~~~~~~

`Nerd Fonts <http://nerdfonts.com>`_


Salto de palabras
-----------------

En iterm2 selccionamos :menuselection:`Preferences --> Profiles --> Keys --> load preset --> Natural Text Editing`.

=== =================================================
⌘ → envia el cursos al inicio de la siguiente palabra
⌘   envia el cursos al inicio de la palabra anterior
=== =================================================


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


Módificaciones al PATH
----------------------

gettetx
~~~~~~~

Para agregar :command:`gettext` al path modificamos el archivo :file:`.bash_profile` o el archivo :file:`.zshrc`

.. code-block:: shell

    export PATH=/usr/local/opt/gettext/bin:$PATH

latex
~~~~~

.. code-block:: shell

   export PATH=$PATH:/Library/TeX/texbin/


Zsh
---

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
---------

Instalamos `Oh My ZSH! <https://ohmyz.sh/>`_

.. code-block:: shell

    $ sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"


Para actuzalizar a la ultima versión.

.. code-block:: shell

   $ omz update


Temas
-----

Editamos el archivo :file:`.zshrc` para definir el tema

.. code-block:: shell

    ZSH_THEME="agnoster"


Spaceship-prompt
~~~~~~~~~~~~~~~~

`Spaceship ZSH <https://github.com/denysdovhan/spaceship-prompt>`_

copiamos el reposistorio:

.. code-block:: shell

   $ git clone https://github.com/denysdovhan/spaceship-prompt.git "$ZSH_CUSTOM/themes/spaceship-prompt"


Hacemos una liga simbolica :file:`spaceship.zsh-theme` al directorio de temas personalizados de `oh-my-zsh <https://ohmyz.sh/>`_

.. code-block:: shell

   $ ln -s "$ZSH_CUSTOM/themes/spaceship-prompt/spaceship.zsh-theme" "$ZSH_CUSTOM/themes/spaceship.zsh-theme"


En el archivo :file:`.zshrc` selccionamos el tema

.. code-block:: shell

   ZSH_THEME="spaceship"

.. warning::

   La rama 4.0 agrego soporte para python


Configuración del prompt en el archivo :file:`.zshrc`

.. code-block:: shell

   SPACESHIP_PROMPT_ORDER=(
       user
       dir
       # host
       git
       # package
       python
       # docker
       venv
       line_sep
       char
   )

   SPACESHIP_PROMPT_FIRST_PREFIX_SHOW="true"
   SPACESHIP_CHAR_PREFIX="\uf79f"
   SPACESHIP_CHAR_SUFFIX=" "
   SPACESHIP_CHAR_COLOR_SUCCESS="yellow"
   SPACESHIP_DIR_COLOR="green"
   SPACESHIP_GIT_BRANCH_PREFIX="\uf7a3"
   SPACESHIP_GIT_BRANCH_COLOR="magenta"
   SPACESHIP_VENV_COLOR="yellow"
   SPACESHIP_VENV_PREFIX="\u "

   # spaceship-prompt v.4.0
   SPACESHIP_PYTHON_SHOW="true"
   SPACESHIP_PYTHON_SYMBOL="\ue235 "
   SPACESHIP_PYTHON_COLOR="yellow"



Powerlevel9k
~~~~~~~~~~~~

.. warning::

   This may be removed

`powerlevel9k <https://github.com/bhilburn/powerlevel9k>`_


copiamos el reposistorio:

.. code-block:: shell

   $ git clone https://github.com/bhilburn/powerlevel9k.git "$ZSH_CUSTOM/themes/powerlevel9k"

Hacemos una liga simbolica :file:`spaceship.zsh-theme` al directorio de temas personalizados de `oh-my-zsh <https://ohmyz.sh/>`_

.. code-block:: shell

   $ ln -s "$ZSH_CUSTOM/themes/powerlevel9k/powerlevel9k.zsh-theme" "$ZSH_CUSTOM/themes/powerlevel9k.zsh-theme"


En el archivo :file:`.zshrc` selccionamos el tema

.. code-block:: shell

   ZSH_THEME="powerlevel9k"

cobalt2
~~~~~~~

`Cobalt2 <https://github.com/wesbos/Cobalt2-iterm>`_

.. code-block:: shell

   $ cp cobalt2.zsh-theme "$ZSH_CUSTOM/themes/cobalt2.zsh-theme"

En el archivo :file:`.zshrc` selccionamos el tema

.. code-block:: shell

   ZSH_THEME="cobalt2"

En la terminal iTerm2 :menuselection:`Preferences --> Profiles --> Colors` importa el archivo :file:`cobalt2.itermcolors` mediante el menu :file:`Color Presets`

En la terminal iTerm2 :menuselection:`Preferences --> Profiles --> Text` cambiamos la fuente para cada tipo (Regular y Non-ASCII) a `Sauce Code Pro Nerd Font Complete`

.. code-block:: shell

   $ source ~/.zshrc


Plugins
-------

git
~~~

Completa con tab los comandos de git

zsh-syntax-highlighting
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

   git clone https://github.com/zsh-users/zsh-syntax-highlighting.git "$ZSH_CUSTOM/plugins/zsh-syntax-highlighting"

.. code-block:: shell

   plugins = (
      colored-man-pages
      git
      pipenv
      python
      zsh-syntax-highlighting
   )

zsh-autosuggestions
~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

   git clone https://github.com/zsh-users/zsh-autosuggestions "$ZSH_CUSTOM/plugins/zsh-autosuggestions"

.. code-block:: shell

   plugins = (
      git
      zsh-autosuggestions
   )


zsh-history-substring-search
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

   git clone https://github.com/zsh-users/zsh-history-substring-search.git "$ZSH_CUSTOM/plugins/zsh-history-substring-search"

.. code-block:: shell

   plugins = (
      git
      history-substring-search
   )

Bibliografía
------------

* `What is ZSH, and Why Should You Use It Instead of Bash? <https://www.howtogeek.com/362409/what-is-zsh-and-why-should-you-use-it-instead-of-bash/>`_
* `You’re Missing Out on a Better Mac Terminal Experience <https://medium.com/@caulfieldOwen/youre-missing-out-on-a-better-mac-terminal-experience-d73647abf6d7>`_
* `MacOS Terminal and Shell Setup with configuration files <https://vict0rs.ch/2018/01/30/mac-terminal-shell-power-user>`_
* `My Terminal Setup: iTerm + Zsh <https://zen-of-programming.com/terminal-setup/>`_
* `zsh <https://sourabhbajaj.com/mac-setup/iTerm/zsh.html>`_
* `Become A Command-Line Power User With Oh-My-ZSH And Z <https://www.smashingmagazine.com/2015/07/become-command-line-power-user-oh-my-zsh-z/>`_
* `Faster and enjoyable ZSH (maybe) <https://htr3n.github.io/2018/07/faster-zsh/>`_

