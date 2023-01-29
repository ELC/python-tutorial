####################################################
## 7. Advanced language Features
####################################################

from __future__ import annotations

####################################################
## Index
####################################################

# 7.1 Additional types
# 7.2 Generators
# 7.3 Iterators
# 7.4 Semi-corroutines (Advanced Generators)
# 7.5 Corrutines (AsyncIO)
# 7.6 Decorators
# 7.7 Context Manager
# 7.8 Pearls of the Standard Library - Pathlib
# 7.9 Pearls of the Standard Library - Itertools
# 7.10 Pearls of the Standard Library - OS
# 7.11 Pearls of the Standard Library - Serialization
# 7.12 Pearls of the Standard Library - Emails


####################################################
## 7.1 Additional Types
####################################################


####################################################
## 7.1.1 NamedTuple and namedtuple
####################################################

## Reference: https://docs.python.org/3/library/collections.html#collections.namedtuple

from dataclasses import dataclass, astuple
from collections import namedtuple


@dataclass
class Vector:
    x: float
    y: float

    def modulo(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5


origin = Vector(0, 0)
origin.x                # => 0
origin.y                # => 0
print(origin)           # => Vector(x=0, y=0)
# x, y = origin         # => Error
x, y = astuple(origin)  # => No Error
# origin[0]             # => Error Cannot use indexes in classes
origin.x = 3            # => Default mutable attributes
origin.y = 4            # => Default mutable attributes
print(origin)           # => Vector(x=3, y=4)

assert origin.modulo() == 5


# Using frozen=True


@dataclass(frozen=True)
class VectorImmutable:
    x: float
    y: float

    def modulo(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5


origin = VectorImmutable(0, 0)
origin.x                # => 0
origin.y                # => 0
print(origin)           # => Vector(x=0, y=0)
# x, y = origin         # => Error
x, y = astuple(origin)  # => No Error
# origin[0]             # => Error Cannot use indexes in classes
# origin.x = 3          # => Error attributes are immutable
# origin.y = 4          # => Error attributes are immutable

assert origin.modulo() == 0


# Using collections.namedtuple


VectorAlternate = namedtuple("VectorAlternate", ["x", "y"])


def modulo_without_types(vector: VectorAlternateVector) -> float:
    return (vector.x**2 + vector.y**2) ** 0.5  # Warning for not knowing types.


point = VectorAlternate(3, 4)
point.x                 # => 3 with Warning: No type specified
point.y                 # => 4 with Warning: No type specified
print(point)            # => VectorAlternate(x=3, y=4)
x, y = point            # => x=3, y=4 with Warning: No type specified
# point.x = 1           # => Error

assert point[0] == 3
assert point[1] == 4
assert modulo_without_types(point) == 5


# Using NamedTuple as superclass


from typing import NamedTuple


class VectorAlternativeTyped(NamedTuple):
    x: float
    y: float

    def modulo(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5


def typed_modulo_1(vector: VectorAlternativeTyped) -> float:
    return (vector.x**2 + vector.y**2) ** 0.5


typed_point_1_str = VectorAlternativeTyped("1", "1")  # Warning String != Float

typed_point_1 = VectorAlternativeTyped(3, 4)
typed_point_1.x                  # => 3
typed_point_1.y                  # => 4
print(typed_point_1)             # => VectorAlternativeTyped(x=3, y=4)
x, y = typed_point_1             # => x=3, y=4
# typed_point_1.x = 1    # => Error

assert typed_point_1[0] == 3
assert typed_point_1[1] == 4
assert typed_modulo_1(typed_point_1) == 5


# Using NamedTuple as a function

VectorAlternativeTyped_2 = NamedTuple(
    "VectorAlternativeTyped_2", [("x", float), ("y", float)]
)


def typed_modulo_2(vector: VectorAlternativeTyped_2) -> float:
    return (vector.x**2 + vector.y**2) ** 0.5


typed_point_2 = VectorAlternativeTyped_2(3, 4)
typed_point_2.x                  # => 1
typed_point_2.x                  # => 1
print(typed_point_2)             # => VectorAlternate(x=1, y=1)
x, y = typed_point_2             # => x=1, y=1
# typed_point_2.x = 1            # => Error

assert typed_point_2[0] == 3
assert typed_point_2[1] == 4
assert typed_modulo_2(typed_point_2) == 5

####################################################
## 7.1.2 Counter
####################################################


# Reference: https://docs.python.org/3/library/collections.html#collections.Counter

from collections import Counter

# Excerpt from Moby-Dick by Herman Melville
# Source: https://www.gutenberg.org/files/2701/2701-h/2701-h.htm#link2HCH0001
text = """
Call me Ishmael. Some years ago—never mind how long precisely—having little or
no money in my purse, and nothing particular to interest me on shore, I thought
I would sail about a little and see the watery part of the world. It is a way I
have of driving off the spleen and regulating the circulation. Whenever I find
myself growing grim about the mouth; whenever it is a damp, drizzly November in
my soul; whenever I find myself involuntarily pausing before coffin warehouses,
and bringing up the rear of every funeral I meet; and especially whenever my
hypos get such an upper hand of me, that it requires a strong moral principle to
prevent me from deliberately stepping into the street, and methodically knocking
people’s hats off—then, I account it high time to get to sea as soon as I can.
This is my substitute for pistol and ball. With a philosophical flourish Cato
throws himself upon his sword; I quietly take to the ship. There is nothing
surprising in this. If they but knew it, almost all men in their degree, some
time or other, cherish very nearly the same feelings towards the ocean with me.
""" 

letter_counter = Counter(text)
letter_counter.most_common(4)  # => [(' ', 184), ('e', 107), ('t', 74), ('i', 68)]

word_counter = Counter(text.split())
word_counter.most_common(4)  # => [('the', 10), ('I', 9), ('and', 7), ('to', 5)]


####################################################
## 7.1.3 Defaultdict
####################################################


# Reference: https://docs.python.org/3/library/collections.html#collections.defaultdict

from collections import defaultdict

student_grade: defaultdict[str, List[int]] = defaultdict(list)

student_grade["Peter"].append(8)  # Does not throw KeyError 
student_grade["Mary"].append(9)
student_grade["Peter"].append(3)
student_grade["Mary"].append(8)
student_grade["Peter"].append(7)

assert student_grade == {"Peter": [8, 3, 7], "Mary": [9, 8]}


####################################################
## 7.1.4 Enum
####################################################


# Reference: https://docs.python.org/3/library/enum.html

from enum import Enum, auto


class Permissions(Enum):
    ADMIN = auto()
    USER = auto()
    EDITOR = auto()

    @staticmethod
    def has_access_control_panel_1(permission: Permissions) -> bool:
        return permission is Permissions.ADMIN or permission is Permissions.EDITOR


Permissions.ADMIN # => Permissions.ADMIN
Permissions.ADMIN.value # => 1
Permissions['ADMIN'] # => Permissions.ADMIN
Permissions['ADMIN'].value # => 1

print(Permissions.__members__.keys())    # => ['ADMIN', 'USER', 'EDITOR']
print(Permissions.__members__.values())  # => [<Permissions.ADMIN: 1>, <Permissions.USER: 2>, <Permissions.EDITOR: 3>]

Permissions.has_access_control_panel_1("REDACTOR")  # No Error - Warning Incompatible Type.

assert Permissions.has_access_control_panel_1(Permissions.ADMIN)


# Alternative using typing.Literal

from typing import Literal

PermissionsA = Literal["ADMIN", "EDITOR", "USER"]


class PermissionsAlternative:
    @staticmethod
    def has_access_control_panel_2(permission: PermissionsA) -> bool:
        return permission in ["ADMIN", "EDITOR"]


PermissionsAlternative.has_access_control_panel_2("EDITOR") # No Error - Warning Type Incompatible

assert PermissionsAlternative.has_access_control_panel_2("ADMIN")

####################################################
## 7.1.4 SimpleNameSpace
####################################################


from dataclasses import dataclass


@dataclass
class Person:
    name: str


employee_1 = Person("John")
employee_1.name           # => John
# employee_1["name"]      # => Error - Cannot use keys with dataclasses
employee_1.age = 24       # => No Error - Monkey Patching - NOT RECOMMENDED 


# Using Dictionaries

employee_2 = {}
employee_2["name"] = "John"
employee_2["name"]        # => John
# employee_2.name         # => Error - Cannot access values using .


# Using SimpleNameSpace

# Reference: https://docs.python.org/3/library/types.html#types.SimpleNamespace

from types import SimpleNamespace

employee_3 = SimpleNamespace()
employee_3.name = "John"  # => No Error - Not Mokey Patching - Correct Usage
# employee_3["name"]      # => Error - Cannot use keys with SimpleNamespace


# Custom SimpleNamespace

from dataclasses import field

from typing import Any


class Employee(SimpleNamespace):
    def __setitem__(self, key: str, value: Any) -> None:
        setattr(self, key, value)
    
    def __getitem__(self, key: str) -> Any:
        return getattr(self, key)


employee_4 = Employee()
employee_4["name"] = "John"   # => No Error - Not Mokey Patching - Correct Usage
employee_4.age = 24           # => No Error - Not Mokey Patching - Correct Usage

assert employee_4.name == "John"
assert employee_4["name"] == "John"
assert employee_4.age == 24
assert employee_4["age"] == 24


####################################################
## 7.2 Generators
####################################################

# Reference: https://docs.python.org/3/tutorial/classes.html#generators

from typing import Generator, Iterator, List


def fibonacci_generator() -> Generator[int, None, None]:
    last: int = 1
    current: int = 1
    yield last
    yield current

    while True:
        current, last = last + current, current
        yield current


generator = fibonacci_generator()
fibonacci_10_first: List[int] = []

for _ in range(10):
    next_fibonacci = next(generator)
    fibonacci_10_first.append(next_fibonacci)

assert fibonacci_10_first == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


# Can take parameters like any function
def primes_smaller_than(number: int) -> Generator[int, None, None]: 
    visited: List[int] = []
    for number in range(2, number):
        not_prime = any(number % possible_divisor == 0 for possible_divisor in visited)
        
        if not_prime:
            continue

        visited.append(number)
        yield number
        

# With traditional loop

generator = primes_smaller_than(25)
primes_smaller_than_25: List[int] = []
for prime in generator:
    primes_smaller_than_25.append(prime)

assert primes_smaller_than_25 == [2, 3, 5, 7, 11, 13, 17, 19, 23]


# With comprehension

generator = primes_smaller_than(25)
primes_smaller_than_25 = [prime for prime in generator]
assert primes_smaller_than_25 == [2, 3, 5, 7, 11, 13, 17, 19, 23]


# With list

generator = primes_smaller_than(25)
primes_smaller_than_25 = list(generator)
assert primes_smaller_than_25 == [2, 3, 5, 7, 11, 13, 17, 19, 23]


####################################################
## 7.3 Iterators
####################################################

# Reference: https://docs.python.org/3/library/stdtypes.html#iterator-types

from dataclasses import dataclass, field
from typing import List


@dataclass
class PrimesSmallerThan:
    number: int
    current_number: int = 1
    visited: List[int] = field(default_factory=list)

    def __iter__(self):  # Required for use in For
        return self

    def __next__(self):  # Necessary for function next
        while True:
            self.current_number += 1
            no_is_prime = any(
                self.current_number % possible_divisor == 0
                for possible_divisor in self.visited
            )
            
            if self.current_number >= self.number:
                raise StopIteration()

            if not no_is_prime or len(self.visited) == 0:
                break

        self.visited.append(self.current_number)
        return self.current_number


# With traditional loop

class_generator: Iterator[int] = PrimesSmallerThan(25)
primes_less_than_25: List[int] = []
for prime in class_generator:
    primes_less_than_25.append(prime)

assert primes_less_than_25 == [2, 3, 5, 7, 11, 13, 17, 19, 23]

# With comprehension

class_generator: Iterator[int] = PrimesSmallerThan(25)
primes_smaller_than_25 = [prime for prime in class_generator]
assert primes_smaller_than_25 == [2, 3, 5, 7, 11, 13, 17, 19, 23]

# With list

class_generator: Iterator[int] = PrimesSmallerThan(25)
primes_smaller_than_25 = list(class_generator)
assert primes_smaller_than_25 == [2, 3, 5, 7, 11, 13, 17, 19, 23]

####################################################
## 7.4 Semi-coroutines (Generators with send)
####################################################

from typing import Generator, Any


def accumulate() -> Generator[float, float, None]:
    accumulator = 0
    while True:
        following = yield accumulator
        accumulator += following


semicoroutine: Generator[float, float, None] = accumulate()
next(semicoroutine)  # Initialize

semicoroutine.send(10)
semicoroutine.send(-1)

accumulator_result: float = semicoroutine.send(20)  # Finish
assert accumulator_result == 29


## Use Case


def processing_deferred() -> Generator[Any, Any, Any]:
    data = yield
    print(f"Processing data... - {data}")  # Replace with complex process
    processed_data = str(data)
    new_data = yield processed_data
    print(f"Processing data... - {new_data}")  # Replace with complex process
    yield "Done"


semicoroutine_deferred: Generator[Any, Any, Any] = processing_deferred()
next(semicoroutine_deferred)  # Initialize

deferred_result: float = semicoroutine_deferred.send(123) # => Processing data... - 123

# Deferred processing
deferred_result = semicoroutine_deferred.send(654) # => Processing data... - 654

assert deferred_result == "Done"

####################################################
## 7.5 Corrutinas (AsyncIO)
####################################################


# Reference: https://docs.python.org/3/library/asyncio-task.html

import asyncio
import time
from typing import Tuple

# Defining corrutines


async def processing_db() -> int:   # Async modifier
    print("DB: Sending database query")
    await asyncio.sleep(1)          # Similar behavior to yield 
    print("DB: Processing query 1")
    await asyncio.sleep(3)
    print("DB: Saving Results")
    return 0


async def responding_api() -> int:
    print("API: Requesting data from user")
    await asyncio.sleep(1) 
    print("API: Building Response")
    await asyncio.sleep(1)
    print("API: Writing Logs")
    await asyncio.sleep(1)
    print("API: Sending Response")
    await asyncio.sleep(1)
    print("API: Receiving confirmation")
    return 1


# Serial Execution of Corrutines


async def main_serial() -> Tuple[int, int]:
    result_db = await processing_db()
    result_api = await responding_api()
    return (result_db, result_api)


async def main_serial_inverted() -> Tuple[int, int]:
    result_api = await responding_api()
    result_db = await processing_db()
    return (result_api, result_db)


print(f"Started: {time.strftime('%X')}") 
results: Tuple[int, int] = asyncio.run(main_serial())
print(f"Completed: {time.strftime('%X')}")
assert results == (0, 1)

# Started: 23:22:24
# DB: Sending database query
# DB: Processing query 1
# DB: Saving Results
# API: Requesting data from user
# API: Building Response
# API: Writing Logs
# API: Sending Response
# API: Receiving confirmation
# Completed: 23:22:32

print(f"Started: {time.strftime('%X')}") 
results: Tuple[int, int] = asyncio.run(main_serial_inverted())
print(f"Completed: {time.strftime('%X')}")
assert results == (1, 0)

# Started: 23:23:06
# API: Requesting data from user
# API: Building Response
# API: Writing Logs
# API: Sending Response
# API: Receiving confirmation
# DB: Sending database query
# DB: Processing query 1
# DB: Saving Results
# Completed: 23:23:14

# Concurrent execution of Tasks (Tasks)


async def main_task() -> Tuple[int, int]:
    db_task = asyncio.create_task(processing_db())
    api_task = asyncio.create_task(responding_api())
    return (await db_task, await api_task)


async def main_task_inverted() -> Tuple[int, int]:
    api_task = asyncio.create_task(responding_api())
    db_task = asyncio.create_task(processing_db())
    return (await api_task, await db_task)


print(f"Started: {time.strftime('%X')}") 
results = asyncio.run(main_task())
print(f"Completed: {time.strftime('%X')}")
assert results == (0, 1)

# Started: 23:23:55
# DB: Sending database query
# API: Requesting data from user
# DB: Processing query 1
# API: Building Response
# API: Writing Logs
# API: Sending Response
# DB: Saving Results
# API: Receiving confirmation
# Completed: 23:23:59

print(f"Started: {time.strftime('%X')}") 
results = asyncio.run(main_task_inverted())
print(f"Completed: {time.strftime('%X')}")
assert results == (1, 0)

# Started: 23:24:30
# API: Requesting data from user
# DB: Sending database query
# API: Building Response
# DB: Processing query 1
# API: Writing Logs
# API: Sending Response
# DB: Saving Results
# API: Receiving confirmation
# Completed: 23:24:34


# Concurrent Execution of Corrutines (Gather)


async def main_gather() -> Tuple[int, int]:
    return await asyncio.gather(processing_db(), responding_api())


async def main_gather_inverted() -> Tuple[int, int]:
    return await asyncio.gather(responding_api(), processing_db())


print(f"Started: {time.strftime('%X')}") 
results = asyncio.run(main_gather())
print(f"Completed: {time.strftime('%X')}")
assert results == [0, 1]

# Started: 23:27:10
# DB: Sending database query
# API: Requesting data from user
# DB: Processing query 1
# API: Building Response
# API: Writing Logs
# API: Sending Response
# DB: Saving Results
# API: Receiving confirmation
# Completed: 23:27:14

print(f"Started: {time.strftime('%X')}") 
results = asyncio.run(main_gather_inverted())
print(f"Completed: {time.strftime('%X')}")
assert results == [1, 0]

# Started: 23:27:51
# API: Requesting data from user
# DB: Sending database query
# API: Building Response
# DB: Processing query 1
# API: Writing Logs
# API: Sending Response
# DB: Saving Results
# API: Receiving confirmation
# Completed: 23:27:55


# Executing asynchronously synchronous code


# Asynchronously executing synchronous code

import time
import asyncio
from typing import List


def wait() -> None:
    time.sleep(1)


def main_blocking() -> List[None]:
    return [wait() for _ in range(10)]


async def main_blocking_async():
    loop = asyncio.get_running_loop()
    futures = [loop.run_in_executor(None, wait) for _ in range(10)]
    return await asyncio.gather(*futures)


print(f"Started: {time.strftime('%X')}") 
results_blocking: List[None] = main_blocking()
print(f"Completed: {time.strftime('%X')}")
assert results_blocking == [None] * 10

# Started: 23:30:18
# Completed: 23:30:28


print(f"Started: {time.strftime('%X')}") 
results_blocking_async: Tuple[None] = asyncio.run(main_blocking_async())
print(f"Completed: {time.strftime('%X')}")
assert results_blocking_async == [None] * 10

# Started: 23:30:59
# Completed: 23:31:00

####################################################
## 7.6 Decorators
####################################################


####################################################
## 7.6.1 Stateless decorators
####################################################


import time
from typing import Tuple, Any


def measure_time(function: Callable[..., Any]) -> Callable[..., Tuple[Any, float]]:
    def helper(*args: Any, **kargs: Any) -> Tuple[Any, float]:
        """Helper function"""
        start: float = time.perf_counter()
        
        result = function(*args, **kargs)
        
        end: float = time.perf_counter()
        
        elapsed: float = end - start 

        return result, elapsed

    return helper


def slow_function() -> str:
    """Original function"""
    time.sleep(2)
    return "Hello world"


# Normal invocation
response: str = slow_function()
assert response == "Hello world"

import math

# Invocation with wrapper without decorator
slow_function_with_time = measure_time(slow_function)
result, run_time = slow_function_with_time()

assert result == "Hello world"
assert math.isclose(run_time, 2, abs_tol=0.1)

assert slow_function.__name__ == "slow_function"
assert slow_function_with_time.__name__ == "helper"  # Undesirable
assert slow_function_with_time.__doc__ == "Helper function"  # Not Desired


# Using wraps to "inherit" name and docstring

from functools import wraps


def measure_time_alternative(
    function: Callable[..., Any]
) -> Callable[..., Tuple[Any, float]]:
    @wraps(function)
    def helper(*args: Any, **kargs: Any) -> Tuple[Any, float]:
        start: float = time.perf_counter()
        
        result = function(*args, **kargs)
        
        end: float = time.perf_counter()
        
        elapsed: float = end - start 

        return result, elapsed

    return helper


slow_function_with_time = measure_time_alternative(slow_function)
result, execution_time = slow_function_with_time()

assert result == "Hello world"
assert math.isclose(execution_time, 2, abs_tol=0.1)

assert slow_function.__name__ == "slow_function"
assert slow_function_with_time.__name__ == "slow_function"  # Desirable
assert slow_function_with_time.__doc__ == "Original function"  # Desirable


# Invocation with decorator


@measure_time_alternative
def function_slow_measure():
    time.sleep(2)
    return "Hello world"


result, execution_time = function_slow_measure()

assert result == "Hello world"
assert math.isclose(execution_time, 2, abs_tol=0.1)


# Stateful decorator


def count_runs(function: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(function)
    def helper(*args: Any, **kwargs: Any):
        helper.runs += 1
        return function(*args, **kwargs)
    
    helper.runs = 0  # Warning - Monkey Patching - NOT RECOMMENDED

    return helper


@count_runs
def function_count() -> str:
    return "Hello world"


for _ in range(10):
    function_count()

assert function_count.runs == 10  # Warning Unknown attribute


####################################################
## 7.6.2 Stateful Decorators
####################################################


from dataclasses import dataclass
from typing import Callable


@dataclass
class Counter:
    func: Callable[..., Any]
    runs: int = 0

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        self.runs += 1
        return self.func(*args, **kwargs)


@Counter
def function_counted_class():
    return "Hello world"


for _ in range(10):
    function_counted_class()

assert function_counted_class.runs == 10  # No Warning


# Use cases - Cache and Memoization Manual


@Counter
def fibonacci(number: int) -> int:
    if number < 2:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


result = fibonacci(20)
assert result == 6765
assert fibonacci.runs == 21_891


from typing import Dict


def memoization(function: Callable[..., Any]) -> Callable[..., Any]:
    cache: Dict[str, Any] = {}

    def helper(*args: Any, **kwargs: Any) -> Any:
        nonlocal cache
        key = str(tuple(sorted(args)) + tuple(sorted(kwargs.items())))
        if key not in cache:
            cache[key] = function(*args, **kwargs)
        return cache[key]
    
    return helper


@Counter
@memoization
def fibonacci_memo(number: int) -> int:
    if number < 2:
        return number
    return fibonacci_memo(number - 1) + fibonacci_memo(number - 2)


result = fibonacci_memo(20)
assert result == 6765
assert fibonacci_memo.runs == 39  # 500 times fewer runs


# Use cases - Cache and Memoization LRU

from functools import lru_cache

# Reference: https://docs.python.org/3/library/functools.html#functools.lru_cache


@Counter
@lru_cache(maxsize=None)  # Equivalent to @cache in Python 3.9+
def fibonacci_lru(number: int) -> int:
    if number < 2:
        return number
    return fibonacci_lru(number - 1) + fibonacci_lru(number - 2)


result = fibonacci_lru(20)
assert result == 6765
assert fibonacci_memo.runs == 39  # 500 times fewer runs


####################################################
## 7.7 Context Manager
####################################################

# Reference: https://docs.python.org/3/library/stdtypes.html#context-manager-types


####################################################
## 7.7.1 Context Manager with Classes
####################################################


from dataclasses import dataclass
from typing import IO, Optional, Any
import time


@dataclass
class Timer:
    start: float = 0
    end: Optional[float] = None
    elapsed: float = -1
    exception: bool = False

    def __enter__(self) -> Timer:
        self.start = time.perf_counter()
        return self

    def __exit__(self, exception_type: Optional[Any], _: Any, __: Any) -> bool:
        self.exception = exception_type is not None
        self.end = time.perf_counter()
        self.elapsed = round(self.end - self.start, 3)
        return True


with Timer() as tempo:
    time.sleep(5)
    raise ValueError

print(tempo)  # => Timer(start=0.1141484, end=5.1158644, elapsed=5.002, exception=True)

assert math.isclose(tempo.elapsed, 5, abs_tol=0.1)
assert tempo.exception == True


####################################################
## 7.7.2 Context Manager with Generators and Contextlib
####################################################

## Reference: https://docs.python.org/3/library/contextlib.html

from contextlib import contextmanager
import time


@contextmanager
def timer():
    internal_data = {
        "start": time.perf_counter(),
        "end": -1,
        "elapsed": None,
        "exception": False,
    }
    try:
        yield internal_data
    except ValueError:
        internal_data["exception"] = True
    finally:
        internal_data['end'] = time.perf_counter()
        internal_data['elapsed'] = round(internal_data['end'] - internal_data['start'], 3)


with timer() as tempo:
    time.sleep(5)
    raise ValueError()

print(tempo)  # => Timer(start=0.1141484, end=5.1158644, elapsed=5.002, exception=True)

assert math.isclose(tempo["elapsed"], 5, abs_tol=0.1)
assert tempo["exception"] == True


## Use Case - Temporary Files

## Reference: https://docs.python.org/3/library/tempfile.html

import tempfile
from typing import IO, Any

temporary_file: IO[Any] = tempfile.TemporaryFile()
temporary_file.write(b"Hello world!")
temporary_file.seek(0)
temporary_file.read()  # => b'Hello world!'
temporary_file.close()

with tempfile.TemporaryFile() as temporary_file:  # Automatic closing
    temporary_file.write(b"Hello world!")
    temporary_file.seek(0)
    temporary_file.read()  # => b'Hello world!'


## Use case - Database

# Reference: https://docs.python.org/3/library/sqlite3.html

import sqlite3

# No Context Manager

connection: sqlite3.Connection = sqlite3.connect(":memory:")
try:
    connection.execute("select * from Person")
    connection.commit()
except sqlite3.OperationalError as exception:
    connection.rollback()

connection.close()  # Close the connection


# With Context Manager

connection: sqlite3.Connection = sqlite3.connect(":memory:")
try:
    with connection:  # Automatic Commit and Rollback
        connection.execute("select * from Person")
except sqlite3.OperationalError as exception:
    pass

connection.close()  # Close the connection


# Close automatically

from contextlib import closing

connection: sqlite3.Connection = sqlite3.connect(":memory:")
try:
    with closing(connection):  # Commit, Rollback and Close Automatically.
        connection.execute("select * from Person")
except sqlite3.OperationalError as exception:
    pass


# Ignoring Exceptions Automatically

from contextlib import suppress

connection: sqlite3.Connection = sqlite3.connect(":memory:")
with suppress(sqlite3.OperationalError):  # Exception ignored automatically
    with closing(connection):  # Commit, Rollback and Close Automatically
        connection.execute("select * from Person")


# Using Nested Context Manager Syntax
# Commit, Rollback, Close and Automatic Exception Handling

connection: sqlite3.Connection = sqlite3.connect(":memory:")
with suppress(sqlite3.OperationalError), closing(connection):   
    connection.execute("select * from Person")

####################################################
## 7.8 Standard Library Pearls - Pathlib
####################################################

from pathlib import Path

## Attributes

example_file = Path("/data/example/main.py")
print(example_file.parent)  # => "/data/example" on Windows, /data/example on Unix
assert example_file.name == "main.py"
assert example_file.stem == "main"
assert example_file.suffix == ".py"

# Concatenation

folder = Path("/data/example")
new_file = folder / "test.py"

# Special case: Current file

current_file = Path(__file__).resolve()

# File manipulation with automatic open and close

current_folder = current_file.parent
new_folder = current_folder / "chapter7"         # New_folder = current_file / "chapter7

new_folder.mkdir(exist_ok=True, parents=True)    # Create directory tree

empty_file = new_folder / "test_pathlib.txt"     # Define new file
empty_file.touch(exist_ok=True)                  # Create empty file

text_file = new_folder / "test_pathlib.txt"      # Define new file
text_file.write_text("Hello World")              # Write Text
contents_text = text_file.read_text()            # Read content

file_bytes = new_folder / "test_bytes.txt"       # Define new file
file_bytes.write_bytes(b"Hello World")           # Write Text
contents_bytes = file_bytes.read_bytes()         # Read contents

empty_file.unlink(missing_ok=True)               # Delete file
text_file.unlink(missing_ok=True)                # Delete file
file_bytes.unlink(missing_ok=True)               # Delete file
new_folder.rmdir()                               # Delete folder

assert contents_text == "Hello World"
assert contents_bytes == b"Hello World"


####################################################
## 7.9 Standard Library Pearls - Itertools
####################################################

import itertools

# Reference: https://docs.python.org/3/library/itertools.html

itertools.accumulate    # Equivalent to reduce but returns intermediate results
itertools.takewhile     # Returns elements of a collection until condition is false
itertools.dropwhile     # Returns elements that do not meet the condition, then returns all of them
itertools.filterfalse   # Equivalent to filter but condition is negated

# Combinatorial
itertools.product       # Cartesian product
itertools.permutations  # Permutations
itertools.combinations  # Combinations
itertools.combinations_with_replacement  # Combinations with replacement

# Featured recipes
# Reference: https://docs.python.org/3/library/itertools.html#itertools-recipes

from typing import Iterable, Any


def pairwise(iterable: Iterable[Any]) -> Iterator[Tuple[Any, Any]]:
    "s -> (s0, s1), (s1, s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def powerset(iterable: Iterable[Any]) -> Iterator[Tuple[Any, ...]]:
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))


def roundrobin(*iterables: List[Iterable[Any]]) -> Generator[Any, None, None]:
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
    # Recipe credited to George Sakkis
    num_active = len(iterables)
    nexts = itertools.cycle(iter(it).__next__ for it in iterables)
    while num_active:
        try:
            for next in nexts:
                yield next()
        except StopIteration:
            num_active -= 1
            nexts = itertools.cycle(itertools.islice(nexts, num_active))


####################################################
## 7.10 Standard Library Pearls - OS
####################################################

import os

# Reference: https://docs.python.org/3/library/os.html

# Read environment variables

os.environ["username"]             # => Error
os.environ.get("username", None)   # => None if username does not exist


####################################################
## 7.11 Standard Library Pearls - Serialization
####################################################

## Using Pickle

import pickle

# Reference: https://docs.python.org/3/library/pickle.html
#            https://docs.python.org/3/library/pickle.html#examples

from dataclasses import dataclass
from collections import Counter


@dataclass
class Student:
    name: str = ""


data = {
    "a": [1, 2.0, 3, 4 + 6j],
    "b": ("character string", b"byte string"),
    "c": {None, True, False},
    "d": [Student(), Student("Mary"), Student("John")],
    "e": Counter(a=10, b=4, c=2),
}

data_file = Path("data.pickle")

with open(data_file, "wb") as pickle_file:
    pickle.dump(data, pickle_file)

with open(data_file, "rb") as f:
    loaded_data = pickle.load(f)

data_file.unlink()

assert data == loaded_data


# Using JSON

import json

# Reference: https://docs.python.org/3/library/json.html

# Only Compatible Data Types:
# dict, list, tuple, str, int, float, bool, None

data = {
    "a": [1, 2.0, 3],
    "b": ("character string"),
    "c": [None, True, False],
}

data_file = Path("data.json")

with open(data_file, "w") as json_file:
    json.dump(data, json_file)

with open(data_file, "r") as json_file:
    loaded_data = json.load(json_file)

data_file.unlink()

assert data == loaded_data


####################################################
## 7.12 Standard Library Pearls - Emails
####################################################

import os
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders


def send_email(email: str, subject: str, content: str = "", file: Optional[str] = None):
    user = os.environ["email_username"]
    password = os.environ["email_password"]

    mime = MIMEMultipart() 
    
    mime["Subject"] = subject
    mime["From"] = "Email Sent Automatically with Python"
    mime["To"] = email
  
    mime.attach(MIMEText(content, "plain"))
    
    if file is not None:
        base = MIMEBase("application", "octet-stream")
        file_bytes = Path(file).read_bytes()
        base.set_payload(file_bytes) 
        encoders.encode_base64(base) 
        base.add_header("Content-Disposition", f"attachment; filename={file}")
        mime.attach(base) 

    server_url = os.environ["email_server"]
    port = int(os.environ["email_port"])

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(server_url, port, context=context) as server:
        server.ehlo()
        server.login(user, password)
        server.sendmail(user, email, mime.as_string())


# quick setup for Gmail:

# email_username = source gmail account
# email_password = application password | Get password from App Passwords at:
# https://myaccount.google.com/security 
# email_server = 'smtp.gmail.com' # email_server = 'smtp.gmail.com' # email_port = 465
# email_port = 465
