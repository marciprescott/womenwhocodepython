"""A program that finds the intersection and union of two sets"""


# Contains all the elements that are common to both sets
def get_intersection(set1, set2):
    return set1.intersection(set2)


# Returns a new set that contains all the items from the original set
def get_union(set1, set2):
    return set1.union(set2)


set1 = {1, 2, 3, 4, 5}  # Returns {4, 5}
set2 = {4, 5, 6, 7, 8}  # Returns {1, 2, 3, 4, 5, 6, 7, 8}
print(get_intersection(set1, set2))
print(get_union(set1, set2))
