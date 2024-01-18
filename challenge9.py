# Write a program to check if a number is even or odd
# Inputs a number to process
# Outputs positive or negative
num = int(input("Enter number to process: "))


def is_even_or_odd(num):
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")


is_even_or_odd(num)
