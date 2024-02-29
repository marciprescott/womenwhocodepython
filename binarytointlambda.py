from functools import reduce

binary = input("Enter a binary number: ")
decimal = reduce(lambda x, y: 2 * x + y, map(int, binary))
print("Decimal equivalent of ", binary, "is", decimal)
