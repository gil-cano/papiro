Network
=======

.. code-block:: bash

    $ nmap 192.168.1.254

    Starting Nmap 6.47 ( http://nmap.org ) at 2016-08-19 00:21 EDT
    Nmap scan report for info.matem.unam.mx (192.168.1.254)
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

.. code-block:: bash

    $ nc -zv 127.0.0.1 111

.. code-block:: bash

    $ netstat -an | grep 111

.. code-block:: bash

    $ service rpcbind stop
    $ update-rc.d nfs-common disable
    $ update-rc.d rpcbind disable
    $ update-rc.d -f rpcbind remove
