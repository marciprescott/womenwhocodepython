"""A function to find the largest common  divisor of two numbers using a function"""


def gcd(a, b):
    """
    Function to find the greatest common divisor (gcd) of two numbers using the Euclidean algorithm.

    Args:
        a (int): First number.
        b (int): Second number.

    Returns:
        int: The largest common divisor of the input numbers.
    """
    while b:
        # Swap the values of a & b,calculate the remainder of a divided by b.
        a, b = b, a % b
    # When b becomes zero, the gcd is found, so return a.
    return a


num1 = 112
num2 = 1084
print("the gretest common divisor  of ", num1, "and", num2, "is", gcd(num1, num2))
