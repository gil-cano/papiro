PostgreSQL
==========

En MacOS instalamos Postgres.app

Para usar la linea de comandos, agregamos al path

.. code-block:: bash

    $ echo /Applications/Postgres.app/Contents/Versions/latest/bin | sudo tee /etc/paths.d/postgresapp


.. code-block:: bash

    $ psql -p5432
    user=# \q
    $ psql -p5432 -d postgres


Listar todas las bases de datos

.. code-block:: bash

    postgres=# \list

Listar todas las tablas en la base datos

.. code-block:: bash

    postgres=# \dt

Cambiar la base de datos

.. code-block:: bash

    postgres=# \connect otherdb

Listar todos los usuarios

.. code-block:: bash

    postgres=# \du

Crear un usuario similar a tu nombre de usuario.

.. code-block:: bash

    $ sudo su - postgres -c "createuser -s $USER"

Because the role login is the same as your unix login unix sockets can be use without a password.


You can see at any time which database is currently selected using

.. code-block:: bash

    mysql> SELECT DATABASE();
    mysql> CREATE DATABASE databasename;
    mysql> CREATE USER 'user'@'localhost' IDENTIFIED BY 'some_password';
    mysql> GRANT SELECT,INSERT,UPDATE,DELETE,CREATE,DROP
        -> ON cons_cmo.*
        -> TO 'user'@'localhost';
    mysql> DESCRIBE table;
    mysql> SELECT * FROM table;


Python
------

.. code-block:: bash



Referencias
-----------

`Postgres.app <http://postgresapp.com/documentation/cli-tools.html>`_

`PostgreSQL Documentation <https://www.postgresql.org/docs/current/static/index.html>`_

`Postgres Guide <http://postgresguide.com/>`_

`Mastering PostgreSQL in Application Development <https://masteringpostgresql.com/>`_
