"""A function to check if a given list is sorted"""


def is_sorted(lst):
    # enumerate(lst[:-1]) allows iterating over
    # the list lst excluding the last element,
    # as we're comparing each element with the next one.
    # Within the loop, index holds the index of current element,
    # and value holds the value of the current element.
    for index, value in enumerate(lst[:-1]):
        if value > lst[index + 1]:
            return False
    return True


# Example usage:
my_list = [1, 2, 3, 4, 5]
print(is_sorted(my_list))  # Output: True

my_list = [5, 4, 3, 2, 1]
print(is_sorted(my_list))  # Output: False
