""" A function that finds the second smallest element in a list."""

# def find_second_smalles(list_1):


# print(smallest_element)
def second_smallest(l):
    list1 = l.sort()
    list2 = l[1]

    return list2


list_1 = [5, 9, 7, 21, 16, 21, 3, 13, 7, 17, 13, 16, 20, 22, 3, 21, 19, 13, 19, 2]
print(second_smallest(list_1))
