""" A function to calculate the factorial of a number calculated using recursion."""


def fact(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)


number = int(input("Enter number to calculate factorial: "))
print("The result of calling factorial on the number ", number, "is", fact(number))
