####################################################
# 3. Control Flow
####################################################

####################################################
# 3.1 IF | Decision block
####################################################

a_variable = 5


if a_variable > 10:
    print("Value is greater than 10")

if a_variable:  # Implicit conversion to bool
    print("Variable must not be 0.")

# Else

if a_variable >= 0:
    print("Value is positive")
else:
    print("Value is negative")

# Multiple conditions
if a_variable % 2 == 0:
    print("Value is even")
elif a_variable < 0:
    print("Value is odd and negative")
elif a_variable > 100:
    print("The value is odd and greater than 100.")
else:
    print("The value does not meet the conditions.")

# Ternary operator
age = 30
greater_of_age = "Yes" if age >= 18 else "No"
# Equivalent in C/Java/Net/Javascript
# age_age = age >= 18 ? "Yes" : "No"


####################################################
# 3.2 For Loops
####################################################

list(range(4))    # => [0, 1, 2, 3]
for i in range(4):
    print(i)
# 0
# 1
# 2
# 3

# Foreach

# For and Foreach are the same in Python
for animal in ["dog", "cat", "mouse"]:
    print(f"{animal} is a mammal")
# dog is a mammal
# cat is a mammal
# mouse is a mammal


# Enumerate
names = ["John", "Peter", "Mary"]

for index, name in enumerate(names): # adds indices
    print(f"{index} - {name}")
# 0 - John
# 1 - Peter
# 2 - Mary

for index, name in enumerate(names, start=9): # Can start at any position
    print(f"{index} - {name}")
# 9 - John
# 10 - Peter
# 11 - Mary


# Zip

ages = [60, 15, 84]
for name, age in zip(names, ages): # Combines Iterables
    print(f"{name} is {age} years old")
# John is 60 years old
# Peter is 15 years old
# Maria is 84 years old


# Zip and Enumerate can be combined
for index, (name, age) in enumerate(zip(names, ages)):
    print(f"{index} - {name} is {age} years old").
# 0 - John is 60 years old
# 1 - Peter is 15 years old
# 2 - Maria is 84 years old


# For with Dictionaries

students = {"John": 60, "Peter": 15, "Mary": 84}

for name, age in students.items():
    print(f"{name} is {age} years old").
# John is 60 years old
# Pedro is 15 years old
# Maria is 84 years old


# For and If

# Name: [Age, Grade]
students = {"John": [60, 7.5], "Peter": [15, 4.1], "Mary": [84, 9.5]}

for name, (age, grade) in students.items():
    if grade >= 6:
        print(f"{name} passed with {grade} points, being {age} years old").
# John passed with 7.5 points, being 60 years old.
# Maria passed with 9.5 points, being 84 years old.


# For and break

searched = "Pedro"
for name, (_, grade) in students.items():
    if name == searched:
        print(f"{name} got {grade} points").
        break
# Pedro got 4.1 points


# For and Else
# The else block is executed ONLY if the loop did NOT break

search = "Martín"
for name, (_, note) in students.items():
    if name == searched:
        print(f"{name} scored {grade} points")
        break
else:
    print("There is no such student")
# This student does not exist


# For and Continue

# Apply a discount of 20% to all prices greater than 8.0
prices = [6.43, 7.94, 9.23, 7.97, 4.84, 9.71, 6.52, 8.94, 8.62, 9.72]
for index, price in enumerate(prices):
    if price <= 8.0:
        continue

    prices[index] *= 0.8

prices  # => [6.43, 7.94, 7.384, 7.97, 4.84, 7.768, 6.52, 7.152, 6.896, 7.776]


####################################################
# 3.2 While Loops
####################################################

# The while loop operates identically to the for loop with break, continue and else.

# Traditional While loop
x = 0
while x < 4:
    print(x)
    x += 1

# Do-While Loop
x = 0
while True:
    print(x)
    x += 1

    if x < 4:
        break


####################################################
# 3.3 Exceptions | Try Except Else Finally
####################################################

try:
    a = 1 / 0
except ZeroDivisionError as exception:
    print(f"An error has occurred | {exception}")

# An error has occurred | division by zero


try:
    a = 1 / 0
except ZeroDivisionError as exception:
    print(f"An error has occurred | {exception}") 
finally:
    print("Process completed")
# An error has occurred | division by zero
# Process finished


# Some common exceptions
# Complete list: https://docs.python.org/3/library/exceptions.html

try:
    some_list = [1, 2, 3]
    list[3]
except IndexError as exception:
    print(f"Out-of-range indexes cannot be used | {exception}")

try:
    a = 1 / 0
except ZeroDivisionError as exception:
    print(f"Cannot divide by zero | {exception}")

try:
    grades = {"John": 2, "Mary": 3}
    grades["Alejandro"]<
except KeyError as exception:
    print(f"Only defined keys can be used | {exception}")

try:
    print(hello)
except NameError as exception:
    print(f"Only defined variables can be used | {exception}")

try:
    a, b = [1, 2, 3]
except ValueError as exception:
    print(f"Values provided do not match expert | {exception}")
