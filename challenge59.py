import math


def is_perfect_square(num):
    if num < 0:
        return False

    # Get square root
    square_root = math.isqrt(num)

    # Check if the square root is equal to its integer value
    return square_root * square_root == num
    # Get number from user


try:
    number = int(input("Enter a number: "))
    if is_perfect_square(number):
        print(f"{number} is a perfect square.")
    else:
        print(f"{number} is not a perfect square.")
except ValueError:
    print("Invalid input, please enter a valid integer. ")
