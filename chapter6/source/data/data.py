from pathlib import Path

print(f"Importaste con Éxito {Path(__file__).parts[-1]}")

name = "data"

from source.controller import controller

controller.name = "Fui modificado en otro módulo"