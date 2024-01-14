# Going to do a list sum with recursion just because I like recursion
# Find sum of all elements in a list
# Inputs list, size of list, outputs sum of list
list_of_elements = [1, 2, 3, 4, 5, 6, 20, 88]


# Recursive function
def sum_of_list(list, size):
    # Check for empty list
    if size == 0:
        return 0
    else:
        return list[size - 1] + sum_of_list(list, size - 1)


# Driver code
total = sum_of_list(list_of_elements, len(list_of_elements))
# Result
print("Sum of all elements in given list: ", total)
