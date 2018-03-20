======
Squid3
======

.. code-block:: shell

   /etc/squid3/squid.conf


.. code-block:: squid

   # chacmool: added this from debianHELP.org; reference at http://www.debianhelp.org/node/1713
   auth_param basic realm Private port. Please go away and have a nice day.
   auth_param basic program /usr/lib/squid3/basic_ncsa_auth /etc/squid3/squid_passwords
   auth_param basic credentialsttl 4 hours
   auth_param basic children 5

   acl SSL_ports port 443
   acl Safe_ports port 80          # http
   acl Safe_ports port 21          # ftp
   acl Safe_ports port 443         # https
   acl Safe_ports port 70          # gopher
   acl Safe_ports port 210         # wais
   acl Safe_ports port 1025-65535  # unregistered ports
   acl Safe_ports port 280         # http-mgmt
   acl Safe_ports port 488         # gss-http
   acl Safe_ports port 591         # filemaker
   acl Safe_ports port 777         # multiling http
   acl CONNECT method CONNECT

   #
   # Recommended minimum Access Permission configuration:
   #
   # Deny requests to certain unsafe ports
   http_access deny !Safe_ports

   # Deny CONNECT to other than secure SSL ports
   http_access deny CONNECT !SSL_ports

   # Only allow cachemgr access from localhost
   http_access allow localhost manager
   http_access deny manager