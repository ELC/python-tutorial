####################################################
# 1. Primitive data types and operators.
####################################################

# One-line comments begin with a hash (or numeral).

""" Multi-line strings can be written
    using three ", and are commonly used as comments.
    as comments.
"""


####################################################
# 1.1 Arithmetic Operations
####################################################


1 + 1       # => 2
8 - 1       # => 7
10 * 2      # => 20
5 ** 2      # => 25   Power
pow(5, 2)   # => 25   Power
25 ** 0.5   # => 5    Root with Fractional Power
35 / 5      # => 7.0  Division (returns float)
35 / 0      # =>      Error
34 // 5     # => 6    Integer division (truncates the quotient)
35 % 6      # => 5    Modulo operator (remainder)
3 * 2.0     # => 6.0  If one of the operands is float, result is float


####################################################
# 1.2 Logic
####################################################

# boolean values are primitive
True
False

# Native boolean operators

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

# Default Short Circuit
True and False and 1 / 0   # => False
True and True and 1 / 0    # => Error
False or True or 1 / 0     # => True
False or False or 1 / 0    # => Error


####################################################
# 1.3 Comparison Operators
####################################################

# Basic operators
1 == 1     # => True
1 != 1     # => False
1 < 10     # => True
1 > 10     # => False
2 <= 2     # => True
2 >= 2     # => True

# Combined Comparisons
1 < 2 < 3          # => True
1 < 3 < 2          # => False
1 < 0 < 1 / 0      # => False (cortocircuito)
1 <= 2 <= 4 <= 6   # => True (longitud Indefinida)
1 != 2 <= 4 != 6   # => True (combinada)


####################################################
# 1.4 Character string (Strings)
####################################################

# Strings are created with ", ', """" or '''
'This is a string."
'This is also a string.'

"""Strings with triple 
quotes can be multi-line""" # A \n is inserted at the end of each line.

"Hello " + "world!"       # => "Hello world!" Concatenation
"Hello " "world!"         # => "Hello world!" Automatic Concatenation
"This is a string"[0]     # => 'E' String as List

# Formatting Strings with format
name = "Ezekiel"
price = 12.50
discount = 0.8
food = "lasagna"
"{} must pay {}$".format(name, price)  # => "Ezequiel must pay $12.50"
"{0} didn't come, {0} left, {0} still owes {1}$".format(name, price * discount) # => "Ezekiel didn't come, Ezekiel left, Ezekiel still owes $10."
"{name} wants to eat {food}".format(food=food, name="Bob") # => "Bob wants to eat lasagna."

# Formatting Strings with f-Strings.
f'{name} wants to eat {food}'  # => "Ezekiel wants to eat lasagna"


####################################################
# 1.5 Object None
####################################################

True is None    # => False
False is None   # => False
None is None    # => True


####################################################
# 1.6 Values interpreted as Booleans
####################################################

bool(0)     # => False
bool(1)     # => True

bool("")    # => False
bool("a")   # => True

bool([])    # => False
bool([3])   # => True

# The above values can be used as booleans

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
# 1.7 Numeric base conversions
####################################################

# Decimal
str(10)           # => 10
int("10")         # => 10

# Binary
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
# 1.7 String conversions
####################################################

chr(65)    # => "A"
chr(191)   # => "¿"
chr(8364)  # => "€"

ord("A")   # => 65
ord("¿")   # => 191
ord("€")   # => 8364
