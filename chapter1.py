####################################################
# 1. Tipos de datos primitivos y operadores.
####################################################

# Comentarios de una línea comienzan con una almohadilla (o numeral)

""" Strings multilinea pueden escribirse
    usando tres ", y comunmente son usados
    como comentarios.
"""


####################################################
# 1.1 Aritmética
####################################################


1 + 1       # => 2
8 - 1       # => 7
10 * 2      # => 20
5 ** 2      # => 25   Potencia
pow(5, 2)   # => 25   Potencia
25 ** 0.5   # => 5    Raiz con Potencia fraccionaria
35 / 5      # => 7.0  División (devuelve float)
35 / 0      # =>      Error
34 // 5     # => 6    División entera (trunca el cociente)
35 % 6      # => 5    Operador Módulo (resto)
3 * 2.0     # => 6.0  Si uno de los operandos es float, el resultado es float


####################################################
# 1.2 Lógica
####################################################

# Valores 'boolean' (booleanos) son primitivos
True
False

# Operadores booleanos nativos

# not
not True          # => False
not False         # => True

# and
True and True     # => True
True and False    # => False
False and True    # => False
False and False   # => False

# or
True or True      # => True
True or False     # => True
False or True     # => True
False or False    # => False

# Cortocircuito por defecto
True and False and 1 / 0   # => False
True and True and 1 / 0    # => Error
False or True or 1 / 0     # => True
False or False or 1 / 0    # => Error


####################################################
# 1.3 Operadores de Comparación
####################################################

# Operadores básicos
1 == 1     # => True
1 != 1     # => False
1 < 10     # => True
1 > 10     # => False
2 <= 2     # => True
2 >= 2     # => True

# Comparaciones Combinadas
1 < 2 < 3          # => True
1 < 3 < 2          # => False
1 < 0 < 1 / 0      # => False (cortocircuito)
1 <= 2 <= 4 <= 6   # => True (longitud Indefinida)
1 != 2 <= 4 != 6   # => True (combinada)


####################################################
# 1.4 Cadena de caracteres (Strings)
####################################################

# Strings se crean con ", ' o """"
"Esto es un string."
'Esto también es un string.'

"""Las strings con triple 
comillas pueden ser multilinea"""  # Se inserta un \n al final de la línea

"Hola " + "mundo!"       # => "Hola mundo!" Concatenación
"Hola " "mundo!"         # => "Hola mundo!" Concatenación Automática
"Esto es un string"[0]   # => 'E' String como Lista

# Formateo de Strings con format
nombre = "Ezequiel"
precio = 12.50
descuento = 0.8
comida = "lasaña"
"{} debe pagar {}$".format(nombre, precio)  # => "Ezequiel debe pagar 12.50$"
"{0} no vino, {0} se fue, {0} debe aún {1}$".format(nombre, precio * descuento) # => "Ezequiel no vino, Ezequiel se fue, Ezequiel debe aún 10$"
"{nombre} quiere comer {comida}".format(comida=comida, nombre="Bob")  # => "Bob quiere comer lasaña"

# Formateo de Strings con f-Strings
f'{nombre} quiere comer {comida}'  # => "Ezequiel quiere comer lasaña"


####################################################
# 1.5 Objeto None
####################################################

True is None    # => False
False is None   # => False
None is None    # => True


####################################################
# 1.6 Valores interpretados como booleanos
####################################################

bool(0)     # => False
bool(1)     # => True

bool("")    # => False
bool("a")   # => True

bool([])    # => False
bool([3])   # => True

# Los valores anteriores pueden usarse como booleanos

not "1"     # => False
not []      # => True

# and
1 and [3]   # => [3] True and True
[3] and 1   # => 1   True and True
[3] and 0   # => 0   True and False
0 and [3]   # => 0   False and True
0 and ""    # => 0   False and False
"" and 0    # => ""  False and False

# or
1 or [3]    # => 1   True or True
[3] or 1    # => [3] True or True
1 or []     # => 1   True or False
[] or 1     # => 1   False or True
0 or []     # => []  False or False
[] or 0     # => 0   False or False


####################################################
# 1.7 Conversiones númericas de base
####################################################

# Decimal
str(10)           # => 10
int("10")         # => 10

# Binario
bin(10)           # => '0b1010'
int("0b1010", 2)  # => 10
int("1010", 2)    # => 10

# Octal
oct(10)           # => '0o12'
int("0o12", 8)    # => 10
int("12", 8)      # => 10

# Hexadecimal
hex(10)           # => '0xa'
int("0xa", 16)    # => 10
int("0xA", 16)    # => 10
int("a", 16)      # => 10
int("A", 16)      # => 10


####################################################
# 1.7 Conversiones de string
####################################################

chr(65)    # => "A"
chr(191)   # => "¿"
chr(8364)  # => "€"

ord("A")   # => 65
ord("¿")   # => 191
ord("€")   # => 8364

####################################################
# 2 Commit Bruno
####################################################
chr(65)    # => "A"
chr(191)   # => "¿"
chr(8364)  # => "€"

ord("A")   # => 65
ord("¿")   # => 191
ord("€")   # => 8364
#agrego cambios a committiar