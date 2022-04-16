####################################################
## 7. Uso avanzado del lenguaje
####################################################

from __future__ import annotations

####################################################
## Índice
####################################################

# 7.1 Tipos adicionales
# 7.2 Generadores
# 7.3 Iteradores
# 7.4 Semicorrutinas (Generadores Avanzados)
# 7.5 Corrutinas (AsyncIO)
# 7.6 Decoradores
# 7.7 Context Manager
# 7.8 Perlas de la Biblioteca Estándar - Pathlib
# 7.9 Perlas de la Biblioteca Estándar - Itertools
# 7.10 Perlas de la Biblioteca Estándar - OS
# 7.11 Perlas de la Biblioteca Estándar - Serialización
# 7.12 Perlas de la Biblioteca Estándar - Emails


####################################################
## 7.1 Tipos Adicionales
####################################################


####################################################
## 7.1.1 namedtuple y NamedTuple
####################################################

# Referencia: https://docs.python.org/3/library/collections.html#collections.namedtuple

from dataclasses import dataclass, astuple
from collections import namedtuple

@dataclass
class Vector:
    x: float
    y: float

    def modulo(self) -> float:
        return (self.x**2 + self.y**2)**0.5

origen = Vector(0, 0)
origen.x                # => 0
origen.y                # => 0
print(origen)           # => Vector(x=0, y=0)
# x, y = origen         # => Error
x, y = astuple(origen)  # => Sin Error
# origen[0]             # => Error No se pueden usar índices en clases
origen.x = 3            # => Atributos mutables por defecto
origen.y = 4            # => Atributos mutables por defecto
print(origen)           # => Vector(x=3, y=4)

assert origen.modulo() == 5


# Usando frozen=True

@dataclass(frozen=True)
class VectorInmutable:
    x: float
    y: float

    def modulo(self) -> float:
        return (self.x**2 + self.y**2)**0.5


origen = VectorInmutable(0, 0)
origen.x                # => 0
origen.y                # => 0
print(origen)           # => Vector(x=0, y=0)
# x, y = origen         # => Error
x, y = astuple(origen)  # => Sin Error
# origen[0]             # => Error No se pueden usar índices en clases
# origen.x = 3          # => Error atributos son inmutables
# origen.y = 4          # => Error atributos son inmutables

assert origen.modulo() == 0


# Usando collections.namedtuple


VectorAlternativo = namedtuple('VectorAlternativo', ['x', 'y'])

def modulo_sin_tipos(vector: VectorAlternativo) -> float:
    return (vector.x**2 + vector.y**2)**0.5  # Warning por desconocer los tipos


punto = VectorAlternativo(3, 4)
punto.x                 # => 3 con Warning: No hay tipo especificado
punto.y                 # => 4 con Warning: No hay tipo especificado
print(punto)            # => VectorAlternativo(x=3, y=4)
x, y = punto            # => x=3, y=4 con Warning: No hay tipo especificado
# punto.x = 1           # => Error

assert punto[0] == 3
assert punto[1] == 4
assert modulo_sin_tipos(punto) == 5


# Usando NamedTuple como superclase


from typing import NamedTuple

class VectorAlternativoTipado(NamedTuple):
    x: float
    y: float

    def modulo(self) -> float:
        return (self.x**2 + self.y**2)**0.5


def modulo_tipado_1(vector: VectorAlternativoTipado) -> float:
    return (vector.x**2 + vector.y**2)**0.5


punto_tipado_str = VectorAlternativoTipado("1", "1")  # Warning String != Float

punto_tipado_1 = VectorAlternativoTipado(3, 4)
punto_tipado_1.x          # => 3
punto_tipado_1.y          # => 4
print(punto_tipado_1)     # => VectorAlternativo(x=3, y=4)
x, y = punto_tipado_1     # => x=3, y=4
# punto_tipado_1.x = 1    # => Error

assert punto_tipado_1[0] == 3
assert punto_tipado_1[1] == 4
assert modulo_tipado_1(punto_tipado_1) == 5


# Usando NamedTuple como función

VectorAlternativoTipado_2 = NamedTuple("VectorAlternativoTipado_2", [('x', float), ('y', float)])

def modulo_tipado_2(vector: VectorAlternativoTipado_2) -> float:
    return (vector.x**2 + vector.y**2)**0.5


punto_tipado_2 = VectorAlternativoTipado_2(3, 4)
punto_tipado_2.x          # => 1
punto_tipado_2.x          # => 1
print(punto_tipado_2)     # => VectorAlternativo(x=1, y=1)
x, y = punto_tipado_2     # => x=1, y=1
# punto_tipado_1.x = 1    # => Error

assert punto_tipado_1[0] == 3
assert punto_tipado_1[1] == 4
assert modulo_tipado_2(punto_tipado_2) == 5


####################################################
## 7.1.2 Counter
####################################################


# Referencia: https://docs.python.org/3/library/collections.html#collections.Counter

from collections import Counter

texto = """
En fe del buen acogimiento y honra que hace Vuestra Excelencia a toda suerte de
libros, como príncipe tan inclinado a favorecer las buenas artes, mayormente 
las que por su nobleza no se abaten al servicio y granjerías del vulgo, he 
determinado de sacar a luz El ingenioso hidalgo don Quijote de la Mancha, al 
abrigo del clarísimo nombre de Vuestra Excelencia, a quien, con el acatamiento 
que debo a tanta grandeza, suplico le reciba agradablemente en su protección, 
para que a su sombra, aunque desnudo de aquel precioso ornamento de elegancia 
y erudición de que suelen andar vestidas las obras que se componen en las casas
de los hombres que saben, ose parecer seguramente en el juicio de algunos que,
conteniéndose en los límites de su ignorancia, suelen condenar con más rigor 
y menos justicia los trabajos ajenos; que, poniendo los ojos la prudencia de 
Vuestra Excelencia en mi buen deseo, fío que no desdeñará la cortedad de tan 
humilde servicio.
"""  # Extracto del corpus de Miguel de Cervantes Saavedra

contador_de_letras = Counter(texto)
contador_de_letras.most_common(4) # => [(' ', 158), ('e', 114), ('a', 84), ('n', 65)]

contador_de_palabras = Counter(texto.split())
contador_de_palabras.most_common(4) # => [('de', 12), ('que', 8), ('a', 6), ('en', 5)]


####################################################
## 7.1.3 Defaultdict
####################################################


# Referencia: https://docs.python.org/3/library/collections.html#collections.defaultdict

from collections import defaultdict

notas_alumnos: defaultdict[str, List[int]] = defaultdict(list)

notas_alumnos["Pedro"].append(8)  # No lanza KeyError 
notas_alumnos["María"].append(9)
notas_alumnos["Pedro"].append(3)
notas_alumnos["María"].append(8)
notas_alumnos["Pedro"].append(7)

assert notas_alumnos == {'Pedro': [8, 3, 7], 'María': [9, 8]}


####################################################
## 7.1.4 Enum
####################################################


# Referencia: https://docs.python.org/3/library/enum.html

from enum import Enum, auto


class Permisos(Enum):
    ADMIN = auto()
    USER = auto()
    EDITOR = auto()

    @staticmethod
    def tiene_acceso_panel_de_control_1(permiso: Permisos) -> bool:
        return permiso is Permisos.ADMIN or permiso is Permisos.EDITOR


Permisos.ADMIN            # => Permisos.ADMIN
Permisos.ADMIN.value      # => 1
Permisos['ADMIN']         # => Permisos.ADMIN
Permisos['ADMIN'].value   # => 1

print(Permisos.__members__.keys())     # => ['ADMIN', 'USER', 'EDITOR']
print(Permisos.__members__.values())   # => [<Permisos.ADMIN: 1>, <Permisos.USER: 2>, <Permisos.EDITOR: 3>]

Permisos.tiene_acceso_panel_de_control_1("REDACTOR")  # Sin Error - Warning Tipo Incompatible

assert Permisos.tiene_acceso_panel_de_control_1(Permisos.ADMIN)


# Alternativa usando typing.Literal

from typing import Literal

PermisosA = Literal["ADMIN", "EDITOR", "USER"]

class PermisosAlternativo:
    @staticmethod
    def tiene_acceso_panel_de_control_2(permiso: PermisosA) -> bool:
        return permiso in ["ADMIN", "EDITOR"]


PermisosAlternativo.tiene_acceso_panel_de_control_2("REDACTOR")  # Sin Error - Warning Tipo Incompatible

assert PermisosAlternativo.tiene_acceso_panel_de_control_2("ADMIN")


####################################################
## 7.1.4 SimpleNameSpace
####################################################


from dataclasses import dataclass


@dataclass
class Persona:
    nombre: str

empleado_1 = Persona("Juan")
empleado_1.nombre              # => Juan
# empleado_1["nombre"]         # => Error - No se pueden usar claves con dataclasses
empleado_1.edad = 24           # => Sin Error - Monkey Patching - NO RECOMENDADO 


# Usando Diccionarios

empleado_2 = {}
empleado_2["nombre"] = "Juan"
empleado_2["nombre"]           # => Juan
#empleado_2.nombre             # => Error - No se pueden acceder a valores usando .


# Usando SimpleNameSpace

# Referencia: https://docs.python.org/3/library/types.html#types.SimpleNamespace

from types import SimpleNamespace

empleado_3 = SimpleNamespace()
empleado_3.nombre = "Juan"     # => Sin Error - No es Mokey Patching - Uso Correcto
# empleado_3["nombre"]         # => Error - No se pueden usar claves con SimpleNamespace


# Custom SimpleNamespace

from dataclasses import field

from typing import Any

class Empleado(SimpleNamespace):
    def __setitem__(self, clave: str, valor: Any) -> None:
        setattr(self, clave, valor)
    
    def __getitem__(self, clave: str) -> Any:
        return getattr(self, clave)


empleado_4 = Empleado()
empleado_4["nombre"] = "Juan"   # => Sin Error - No es Mokey Patching - Uso Correcto
empleado_4.edad = 24            # => Sin Error - No es Mokey Patching - Uso Correcto

assert empleado_4.nombre == "Juan"
assert empleado_4["nombre"] == "Juan"
assert empleado_4.edad == 24
assert empleado_4["edad"] == 24


####################################################
## 7.2 Generadores
####################################################

# Referencia: https://docs.python.org/3/tutorial/classes.html#generators

from typing import Generator, Iterator, List

def fibonacci_generador() -> Generator[int, None, None]:
    last: int = 1
    current: int = 1
    yield last
    yield current

    while True:
        current, last = last + current, current
        yield current

generador = fibonacci_generador()
fibonacci_10_primeros: List[int] = []

for _ in range(10):
    next_fibonacci = next(generador)
    fibonacci_10_primeros.append(next_fibonacci)

assert fibonacci_10_primeros == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


# Pueden tomar parámetros comoo cualquier función
def primos_menores(numero: int) -> Generator[int, None, None]: 
    visitados: List[int] = []
    for number in range(2, numero):
        no_es_primo = any(number % possible_divisor == 0 for possible_divisor in visitados)
        
        if not no_es_primo:
            visitados.append(number)
            yield number
        

# Con bucle tradicional

generador = primos_menores(25)
primos_menores_25: List[int] = []
for primo in generador:
    primos_menores_25.append(primo)

assert primos_menores_25 == [2, 3, 5, 7, 11, 13, 17, 19, 23]


# Con comprensión

generador = primos_menores(25)
primos_menores_25 = [primo for primo in generador]
assert primos_menores_25 == [2, 3, 5, 7, 11, 13, 17, 19, 23]


# Con list

generador = primos_menores(25)
primos_menores_25 = list(generador)
assert primos_menores_25 == [2, 3, 5, 7, 11, 13, 17, 19, 23]


####################################################
## 7.3 Iteradores
####################################################

# Referencia: https://docs.python.org/3/library/stdtypes.html#iterator-types

from dataclasses import dataclass, field
from typing import List

@dataclass
class PrimosMenores:
    numero: int
    numero_actual: int = 1
    visitados: List[int] = field(default_factory=list)

    def __iter__(self):   # Necesario para usar en For
        return self

    def __next__(self):   # Necesario para función next
        while True:
            self.numero_actual += 1
            no_es_primo = any(self.numero_actual % possible_divisor == 0 
                                    for possible_divisor in self.visitados)
            
            if self.numero_actual >= self.numero:
                raise StopIteration()

            if not no_es_primo or len(self.visitados) == 0:
                break

        self.visitados.append(self.numero_actual)
        return self.numero_actual


# Con bucle tradicional

generador_con_clase: Iterator[int] = PrimosMenores(25)
primos_menores_25: List[int] = []
for primo in generador_con_clase:
    primos_menores_25.append(primo)

assert primos_menores_25 == [2, 3, 5, 7, 11, 13, 17, 19, 23]

# Con comprensión

generador_con_clase: Iterator[int] = PrimosMenores(25)
primos_menores_25 = [primo for primo in generador_con_clase]
assert primos_menores_25 == [2, 3, 5, 7, 11, 13, 17, 19, 23]

# Con list

generador_con_clase: Iterator[int] = PrimosMenores(25)
primos_menores_25 = list(generador_con_clase)
assert primos_menores_25 == [2, 3, 5, 7, 11, 13, 17, 19, 23]


####################################################
## 7.4 Semicorrutinas (Generadores con send)
####################################################

from typing import Generator, Any

def acumular() -> Generator[float, float, None]:
    acumulador = 0
    while True:
        siguiente = yield acumulador
        acumulador += siguiente


semicorrutina: Generator[float, float, None] = acumular()
next(semicorrutina) # Inicializar

semicorrutina.send(10)
semicorrutina.send(-1)

resultado_acumulador: float = semicorrutina.send(20) # Finalizar
assert resultado_acumulador == 29


## Caso de Uso

def procesamiento_diferido() -> Generator[Any, Any, Any]:
    datos = yield
    print(f"Procesando datos... - {datos}")   # Reemplazar con proceso complejo
    datos_procesados = str(datos)
    nuevos_datos = yield datos_procesados
    print(f"Procesando datos... - {nuevos_datos}")   # Reemplazar con proceso complejo
    yield "Listo"

semicorrutina_diferida: Generator[Any, Any, Any] = procesamiento_diferido()
next(semicorrutina_diferida) # Inicializar

resultado_diferido: float = semicorrutina_diferida.send(123) # => Procesando datos... - 123

# Proceso diferido
resultado_diferido = semicorrutina_diferida.send(654) # => Procesando datos... - 654

assert resultado_diferido == "Listo"


####################################################
## 7.5 Corrutinas (AsyncIO)
####################################################


# Referencia: https://docs.python.org/3/library/asyncio-task.html

import asyncio
import time
from typing import Tuple

# Definiendo corrutinas

async def procesamiento_db() -> int:    # Modificador Async
    print("DB: Enviando Consulta a la base de datos")
    await asyncio.sleep(1)              # Comportamiento similar a yield 
    print("DB: Procesando consulta 1")
    await asyncio.sleep(3)
    print("DB: Guardando Resultados")
    return 0

async def respondiendo_api() -> int:
    print("API: Solicitando datos al usuario")
    await asyncio.sleep(1) 
    print("API: Construyendo Response")
    await asyncio.sleep(1)
    print("API: Escribiendo Logs")
    await asyncio.sleep(1)
    print("API: Enviando respuesta")
    await asyncio.sleep(1)
    print("API: Recibiendo confirmación")
    return 1

# Ejecución Serial de Corrutinas

async def main_serial() -> Tuple[int, int]:
    resultado_db = await procesamiento_db()
    resultado_api = await respondiendo_api()
    return (resultado_db, resultado_api)

async def main_serial_invertido() -> Tuple[int, int]:
    resultado_api = await respondiendo_api()
    resultado_db = await procesamiento_db()
    return (resultado_api, resultado_db)

print(f"Empezado: {time.strftime('%X')}") 
resultados: Tuple[int, int] = asyncio.run(main_serial())
print(f"Finalizado: {time.strftime('%X')}")
assert resultados == (0, 1)

# Empezado: 09:47:35
# DB: Enviando Consulta a la base de datos
# DB: Procesando consulta 1
# DB: Guardando Resultados
# API: Solicitando datos al usuario
# API: Construyendo Response
# API: Escribiendo Logs
# API: Enviando respuesta
# API: Recibiendo confirmación
# Finalizado: 09:47:43

print(f"Empezado: {time.strftime('%X')}") 
resultados: Tuple[int, int] = asyncio.run(main_serial_invertido())
print(f"Finalizado: {time.strftime('%X')}")
assert resultados == (1, 0)

# Empezado: 09:47:43
# API: Solicitando datos al usuario
# API: Construyendo Response
# API: Escribiendo Logs
# API: Enviando respuesta
# API: Recibiendo confirmación
# DB: Enviando Consulta a la base de datos
# DB: Procesando consulta 1
# DB: Guardando Resultados
# Finalizado: 09:47:51

# Ejecución Concurrente de Corrutinas (Tasks)

async def main_task() -> Tuple[int, int]:
    db_task = asyncio.create_task(procesamiento_db())
    api_task = asyncio.create_task(respondiendo_api())
    return (await db_task, await api_task)

async def main_task_invertido() -> Tuple[int, int]:
    api_task = asyncio.create_task(respondiendo_api())
    db_task = asyncio.create_task(procesamiento_db())
    return (await api_task, await db_task)

print(f"Empezado: {time.strftime('%X')}") 
resultados = asyncio.run(main_task())
print(f"Finalizado: {time.strftime('%X')}")
assert resultados == (0, 1)

# Empezado: 09:47:52
# DB: Enviando Consulta a la base de datos
# API: Solicitando datos al usuario       
# DB: Procesando consulta 1
# API: Construyendo Response
# API: Escribiendo Logs
# API: Enviando respuesta
# DB: Guardando Resultados
# API: Recibiendo confirmación
# Finalizado: 09:47:56

print(f"Empezado: {time.strftime('%X')}") 
resultados = asyncio.run(main_task_invertido())
print(f"Finalizado: {time.strftime('%X')}")
assert resultados == (1, 0)

# Empezado: 09:47:56
# API: Solicitando datos al usuario
# DB: Enviando Consulta a la base de datos
# API: Construyendo Response
# DB: Procesando consulta 1
# API: Escribiendo Logs
# API: Enviando respuesta
# DB: Guardando Resultados
# API: Recibiendo confirmación
# Finalizado: 09:48:00


# Ejecución Concurrente de Corrutinas (Gather)

async def main_gather() -> Tuple[int, int]:
    return await asyncio.gather(procesamiento_db(), respondiendo_api())

async def main_gather_invertido() -> Tuple[int, int]:
    return await asyncio.gather(respondiendo_api(), procesamiento_db())

print(f"Empezado: {time.strftime('%X')}") 
resultados = asyncio.run(main_gather())
print(f"Finalizado: {time.strftime('%X')}")
assert resultados == [0, 1]

# Empezado: 09:48:00
# DB: Enviando Consulta a la base de datos
# API: Solicitando datos al usuario
# DB: Procesando consulta 1
# API: Construyendo Response
# API: Escribiendo Logs
# API: Enviando respuesta
# DB: Guardando Resultados
# API: Recibiendo confirmación
# Finalizado: 09:48:04

print(f"Empezado: {time.strftime('%X')}") 
resultados = asyncio.run(main_gather_invertido())
print(f"Finalizado: {time.strftime('%X')}")
assert resultados == [1, 0]

# Empezado: 09:48:04
# API: Solicitando datos al usuario
# DB: Enviando Consulta a la base de datos
# API: Construyendo Response
# DB: Procesando consulta 1
# API: Escribiendo Logs
# API: Enviando respuesta
# DB: Guardando Resultados
# API: Recibiendo confirmación
# Finalizado: 09:48:08


# Ejecutando de manera asíncrona código síncrono

import time
import asyncio
from typing import List

def esperar() -> None:
    time.sleep(1)

def main_blocking() -> List[None]:
    return [esperar() for _ in range(10)]

async def main_blocking_async():
    loop = asyncio.get_running_loop()
    futuros = [loop.run_in_executor(None, esperar) for _ in range(10)]
    return await asyncio.gather(*futuros)


print(f"Empezado: {time.strftime('%X')}") 
resultados_blocking: List[None] = main_blocking()
print(f"Finalizado: {time.strftime('%X')}")
assert resultados_blocking == [None] * 10

# Empezado: 10:28:34
# Finalizado: 10:28:44


print(f"Empezado: {time.strftime('%X')}") 
resultados_blocking_async: Tuple[None] = asyncio.run(main_blocking_async())
print(f"Finalizado: {time.strftime('%X')}")
assert resultados_blocking_async == [None] * 10

# Empezado: 10:28:44
# Finalizado: 10:28:46

####################################################
## 7.6 Decoradores
####################################################


####################################################
## 7.6.1 Decoradores sin estado
####################################################


import time
from typing import Tuple, Any

def medir_tiempo(function: Callable[..., Any]) ->Callable[..., Tuple[Any, float]]:

    def helper(*args: Any, **kargs: Any) -> Tuple[Any, float]:
        """Función Auxiliar"""
        inicio: float = time.perf_counter()
        
        resultado = function(*args, **kargs)
        
        fin: float = time.perf_counter()
        
        transcurrido: float = fin - inicio 

        return resultado, transcurrido

    return helper


def funcion_lenta() -> str:
    """Función Original"""
    time.sleep(2)
    return "Hola mundo"


# Invocación normal
respuesta: str = funcion_lenta()
assert respuesta == "Hola mundo"

import math

# Invocación con wrapper sin decorador
funcion_lenta_con_tiempo = medir_tiempo(funcion_lenta)
resultado, tiempo_ejecucion = funcion_lenta_con_tiempo()

assert resultado == 'Hola mundo'
assert math.isclose(tiempo_ejecucion, 2, abs_tol=0.1)

assert funcion_lenta.__name__ == "funcion_lenta"
assert funcion_lenta_con_tiempo.__name__ == "helper"           # No Deseable
assert funcion_lenta_con_tiempo.__doc__ == "Función Auxiliar"  # No Deseable


# Usando Wraps para "heredar" nombre y docstring

from functools import wraps

def medir_tiempo_alternativo(function: Callable[..., Any]) ->Callable[..., Tuple[Any, float]]:

    @wraps(function)
    def helper(*args: Any, **kargs: Any) -> Tuple[Any, float]:
        inicio: float = time.perf_counter()
        
        resultado = function(*args, **kargs)
        
        fin: float = time.perf_counter()
        
        transcurrido: float = fin - inicio 

        return resultado, transcurrido

    return helper


funcion_lenta_con_tiempo = medir_tiempo_alternativo(funcion_lenta)
resultado, tiempo_ejecucion = funcion_lenta_con_tiempo()

assert resultado == 'Hola mundo'
assert math.isclose(tiempo_ejecucion, 2, abs_tol=0.1)

assert funcion_lenta.__name__ == "funcion_lenta"
assert funcion_lenta_con_tiempo.__name__ == "funcion_lenta"     # Deseable
assert funcion_lenta_con_tiempo.__doc__ == "Función Original"   # Deseable


# Invocación con decorador

@medir_tiempo_alternativo
def funcion_lenta_medida():
    time.sleep(2)
    return "Hola mundo"

resultado, tiempo_ejecucion = funcion_lenta_medida()

assert resultado == 'Hola mundo'
assert math.isclose(tiempo_ejecucion, 2, abs_tol=0.1)


# Decorador con estado (Stateful)

def contar_ejecuciones(funcion: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(funcion)
    def helper(*args: Any, **kwargs: Any):
        helper.ejecuciones += 1
        return funcion(*args, **kwargs)
    
    helper.ejecuciones = 0  # Warning - Monkey Patching - NO RECOMENDADO

    return helper

@contar_ejecuciones
def funcion_contada() -> str:
    return "Hola mundo"

for _ in range(10):
    funcion_contada()

assert funcion_contada.ejecuciones == 10  # Warning Atributo desconocido


####################################################
## 7.6.1 Decoradores con estado (Stateful)
####################################################


from dataclasses import dataclass
from typing import Callable

@dataclass
class Contador:
    func: Callable[..., Any]
    ejecuciones: int = 0

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        self.ejecuciones += 1
        return self.func(*args, **kwargs)


@Contador
def funcion_contada_clase():
    return "Hola mundo"

for _ in range(10):
    funcion_contada_clase()

assert funcion_contada_clase.ejecuciones == 10   # Sin Warning


# Casos de uso - Cache y Memoization Manual

@Contador
def fibonacci(numero: int) -> int:
    if numero < 2:
        return numero
    return fibonacci(numero - 1) + fibonacci(numero - 2)

resultado = fibonacci(20)
assert resultado == 6765
assert fibonacci.ejecuciones == 21_891


from typing import Dict


def memoization(funcion: Callable[..., Any]) -> Callable[..., Any]:
    cache: Dict[str, Any] = {}

    def helper(*args: Any, **kwargs: Any) -> Any:
        nonlocal cache
        key = str(tuple(sorted(args)) + tuple(sorted(kwargs.items())))
        if key not in cache:
            cache[key] = funcion(*args, **kwargs)
        return cache[key]
    
    return helper


@Contador
@memoization
def fibonacci_memo(numero: int) -> int:
    if numero < 2:
        return numero
    return fibonacci_memo(numero - 1) + fibonacci_memo(numero - 2)


resultado = fibonacci_memo(20)
assert resultado == 6765
assert fibonacci_memo.ejecuciones == 39  # 500 veces menos ejecuciones


# Casos de uso - Cache y Memoization LRU

from functools import lru_cache

# Referencia: https://docs.python.org/3/library/functools.html#functools.lru_cache

@Contador
@lru_cache(maxsize=None) # Equivalente a @cache en Python 3.9+
def fibonacci_lru(numero: int) -> int:
    if numero < 2:
        return numero
    return fibonacci_lru(numero - 1) + fibonacci_lru(numero - 2)

resultado = fibonacci_lru(20)
assert resultado == 6765
assert fibonacci_memo.ejecuciones == 39  # 500 veces menos ejecuciones


####################################################
## 7.7 Context Manager
####################################################

# Referencia: https://docs.python.org/3/library/stdtypes.html#context-manager-types


####################################################
## 7.7.1 Context Manager con Clases
####################################################


from dataclasses import dataclass
from typing import IO, Optional, Any
import time

@dataclass
class Temporizador:
    inicio: float = 0
    fin: Optional[float] = None
    transcurrido: float = -1
    excepcion: bool = False

    def __enter__(self) -> Temporizador:
        self.inicio = time.perf_counter()
        return self

    def __exit__(self, tipo_excepcion: Optional[Any], _: Any, __: Any) -> bool:
        self.excepcion = tipo_excepcion is not None
        self.fin = time.perf_counter()
        self.transcurrido = round(self.fin - self.inicio, 3)
        return True

with Temporizador() as tempo:
    time.sleep(5)
    raise ValueError

print(tempo)  # => Temporizador(inicio=0.1141484, fin=5.1158644, transcurrido=5.002, excepcion=True)

assert math.isclose(tempo.transcurrido, 5, abs_tol=0.1)
assert tempo.excepcion == True


####################################################
## 7.7.2 Context Manager con Generadores y Contextlib
####################################################

# Referencia: https://docs.python.org/3/library/contextlib.html

from contextlib import contextmanager
import time

@contextmanager
def temporizador():
    datos_internos = {
        "inicio": time.perf_counter(),
        "fin": -1,
        "transcurrido": None,
        "excepcion": False
    }
    try:
        yield datos_internos
    except ValueError:
        datos_internos['excepcion'] = True
    finally:
        datos_internos['fin'] = time.perf_counter()
        datos_internos['transcurrido'] = round(datos_internos['fin'] - datos_internos['inicio'], 3)


with temporizador() as tempo:
    time.sleep(5)
    raise ValueError()

print(tempo)  # => Temporizador(inicio=0.1141484, fin=5.1158644, transcurrido=5.002, excepcion=True)

assert math.isclose(tempo["transcurrido"], 5, abs_tol=0.1)
assert tempo["excepcion"] == True


## Caso de uso - Archivos Temporales

# Referencia: https://docs.python.org/3/library/tempfile.html

import tempfile
from typing import IO, Any

archivo_temporal: IO[Any] = tempfile.TemporaryFile()
archivo_temporal.write(b'Hello world!')
archivo_temporal.seek(0)
archivo_temporal.read()      # => b'Hello world!'
archivo_temporal.close()

with tempfile.TemporaryFile() as archivo_temporal: # Cierre automático
    archivo_temporal.write(b'Hello world!')
    archivo_temporal.seek(0)
    archivo_temporal.read()  # => b'Hello world!'


## Caso de uso - Base de Datos

# Referencia: https://docs.python.org/3/library/sqlite3.html

import sqlite3

# Sin Context Manager

conexion: sqlite3.Connection = sqlite3.connect(":memory:")
try:
    conexion.execute("select * from Persona")
    conexion.commit()
except sqlite3.OperationalError as exception:
    conexion.rollback()

conexion.close()    # Cerrar la conexión 


# Con Context Manager

conexion: sqlite3.Connection = sqlite3.connect(":memory:")
try:
    with conexion:  # Commit y Rollback Automático
        conexion.execute("select * from Persona")
except sqlite3.OperationalError as exception:
    pass

conexion.close()    # Cerrar la conexión


# Cerrar automaticamente

from contextlib import closing

conexion: sqlite3.Connection = sqlite3.connect(":memory:")
try:
    with closing(conexion):   # Commit, Rollback y Close Automático
        conexion.execute("select * from Persona")
except sqlite3.OperationalError as exception:
    pass


# Ignorando Excepciones Automáticamente

from contextlib import suppress

conexion: sqlite3.Connection = sqlite3.connect(":memory:")
with suppress(sqlite3.OperationalError): # Excepción ignorada automáticamente
    with closing(conexion):   # Commit, Rollback y Close Automático
        conexion.execute("select * from Persona")


# Usando Sintaxis de Context Manager Anidados
# Commit, Rollback, Close y manejo de Excepción Automático

conexion: sqlite3.Connection = sqlite3.connect(":memory:")
with suppress(sqlite3.OperationalError), closing(conexion):   
    conexion.execute("select * from Persona")


####################################################
## 7.8 Perlas de la Biblioteca Estándar - Pathlib
####################################################

from pathlib import Path

# Atributos

archivo_ejemplo = Path("/data/ejemplo/main.py")
print(archivo_ejemplo.parent)  # => "\data\ejemplo" en Windows, /data/ejemplo en Unix
assert archivo_ejemplo.name == "main.py"
assert archivo_ejemplo.stem == "main"
assert archivo_ejemplo.suffix == ".py"

# Concatenación

carpeta = Path("/data/ejemplo")
archivo_nuevo = carpeta / "test.py"

# Caso espcial: Archivo actual

archivo_actual = Path(__file__).resolve()

# Manipulación de Archivos con open y close automáticos

carpeta_actual = archivo_actual.parent
carpeta_nueva = carpeta_actual / "chapter7"

carpeta_nueva.mkdir(exist_ok=True, parents=True)    # Crea arbol de directorios

archivo_vacio = carpeta_nueva / "test_pathlib.txt"  # Definir archivo nuevo
archivo_vacio.touch(exist_ok=True)                  # Crea un archivo vacio

archivo_texto = carpeta_nueva / "test_pathlib.txt"  # Definir archivo nuevo
archivo_texto.write_text("Hola Mundo")              # Escribir Texto
contenido_text = archivo_texto.read_text()               # Leer contenido

archivo_bytes = carpeta_nueva / "test_bytes.txt"    # Definir archivo nuevo
archivo_bytes.write_bytes(b"Hola Mundo")            # Escribir Texto
contenido_bytes = archivo_bytes.read_bytes()        # Leer contenido

archivo_vacio.unlink(missing_ok=True)               # Borrar archivo
archivo_texto.unlink(missing_ok=True)               # Borrar archivo
archivo_bytes.unlink(missing_ok=True)               # Borrar archivo
carpeta_nueva.rmdir()                               # Borrar carpeta

assert contenido_text == "Hola Mundo"
assert contenido_bytes == b"Hola Mundo"


####################################################
## 7.9 Perlas de la Biblioteca Estándar - Itertools
####################################################

import itertools

# Referencia: https://docs.python.org/3/library/itertools.html

itertools.accumulate    # Equivalente a reduce pero devuelve resultados intermedios
itertools.takewhile     # Devuelve elementos de una colleción hasta que la condición sea falsa
itertools.dropwhile     # Devuelve elementos que no cumplan la condición, luego devuelve todos
itertools.filterfalse   # Equivalente a filter pero la condición está negada

# Combinatoria
itertools.product       # Producto Cartesiano
itertools.permutations  # Permutaciones
itertools.combinations  # Combinaciones
itertools.combinations_with_replacement # Combinaciones con reemplazo

# Recetas destacadas
# Referencia: https://docs.python.org/3/library/itertools.html#itertools-recipes

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
## 7.10 Perlas de la Biblioteca Estándar - OS
####################################################

import os

# Referencia: https://docs.python.org/3/library/os.html

# Leer variables de entorno

os.environ["username"]             # => Error
os.environ.get("username", None)   # => None si username no existe


####################################################
## 7.11 Perlas de la Biblioteca Estándar - Serialización
####################################################

# Usando Pickle

import pickle

# Referencia: https://docs.python.org/3/library/pickle.html
#             https://docs.python.org/3/library/pickle.html#examples

from dataclasses import dataclass
from collections import Counter

@dataclass
class Alumno():
    nombre: str = ""

datos = {
    'a': [1, 2.0, 3, 4+6j],
    'b': ("character string", b"byte string"),
    'c': {None, True, False},
    'd': [Alumno(), Alumno("Maria"), Alumno("Juan")],
    'e': Counter(a=10, b=4, c=2)
}

archivo = Path('datos.pickle')

with open(archivo, 'wb') as pickle_file:
    pickle.dump(datos, pickle_file)

with open(archivo, 'rb') as f:
    datos_cargados = pickle.load(f)

archivo.unlink()

assert datos == datos_cargados



# Usando JSON

import json

# Referencia: https://docs.python.org/3/library/json.html

# Únicos Tipos de Dato Compatibles:
# dict, list, tuple, str, int, float, bool, None

datos = {
    'a': [1, 2.0, 3],
    'b': ("character string"),
    'c': [None, True, False],
}

archivo = Path('datos.json')

with open(archivo, 'w') as json_file:
    json.dump(datos, json_file)

with open(archivo, 'r') as json_file:
    datos_cargados = json.load(json_file)

archivo.unlink()

assert datos == datos_cargados


####################################################
## 7.12 Perlas de la Biblioteca Estándar - Emails
####################################################

import os
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders


def enviar_email(email: str, asunto: str, contenido: str = "", archivo: Optional[str] = None):
    usuario = os.environ["email_username"]
    clave = os.environ["email_password"]

    mime = MIMEMultipart() 
    
    mime['Subject'] = asunto
    mime['From'] = 'Email Enviado automáticamente con Python'
    mime['To'] = email
  
    mime.attach(MIMEText(contenido, 'plain')) 
    
    if archivo is not None:
        base = MIMEBase('application', 'octet-stream') 
        archivo_bytes = Path(archivo).read_bytes()
        base.set_payload(archivo_bytes) 
        encoders.encode_base64(base) 
        base.add_header('Content-Disposition', f"attachment; filename={archivo}") 
        mime.attach(base) 

    servidor_url = os.environ["email_server"]
    puerto = int(os.environ["email_port"])

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(servidor_url, puerto, context=context) as servidor:
        servidor.ehlo()
        servidor.login(usuario, clave)
        servidor.sendmail(usuario, email, mime.as_string())


# Configuración rápida para Gmail:

# email_username = cuenta de gmail de origen
# email_password = contraseña de aplicación | Obtener contraseña en App Passwords en:
#                                             https://myaccount.google.com/security 
# email_server = 'smtp.gmail.com'
# email_port = 465

