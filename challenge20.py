""" A function that takes a list of numbers and returns a new list containing only the even numbers"""
# Inputs a list of numbers, outputs a list of even numbers

list_of_nums = [5, 6, 7, 9, 10, 23, 24, 50, 55, 99, 101, 102, 98, 106]
list_of_even_nums = []

for i in list_of_nums:
    if i % 2 == 0:
        list_of_even_nums.append(i)
print("The even numbers in the list are:\n ", list_of_even_nums)
