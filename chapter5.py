####################################################
# 5. Classes
####################################################


####################################################
# 5.1 Inicializador y Métodos de instancia
####################################################

from __future__ import annotations


class Rectangulo:
    def __init__(self, base: float, altura: float) -> None:
        self.base: float = base
        self.altura: float = altura

    def area(self) -> float:
        return self.base * self.altura

rec = Rectangulo(10, 10)
rec.base     # => 10
rec.altura   # => 10
rec.area()   # => 100

Rectangulo(10, 10).area()  # => 100
Rectangulo(10, 0).area()   # => 0
Rectangulo(0, 10).area()   # => 0


####################################################
# 5.2 Variables y Métodos de clase
####################################################


class ArticuloBase:
    _last_id: int = 0

    def __init__(self, nombre: str = "") -> None:
        self.nombre: str = nombre
        self.id_: int = self._get_next_id()

    @classmethod
    def _get_next_id(cls):
        cls._last_id += 1
        return cls._last_id


art1 = ArticuloBase("manzana")
art2 = ArticuloBase("pera")
art3 = ArticuloBase()
art3.nombre = "tv"

art1.nombre  # => "manzana"
art2.nombre  # => "pera"
art3.nombre  # => "tv"

art1.id_     # => 1
art2.id_     # => 2
art3.id_     # => 3


####################################################
# 5.3 Dataclasses
####################################################


from typing import ClassVar
from dataclasses import dataclass, field
import uuid

class Persona:
    _dni: int = 0

    def __init__(self, nombre: str, edad: int, altura: float, propiedades: Optional[List[str]] = None) -> None:
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.propiedades = propiedades or []
        self.id_socio = f"{nombre[0].upper()}-{str(uuid.uuid4())[:8]}"
        self.dni = str(Persona._get_next_dni()).zfill(8)

    def es_mayor_edad(self) -> bool:
        return self.edad >= 17

    @classmethod
    def _get_next_dni(cls) -> int:
        cls._dni += 1
        return cls._dni


juan: Persona = Persona("Juan", 18, 175.9)
juan.es_mayor_edad()  # => True
Persona("Julia", 16, 162.4).es_mayor_edad()  # => False
print(juan)  # => <__main__.Persona object at 0x000001C90BBF8688>


@dataclass
class PersonaDataClass:
    nombre: str
    edad: int
    sexo: str
    peso: float
    altura: float
    propiedades: List[str] = field(default_factory=list)
    id_socio: str = field(init=False)
    dni: str = field(init=False)
    _dni: ClassVar[int] = 0

    def __post_init__(self):
        self.id_socio: str = f"{self.nombre[0].upper()}-{str(uuid.uuid4())[:8]}"
        self.dni = str(PersonaDataClass._get_next_dni()).zfill(8)

    def es_mayor_edad(self) -> bool:
        return self.edad >= 18

    @classmethod
    def _get_next_dni(cls) -> int:
        cls._dni += 1
        return cls._dni


pedro: PersonaDataClass = PersonaDataClass("Pedro", 18, "H", 85, 175.9)
pedro.es_mayor_edad()  # => True
PersonaDataClass("Julia", 16, "M", 65, 162.4).es_mayor_edad()  # => False
print(pedro) # => PersonaDataClass(nombre='Pedro', edad=18, sexo='H', peso=85, altura=175.9, propiedades=[], id_socio='P-f642581c', dni='00000001')


####################################################
# 5.4 Sobrecarga de Operadores
####################################################


# Referencia: https://docs.python.org/3/reference/datamodel.html#basic-customization

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


manzana = Article("Manzana")
pera = Article("Pera")
tv = Article("Television")

# Test de conversión a String
str(ShoppingCart().add(manzana).add(pera))  # => ['Manzana', 'Pera']

# Test de reproducibilidad
carrito = ShoppingCart().add(manzana).add(pera)
assert carrito == eval(repr(carrito))
print(repr(carrito))  # => ShoppingCart([Article('Manzana'), Article('Pera')])

# Test de igualdad
assert ShoppingCart().add(manzana) == ShoppingCart().add(manzana)  # => True
print(ShoppingCart().add(manzana))  # => ['Manzana']

# Test de remover objeto
assert ShoppingCart().add(tv).add(pera).remove(tv) == ShoppingCart().add(pera)  # => True
print(ShoppingCart().add(tv).add(pera).remove(tv))  # => ['Pera']

# Test de igualdad con distinto orden
assert ShoppingCart().add(tv).add(pera) == ShoppingCart().add(pera).add(tv)  # => True
print(ShoppingCart().add(tv).add(pera))  # => ['Television', 'Pera']

# Test de suma
combinado = ShoppingCart().add(manzana) + ShoppingCart().add(pera)
assert combinado == ShoppingCart().add(manzana).add(pera)  # => True
print(combinado)  # => ['Manzana', 'Pera']


####################################################
# 5.5 Instancias como Functiones (__call__)
####################################################


@dataclass
class Acumulador:
    valor_inicial: Union[int, float] = 0
    valor: Union[int, float] = field(init=False)

    def __post_init__(self):
        self.valor = self.valor_inicial

    def incrementar(self, valor: Union[int, float]) -> None:
        self.valor += valor


acumulador_1 = Acumulador()
acumulador_1.incrementar(5)
acumulador_1.incrementar(10)
acumulador_1.incrementar(-2)

assert acumulador_1.valor == 13 

@dataclass
class AcumuladorAlternativo:
    valor_inicial: Union[int, float] = 0
    valor: Union[int, float] = field(init=False)

    def __post_init__(self):
        self.valor = self.valor_inicial

    def __call__(self, valor: Union[int, float]) -> None:
        self.valor += valor

acumulador_2 = AcumuladorAlternativo()
acumulador_2(5)
acumulador_2(10)
acumulador_2(-2)

assert acumulador_2.valor == 13


####################################################
# 5.6 Propiedades y Copia Profunda
####################################################


# Referencia: https://docs.python.org/3/library/copy.html

@dataclass
class Producto:
    _nombre: str
    _precio: float

    @property
    def nombre(self) -> str:
        return self._nombre.capitalize()

    @nombre.setter
    def nombre(self, value: str) -> None:
        self._nombre = value

    @property
    def precio(self) -> float:
        return round(self._precio, 2)

    @precio.setter
    def precio(self, value: float) -> None:
        self._precio = value


from copy import deepcopy           # Biblioteca Estandar

def actualizar_precio(productos: List[Producto], porcentaje_aumento: float) -> List[Producto]:
    nuevos: List[Producto] = []
    for producto in deepcopy(productos):
        producto.precio *= 1 + porcentaje_aumento / 100
        nuevos.append(producto)
    return nuevos


nombres = ["sábana", "parlante", "computadora", "tasa", "botella", "celular"]
precios = [10.25, 5.258, 350.159, 25.99, 18.759, 215.231]

productos = [Producto(nombre, precio)
             for nombre, precio in zip(nombres, precios)]
porcentaje_aumento = 10

productos_actualizados: List[Producto] = actualizar_precio(productos, porcentaje_aumento)
precios_desactualizados: List[float] = [producto.precio for producto in productos]
precios_actualizados: List[float] = [producto.precio for producto in productos_actualizados]

print(precios_desactualizados)  # => [10.25, 5.26, 350.16, 25.99, 18.76, 215.23]
print(precios_actualizados)     # => [11.28, 5.79, 385.18, 28.59, 20.64, 236.75]


####################################################
# 5.7 Herencia
####################################################


@dataclass
class Animal():
    edad: int = 0

    def descripcion(self) -> str:
        return f"Tengo {self.edad} años"


@dataclass
class Perro(Animal):
    raza: str = ""

    def descripcion(self) -> str:
        return f'Soy un perro y {super().descripcion().lower()}'

terrier = Perro(8, "Yorkshire Terrier")
dogo = Perro(raza="Dogo")
cachorro = Perro(edad=1)

print(terrier.descripcion())  # => Soy un perro y tengo 8 años


####################################################
# 5.8 Constructor (__new__)
####################################################


@dataclass
class Auto:
    velocidad_maxima: float
    precio: float

    def __new__(cls, velocidad_maxima: float, precio: float) -> Auto:
        
        if velocidad_maxima >= 300:
            auto = super().__new__(AutoDeportivo)
        elif precio >= 100_000:
            auto = super().__new__(AutoLujoso)
        else:
            auto = super().__new__(cls)
        
        auto.velocidad_maxima = velocidad_maxima
        auto.precio = precio
        return auto


class AutoLujoso(Auto):
    ...


class AutoDeportivo(Auto):
    ...


auto_familiar = Auto(170, 3_000)
auto_formula1 = Auto(370, 5_000_000)
auto_famoso = Auto(250, 500_000)

assert isinstance(auto_familiar, Auto)
assert isinstance(auto_formula1, Auto)
assert isinstance(auto_famoso, Auto)
assert isinstance(auto_formula1, AutoDeportivo)
assert isinstance(auto_famoso, AutoLujoso)


####################################################
# 5.8 Clases y Métodos abstractos
####################################################


# Referencia: https://docs.python.org/3/library/abc.html

from abc import ABC, abstractmethod
from typing import final  #  Python 3.8+

@dataclass
class Item(ABC):
    _id: ClassVar[int]
    id_: int = field(init=False)
    _nombre: str

    def __post_init__(self):
        self.id_ = self.__class__._get_next_id()

    @classmethod
    @abstractmethod
    def _get_next_id(cls) -> int:
        ...

    @abstractmethod
    def mostrar_id(self) -> str:
        ...

    @property
    @abstractmethod
    def nombre(self) -> str:
        ...

    @nombre.setter
    @abstractmethod
    def nombre(self, value: str) -> None:
        ...

    @final
    def descripcion(self) -> str:
        return f"ID: {self.id_} - Nombre: {self.nombre}"

@dataclass
class Ropa(Item):
    ...

@dataclass
class Material(Item):
    _id: ClassVar[int] = 0
    id_: int = field(init=False)
    _nombre: str

    @classmethod
    def _get_next_id(cls) -> int:
        cls._id += 1
        return cls._id

    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, value: str) -> None:
        self._nombre = value
    
    def mostrar_id(self) -> str:
        return str(self.id_).zfill(10)

@dataclass
class MaterialLujoso(Material):

    def descripcion(self) -> str:
        return f'{super().descripcion()} - Material de Lujo'


# item = Item("Item")                         # => Error
# item = Ropa("Camisa")                       # => Error
item_lujoso = MaterialLujoso("Formula 1")     # => Sin Error - Warning en la declaración
print(item_lujoso.descripcion())

item = Material("Madera")
print(item)  # => Material(id_=1, _nombre='Madera')

assert issubclass(type(item), Item)
assert issubclass(type(item), Material)
assert isinstance(item, Item)
assert isinstance(item, Material)


####################################################
# 5.9 Interfaces (Protocols)
####################################################


from typing import Protocol


class Identificable(Protocol):
    @property
    def nombre(self) -> str: 
        ...
    
    @property
    def id_(self) -> int:
        ...


def get_datos_resumen(objeto: Identificable):
    return f"{objeto.id_} - {objeto.nombre}"


madera = Material("Madera")

resumen = get_datos_resumen(madera)  # No hay Warning de Tipos
                                     # Incluso si Material no hereda de Identificable
                                     # Incluso si id_ no es una property
                                     # Incluso si


####################################################
# 5.10 Sobrecarga de Métodos
####################################################


from typing import overload, Sequence

@overload
def duplicar(x: int) -> int:
    ...

@overload
def duplicar(x: Sequence[int]) -> list[int]:
    ...

def duplicar(x: int | Sequence[int]) -> int | list[int]:
    if isinstance(x, Sequence):
        return [i * 2 for i in x]
    return x * 2

assert duplicar(2) == 4                  # Sin Warning
assert duplicar([1, 2, 3]) == [2, 4, 6]  # Sin Warning


####################################################
# 5.11 Sobrecarga de Métodos - Caso Especial - Python 3.8+
####################################################


from typing import Union

@dataclass
class Empleado:
    sueldo: float

    def calcular_sueldo(self, impuesto: Union[int, float]) -> float:
        if isinstance(impuesto, int) or impuesto >= 1:
            return self.sueldo - impuesto

        return self.sueldo * (1 - impuesto)


personal_limpieza_1 = Empleado(10_000)


from functools import singledispatchmethod   # Biblioteca Estandar

@dataclass
class EmpleadoAlternativo:
    sueldo: float

    @singledispatchmethod
    def calcular_sueldo(self, impuesto: float) -> float:
        raise NotImplementedError()


    @calcular_sueldo.register
    def _(self, impuesto: float) -> float:
        if impuesto >= 1:
            return self.sueldo - impuesto
        return self.sueldo * (1 - impuesto)

    @calcular_sueldo.register
    def _(self, impuesto: int) -> float:
        return self.sueldo - impuesto


personal_limpieza_2 = EmpleadoAlternativo(10_000)
assert personal_limpieza_2.calcular_sueldo(1500) == 8_500
assert personal_limpieza_2.calcular_sueldo(0.1) == 9_000

assert personal_limpieza_1.calcular_sueldo(1500) == personal_limpieza_2.calcular_sueldo(1500)
assert personal_limpieza_1.calcular_sueldo(0.1) == personal_limpieza_2.calcular_sueldo(0.1)


####################################################
# 5.12 Mixins (Herencia Múltiple)
####################################################


import json
from typing import Any


class JsonSerializer:

    def to_json(self) -> str:
        return json.dumps(vars(self))

    def from_json(self, json_string: str) -> Any:
        return json.loads(json_string)


@dataclass
class EmpleadoBaseDeDatos(EmpleadoAlternativo, JsonSerializer):
    tabla: str


personal_limpieza_2 = EmpleadoBaseDeDatos(10_000, "Empleados")

assert personal_limpieza_2.to_json() == '{"sueldo": 10000, "tabla": "Empleados"}'


####################################################
# 5.13 Descriptores
####################################################


class Positivo:

    def __set_name__(self, _: Any, nombre: str) -> None:
        self.nombre_atributo: str = f"_{nombre}"

    def __get__(self, objeto: Any, _: Any = None) -> Union[float, int]:
        return getattr(objeto, self.nombre_atributo)  # type: ignore

    def __set__(self, objeto: Any, valor: Union[float, int]) -> None:
        if valor < 0:
            raise ValueError(f"{self.nombre_atributo} debe ser positivo")

        setattr(objeto, self.nombre_atributo, valor)


class Celcius:

    def __get__(self, instancia: Any, _: Any = None) -> float:
        return (instancia.farenheit - 32) * 5 / 9

    def __set__(self, instancia: Any, valor: float) -> None:
        instancia.farenheit = 32 + valor * 9 / 5


@dataclass
class MaterialExperimento:
    masa: float = Positivo()
    temperatura: float = Celcius()


concreto_armado = MaterialExperimento(masa=50, temperatura=100)
assert concreto_armado.masa == 50
assert concreto_armado.temperatura == 100
assert concreto_armado.farenheit == 212     # Warning pero no Error


#oxigeno = MaterialExperimento(masa=-21, -30)  # Error -> ValueError: _masa debe ser positivo
