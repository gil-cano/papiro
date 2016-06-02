Vagrant
=======

This is a kit for setting up a development enviroment for `Django <https://www.djangoproject.com/>`_ in a hosted virtual machine.

To develop with Django, you need Python (an interpreter for the Python programming language) plus eggs (software libraries) containing the Django web application development framework.

We need an easy way to switch between Python versions. We use pip to manage Django versions and eggs because it is popular, well-supported, and full-featured


Installation
------------

1. Install `VirtualBox <https://www.virtualbox.org>`_

2. Install `Vagrant <http://www.vagrantup.com>`_

3. Clone the repository::

    $ git clone  https://github.com/gil-cano/djangodev.vagrant.git

4. Change directory into the djangodev.vagrant directory. Run "vagrant up"::

    $ cd djangodev.vagrant
    $ vagrant up

This is going to download a virtual box kit, download and install `Virtualenv <https://pypi.python.org/pypi/virtualenv/>`_, `python <https://www.python.org/>`_ 3.4.3, `Django <https://www.djangoproject.com/>`_ 1.8.4, and set up some convenience scripts.

Using the Vagrant-installed VirtualBox
--------------------------------------

You may now start and stop the virtual machine by issuing command in the same directory::

    $ vagrant suspend

stops the virtual machine, saving an image of its state so that you may later restart with::

    $ vagrant resume

Finally, you may remove the VirtualBox (deleting its image) with the command::

    $ vagrant destroy

How you get a command prompt on your "guest" machine will depend on your host operating system. On Unix workalikes, use the command::


    $ vagrant ssh


References
----------

