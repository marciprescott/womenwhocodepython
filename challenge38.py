""" A program to flatten a nested list"""


def flatten_list(l):
    flat_list = []
    for row in l:
        flat_list += row
    return flat_list


list1 = [
    [9, 3, 8, 3],
    [4, 5, 2, 8],
    [6, 4, 3, 1],
    [1, 0, 4, 5],
]
# Driver Code
print(flatten_list(list1))
# Prints [9, 3, 8, 3, 4, 5, 2, 8, 6, 4, 3, 1, 1, 0, 4, 5]
