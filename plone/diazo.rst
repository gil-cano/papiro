Diazo
=====

Hacemos una copia del "Barceloneta Theme" en Site Setup - Theming.

Creamos un archivo `styles.less`

.. code-block:: console

    /* Import Barceloneta styles */
    @import "++theme++barceloneta/less/barceloneta.plone.less";

    /* Customize whatever you want */

En el archivo `manifest.cfg` hacemos referencia a este nuevo archivo:

.. code-block:: console

    [theme]
    title = CMO
    description =
    preview = preview.png
    rules = /++theme++cmo/rules.xml
    prefix = /++theme++cmo
    doctype = <!DOCTYPE html>
    enabled-bundles =
    disabled-bundles =
    development-css = /++theme++cmo/styles.less
    production-css = /++theme++cmo/styles.css
    tinymce-content-css = /++theme++cmo/less/barceloneta-compiled.css
    development-js =
    production-js =

seleccionamos el archivo `styles.less` y lo compilamos con el botón `Build CSS`

Podemos cambiar el fondo de la barra de navegación::

    @plone-sitenav-bg: rgb(193,39,45);


El archivo `rules.xml` es el puente entre el contenido del sistema y el tema.

Podemos agregar cosas como:

.. code-block:: console


    <drop css:content="#portal-breadcrumbs" />


Referencias
-----------


`Diazo Theming Guidelines <https://plone-theming-with-diazo.readthedocs.org/en/latest/index.html>`_

`Some xslt hints <https://www.nathanvangheem.com/news/new-diazo-theme-and-some-xslt-hints>`_

`Theming Plone <http://docs.plone.org/adapt-and-extend/theming/index.html>`_

`Learning the Web <https://developer.mozilla.org/en-US/Learn/Getting_started_with_the_web>`_

