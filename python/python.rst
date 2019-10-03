Python
======


Decoradores
-----------


Interfaces
----------


Adaptadores
-----------



Diccionarios
------------

Para clasificar por tipo una lista de objetos, gurdamos como llave el tipo y como valor la lista de objetos de ese tipo.

.. code-block:: python

    by_state = {}
    for brain in brains:
        by_state.setdefault(brain.review_state, []).append(brain)


Para iterar sobre la información de un diccionario

.. code-block:: python

    for k, v in by_state.items():
        print('{0}: {1}'.format(k, len(v)))
