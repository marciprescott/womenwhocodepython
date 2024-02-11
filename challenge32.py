"""A function that calculates the average of a list of numbers"""

from challenge29 import *


def calculate_average(l):
    average = sum(list_of_nums) / len(list_of_nums)
    return average


# Used day 29 challenge to generate list of random numbers
list_of_nums = random_integers(start_num, end_num, num)
print("The first list of random numbers is: ", list_of_nums)
average = float(calculate_average(list_of_nums))
print("The average of the first list using sum and len is: {:.2f}".format(average))


# Calculate with for loops instead of sum and len
def get_average(l):
    sum = 0
    length = 0
    for num in list2:
        sum += num
    for num in list2:
        length += 1
    average = sum / length
    return average


# Used day 29 function to generate list of random numbers
list2 = random_integers(start_num, end_num, num)
print("The second list of random numbers is: ", list2)
value = get_average(list2)
print("The average of the second list using a for loop is: {:.2f}".format(value))
