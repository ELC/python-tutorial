from pathlib import Path

print(f"You successfully imported {Path(__file__).parts[-1]}")

name = "data"

from source.controller import controller

controller.name = "I was modified in another module"
