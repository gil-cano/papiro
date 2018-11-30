Network
=======

Mostrar que IP estas usando

.. code-block:: shell

    $ ip a

    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
        inet 127.0.0.1/8 scope host lo
           valid_lft forever preferred_lft forever
        inet6 ::1/128 scope host
           valid_lft forever preferred_lft forever
    2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
        inet 192.168.10.82/24 brd 192.168.10.255 scope global eth0

Mostrar el nombre

.. code-block:: shell

    $ hostname
    $ hostname -f


Escanear los puestos
--------------------

Para escanear los puestos en un servidor podemos usar nmap:

.. code-block:: shell

    $ nmap 192.168.1.254

    Starting Nmap 6.47 ( http://nmap.org ) at 2016-08-19 00:21 EDT
    Nmap scan report for myhost.my.domain (192.168.1.254)
    Host is up (0.00052s latency).
    Not shown: 994 closed ports
    PORT     STATE SERVICE
    22/tcp   open  ssh
    80/tcp   open  http
    111/tcp  open  rpcbind
    3128/tcp open  squid-http
    8080/tcp open  http-proxy
    8083/tcp open  us-srv

    Nmap done: 1 IP address (1 host up) scanned in 0.16 seconds

o netcat [nc]:

.. code-block:: shell

    $ nc -zv 127.0.0.1 111
    localhost [127.0.0.1] 111 (sunrpc) : Connection refused

    $ nc -zv 127.0.0.1 22
    localhost [127.0.0.1] 22 (ssh) open


.. code-block:: shell

    $ netstat -an | grep 111
    unix  3      [ ]         STREAM     CONNECTED     11143

    $ netstat -an | grep 22
    tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN
    tcp        0      0 192.168.1.254:22        192.168.1.41:62844     ESTABLISHED
    tcp6       0      0 :::22                   :::*                    LISTEN
    unix  2      [ ]         DGRAM                    13195    /run/user/122/systemd/notify
    unix  2      [ ACC ]     STREAM     LISTENING     13197    /run/user/122/systemd/private
    unix  2      [ ]         DGRAM                    22748
    unix  3      [ ]         STREAM     CONNECTED     14224
    unix  2      [ ]         STREAM     CONNECTED     15223
    unix  3      [ ]         STREAM     CONNECTED     22757    /var/run/dbus/system_bus_socket
    unix  3      [ ]         STREAM     CONNECTED     22746
    unix  3      [ ]         STREAM     CONNECTED     14225    /var/run/dbus/system_bus_socket
    unix  3      [ ]         STREAM     CONNECTED     22747    /run/systemd/journal/stdout
    unix  3      [ ]         STREAM     CONNECTED     22756
    unix  2      [ ]         DGRAM                    22311

Verificar si el puerto esta en uso

.. code-block:: shell

    $ lsof -i
    ...
    Dropbox   20723  username   62u  IPv4 0xb0d9e70c6df58efd      0t0  TCP mi.site.com:53242->162.125.34.129:https (ESTABLISHED)

rpcbind
-------
.. code-block:: shell

    $ sudo service rpcbind stop
    $ sudo systemctl disable rpcbind.service

Uninstall rpcbind
~~~~~~~~~~~~~~~~~

To remove just rpcbind package itself from Debian 8 (Jessie) execute on terminal:

.. code-block:: shell

    $ apt-get -s remove rpcbind
    $ sudo apt-get remove rpcbind

Uninstall rpcbind and it's dependent packages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To remove the rpcbind package and any other dependant package which are no longer needed from Debian Jessie.


.. code-block:: shell

    $ sudo apt-get remove --auto-remove rpcbind

Purging rpcbind
~~~~~~~~~~~~~~~

If you also want to delete configuration and/or data files of rpcbind from Debian Jessie then this will work:

.. code-block:: shell

    $ sudo apt-get purge rpcbind

To delete configuration and/or data files of rpcbind and it's dependencies from Debian Jessie then execute:

.. code-block:: shell

    $ apt-get -s purge --auto-remove rpcbind
    $ sudo apt-get purge --auto-remove rpcbind


Find hostname from an IP Address
--------------------------------

.. code-block:: shell

    $ nslookup ip


The basic network reconfiguration
---------------------------------

When you try to reconfigure the interface, e.g. eth0, you must disable it first with the "sudo ifdown eth0" command. This removes the entry of eth0 from the "/etc/network/run/ifstate" file. (This may result in some error message if eth0 is not active or it is configured improperly previously. So far, it seems to be safe to do this for the simple single user work station at any time.)

You are now free to rewrite the "/etc/network/interfaces" contents as needed to reconfigure the network interface, eth0.

Then, you can reactivate eth0 with the "sudo ifup eth0" command.

Para agregar una direccion ip al server

.. code-block:: shell

    $ nano -w /etc/network/interfaces

.. code-block:: shell

    auto eth0:0
    allow-hotplug eth0:0
    iface eth0:0 inet static
        address 192.168.1.23
        netmask 255.255.255.0

.. code-block:: shell

    $ sudo ifup eth0:0

De manera alternativa

.. code-block:: shell

    $ sudo service networking restart

DNS se define en:

.. code-block:: shell

    $ nano -w /etc/resolv.conf

Nombre en:

.. code-block:: shell

    $ nano -w /etc/hostname

Network adapter
---------------

Linux

.. code-block:: shell

    $ sudo ethtool eth0

Mac

.. code-block:: shell

    $ ifconfig en0 


