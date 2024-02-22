"""A program that uses a try-except block to handle division by zero"""


def try_except(x, y):
    try:
        return a / b
    except ZeroDivisionError as e:
        print("Error: Cannot divide by zero")


a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

print(try_except(a, b))
