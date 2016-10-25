iTerm2
======

Cuando iniciamos una instancia de Plone marca el error

.. code-block:: bash

    unknown locale: UTF-8

para solucionar eso hay que agregar al .bash_profile

.. code-block:: bash

    # iTerm2 fix
    export LC_ALL=en_US.UTF-8
    export LANG=en_US.UTF-8
