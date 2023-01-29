####################################################
# 2. Variables and Collections
####################################################

# Python has a function to print
print("I'm Python. Nice to meet you.")

# There is no need to declare variables before assigning them.
a_variable = 5           # The convention is to use lowercase underscores (snake_case).
one_variable: float = 5  # Optional type-hints | RECOMMENDED
one_variable             # => 5
# other_variable         # Error unassigned variable

# Operators with re-assignment
one_variable += 2        # one_variable == 7
one_variable -= 1        # one_variable == 6
one_variable *= 5        # one_variable == 30
one_variable /= 5        # one_variable == 3.0
one_variable **= 3       # one_variable == 27.0
one_variable %= 10       # one_variable == 7.0
one_variable //= 5       # one_variable == 1.0

# Multiple assignment
a = b = 3  # a = 3 and b = 3


####################################################
# 2.1 Lists
####################################################

# Lists stores sequences
some_list = []                    # Empty
other = [4, 5, 6]                 # With initial values
multiple = [2, "John", [2]]       # Values of different type (heterogeneous)

# List methods
some_list.append(1)               # Add an element at the end
some_list.extend([2, 4, 3])       # Add multiple elements
some_list.pop()                   # => 3 and list=[1, 2, 4])
some_list.insert(3, 3)            # Add an element at the given position
len(some_list)                    # 4

# Simple indexing
some_list[0]       # => 1 First element
some_list[-1]      # => 4 Last element
# some_list[4]     # Error - Out of bounds

# Slicing list[start:end:step]
some_list[1:3]     # => [2, 4]
some_list[2:]      # => [4, 3]
some_list[:3]      # => [1, 2, 4]
some_list[::2]     # => [1, 4]
some_list[::-1]    # => [3, 4, 2, 1]
some_list[:]       # => Creates an identical copy of list


# Operations with Lists
some_list + other  # => [1, 2, 4, 3, 4, 5, 6] 
some_list * 2      # => [1, 2, 4, 3, 1, 2, 4, 3]

# Operator in
1 in some_list              # => True

# The not operator can be used before or after
not 5 in some_list          # => True
5 not in some_list          # => True

# Operator ==
some_list == [1, 2, 4, 3]   # => True
some_list == some_list[:]   # => True
some_list == some_list      # => True

# Operator is
some_list is [1, 2, 4, 3] # => False
some_list is some_list[:] # => False
some_list is some_list # => True


# Special operations for Boolean lists
any(some_list)  # => True | Returns True if at least one of the elements is True
all(some_list)  # => True | Returns True if all the elements are True


####################################################
# 2.2 Tuples, immutable collections
####################################################

some_tuple = (1, 2, 3)  # They are defined with (,) instead of []
some_tuple = 1, 2, 3    # Parentheses are optional
some_tuple[0]           # => 1
# some_tuple[0] = 3     # TypeError

# Methods identical to lists but without assignment
len(some_tuple)         # => 3
some_tuple + (4, 5, 6)  # => (1, 2, 3, 4, 5, 6)
some_tuple[:2]          # => (1, 2)
2 in some_tuple         # => True


####################################################
# 2.3 Unpacking
####################################################

# Simple unpacking
a, b, c = (1, 2, 3)         # a == 1, b == 2, c == 3
a, b, c = [1, 2, 3]         # a == 1, b == 2, c == 3
# a, b = [1, 2, 3]          # Error | Number of elements must be identical
a, b = b, a                 # Exchange a == 2, b == 1

# Unpacking With wildcards
a, *rest = [1, 2, 3, 4]     # a == 1, rest == [2, 3, 4]
*rest, b = [1, 2, 3, 4]     # b == 4, rest == [2, 3, 4]
a, *rest, b = [1, 2, 3, 4]  # a == 1, b == 4, rest == [2, 3]

# Nested Unpacking
(a, b), c = [[1, 2], [3]]   # a == 1, b == 2, c == [3]


####################################################
# 2.4 Dictionaries - Key-Value Collections
####################################################

empty_dictionary = {}      # Empty
dictionary = {
    "one": 1,              # Multiline declaration           
    "two": 2,           
    "three": 3,            # Comma at the end valid
}
dictionary["one"]          # => 1 - Indexed with Keys
# dictionary["four"]       # Error

dictionary.get("one")      # => 1
dictionary.get("four")     # => None instead of Error
dictionary.get("one", 4)   # => 1
dictionary.get("four", 4)  # => Default value instead of None

# Methods
list(dictionary.keys())    # => ["three", "two", "one"]                        # => ["three", "two", "one"]
list(dictionary.values())  # => [3, 2, 1]                      # => ["three", "two", "one"]                    # => [3, 2, 1
list(dictionary.items())   # => [('one', 1), ('two', 2), ('three', 3)]

# Operators with Dictionaries | in verifies the keys.
"one" in dictionary        # => True
1 in dictionary            # => False

# Dictionary update
new_data = {"four": None, "five": 5}
dictionary.update(new_data)
dictionary                 # {'one': 1, 'two': 2, 'three': 3, 'four': None, 'five': 5}

# Keys and values could be Heterogeneous
multiple = {
    "one": 1,
    2: "two",
    (1, 3): [1, 5],
}

# Keys must be inmutable (hashable)
# invalid = {[1, 2]: "1"}    # Error


####################################################
# 2.4 Sets | Collections without duplicates
####################################################

empty_set = set()
some_set = {1, 2, 2, 2, 3, 4}  # => {1, 2, 3, 4}
some_set.add(5)                # => {1, 2, 3, 4, 5}
some_set.add(6)                # => {1, 2, 3, 4, 5, 6}
some_set.discard(7)            # => {1, 2, 3, 4, 5, 6}
# some_set.remove(7)           # => Error | Remove assumes element is in set
some_set.remove(6)             # => {1, 2, 3, 4, 5, 6}

# Set Operations
other_set = {3, 4, 5, 6}

# In Operator
2 in some_set                              # => True

# Intersection
some_set & other_set                       # => {3, 4, 5}
some_set.intersection(other_set)           # => {3, 4, 5}

# Union
some_set | other_set                       # => {1, 2, 3, 4, 5, 6}
some_set.union(other_set)                  # => {1, 2, 3, 4, 5, 6}

# Difference
some_set - other_set                       # => {1, 2}
some_set.difference(other_set)             # => {1, 2}

# Symmetric difference
some_set ^ other_set                       # => {1, 2, 5, 6}
some_set.symmetric_difference(other_set)   # => {1, 2, 5, 6}

# Subset
subset = {1, 2, 3, 4, 5}
subset <= some_set                         # => True
subset.issubset(some_set)                  # => True

# Proper Subset
proper_subset = {1, 2, 3}
subset < some_set                          # => False 
proper_subset < some_set                   # => True 

# Superset
superset = {1, 2, 3, 4, 5}
superset >= some_set                       # => True
superset.issuperset(some_set)              # => True

# Proper Superset
proper_superset = {1, 2, 3, 4, 5, 6}
superset > some_set                        # => False 
proper_superset > some_set                 # => True 

# Disjoint
extra_set = {9, 10, 11}
some_set.intersection(other_set) == set()  # => False
some_set.isdisjoint(other_set)             # => False

some_set.intersection(extra_set) == set() # => True
some_set.isdisjoint(extra_set)            # => True
