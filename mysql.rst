MySQL
=====

.. code-block:: bash

    $ sudo apt-get install mysql-server

.. code-block:: bash

    $ mysql -u user -p
    mysql> CREATE DATABASE databasename;
    mysql> SHOW DATABASES;
    mysql> CREATE USER 'user'@'localhost' IDENTIFIED BY 'some_password';
    mysql> GRANT SELECT,INSERT,UPDATE,DELETE,CREATE,DROP
        -> ON cons_cmo.*
        -> TO 'user'@'localhost';
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


Python
------

.. code-block:: bash

    (venv)$ pip install mysql-connector==2.1.4


Referencias
-----------

`MySQL Connector/Python Developer Guide <https://dev.mysql.com/doc/connector-python/en/>`_

`mysql-connector <https://github.com/sanpingz/mysql-connector>`_
