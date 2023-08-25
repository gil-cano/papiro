# Actrualizar Python (despues de actualizar a Ventura)

Verificamos que paquetes de brew hayq ue actualizar

```shell
brew outdated
```

actualizamos todos
```shell
brew upgrade
```

listamos las versiones e instancias virtuales que tenemos

```shell
pyenv versions
```

guardamos el resultado

```shell
  2.7.18
  2.7.18/envs/info
  2.7.18/envs/migration2.7
  2.7.18/envs/nudos
  2.7.18/envs/plone4
  3.7.16
  3.7.16/envs/escuelas
  3.7.16/envs/inventariodp
  3.11.4
  3.11.4/envs/kardex
  3.11.4/envs/plone6.0.4
  3.11.4/envs/plone6.import
```

desintalamos todos los ambientes virtuales

```shell
pyenv virtualenv-delete info
```

desinstalamos las versiones de python

```shell
pyenv uninstall 2.7.18
```

para ver que versiones podemos instalar

```shell
pyenv install --list
```

volvemos a instalar las versiones de python que teniamos (de preferencia las más actuales).

```shell
pyenv install 2.7.18
```

creamos las instancias virtaules que teniamos

```shell
pyenv virtualenv 2.7.18 info
```

Asignamos una version default

```shell
pyenv global 3.11.4 2.7.18
```


# buildout

Volvemos a correr el buildout en cada instancia

```shell
cd matem-4.3.3
# esto solo es necesario si no esta activado el ambiente virtual
pyenv local info
# instalamos zc.buildout y setuptools
pip install -r requirements.txt
# ejecutamos el buildout
buildout
# iniciamos la instancia
bin/instance fg
```
