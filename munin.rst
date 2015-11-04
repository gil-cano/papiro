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

.. sourcecode:: sh

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

.. sourcecode:: sh

    $ aptitude -t squeeze-backports install munin-node
    The following NEW packages will be installed:
      gawk{a} libcgi-fast-perl{a} libdate-manip-perl{a} libdbi0{a} libfcgi-perl{a} libhtml-template-perl{a} libio-multiplex-perl{a}
      libio-socket-inet6-perl{a} libipc-shareable-perl{a} liblist-moreutils-perl{a} liblog-dispatch-perl{a} liblog-log4perl-perl{a}
      libnet-cidr-perl{a} libnet-server-perl{a} libnet-snmp-perl{a} libparams-validate-perl{a} librrd4{a} librrds-perl{a} libsigsegv0{a}
      libsocket6-perl{a} libyaml-syck-perl{a} munin munin-common{a} munin-doc{a} munin-node{a} munin-plugins-core{a} munin-plugins-extra{a}
      rrdtool{a}
    0 packages upgraded, 28 newly installed, 0 to remove and 107 not upgraded.
    Need to get 6,615 kB of archives. After unpacking 27.9 MB will be used.
    Do you want to continue? [Y/n/?] y
    ...
    Setting up munin (2.0.6-1~bpo60+1) ...
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

.. sourcecode:: sh

    cidr_allow 132.248.17.41/32


/etc/munin/munin.conf

.. sourcecode:: sh

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


