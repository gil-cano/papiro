# Papiro

This repository is a work in progress

.. contents:: :local:

## Introduction

This package provides the source for documentation of some tools used for Plone development.


## Building The Documentation

# pyenv

```shell
git clone https://github.com/gil-cano/papiro.git
cd papiro
pyenv virtualenv 3.12.2 sphinx
pyenv local sphinx
```

# pipenv

.. code:: bash

    git clone https://github.com/gil-cano/papiro.git
    $ cd papiro
    $ pipenv install
    $ pipenv run make html

# pip and virtualenv

.. code:: bash

    $ git clone https://github.com/gil-cano/papiro.git
    $ cd papiro
    $ virtualenv-3.6 .
    $ source bin/activate
    (papiro)$ pip install -r requirements.txt
    (papiro)$ make html



At the end of a successful build, you will see the location of the
resulting HTML pages.


Link Testing
------------

.. code:: bash

    $ pipenv run make linkcheck


License
-------

Copyright © 2011-2018 Gildardo Bautista.
