# How to execute the file (while standing inside the chapter6 folder):
# $PATH$/chapter6> python -m source.chapter6_2

# => This message will be executed before the imports of this module. 

####################################################
## 6.4 Importing from a parent from a child directory
####################################################

import main
# => I was invoked directly or indirectly
# => I was invoked indirectly (via an import)
# => You successfully imported main.py

####################################################
## 6.5 Import from a parent's neighbor
####################################################

import config.test_config as test_config
# => You successfully imported test_config.py


####################################################
## 6.5 Import from a parent's neighbor child
####################################################

import config.db_config.migrations as migrations
# => Successfully imported migrations.py


# Imports from the same directory and neighbors work the same as in chapter6_1
# Prints omitted
import source.util as util
import source.controller.controller as controller

# Continue reading in chapter6/source/controller/chapter6_3.py
