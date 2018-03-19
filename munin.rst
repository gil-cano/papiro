Munin (Debian squeeze)
======================

Add backports to your sources.list
----------------------------------

* Add this line to your sources.list (or add a new file to /etc/apt/sources.list.d/) ::

    deb http://backports.debian.org/debian-backports squeeze-backports main

* Run ::

    $ apt-get update

Install a package from backports
--------------------------------

.. sourcecode:: shell

    $ aptitude -t squeeze-backports show munin-node
    Package: munin-node
    State: not installed
    Version: 2.0.6-1~bpo60+1
    Priority: optional
    Section: net
    Maintainer: Munin Debian Maintainers <packaging@munin-monitoring.org>
    Uncompressed Size: 430 k
    Depends: perl, libnet-server-perl, procps, adduser, lsb-base (>= 3.2-4), gawk, munin-common (>= 2.0.6-1~bpo60+1), munin-plugins-core
    Recommends: libnet-snmp-perl, munin-plugins-extra


.. sourcecode:: shell

    $ aptitude -t squeeze-backports install munin-node
    The following NEW packages will be installed:
    Do you want to continue? [Y/n/?] y
    Adding system user `munin' (UID 110) ...
    Adding new group `munin' (GID 117) ...
    Adding new user `munin' (UID 110) with group `munin' ...
    Not creating home directory `/var/lib/munin'.
    Setting up munin-doc (2.0.6-1~bpo60+1) ...
    Setting up munin-plugins-core (2.0.6-1~bpo60+1) ...
    Setting up munin-node (2.0.6-1~bpo60+1) ...
    Initializing plugins..done.
    Restarting munin-node..Stopping Munin-Node: stopped beforehand.
    Starting Munin-Node: done.
    Starting Munin-Node: started beforehand.
    Setting up munin-plugins-extra (2.0.6-1~bpo60+1) ...


/etc/munin/munin-node.conf

.. sourcecode:: shell

    cidr_allow 132.248.17.41/32


/etc/munin/munin.conf

.. sourcecode:: shell

    # a simple host tree
    [localhost.localdomain]
        address 127.0.0.1
        use_node_name yes

    [caoba.matem.unam.mx]
        address 127.0.0.1
        use_node_name yes

    [jacaranda.matem.unam.mx]
        address 132.248.17.205
        use_node_name yes


`squeeze-backports <http://packages.debian.org/squeeze-backports/munin>`_

`backports <http://backports-master.debian.org/Instructions/>`_

http://munin-monitoring.org/wiki/Documentation

http://beeznest.wordpress.com/2012/06/25/munin-2-0-on-debian-2/

http://munin-monitoring.org/wiki/CgiHowto2


