"""A function to check if a number is a prime number"""


def is_prime(number):
    # Check if the number is less than 2
    if number < 2:
        return False
    # Check if the number is divisible by any number other than 1 and itself
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


# Example usage:
print(is_prime(7))  # Output: True
print(is_prime(10))  # Output: False
