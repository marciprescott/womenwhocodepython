# Write a program to check if a number is positive, negative, or zero


def checkNumber(number):
    if number == 0:
        print("The number you entered is zero")
    elif number > 0:
        print("The number you entered is positive")
    else:
        print("The number you entered is negative")


number = int(input("Enter number to process: "))
checkNumber(number)
