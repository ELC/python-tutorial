####################################################
## 7. Uso avanzado del lenguaje
####################################################

from __future__ import annotations

####################################################
## Índice
####################################################

# 7.1 Namedtuple
# 7.2 Otras colecciones
# 7.3 Generadores
# 7.4 Iteradores
# 7.5 Semicorrutinas (Generadores Avanzados)
# 7.6 Corrutinas (AsyncIO)
# 7.7 Decoradores
# 7.8 Context Manager
# 7.9 Perlas de la Biblioteca Estándar - Itertools
# 7.10 Perlas de la Biblioteca Estándar - OS
# 7.11 Perlas de la Biblioteca Estándar - Serialización
# 7.12 Perlas de la Biblioteca Estándar - Emails


####################################################
## 7.1 Namedtuple
####################################################

# Referencia: https://docs.python.org/3/library/collections.html#collections.namedtuple

from dataclasses import dataclass
from collections import namedtuple

@dataclass
class Vector:
    x: float
    y: float

origen: Vector = Vector(0, 0)
origen.x       # => 0
origen.y       # => 0
print(origen)  # => Vector(x=0, y=0)
# x, y = origen  # => Error
origen.x = 1
origen.y = 1
print(origen)  # => Vector(x=1, y=1)



VectorAlternativo = namedtuple('VectorAlternativo', ['x', 'y'])
punto: VectorAlternativo = VectorAlternativo(1, 1)
punto.x          # => 1
punto.x          # => 1
print(punto)     # => VectorAlternativo(x=1, y=1)
x, y = punto     # => x=1, y=1
# punto.x = 1    # => Error


####################################################
## 7.2 Otras colecciones
####################################################

## Counter

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

## Defaultdict

# Referencia: https://docs.python.org/3/library/collections.html#collections.defaultdict

from collections import defaultdict

notas_alumnos = defaultdict(list)

notas_alumnos["Pedro"].append(8)  # No lanza KeyError 
notas_alumnos["María"].append(9)
notas_alumnos["Pedro"].append(3)
notas_alumnos["María"].append(8)
notas_alumnos["Pedro"].append(7)
notas_alumnos # => {'Pedro': [8, 3, 7], 'María': [9, 8]}


## Enum

# Referencia: https://docs.python.org/3/library/enum.html

from enum import Enum

class Permisos(Enum):
    ADMIN = 1
    USER = 2
    EDITOR = 3

Permisos.ADMIN            # => Permisos.ADMIN
Permisos.ADMIN.value      # => 1
Permisos['ADMIN']         # => Permisos.ADMIN
Permisos['ADMIN'].value   # => 1


####################################################
## 7.3 Generadores
####################################################

# Referencia: https://docs.python.org/3/tutorial/classes.html#generators

from typing import Generator, Iterator, List

def fibonacci_generador() -> Generator[int]:
    last: int = 1
    current: int = 1
    yield last
    yield current

    while True:
        current, last = last + current, current
        yield current

generador: Generator[int] = fibonacci_generador()
fibonacci_10_primeros: List[int] = []

for i in range(10):
    next_fibonacci = next(generador)
    fibonacci_10_primeros.append(next_fibonacci)

fibonacci_10_primeros  # => [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


# Pueden tomar parámetros comoo cualquier función
def primos_menores(numero: int) -> Generator[int, None, None]: 
    visitados = []
    for number in range(1, numero):
        no_es_primo = any(number % possible_divisor == 0 for possible_divisor in visitados)
        
        if not no_es_primo:
            visitados.append(number)
            yield number
        

# Con bucle tradicional
generador: Generator[int] = primos_menores(25)
primos_menores_25 = []
for primo in generador:
    primos_menores_25.append(primo)

primos_menores_25   # => [2, 3, 5, 7, 11, 13, 17, 19, 23]

# Con comprensión
generador: Generator[int] = primos_menores(25)
primos_menores_25 = [primo for primo in generador]
primos_menores_25   # => [2, 3, 5, 7, 11, 13, 17, 19, 23]


####################################################
## 7.4 Iteradores
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


generador_con_clase: Iterator[int] = PrimosMenores(25)
primos_menores_25: List[int] = []
for i in range(9):
    siguiente_fibonacci: int = next(generador_con_clase)
    primos_menores_25.append(siguiente_fibonacci)
primos_menores_25   # => [2, 3, 5, 7, 11, 13, 17, 19, 23]

# Con comprensión
generador_con_clase: Iterator[int] = PrimosMenores(25)
primos_menores_25: List[int] = [primo for primo in generador_con_clase]
primos_menores_25   # => [2, 3, 5, 7, 11, 13, 17, 19, 23]


####################################################
## 7.5 Semicorrutinas (Generadores Avanzados)
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
resultado_acumulador   # => 29


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
resultado_diferido # => Listo


####################################################
## 7.6 Corrutinas (AsyncIO)
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

async def main_serial_alternativo() -> Tuple[int, int]:
    resultado_api = await respondiendo_api()
    resultado_db = await procesamiento_db()
    return (resultado_api, resultado_db)

print(f"Empezado: {time.strftime('%X')}") 
resultados: Tuple[int, int] = asyncio.run(main_serial())
print(f"Finalizado: {time.strftime('%X')}")
resultados # => (0, 1)

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
resultados: Tuple[int, int] = asyncio.run(main_serial_alternativo())
print(f"Finalizado: {time.strftime('%X')}")
resultados # => (1, 0)

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

async def main_task_alternativo() -> Tuple[int, int]:
    api_task = asyncio.create_task(respondiendo_api())
    db_task = asyncio.create_task(procesamiento_db())
    return (await api_task, await db_task)

print(f"Empezado: {time.strftime('%X')}") 
resultados = asyncio.run(main_task())
print(f"Finalizado: {time.strftime('%X')}")
resultados # => (0, 1)

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
resultados = asyncio.run(main_task_alternativo())
print(f"Finalizado: {time.strftime('%X')}")
resultados # => (1, 0)

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

async def main_gather_alternativo() -> Tuple[int, int]:
    return await asyncio.gather(respondiendo_api(), procesamiento_db())

print(f"Empezado: {time.strftime('%X')}") 
resultados= asyncio.run(main_gather())
print(f"Finalizado: {time.strftime('%X')}")
resultados # => (0, 1)

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
resultados = asyncio.run(main_gather_alternativo())
print(f"Finalizado: {time.strftime('%X')}")
resultados # => (1, 0)

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
resultados_blocking # => [None, None, None, None, None, None, None, None, None, None]

# Empezado: 10:28:34
# Finalizado: 10:28:44


print(f"Empezado: {time.strftime('%X')}") 
resultados_blocking_async: Tuple[None] = asyncio.run(main_blocking_async())
print(f"Finalizado: {time.strftime('%X')}")
resultados_blocking_async # => [None, None, None, None, None, None, None, None, None, None]

# Empezado: 10:28:44
# Finalizado: 10:28:46

####################################################
## 7.7 Decoradores
####################################################

import time
from typing import Tuple, Any

def medir_tiempo(function):

    def helper(*args, **kargs) -> Tuple[Any, float]:
        inicio: float = time.perf_counter()
        
        resultado = function(*args, **kargs)
        
        fin: float = time.perf_counter()
        
        transcurrido: float = fin - inicio 

        return resultado, transcurrido

    return helper


def funcion_lenta():
    time.sleep(2)
    return "Hola mundo"


# Invocación normal
respuesta: str = funcion_lenta()
respuesta # => "Hola mundo"


# Invocación con wrapper sin decorador
funcion_lenta_con_tiempo = medir_tiempo(funcion_lenta)
resultado: Tuple[str, float] = funcion_lenta_con_tiempo()
resultado   # => ('Hola mundo', 2.0035091)


# Invocación con decorador

@medir_tiempo
def funcion_lenta_medida():
    time.sleep(2)
    return "Hola mundo"

resultado: Tuple[str, float] = funcion_lenta_con_tiempo()
resultado   # => ('Hola mundo', 2.0083497)


# Decorador con estado (Stateful)

def contar_ejecuciones(func):
    
    def helper(*args, **kwargs):
        helper.ejecuciones += 1
        return func(*args, **kwargs)
    
    helper.ejecuciones = 0

    return helper

@contar_ejecuciones
def funcion_contada():
    return "Hola mundo"

for _ in range(10):
    funcion_contada()

funcion_contada.ejecuciones   # => 10


# Decorador con estado basado en clases (Stateful)

from dataclasses import dataclass
from typing import Callable

@dataclass
class Contador:
    func: Callable
    ejecuciones: int = 0

    def __call__(self, *args, **kwargs):
        self.ejecuciones += 1
        return self.func(*args, **kwargs)


@Contador
def funcion_contada_clase():
    return "Hola mundo"

for _ in range(10):
    funcion_contada_clase()

funcion_contada_clase.ejecuciones   # => 10


# Casos de uso - Cache y Memoization Manual

@contar_ejecuciones
def fibonacci(numero):
    if numero < 2:
        return numero
    return fibonacci(numero - 1) + fibonacci(numero - 2)

resultado = fibonacci(20)
resultado  # => 6765
fibonacci.ejecuciones # => 21.891


def memoization(func):

    def helper(x):
        if x not in helper.cache:
            helper.cache[x] = func(x)
        return helper.cache[x]
    
    helper.cache = {}
    
    return helper

@contar_ejecuciones
@memoization
def fibonacci_memo(numero):
    if numero < 2:
        return numero
    return fibonacci_memo(numero - 1) + fibonacci_memo(numero - 2)

resultado = fibonacci_memo(20)
resultado  # => 6765
fibonacci_memo.ejecuciones  # => 39 | 500 veces menos ejecuciones


# Casos de uso - Cache y Memoization LRU

from functools import lru_cache

# Referencia: https://docs.python.org/3/library/functools.html#functools.lru_cache

@contar_ejecuciones
@lru_cache(maxsize=None) # Equivalente a @cache en Python 3.9+
def fibonacci_lru(numero):
    if numero < 2:
        return numero
    return fibonacci_lru(numero - 1) + fibonacci_lru(numero - 2)

resultado = fibonacci_lru(20)
resultado  # => 6765
fibonacci_lru.ejecuciones  # => 39 | 500 veces menos ejecuciones

# Otros casos de uso:
# Dataclasses
# Métodos de Clase
# Propiedades
# Bibliotecas


####################################################
## 7.8 Context Manager
####################################################

# Referencia: https://docs.python.org/3/library/stdtypes.html#context-manager-types

# Usando Clases

from dataclasses import dataclass
from typing import IO, Optional, Any
import time

@dataclass
class Temporizador:
    inicio: float = 0
    fin: Optional[float] = None
    transcurrido: Optional[float] = None
    excepcion: bool = False

    def __enter__(self) -> Temporizador:
        self.inicio = time.perf_counter()
        return self

    def __exit__(self, tipo_excepcion: Optional[Any], _, __) -> bool:
        self.excepcion = tipo_excepcion is not None
        self.fin = time.perf_counter()
        self.transcurrido = round(self.fin - self.inicio, 3)
        return True

with Temporizador() as tempo:
    time.sleep(5)
    raise ValueError

tempo  # => Temporizador(inicio=0.1141484, fin=5.1158644, transcurrido=5.002, excepcion=True)


# Usando contexlib

# Referencia: https://docs.python.org/3/library/contextlib.html

from contextlib import contextmanager
import time

@contextmanager
def temporizador():
    datos_internos = {
        "inicio": time.perf_counter(),
        "fin": None,
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
    raise ValueError

tempo  # => {'inicio': 5.1166176, 'fin': 10.1197138, 'transcurrido': 5.003, 'excepcion': True}


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

def pairwise(iterable: Iterable) -> Iterator[Tuple[Any, Any]]:
    "s -> (s0, s1), (s1, s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def powerset(iterable: Iterable) -> Iterator[Tuple[Any, ...]]:
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))


def roundrobin(*iterables: List[Iterable]) -> Generator[Any]:
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

with open('datos.pickle', 'wb') as pickle_file:
    pickle.dump(datos, pickle_file)

with open('datos.pickle', 'rb') as f:
    datos_cargados = pickle.load(f)

datos == datos_cargados  # => True


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

with open('datos.json', 'w') as json_file:
    json.dump(datos, json_file)

with open('datos.json', 'r') as json_file:
    datos_cargados = json.load(json_file)

datos == datos_cargados   # => True


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


def enviar_email(email, asunto, contenido="", archivo=None):
    usuario = os.environ["email_username"]
    clave = os.environ["email_password"]

    mime = MIMEMultipart() 
    
    mime['Subject'] = asunto
    mime['From'] = 'Email Enviado automáticamente con Python'
    mime['To'] = email
  
    mime.attach(MIMEText(contenido, 'plain')) 
    
    if archivo is not None:        
        with open(archivo, "rb") as attachment:
            base = MIMEBase('application', 'octet-stream') 
            base.set_payload(attachment.read()) 
            encoders.encode_base64(base) 
            base.add_header('Content-Disposition', f"attachment; filename= {archivo}") 
            mime.attach(base) 

    context = ssl.create_default_context()

    servidor_url = os.environ["email_server"]
    puerto = int(os.environ["email_port"])

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

