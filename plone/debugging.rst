Debugging Zope
--------------

 Para poder usar el debugger de Zope es necesario que antes de compilar python instales ``gdbm`` (ver :doc:`../brew`)

.. code-block:: shell

   $ brew install gdbm

El debugger se encunetra en ``Control_Panel/DebugInfo``.

Para abilitar el tab profiler debemos agregar en el buildout

.. code-block:: shell

    [instance]
    environment-vars =
        PROFILE_PUBLISHER 1

    zope-conf-additional =
        publisher-profile-file ${buildout:directory}/var/profile.dat

Bibliografía
------------

* `Profiling Plone 4 <https://lionfacelemonface.wordpress.com/2011/02/08/profiling-plone-4-well-profiling-zope-while-running-plone-4/>`_

* `Zope Developers Guide >> Testing and Debugging <https://zope.readthedocs.io/en/latest/zdgbook/TestingAndDebugging.html>`_
