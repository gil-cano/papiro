Network Speed
=============

Instalación de iper::

    apt-get install iperf

En el servidor que queremos probar::

    iperf -s

En el cliente::

    iperf -c 192.168.0.1


.. code-block:: bash

    vagrant$ iperf -c 192.168.0.1
    ------------------------------------------------------------
    Client connecting to 192.168.0.1, TCP port 5001
    TCP window size:  170 KByte (default)
    ------------------------------------------------------------
    [  3] local 10.0.2.15 port 51634 connected with 192.168.0.1 port 5001
    [ ID] Interval       Transfer     Bandwidth
    [  3]  0.0-10.6 sec  5.25 MBytes  4.17 Mbits/sec

    jacaranda$ iperf -s
    ------------------------------------------------------------
    Server listening on TCP port 5001
    TCP window size: 85.3 KByte (default)
    ------------------------------------------------------------
    [  4] local 192.168.0.1 port 5001 connected with 187.145.240.239 port 57694
    [ ID] Interval       Transfer     Bandwidth
    [  4]  0.0-11.6 sec  5.25 MBytes  3.80 Mbits/sec


.. code-block:: bash

    $ iperf -c 192.168.0.2
    ------------------------------------------------------------
    Client connecting to 192.168.0.2, TCP port 5001
    TCP window size: 85.0 KByte (default)
    ------------------------------------------------------------
    [  3] local 10.0.2.15 port 44893 connected with 192.168.0.2 port 5001
    [ ID] Interval       Transfer     Bandwidth
    [  3]  0.0-10.4 sec  4.88 MBytes  3.92 Mbits/sec

    ceiba$ iperf -s
    ------------------------------------------------------------
    Server listening on TCP port 5001
    TCP window size: 85.3 KByte (default)
    ------------------------------------------------------------
    [  4] local 192.168.0.2 port 5001 connected with 187.145.240.239 port 57668
    [ ID] Interval       Transfer     Bandwidth
    [  4]  0.0-12.8 sec  4.88 MBytes  3.19 Mbits/


.. code-block:: bash

    jacaranda$ iperf -c 192.168.0.3
    ------------------------------------------------------------
    Client connecting to 192.168.0.3, TCP port 5001
    TCP window size: 85.0 KByte (default)
    ------------------------------------------------------------
    [  3] local 192.168.0.2 port 39766 connected with 192.168.0.3 port 5001
    [ ID] Interval       Transfer     Bandwidth
    [  3]  0.0-10.1 sec   116 MBytes  96.2 Mbits/sec

    ceiba$ iperf -s
    ------------------------------------------------------------
    Server listening on TCP port 5001
    TCP window size: 85.3 KByte (default)
    ------------------------------------------------------------
    [  4] local 192.168.0.3 port 5001 connected with 192.168.0.2 port 39766
    [ ID] Interval       Transfer     Bandwidth
    [  4]  0.0-10.3 sec   116 MBytes  94.1 Mbits/sec



Referencias
-----------

`Diagnosing Network Speed with Iperf <https://www.linode.com/docs/networking/diagnostics/diagnosing-network-speed-with-iperf>`_