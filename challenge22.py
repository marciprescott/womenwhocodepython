""" A program to find the second-largest element in a list."""


def second_largest(l):
    list1 = l.sort()
    list2 = l[-2]

    return list2


l = [9, 100, 2, 300, 250, 999, 1011, 2500, 9999, 10225, 987, 1245]
# print(second_largest(l))
print("the second largest element in the list is", second_largest(l))
