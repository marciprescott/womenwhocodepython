""" A function that generates a random number between a given range. """

import random

# Given lower and upper limits from start to end and store in a list
# Using random.randrange


def random_integers(start_num, end_num, num):
    result = []
    for i in range(num):
        result.append(random.randint(start_num, end_num))
    return result


num = int(input("Enter the number of random numbers to generate: "))
start_num = int(input("Enter start of range: "))
end_num = int(input("Enter the end of range: "))
print(f"Random integers between {start_num} and {end_num}")
print(random_integers(start_num, end_num, num))
