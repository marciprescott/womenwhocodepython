"""A program that checks to see if a number is prime."""

import math


def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


# Example usage
number = int(input("Enter number to test for prime: "))
if is_prime(number):
    print(f"{number} is prime")
else:
    print(f"{number} is not prime")
