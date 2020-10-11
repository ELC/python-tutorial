"""En este módulo se encuentra el código fuente principal de la aplicación"""

print("Este mensaje se ejecutará antes de los imports de este módulo")

nombres = ["sábana", "parlante", "computadora", "tasa", "botella", "celular"]
precios = [10.25, 5.258, 350.159, 25.99, 18.759, 215.231]

articulos = {nombre:precio for nombre, precio in zip(nombres, precios)}
