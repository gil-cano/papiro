.. code-block:: shell

    $ kitty list-fonts 
    $ brew tap homebrew/cask-fonts
    $ brew search nerd-font
    $ brew install font-fira-code  
    $ brew install font-jetbrains-mono
    $ brew install font-monoid-nerd-font
    $ brew install font-sauce-code-pro-nerd-font
    $ brew uninstall --casks font-dejavu-sans-mono-nerd-font
    $ brew list --casks


.. code-block:: shell

    .config/kitty/kitty.conf
    
    font_family        JetBrains Mono
    font_size 14.0


.. code-block:: shell

    kitty +kitten icat hellow.gif
    kitty +kitten diff correos202112.csv correos202203.csv
    

https://ohmyposh.dev

.. code-block:: shell

    brew tap jandedobbeleer/oh-my-posh
    brew install oh-my-posh


Add the following to ~/.zshrc:

.. code-block:: shell

    eval "$(oh-my-posh prompt init zsh)"


.. code-block:: shell

    source ~/.zshrc

