Cadenas
=======


Para dar formato a nombres con acentos

.. code-block:: python

    string.capwords(brain.Title)




URL's
=====

Pasar parametros en URLs

.. code-block:: python

    import urllib

    form_fields = {'key1': 'value1', 'key2': 'value2'}

    url = 'http://httpbin.org/get?' + urllib.urlencode(form_fields)


Requets
=======

Pasar parametros en URLs

.. code-block:: python

    import requests
    form_fields = {'key1': 'value1', 'key2': 'value2'}
    r = request.get('http://httpbin.org/get', params=form_fields)
