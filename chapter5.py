####################################################
# 5. Classes
####################################################


####################################################
# 5.1 Constructor y Métodos de instancia
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

from dataclasses import dataclass   # Biblioteca Estándar

class Persona:
    def __init__(self, nombre: str, edad: int, sexo: str,
                 peso: float, altura: float) -> None:
        self.nombre: str = nombre
        self.edad: int = edad
        self.sexo: str = sexo
        self.peso: float = peso
        self.altura: float = altura

    def es_mayor_edad(self) -> bool:
        return self.edad >= 17


juan: Persona = Persona("Juan", 18, "H", 85, 175.9)
juan.es_mayor_edad()  # => True
Persona("Julia", 16, "M", 65, 162.4).es_mayor_edad()  # => False
print(juan)  # => <__main__.Persona object at 0x000001C90BBF8688>


@dataclass
class PersonaDataClass:
    nombre: str
    edad: int
    sexo: str
    peso: float
    altura: float

    def es_mayor_edad(self) -> bool:
        return self.edad >= 18


pedro: PersonaDataClass = PersonaDataClass("Pedro", 18, "H", 85, 175.9)
pedro.es_mayor_edad()  # => True
PersonaDataClass("Julia", 16, "M", 65, 162.4).es_mayor_edad()  # => False
print(pedro) # => PersonaDataClass(nombre='Pedro', edad=18, sexo='H', peso=85, altura=175.9)


####################################################
# 5.4 Sobrecarga de Operadores
####################################################

# Referencia: https://docs.python.org/3/reference/datamodel.html#basic-customization

from typing import List, Optional  # Biblioteca Estándar

class Article:
    def __init__(self, name: str) -> None:
        self.name = name

    def __eq__(self, other: Article) -> bool:
        return self.name == other.name

    def __hash__(self) -> int:
        return hash(self.name)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Article('{self.name}')"


class ShoppingCart:
    def __init__(self, articles: List[Article] = None) -> None:
        if articles is None:
            self.articles = []
        else:
            self.articles = articles

    def add(self, article: Article) -> ShoppingCart:
        self.articles.append(article)
        return self

    def remove(self, remove_article: Article) -> ShoppingCart:
        new_articles = []

        for article in self.articles:
            if article != remove_article:
                new_articles.append(article)

        self.articles = new_articles

        return self

    def __eq__(self, other: ShoppingCart) -> bool:
        return set(self.articles) == set(other.articles)

    def __str__(self) -> str:
        return str([str(i) for i in self.articles])

    def __repr__(self) -> str:
        return f"ShoppingCart({[art for art in self.articles]})"

    def __add__(self, other: ShoppingCart) -> ShoppingCart:
        return ShoppingCart(self.articles + other.articles)


manzana = Article("Manzana")
pera = Article("Pera")
tv = Article("Television")

# Test de conversión a String
str(ShoppingCart().add(manzana).add(pera))  # => ['Manzana', 'Pera']

# Test de reproducibilidad
carrito = ShoppingCart().add(manzana).add(pera)
carrito == eval(repr(carrito))  # => True
print(repr(carrito))  # => ShoppingCart([Article('Manzana'), Article('Pera')])

# Test de igualdad
ShoppingCart().add(manzana) == ShoppingCart().add(manzana)  # => True
print(ShoppingCart().add(manzana))  # => ['Manzana']

# Test de remover objeto
ShoppingCart().add(tv).add(pera).remove(tv) == ShoppingCart().add(pera)  # => True
print(ShoppingCart().add(tv).add(pera).remove(tv))  # => ['Pera']

# Test de igualdad con distinto orden
ShoppingCart().add(tv).add(pera) == ShoppingCart().add(pera).add(tv)  # => True
print(ShoppingCart().add(tv).add(pera))  # => ['Television', 'Pera']

# Test de suma
combinado = ShoppingCart().add(manzana) + ShoppingCart().add(pera)
combinado == ShoppingCart().add(manzana).add(pera)  # => True
print(combinado)  # => ['Manzana', 'Pera']


####################################################
# 5.5 Propiedades y Copia Profunda
####################################################


@dataclass
class Articulo:
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

def actualizar_precio(articulos: List[Articulo], porcentaje_aumento: float) -> List[Articulo]:
    nuevos = []
    for articulo in deepcopy(articulos):
        articulo.precio *= 1 + porcentaje_aumento / 100
        nuevos.append(articulo)
    return nuevos


nombres = ["sábana", "parlante", "computadora", "tasa", "botella", "celular"]
precios = [10.25, 5.258, 350.159, 25.99, 18.759, 215.231]

articulos = [Articulo(nombre, precio)
             for nombre, precio in zip(nombres, precios)]
porcentaje_aumento = 10

articulos_actualizados: List[Articulo] = actualizar_precio(articulos, porcentaje_aumento)
precios_desactualizados: List[float] = [articulo.precio for articulo in articulos]
precios_actualizados: List[float] = [articulo.precio for articulo in articulos_actualizados]

precios_desactualizados  # => [10.25, 5.26, 350.16, 25.99, 18.76, 215.23]
precios_actualizados     # => [11.28, 5.79, 385.18, 28.59, 20.64, 236.75]


####################################################
# 5.5 Herencia
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
# 5.5 Clases y Métodos abstractos
####################################################

from abc import ABC, abstractmethod

@dataclass
class Objeto(ABC):
    id_: int
    _nombre: str

    @abstractmethod
    def mostrar_id(self) -> str:
        return str(self.id_)

    @property
    @abstractmethod
    def nombre(self) -> str:
        return self._nombre.capitalize()

    @nombre.setter
    def nombre(self, value: str) -> None:
        self._nombre = value

class Ropa(Objeto):
    pass

class Material(Objeto):

    def nombre(self) -> str:
        return self._nombre
    
    def mostrar_id(self) -> str:
        return super().mostrar_id()


# objeto = Objeto(10, "Objeto")       # => Error
# objeto = Ropa(10, "Camisa")         # => Error
objeto = Material(10, "Madera")
print(objeto)  # => Material(id_=10, _nombre='Madera')

issubclass(type(objeto), Objeto)     # => True
issubclass(type(objeto), Material)   # => True
isinstance(objeto, Objeto)           # => True
isinstance(objeto, Material)         # => True


####################################################
# 5.6 Sobrecarga de Métodos - Python 3.8+
####################################################

from functools import singledispatchmethod   # Biblioteca Estandar

@dataclass
class Empleado:
    sueldo: float

    @singledispatchmethod
    def calcular_sueldo(self, impuesto):
        raise NotImplementedError

    @calcular_sueldo.register
    def _(self, impuesto: float) -> float:
        if impuesto >= 1:
            raise ValueError
        return self.sueldo * (1 - impuesto)

    @calcular_sueldo.register
    def _(self, impuesto: int) -> float:
        return self.sueldo - impuesto


personal_limpieza = Empleado(10_000)
personal_limpieza.calcular_sueldo(1500)   # => 8500
personal_limpieza.calcular_sueldo(0.1)    # => 9000.0

from typing import Optional

@dataclass
class EmpleadoAlternativo:
    sueldo: float
    ventas: Optional[float] = None
    comision: Optional[float] = None

    def calcular_sueldo(self, impuesto: Optional[float]=None, 
                              con_comision: bool=False) -> float:
        if impuesto is None and con_comision is False:
            return self.sueldo
        
        sueldo: float = self.sueldo

        if con_comision and self.ventas is not None and self.comision is not None:
            sueldo += self.ventas * self.comision
        
        if impuesto is not None:
            if impuesto >= 1:
                sueldo -= impuesto
            else:
                sueldo *= (1 - impuesto)
        
        return sueldo


manager = EmpleadoAlternativo(15_000)
manager.calcular_sueldo()       # => 15000
manager.calcular_sueldo(1500)   # => 13500
manager.calcular_sueldo(0.2)    # => 12000

vendedor = EmpleadoAlternativo(15_000, ventas=7000, comision=0.05)
vendedor.calcular_sueldo()                                   # => 15000
vendedor.calcular_sueldo(1500)                               # => 13500
vendedor.calcular_sueldo(0.2)                                # => 12000
vendedor.calcular_sueldo(1500, True)                         # => 13850
vendedor.calcular_sueldo(con_comision=True)                  # => 15350
vendedor.calcular_sueldo(impuesto=1500, con_comision=True)   # => 13850
