"""Este es el módulo principal de la aplicación (Docstring)"""

print("Me invocaron directa o indirectamente")


if __name__ == "__main__":
    print("Me invocaron directamente")


if __name__ != "__main__":
    print("Me invocaron indirectamente (mediante un import)")
    
    from pathlib import Path

    print(f"Importaste con Éxito {Path(__file__).parts[-1]}")

    name = "main"