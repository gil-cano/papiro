Postfix
-------

.. code-block:: bash

    $ sudo apt-get install mailutils
    $ sudo apt-get install postfix


El archivo de configuracion es::

    $ sudo nano /etc/postfix/main.cf

Cambiamos el valor de la variable `inet_interfaces`

.. code-block:: bash

    mailbox_size_limit = 0
    recipient_delimiter = +
    inet_interfaces = loopback-only

Another directive you'll need to modify is mydestination, which is used to specify the list of domains that are delivered via the local_transport mail delivery transport.

.. code-block:: bash

    mydestination = $myhostname, localhost.$mydomain, localhost
    mydestination = ceiba.matem.unam.mx, localhost.matem.unam.mx, , localhost

Reiniciamos el servicio.

.. code-block:: bash

    $ sudo service postfix restart

Para enviar un correo de prueba:

.. code-block:: bash

    $ echo "This is the body of the email" | mail -s "This is the subject line" your@email.address


para revisar la cola de corre:

.. code-block:: bash

    $ mailq


para eliminar todo el correo de la cola:

.. code-block:: bash

    $ sudo postsuper -d ALL

References
----------
`How to Install and Configure Postfix as a Send-Only SMTP Server on Ubuntu 16.04 <https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-postfix-as-a-send-only-smtp-server-on-ubuntu-16-04>`_
