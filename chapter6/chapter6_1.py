# Ways to run the file (while standing inside the chapter6 folder):
# $PATH$/chapter6> python chaper6_1.py
# $PATH$/chapter6> python -m chapter6_1

# Reference: https://docs.python.org/3/reference/import.html#the-import-system
# https://docs.python.org/3/tutorial/modules.html

####################################################
## 6.1 Import into the same directory
####################################################


import main
# => I was invoked directly or indirectly.
# => I was invoked indirectly (via an import)
# => You successfully imported main.py

print(f'The value of {main.name=}') # => The value of main.name='main'
main.__doc__ # => This is the main module of the application (Docstring)


####################################################
## 6.2 Import from a neighboring directory
####################################################

from source import items
# => This message will be executed before the imports of this module

items  # => {'sheet': 10.25, 'speaker': 5.258, 'computer': 350.159, 
       # 'cup': 25.99, 'bottle': 18.759, 'cellular': 215.231}


import source.util as util
# => Successfully imported util.py

print(f'The value of {util.name=}') # => The value of util.name='util'.


####################################################
## 6.3 Import from a child of a neighboring directory
####################################################


import source.controller.controller as controller
# => You successfully imported controller.py

print(f'The value of {controller.name=}') # => The value of controller.name='controller'
