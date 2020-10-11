# Formas de ejecutar el archivo (estando parados dentro de la carpeta chapter6):
# $PATH$/chapter6> python chaper6_1.py
# $PATH$/chapter6> python -m chapter6_1

# Referencia: https://docs.python.org/3/reference/import.html#the-import-system
#             https://docs.python.org/3/tutorial/modules.html

####################################################
## 6.1 Importar dentro del mismo directorio
####################################################


import main
# => Me invocaron directa o indirectamente
# => Me invocaron indirectamente (mediante un import)
# => Importaste con Éxito main.py

print(f'El valor de {main.name=}') # => El valor de main.name='main'
main.__doc__  # => Este es el módulo principal de la aplicación (Docstring)


####################################################
## 6.2 Importar de un directorio vecino
####################################################

from source import articulos
# => Este mensaje se ejecutará antes de los imports de este módulo

articulos # => {'sábana': 10.25, 'parlante': 5.258, 'computadora': 350.159, 
          #     'tasa': 25.99, 'botella': 18.759, 'celular': 215.231}


import source.util as util
# => Importaste con Éxito util.py

print(f'El valor de {util.name=}') # => El valor de util.name='util'


####################################################
## 6.3 Importar de un hijo de un directorio vecino
####################################################


import source.controller.controller as controller
# => Importaste con Éxito controller.py

print(f'El valor de {controller.name=}') # => El valor de controller.name='controller'
