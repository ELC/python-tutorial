"""This is the main module of the application (Docstring)"""

print("I was invoked directly or indirectly.")


if __name__ == "__main__":
    print("I was invoked directly")


if __name__ != "__main__":
    print("I was invoked indirectly (via an import)")

    from pathlib import Path

    print(f"You successfully imported {Path(__file__).parts[-1]}")

    name = "main"
