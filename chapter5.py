####################################################
# 5. Classes
####################################################


####################################################
# 5.1 Initializer and Instance Methods
####################################################

from __future__ import annotations


class Rectangle:
    def __init__(self, base: float, height: float) -> None:
        self.base: float = base
        self.height: float = height

    def area(self) -> float:
        return self.base * self.height

rec = Rectangle(10, 10)
rec.base     # => 10
rec.height   # => 10
rec.area()   # => 100

Rectangle(10, 10).area()  # => 100
Rectangle(10, 0).area()   # => 0
Rectangle(0, 10).area()   # => 0


####################################################
# 5.2 Class Variables and Methods
####################################################


class BaseArticle:
    _last_id: int = 0

    def __init__(self, name: str = "") -> None:
        self.name: str = name
        self.id_: int = self._get_next_id()

    @classmethod
    def _get_next_id(cls):
        cls._last_id += 1
        return cls._last_id


art1 = BaseArticle("apple")
art2 = BaseArticle("pear")
art3 = BaseArticle()
art3.name = "tv"

art1.name    # => "apple"
art2.name    # => "pear"
art3.name    # => "tv"

art1.id_     # => 1
art2.id_     # => 2
art3.id_     # => 3


####################################################
# 5.3 Static methods
####################################################


class Temperature:

    def __init__(self, region: str, temperature: float) -> None:
        self.region = region
        self.temperature = temperature

    @staticmethod
    def celcius_to_farenheit(temperature: float) -> float: # Without self
        return 32 + temperature * 9 / 5

    @staticmethod
    def farenheit_to_celcius(temperature: float) -> float: # Without self
        return (temperature - 32) * 5 / 9


temperature_today = Temperature("Mesopotamia", 35)

assert Temperature.celcius_to_farenheit(35) == 95        # Invocation from class
assert Temperature.farenheit_to_celcius(95) == 35        # Call from class
assert temperature_today.celcius_to_farenheit(35) == 95  # Invocation from instance
assert temperature_today.farenheit_to_celcius(95) == 35  # Invocation from instance


####################################################
# 5.4 Dataclasses
####################################################


from typing import ClassVar
from dataclasses import dataclass, field
import uuid

class Person:
    _personal_id: int = 0

    def __init__(self, name: str, age: int, height: float, properties: Optional[List[str]] = None) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.properties = properties or []
        self.member_id = f"{name[0].upper()}-{str(uuid.uuid4())[:8]}"
        self.personal_id = str(Person._get_next_personal_id()).zfill(8)

    def is_old_enough(self) -> bool:
        return self.age >= 17

    @classmethod
    def _get_next_personal_id(cls) -> int:
        cls._personal_id += 1
        return cls._personal_id


juan: Person = Person("Juan", 18, 175.9)
juan.is_old_enough()  # => True
Person("Julia", 16, 162.4).is_old_enough()  # => False
print(juan)  # => <__main__.Persona object at 0x000001C90BBF8688>


@dataclass
class PersonDataClass:
    name: str
    age: int
    gender: str
    weight: float
    height: float
    properties: List[str] = field(default_factory=list)
    member_id: str = field(init=False)
    personal_id: str = field(init=False)
    _personal_id: ClassVar[int] = 0

    def __post_init__(self):
        self.member_id: str = f"{self.name[0].upper()}-{str(uuid.uuid4())[:8]}"
        self.personal_id = str(PersonDataClass._get_next_personal_id()).zfill(8)

    def is_old_enough(self) -> bool:
        return self.age >= 18

    @classmethod
    def _get_next_personal_id(cls) -> int:
        cls._personal_id += 1
        return cls._personal_id


pedro: PersonDataClass = PersonDataClass("Pedro", 18, "H", 85, 175.9)
pedro.is_old_enough()  # => True
PersonDataClass("Julia", 16, "M", 65, 162.4).is_old_enough()  # => False
print(pedro) # => PersonaDataClass(name='Pedro', age=18, gender='H', weight=85, height=175.9, properties=[], member_id='P-f642581c', dni='00000001')

####################################################
# 5.5 Operator Overloading
####################################################


# Reference: https://docs.python.org/3/reference/datamodel.html#basic-customization

from typing import List, Optional  

@dataclass
class Article:
    name: str

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Article):
            raise NotImplementedError()

        return self.name == other.name

    def __hash__(self) -> int:
        return hash(self.name)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Article('{self.name}')"


@dataclass
class ShoppingCart:
    articles: List[Article] = field(default_factory=list)

    def add(self, article: Article) -> ShoppingCart:
        self.articles.append(article)
        return self

    def remove(self, remove_article: Article) -> ShoppingCart:
        self.articles = [article for article in self.articles if article != remove_article]
        return self

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ShoppingCart):
            raise NotImplementedError()
        return set(self.articles) == set(other.articles)

    def __str__(self) -> str:
        return str(self.articles)

    def __repr__(self) -> str:
        return f"ShoppingCart({self.articles})"

    def __add__(self, other: ShoppingCart) -> ShoppingCart:
        return ShoppingCart(self.articles + other.articles)


apple = Article("Apple")
pear = Article("Pear")
tv = Article("Television")

# Test conversion to String
str(ShoppingCart().add(apple).add(pear))  # => ['Apple', 'Pear'])

# Reproducibility test
cart = ShoppingCart().add(apple).add(pear)
assert cart == eval(repr(cart))
print(repr(cart))  # => ShoppingCart([Article('Apple'), Article('Pear')])

# Equality test
assert ShoppingCart().add(apple) == ShoppingCart().add(apple)  # => True
print(ShoppingCart().add(apple))  # => ['Apple']]

# Test object removal
assert ShoppingCart().add(tv).add(pear).remove(tv) == ShoppingCart().add(pear)  # => True
print(ShoppingCart().add(tv).add(pear).remove(tv))  # => ['Pear'])

# Equality test with different order
assert ShoppingCart().add(tv).add(pear) == ShoppingCart().add(pear).add(tv)  # => True
print(ShoppingCart().add(tv).add(pear))  # => ['Television', 'Pear']

# Sum test
combined = ShoppingCart().add(apple) + ShoppingCart().add(pear)
assert combined == ShoppingCart().add(apple).add(pear)  # => True
print(combined)  # => ['Apple', 'Pear']


####################################################
# 5.6 Instances as Functions (__call__)
####################################################


@dataclass
class Accumulator:
    initial_value: Union[int, float] = 0
    value: Union[int, float] = field(init=False)

    def __post_init__(self):
        self.value = self.initial_value

    def increment(self, value: Union[int, float]) -> None:
        self.value += value


accumulator_1 = Accumulator()
accumulator_1.increment(5)
accumulator_1.increment(10)
accumulator_1.increment(-2)

assert accumulator_1.value == 13 

@dataclass
class AccumulatorAlternative:
    initial_value: Union[int, float] = 0
    value: Union[int, float] = field(init=False)

    def __post_init__(self):
        self.value = self.initial_value

    def __call__(self, value: Union[int, float]) -> None:
        self.value += value


accumulator_2 = AccumulatorAlternative()
accumulator_2(5)
accumulator_2(10)
accumulator_2(-2)

assert accumulator_2.value == 13

####################################################
# 5.7 Properties and Deep Copy
####################################################


# Reference: https://docs.python.org/3/library/copy.html

@dataclass
class Product:
    _name: str
    _price: float

    @property
    def name(self) -> str:
        return self._name.capitalize()

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def price(self) -> float:
        return round(self._price, 2)

    @price.setter
    def price(self, value: float) -> None:
        self._price = value


from copy import deepcopy           # Standard Library

def update_price(products: List[Product], percentage_increase: float) -> List[Product]:
    new: List[Product] = []
    for product in deepcopy(products):
        product.price *= 1 + percentage_increase / 100
        new.append(product)
    return new


names = ["sheet", "speaker", "computer", "cup", "bottle", "cellular"]
prices = [10.25, 5.258, 350.159, 25.99, 18.759, 215.231]

products = [
    Product(name, price)  for name, price in zip(names, prices)
]
percentage_increase = 10

updated_products: List[Product] = update_price(products, percentage_increase)
out_of_date_prices: List[float] = [product.price for product in products]
updated_prices: List[float] = [product.price for product in updated_products]

print(out_of_date_prices) # => [10.25, 5.26, 350.16, 25.99, 18.76, 215.23]
print(updated_prices) # => [11.28, 5.79, 385.18, 28.59, 20.64, 236.75]


####################################################
# 5.8 Inheritance
####################################################


@dataclass
class Animal():
    age: int = 0

    def description(self) -> str:
        return f"I am {self.age} years old."


@dataclass
class Dog(Animal):
    breed: str = ""

    def description(self) -> str:
        return f"I'm a dog and {super().description().lower()}"

terrier = Dog(8, "Yorkshire Terrier")
dogo = Dog(breed="Dogo")
puppy = Dog(age=1)

print(terrier.description()) # => I am a dog and I am 8 years old.


####################################################
# 5.9 Constructor (__new__)
####################################################


@dataclass
class Car:
    max_speed: float
    price: float

    def __new__(cls, max_speed: float, price: float) -> Car:
        auto: Car

        if max_speed >= 300:
            auto = super().__new__(SportCar)
        elif price >= 100_000:
            auto = super().__new__(LuxuryCar)
        else:
            auto = super().__new__(cls)
        
        auto.max_speed = max_speed
        auto.price = price
        return auto


class LuxuryCar(Car):
    ...


class SportCar(Car):
    ...


family_car = Car(170, 3_000)
f1_car = Car(370, 5_000_000)
famous_car = Car(250, 500_000)

assert isinstance(family_car, Car)
assert isinstance(f1_car, Car)
assert isinstance(famous_car, Car)
assert isinstance(f1_car, SportCar), f1_car
assert isinstance(famous_car, LuxuryCar)

####################################################
# 5.10 Abstract Classes and Methods
####################################################


# Reference: https://docs.python.org/3/library/abc.html

from abc import ABC, abstractmethod
from typing import final  # Python 3.8+

@dataclass
class Item(ABC):
    _id: ClassVar[int]
    id_: int = field(init=False)
    _name: str

    def __post_init__(self):
        self.id_ = self.__class__._get_next_id()

    @classmethod
    @abstractmethod
    def _get_next_id(cls) -> int:
        ...

    @abstractmethod
    def show_id(self) -> str:
        ...

    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @name.setter
    @abstractmethod
    def name(self, value: str) -> None:
        ...

    @final
    def description(self) -> str:
        return f"ID: {self.id_} - Name: {self.name}"

@dataclass
class Clothing(Item):
    ...

@dataclass
class Material(Item):
    _id: ClassVar[int] = 0
    id_: int = field(init=False)
    _name: str

    @classmethod
    def _get_next_id(cls) -> int:
        cls._id += 1
        return cls._id

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str) -> None:
        self._name = value
    
    def show_id(self) -> str:
        return str(self.id_).zfill(10)

@dataclass
class LuxuryMaterial(Material):

    def description(self) -> str:
        return f'{super().description()} - Luxurious Material'


# item = Item("Item")                      # => Error
# item = Apparel("Shirt")                  # => Error
luxury_item = LuxuryMaterial("Formula 1")  # => No Error - Warning in the declaration
print(luxury_item.description())

item = Material("Wood")
print(item) # => Material(id_=1, _name='Wood')

assert issubclass(type(item), Item)
assert issubclass(type(item), Material)
assert isinstance(item, Item)
assert isinstance(item, Material)


####################################################
# 5.11 Interfaces (Protocols)
####################################################


from typing import Protocol


class Identifiable(Protocol):
    @property
    def name(self) -> str: 
        ...
    
    @property
    def id_(self) -> int:
        ...


def get_data_summary(element: Identifiable):
    return f"{element.id_} - {element.name}"


wood = Material("Wood")

summary = get_data_summary(wood)   # No Warning of Types.
                                   # Even if Material does not inherit from Identifiable
                                   # Even if id_ is not a property
                                   # Even if


####################################################
# 5.12 Method Overloading
####################################################


from typing import overload, Sequence

@overload
def duplicate(x: int) -> int:
    ...

@overload
def duplicate(x: Sequence[int]) -> list[int]:
    ...

def duplicate(x: int | Sequence[int]) -> int | list[int]:
    if isinstance(x, Sequence):
        return [i * 2 for i in x]
    return x * 2

assert duplicate(2) == 4                  # No Warning
assert duplicate([1, 2, 3]) == [2, 4, 6]  # No Warning


####################################################
# 5.13 Method Overloading - Special Case - Python 3.8+
####################################################


from typing import Union

@dataclass
class Employee:
    salary: float

    def calculate_salary(self, tax: Union[int, float]) -> float:
        if isinstance(tax, int) or tax >= 1:
            return self.salary - tax

        return self.salary * (1 - tax)


cleanning_staff_1 = Employee(10_000)


from functools import singledispatchmethod   # Standard Library

@dataclass
class EmployeeAlternate:
    salary: float

    @singledispatchmethod
    def calculate_salary(self, tax: float) -> float:
        raise NotImplementedError()


    @calculate_salary.register
    def _(self, tax: float) -> float:
        if tax >= 1:
            return self.salary - tax
        return self.salary * (1 - tax)

    @calculate_salary.register
    def _(self, tax: int) -> float:
        return self.salary - tax


cleanning_staff_2 = EmployeeAlternate(10_000)
assert cleanning_staff_2.calculate_salary(1500) == 8_500
assert cleanning_staff_2.calculate_salary(0.1) == 9_000

assert cleanning_staff_1.calculate_salary(1500) == cleanning_staff_2.calculate_salary(1500)
assert cleanning_staff_1.calculate_salary(0.1) == cleanning_staff_2.calculate_salary(0.1)

####################################################
# 5.14 Mixins (Multiple Inheritance)
####################################################


import json
from typing import Any


class JsonSerializer:

    def to_json(self) -> str:
        return json.dumps(vars(self))

    def from_json(self, json_string: str) -> Any:
        return json.loads(json_string)


@dataclass
class EmployeeDatabase(EmployeeAlternate, JsonSerializer):
    table: str


cleanning_staff_2 = EmployeeDatabase(10_000, "Employees")

assert cleanning_staff_2.to_json() == '{"salary": 10000, "table": "Employees"}'


####################################################
# 5.15 Descriptors
####################################################


class Positive:

    def __set_name__(self, _: Any, name: str) -> None:
        self.attribute_name: str = f"_{name}"

    def __get__(self, instance: Any, _: Any = None) -> Union[float, int]:
        return getattr(instance, self.attribute_name)  # type: ignore.

    def __set__(self, instance: Any, value: Union[float, int]) -> None:
        if value < 0:
            raise ValueError(f"{self.attribute_name} must be positive")

        setattr(instance, self.attribute_name, value)


class Celcius:

    def __get__(self, instance: Any, _: Any = None) -> float:
        return (instance.farenheit - 32) * 5 / 9

    def __set__(self, instance: Any, value: float) -> None:
        instance.farenheit = 32 + value * 9 / 5


@dataclass
class ExperimentalMaterial:
    mass: float = Positive()
    temperature: float = Celcius()


reinforced_concrete = ExperimentalMaterial(mass=50, temperature=100)
assert reinforced_concrete.mass == 50
assert reinforced_concrete.temperature == 100
assert reinforced_concrete.farenheit == 212 # Warning but no Error

reinforced_concrete.temperature = 50
assert reinforced_concrete.temperature == 50
assert reinforced_concrete.farenheit == 122
#oxygen = MaterialExperiment(mass=-21, -30) # Error -> ValueError: _mass must be positive


