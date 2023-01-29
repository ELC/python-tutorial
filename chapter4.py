####################################################
# 4. Functions
####################################################


def divide(x, y):      # Function and its parameters
    return x / y


def without_return(x, y):  # Default returns None
    x / y


def divide(x: float, y: float) -> float:     # Type-Hints | RECOMMENDED
    return x / y


def without_return(x: float, y: float) -> float: # Recommendations with Type-Hints
    x / y


assert divide(10, 8) == 1.25      # Order identical to the definition
assert divide(8, 10) == 0.8       # Order is important
assert divide(x=10, y=8) == 1.25  # Using keyword parameters
assert divide(y=8, x=10) == 1.25  # Order is irrelevant when using keyword parameters


def is_older_age(age: int, limit: int = 18) -> bool:  # Default value
    if age >= limit:
        result = True
    else:
        result = False
    return result


def is_older_age(age: int, limit: int = 18) -> bool:  # Multiple returns
    if age >= limit:
        return True
    return False


def is_older_age(age: int, limit: int = 18) -> bool:  # Return expression
    return age >= limit


# In all cases limit is assumed to be 18
assert not is_older_age(10)
assert is_older_age(18)
assert is_older_age(24)

# It can be passed explicitly as well
assert is_older_age(24, 18)
assert is_older_age(24, limit=18)


from typing import List, Tuple  # Standard Library.

prices: List[float] = [4.04, 5.37, 7.77, 0.09, 9.11, 4.96, 9.12, 2.28, 8.09, 7.36]


# Return with multiple values
def is_discounted(prices: List[float]) -> Tuple[bool, float]:
    lowest_price = min(prices)
    if lowest_price < 3:
        return True, lowest_price
    return False, lowest_price


assert is_discounted(prices) == (True, 0.09)  # => Return Tuple
exists_offer, amount = is_discounted(prices)  # => Unpacked
assert exists_offer
assert amount == 0.09


####################################################
# 4.1 Arbitrary parameters
####################################################


def summation(*args: float):  # Arbitrary positional parameters
    result = 0
    for value in args:
        result += value
    return result


assert summation(1, 2, 3) == 6


from typing import Dict  # Standard Library


def concatenate(**kwargs: str):  # Arbitrary keyword parameters
    return " ".join(kwargs.values())


concatenate(a="Hello", b="World")  # => 'Hello World '

numbers: List[float] = [1, 2, 3, 4]
words: Dict[str, str] = {"a": "Hello", "b": "World"}
assert summation(*numbers) == 10
assert concatenate(**words) == "Hello World"


####################################################
# 4.2 Higher order functions
####################################################

from typing import Callable  # Standard library

# Functions as parameters


def apply(list: List[float], function: Callable[[float], float]) -> List[float]:
    results = []
    for element in list:
        result = function(element)
        results.append(result)
    return results


def square(x: float) -> float:
    return x**2


some_list: List[float] = [1, 2, 3, 4, 5, 6]
assert apply(some_list, square) == [1, 4, 9, 16, 25, 36]


# Functions within functions (Closures)


def power(y: float) -> Callable[[float], float]:
    def auxiliary(x: float) -> float:
        return x**y

    return auxiliary


some_list: List[float] = [1, 2, 3, 4, 5, 6]
square_power: Callable[[float], float] = power(2)
assert apply(some_list, square_power) == [1, 4, 9, 16, 25, 36]


# Partial evaluation

from functools import partial  # Standard library


def x_to_the_y_power(x: float, y: float) -> float:
    return x**y


some_list: List[float] = [1, 2, 3, 4, 5, 6]
square_partial: Callable[[float], float] = partial(x_to_the_y_power, y=2)
assert apply(some_list, square_partial) == [1, 4, 9, 16, 25, 36]


# Anonymous functions (Lambdas)

some_list: List[float] = [1, 2, 3, 4, 5, 6]
assert apply(some_list, lambda x: x**2) == [1, 4, 9, 16, 25, 36]


####################################################
# 4.3 Common higher-order functions (map, filter reduce)
####################################################

from typing import Iterator     # Standard library
from functools import reduce    # Standard library

some_list: List[float] = [1, 2, 3, 4, 5, 6]
squares: Iterator[float] = map(lambda x: x**2, some_list)         # => [1, 4, 9, 16, 25, 36]
squares_filtered: Iterator[float] = filter(lambda x: x > 5, squares)   # => [9, 16, 25, 36]
sum_filtered: float = reduce(lambda x, y: x + y, squares_filtered)        # => 86

assert sum_filtered == 86


####################################################
# 4.4 Comprehensions
####################################################

some_list: List[float] = [1, 2, 3, 4, 5, 6]
squares_: List[float] = [square_power(x) for x in some_list]          # => [1, 4, 9, 16, 25, 36]
squares_filtered_: List[float] = [x for x in squares_ if x > 5]    # => [9, 16, 25, 36]
sum_filtered: float = summation(*squares_filtered_)                          # => 86

assert sum_filtered == 86

some_list: List[float] = [1, 2, 3, 4, 5, 6]
sum_filtered: float = summation(*[square_power(x) for x in some_list if square_power(x) > 5])

assert sum_filtered == 86


# Code equivalent using a FOR loop

result: float = 0

for element in some_list:
    auxiliary: float = square_power(element)
    if auxiliary > 5:
        result += auxiliary

assert result == 86
