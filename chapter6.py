####################################################
## 6. Modules
####################################################

# Import the whole module with name
import math

math.sqrt(16)  # => 4.0


# Import specific members (submodules, variables, functions) only
from math import ceil, floor

ceil(3.7)      # => 4.0
floor(3.7)     # => 3.0


# Import all members of a module into the global namespace | NOT RECOMMENDED
from math import *             


# Alias for modules
import math as m               

# Modules as objects

# Modules are objects and can be compared with each other
math == m      # => True

# There is a single instance of a module in memory
math is m      # => True

math.__doc__   # => This module provides access to the mathematical functions 
               # defined by the C standard.

# Programmatic Import (Advanced)

# It is possible to programmatically import a module
import importlib

math_programmatically = importlib.import_module("math")

assert math_programmatically is m

floor_programmatically = getattr(math_programmatically, "floor")

assert floor_programmatically is floor

# If the module changes at execution time it can be reloaded
# The import/from..import syntax does NOT reload modules
importlib.reload(math)
importlib.reload(math_programmatically)

# Continue reading in chapter6/chapter6_1.py
