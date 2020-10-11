una_variable = 100

hex(10)
int("0xa", 16)

def dividir(x, y):     # Comentario
    return x / y


if una_variable % 2 == 0:
    print("El valor es par")
elif una_variable < 0:
    print("El valor es impar y negativo")
elif una_variable > 100:
    print("El valor es impar y mayor a 100")
else:
    print("El valor no cumple las condiciones")

nombres = ["Juan", "Pedro", "Maria"]
edades = [60, 15, 84]
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")

class Rectangulo:
    def __init__(self, base: float, altura: float) -> None:
        self.base: float = base
        self.altura: float = altura

    def area(self) -> float:
        return self.base * self.altura

rec = Rectangulo(10, 10)
rec.base
rec.area()
