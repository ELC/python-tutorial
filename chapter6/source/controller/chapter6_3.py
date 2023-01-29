# How to execute the file (while standing inside the chapter6 folder):
# $PATH$/chapter6> python -m source.controller.chapter6_3

# => This message will be executed before the imports of this module

####################################################
## 6.5 Same logic for n depth levels
####################################################

## Prints omitted
import main
import source.util as util
import source.controller.controller as controller
import config.test_config as test_config
import config.db_config.migrations as migrations


####################################################
## 6.6 Singleton behavior of packages
####################################################

import source.controller.controller as controller

# => You successfully imported controller.py
print(controller.name)  # => controller

import source.data.data as data

# => Successfully imported data.py
print(controller.name)  # => I was modified in another module


# Re-importing with the import keyword will NOT reset the value
import source.controller.controller as controller

print(controller.name)  # => I was modified in another module


# Re-importing using imporlib.reload will reset the value
import importlib

importlib.reload(controller)
print(controller.name)  # => controller


####################################################
## 6.7 Relative (intra-package) Imports
####################################################

from . import controller as controller  # => You imported with Success controller.py
from .. import util as util  # => Successfully imported util.py
from ..data import data as data  # => You imported with Success data.py

# You cannot import modules that are in the root of the directory tree.
from ... import main  # => Error
from ...config import test_config as test_config  # => Error
from ...config.db_config import migrations as migrations  # => Error<
