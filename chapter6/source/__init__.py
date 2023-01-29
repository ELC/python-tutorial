"""In this module you can find the main source code of the application"""

print("This message will be executed before the imports of this module")

names = ["sheet", "speaker", "computer", "cup", "bottle", "cellular"]
prices = [10.25, 5.258, 350.159, 25.99, 18.759, 215.231]

items = {name: price for name, price in zip(names, prices)}
