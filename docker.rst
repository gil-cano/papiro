Docker
======

.. code-block:: bash

    $ docker ps
    $ docker images

Dockerfile::

    FROM docker/whalesay:latest
    RUN apt-get -y update && apt-get install -y fortunes
    CMD /usr/games/fortune -a | cowsay

Hacer una imagen apartir del Dockerfile

.. code-block:: bash

    $ docker build -t docker-whale .