=======
Jenkins
=======

Jenkins Installation
====================

To use the Debian package repository of Jenkins to automate installation and 
upgrade, first add the key to your system:

.. code-block:: sh

   wget -q -O - http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | sudo apt-key add -

Then add the following entry in your `/etc/apt/sources.list`:

.. code-block:: sh

   deb http://pkg.jenkins-ci.org/debian binary/

Update your local package index, then finally install Jenkins:

.. code-block:: sh

   sudo apt-get update
   sudo apt-get install jenkins


Para asegurar el sistema continuamos con:

.. code-block:: sh

    https://wiki.jenkins-ci.org/display/JENKINS/Standard+Security+Setup


Configurar git plugin
=====================

Para asegurar el sistema continuamos con:

.. code-block:: sh

    $ sudo su - -s /bin/bash jenkins
    $ cd /var/lib/jenkins/jobs/UNAM.imateCVct Plone 4.3/workspace
    $ git config user.email "some@email.com"
    $ git config user.name "jenkins"
