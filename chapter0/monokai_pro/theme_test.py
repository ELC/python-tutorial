a_variable = 100

hex(10)
int("0xa", 16)

def multiply(x: float, y: float) -> float: # Comment
    return x * y


if a_variable % 2 == 0:
    print("Value is even")
elif a_variable < 0:
    print("The value is odd and negative.")
elif a_variable > 100:
    print("The value is odd and greater than 100.")
else:
    print("The value does not meet the conditions.")

names = ["John", "Peter", "Mary"]
ages = [60, 15, 84]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

class Rectangle:
    def __init__(self, base: float, height: float) -> None:
        self.base: float = base
        self.height: float = height

    def area(self) -> float:
        return self.base * self.height

rec = Rectangle(10, 10)
rec.base
rec.area()
