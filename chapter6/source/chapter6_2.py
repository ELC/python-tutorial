# Forma de ejecutar el archivo (estando parados dentro de la carpeta chapter6):
# $PATH$/chapter6> python -m source.chapter6_2

# => Este mensaje se ejecutará antes de los imports de este módulo 

####################################################
## 6.4 Importar de un padre desde un directorio hijo
####################################################

import main
# => Me invocaron directa o indirectamente
# => Me invocaron indirectamente (mediante un import)
# => Importaste con Éxito main.py

####################################################
## 6.5 Importar del vecino de un padre
####################################################

import config.test_config as test_config
# => Importaste con Éxito test_config.py


####################################################
## 6.5 Importar del hijo del vecino de un padre
####################################################

import config.db_config.migrations as migrations
# => Importaste con Éxito migrations.py


# Los imports del mismo directorio y vecinos funcionan igual que en chapter6_1
# Prints omitidos
import source.util as util
import source.controller.controller as controller
