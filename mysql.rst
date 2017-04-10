MySQL
=====

.. code-block:: bash

    $ sudo apt-get install mysql-server

.. code-block:: bash

    $ mysql -u user -p
    mysql> CREATE DATABASE databasename;
    mysql> SHOW DATABASES;
    mysql> \q
    $ mysql -u user -p databasename < dump_file.sql


.. code-block:: bash

    $ mysql -u user -p
    mysql> USE databasename;


You can see at any time which database is currently selected using

.. code-block:: bash

    mysql> SELECT DATABASE();


.. code-block:: bash

    mysql> SHOW TABLES;
    mysql> DESCRIBE table;
    mysql> SELECT * FROM table;
