####################################################
## 6. Módulos
####################################################

import math                    # Importar todo el módulo con nombre
math.sqrt(16)                  # => 4.0


from math import ceil, floor   # Importar sólo partes específicas
ceil(3.7)                      # => 4.0
floor(3.7)                     # => 3.0


from math import *   # Importar todas las partes de un módulo | NO RECOMENDABLE


import math as m     # Es posible utilizar alias para los módulos
math.sqrt(16) == m.sqrt(16)  # => True

math.__doc__ # => This module provides access to the mathematical functions 
             #    defined by the C standard.