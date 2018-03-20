GnuPG
=====

.. code-block:: shell

    $ brew info --json gnupg
    gnupg: stable 1.4.20 (bottled)
    GNU Pretty Good Privacy (PGP) package

    $ brew install gnupg



http://www.integralist.co.uk/posts/security-basics.html
https://www.gnupg.org/gph/en/manual/x56.html


SSH
===

Llave publica::

     ~/.ssh/id_rsa.pub

Llave privada::

     ~/.ssh/id_rsa


Para obtener la huella digital (SSH RSA)

.. code-block:: shell

    $ ssh-keygen -lf ~/.ssh/id_rsa.pub

en las ultimas versiones de ssh-keygen

.. code-block:: shell

    $ ssh-keygen -E md5 -lf ~/.ssh/id_rsa.pub
