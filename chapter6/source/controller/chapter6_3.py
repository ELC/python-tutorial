# Forma de ejecutar el archivo (estando parados dentro de la carpeta chapter6):
# $PATH$/chapter6> python -m source.controller.chapter6_3

# => Este mensaje se ejecutará antes de los imports de este módulo

####################################################
## 6.5 Misma lógica para n niveles de profundidad
####################################################

# Prints omitidos
import main
import source.util as util
import source.controller.controller as controller
import config.test_config as test_config
import config.db_config.migrations as migrations


####################################################
## 6.6 Comportamiento singleton de los paquetes
####################################################

import source.controller.controller as controller # => Importaste con Éxito controller.py
print(controller.name) # => controller

import source.data.data as data # => Importaste con Éxito data.py
print(controller.name) # => Fui modificado en otro módulo


####################################################
## 6.7 Imports relativos (intra-paquete)
####################################################

from . import controller as controller  # => Importaste con Éxito controller.py
from .. import util as util             # => Importaste con Éxito util.py
from ..data import data as data         # => Importaste con Éxito data.py

# No se pueden importar módulos que estén en la raiz del arbol de directorios
from ... import main # => Error
from ...config import test_config as test_config # => Error
from ...config.db_config import migrations as migrations # => Error<
