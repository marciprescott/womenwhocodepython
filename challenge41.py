"Program to print all permutations using recursion"


def permutation(lst):
    # If the list is empty then there are no perms so return empty list
    if len(lst) == 0:
        return []
    # If there is only one element then return the list
    if len(lst) == 1:
        return [lst]

    # Find the permutations for the first char if there are more than 1
    # Empty list that will store current perm
    arr = []
    # Iterate the input list and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]
        # print m
        remaining_list = lst[:i] + lst[i + 1 :]
        for perm in permutation(remaining_list):
            arr.append([m] + perm)
    return arr


data = list("ABCDE")
for p in permutation(data):
    print(p)
