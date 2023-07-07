# Python For Programmers

This is a "tutorial" in a cheatsheet style for programmers who want to learn
Python. Programming basics such as data types, control flow, object-oriented
programming are assumed.

## Why?

In recent years there has been a trend to incorporate different programming
languages to solve different problems, this practice was usually referred to as
[Polyglot
Programming](https://www.thoughtworks.com/radar/techniques/polyglot-programming).
Python in particular has been the de facto language for Artificial Intelligence
Applications (AI/ML/DP) for several years, with presence in other fields like QA
automation, Back-End Web Development, Robotic Process Automation, Command Line
Interface development and Infrastructure. Therefore, many programmers coming
from different backgrounds are and will be learning Python.

However, Python has some distinct aspects that set it apart from most languages,
most notably it is indentation-based and it is interpreted. Not only that but it
also encourages a way to structure the code that differs substantially from
traditional .Net or Java styles.

This tutorial aims to show what idiomatic Python looks like, the syntax
can be learned fairly quickly, but Programming Python "á la Java/.Net/Javascript"
should be avoided.

Some examples:
- Java and C# use classes explicitly and extensively, but in Python, many things
  are built so that the consumer of the code may not know that it is using
  custom classes. Iterators, Context Managers, and Decorators are examples of
  these patterns.
- Many design patterns are way simpler in Python due to the feature that it has,
  such as first-class functions and first-class Types. No need to have many
  classes with a single method if you can pass a user-defined function as a
  parameter (Strategy Pattern).
- Python has no private/internal members for classes, and most members can be
  treated as C# Properties, so getters and setters are rarely used.
- Python natively incorporates elements from functional programming without
  going to Javascript extremes ([callback
  hell](https://en.wiktionary.org/wiki/callback_hell)). Mixing it with Object
  Oriented Patterns.
- Python types are not enforced but only used by the IDE as suggestions to throw
  warnings.
- Many more, but you can notice them by reading the different chapters.

## Chapters

This tutorial is divided into chapters, each chapter consists of a file
detailing syntax and examples as well as how the outputs should look like.

All the chapters are runnable Python files when code that would throws errors
appears, it is always commented out.

The chapters can be read as a cookbook as there are no cross-references but the
more complex topics assume previous chapter content was understood.

The following is a summary of each chapter.

### 0. Introduction - Environment and Tips

This optional chapter shows IDE configuration, themes, fonts, and extensions
useful for Python developers.

### 1. Primitive data types and operators.

Topics covered:

- Arithmetic
- Logic
- Comparison Operators
- Strings
- Object None
- Non-boolean Values interpreted as Booleans
- Numeric base conversions
- String conversions to Unicode
- Bitwise Operations

Topics to add:
- [Complex numeric type](https://docs.python.org/3/library/functions.html#complex)
- [Bytes and Bytesarray](https://docs.python.org/3/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview)


### 2. Variables and Collections

Topics covered:

- Lists
- Tuples, immutable collections
- Unpacking
- Dictionaries - Key-Value Collections
- Sets | Collections without duplicates
- Frozensets | Sets but immutable
- Recursive Collections


### 3. Control Flow

Topics covered:

- IF | Decision block
- For Loops
- While Loops
- Exceptions | Try Except Else Finally

### 4. Functions

Topics covered:

- Basic Function Definitions
- Arbitrary parameters
- Higher-order functions
- Closures
- Partial Evaluation
- Common higher-order functions (map, filter reduce)
- Comprehensions

Topics to add:
- [Ellipsis Object](https://docs.python.org/3/library/constants.html#Ellipsis)
- Dictionary and Set Comprehensions
- [Functools](https://docs.python.org/3/library/functools.html)

### 5. Classes

Topics covered:

- Classes
- Initializer and Instance Methods
- Class Variables and Methods
- Static methods
- Dataclasses
- Operator Overloading
- Instances as Functions (`__call__`)
- Properties and Deep Copy
- Inheritance
- Constructor (`__new__`)
- Abstract Classes and Methods
- Interfaces (Protocols)
- Method Overloading
- Mixins (Multiple Inheritance)
- Descriptors

Topics to add:
- [Generics](https://docs.python.org/3/library/stdtypes.html#generic-alias-type)

### 6. Modules and Imports Structure

Topics covered:

- Import Structure
- Relative Imports
- Programmatic Imports
- Import Reloading

### 7. Advanced Language Features

Topics covered:

- Additional Types
    - NamedTuple and namedtuple
    - Counter
    - Defaultdict
    - Enum
    - SimpleNameSpace
- Generators
- Iterators
- Semi-coroutines (Generators with send)
- Corrutinas (AsyncIO)
- Decorators
    - Stateless decorators
    - Stateful Decorators
- Context Managers
- Standard Library Pearls - Pathlib
- Standard Library Pearls - Itertools
- Standard Library Pearls - OS
- Standard Library Pearls - Serialization
- Standard Library Pearls - Emails

Topics to add:
- [TypedDict](https://docs.python.org/3/library/typing.html#typing.TypedDict)
- [Secrets module](https://docs.python.org/3/library/secrets.html)


### 8. Python Ecosystem

This is a special no-code chapter that consists of an infography showing which
are the most popular libraries depending on the field. Raging from Web
Development to Data Science and QA Automation. 

The image is high resolution to comfortably zooming in.

### 9. Appendices

Topics to add:

- Caveats of dealing with floats (WIP)
- Type Theory (Bounds, Covariant, Contravariant, Unions)
- Metaprogramming and self-modifying code
- MultiParadigm Programming


## Feedback and Contact

Contact and feedback are much appreciated, please feel free to reach out through
[LinkedIn](https://www.linkedin.com/in/ezequielcastano/) or by submitting a
GitHub issue.

## Inspiration

This Tutorial style was inspired by https://learnxinyminutes.com/docs/python/
