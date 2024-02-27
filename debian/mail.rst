Mail
====

Postfix
-------

.. code-block:: shell

    $ sudo apt-get install mailutils
    $ sudo apt-get install postfix


El archivo de configuracion es::

    $ sudo nano /etc/postfix/main.cf

Cambiamos el valor de la variable `inet_interfaces`

.. code-block:: shell

    mailbox_size_limit = 0
    recipient_delimiter = +
    inet_interfaces = loopback-only

Another directive you'll need to modify is mydestination, which is used to specify the list of domains that are delivered via the local_transport mail delivery transport.

.. code-block:: shell

    mydestination = $myhostname, localhost.$mydomain, localhost
    mydestination = ceiba.matem.unam.mx, localhost.matem.unam.mx, , localhost

Reiniciamos el servicio.

.. code-block:: shell

    $ sudo service postfix restart

Para enviar un correo de prueba:

.. code-block:: shell

    $ echo "This is the body of the email" | mail -s "This is the subject line" your@email.address


para revisar la cola de corre:

.. code-block:: shell

    $ mailq


para eliminar todo el correo de la cola:

.. code-block:: shell

    $ sudo postsuper -d ALL


display the current mail queue status, including the number of messages 

.. code-block:: shell

    postqueue -p

This will display a list of queued messages along with their queue IDs, size, arrival time, sender, and recipient information.

.. code-block:: shell

-Queue ID- --Size-- ----Arrival Time---- -Sender/Recipient-------
BBFBE12345      1024 Mon, 01 Jan 2023 10:00:00 +0000 sender@example.com
                                         recipient1@example.com

CDEFG67890      2048 Tue, 02 Jan 2023 15:30:00 +0000 sender2@example.com
                                         recipient2@example.com

-Queue ID-  --Size-- ----Arrival Time---- -Sender/Recipient-------
6CC9497         878 Tue Feb 27 21:15:30  sender@example.com
(host ALT1.ASPMX.L.GOOGLE.COM[142.250.152.27] said: 421-4.7.26 This mail has been rate limited because it is unauthenticated. Gmail 421-4.7.26 requires all senders to authenticate with either SPF or DKIM. 421-4.7.26  421-4.7.26  Authentication results: 421-4.7.26  DKIM = did not pass 421-4.7.26  SPF [jacaranda.matem.unam.mx] with ip: [132.248.17.205] = did not 421-4.7.26 pass 421-4.7.26  421-4.7.26  For instructions on setting up authentication, go to 421 4.7.26  https://support.google.com/mail/answer/81126#authentication b7-20020a92db07000000b00365067c1dfesi2356002iln.115 - gsmtp (in reply to end of DATA command))
                                         recipient1@example.com

.. code-block:: shell

    cd /var/log/
    sudo tail -f mail.info



References
----------
`How to Install and Configure Postfix as a Send-Only SMTP Server on Ubuntu 16.04 <https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-postfix-as-a-send-only-smtp-server-on-ubuntu-16-04>`_
