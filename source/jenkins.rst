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
