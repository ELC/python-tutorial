####################################################
# 4. Funciones
####################################################


def dividir(x, y):     # Función y sus parametros
    return x / y


def sin_return(x, y):  # Por defecto se devuelve None
    x / y


def dividir(x: float, y: float) -> float:     # Type-Hints | RECOMENDADO
    return x / y


def sin_return(x: float, y: float) -> float:  # Recomendaciones con Type-Hints
    x / y


dividir(10, 8)        # => 1.25 Orden idéntico a la definición
dividir(8, 10)        # => 0.8  El Orden es importante
dividir(x=10, y=8)    # => 1.25 Usando parametros explícitos
dividir(y=8, x=10)    # => 1.25 Orden irrelevante


def es_mayor_de_edad(edad: int, limite: int = 18) -> bool:  # Valor por defecto
    if edad >= limite:
        resultado = True
    else:
        resultado = False
    return resultado


def es_mayor_de_edad(edad: int, limite: int = 18) -> bool:  # Múltiples returns
    if edad >= limite:
        return True
    return False


def es_mayor_de_edad(edad: int, limite: int = 18) -> bool:  # Return expression
    return edad >= limite


es_mayor_de_edad(10)  # => False
es_mayor_de_edad(18)  # => True
es_mayor_de_edad(24)  # => True


from typing import List, Tuple   # Biblioteca Estándar

precios: List[float] = [4.04, 5.37, 7.77, 0.09, 9.11, 4.96, 9.12, 2.28, 8.09, 7.36]


# Return con múltiples valores
def hay_oferta(precios: List[float]) -> Tuple[bool, float]:
    precio_mas_bajo = min(precios)
    if precio_mas_bajo < 3:
        return True, precio_mas_bajo
    return False, precio_mas_bajo


hay_oferta(precios)                         # => (True, 0.09) | Devuelve Tupla
existe_oferta, monto = hay_oferta(precios)  # => Desempaquetado
existe_oferta    # => True
monto            # => 0.09


####################################################
# 4.1 Parametros Arbitrarios
####################################################

def suma(*args: float):           # Parametros posicionales arbitrarios
    resultado = 0
    for valor in args:
        resultado += valor
    return resultado


suma(1, 2, 3)  # => 6


from typing import Dict   # Biblioteca Estándar

def concatenate(**kwargs: str):   # Parametros de palabra clave arbitrarios
    result = ""
    for arg in kwargs.values():
        result += arg + " "
    return result


concatenate(a="Hola", b="Mundo")  # => 'Hola Mundo '

numeros: List[float] = [1, 2, 3, 4]
palabras: Dict[str, str] = {"a": "Hola", "b": "Mundo"}
suma(*numeros)            # => 10
concatenate(**palabras)   # => 'Hola Mundo '


####################################################
# 4.2 Funciones de orden superior
####################################################

from typing import Callable   # Biblioteca Estándar

# Funciones como parámetros

def aplicar_funcion(lista: List[float], funcion: Callable[[float], float]) -> List[float]:
    resultados = []
    for elemento in lista:
        resultado = funcion(elemento)
        resultados.append(resultado)
    return resultados


def cuadrado(x: float) -> float:
    return x ** 2


lista: List[float] = [1, 2, 3, 4, 5, 6]
aplicar_funcion(lista, cuadrado)   # => [1, 4, 9, 16, 25, 36]


# Funciones dentro de funciones (Closures)

def elevar(y: float) -> Callable[[float], float]:

    def auxiliar(x: float) -> float:
        return x ** y

    return auxiliar


lista: List[float] = [1, 2, 3, 4, 5, 6]
elevar_cuadrado: Callable[[float], float] = elevar(2)
aplicar_funcion(lista, elevar_cuadrado)   # => [1, 4, 9, 16, 25, 36]


# Evaluación Parcial

from functools import partial  # Biblioteca estandar

def elevar_xy(x: float, y: float) -> float:
    return x ** y


lista: List[float] = [1, 2, 3, 4, 5, 6]
elevar_cuadrado_parcial: Callable[[float], float] = partial(elevar_xy, y=2)
aplicar_funcion(lista, elevar_cuadrado_parcial)   # => [1, 4, 9, 16, 25, 36]


# Funciones anónimas (Lambdas)

lista: List[float] = [1, 2, 3, 4, 5, 6]
aplicar_funcion(lista, lambda x: x**2)   # => [1, 4, 9, 16, 25, 36]


####################################################
# 4.3 Funciones sobre Funciones
####################################################

from typing import Iterator     # Biblioteca estándar
from functools import reduce    # Biblioteca estándar

lista: List[float] = [1, 2, 3, 4, 5, 6]
cuadrados: Iterator[float] = map(lambda x: x ** 2, lista)              # => [1, 4, 9, 16, 25, 36]
cuadrados_pares: Iterator[float] = filter(lambda x: x > 5, cuadrados)  # => [9, 16, 25, 36]
suma_pares: float = reduce(lambda x, y: x + y, cuadrados_pares)        # => 86


####################################################
# 4.4 Comprensiones
####################################################

lista: List[float] = [1, 2, 3, 4, 5, 6]
cuadrados_: List[float] = [elevar_cuadrado(x) for x in lista]      # => [1, 4, 9, 16, 25, 36]
cuadrados_pares_: List[float] = [x for x in cuadrados_ if x > 5]   # => [9, 16, 25, 36]
suma_pares: float = sum(cuadrados_pares_)                          # => 86


lista: List[float] = [1, 2, 3, 4, 5, 6]
suma_pares: float = sum(elevar_cuadrado(x) for x in lista if elevar_cuadrado(x) > 5)
suma_pares  # => 86<


# Código equivalente a la comprensión con bucle FOR

resultado: float = 0

for elemento in lista:
    auxiliar: float = elevar_cuadrado(elemento)
    if auxiliar > 5:
        resultado += auxiliar

resultado   # => 86
