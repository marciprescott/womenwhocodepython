""" A program to remove a specific element from a set."""


def remove_element(l, element):
    try:
        return l.remove(element_to_remove)

    except KeyError:
        print("You have entered an item that is not in the set")
        exit()


list_of_things = [
    "fork",
    "fork",
    "knife",
    "knife",
    "spoon",
    "plate",
    "spoon",
    "bowl",
    "plate",
]
list_of_things = set(list_of_things)
element_to_remove = input("Enter element from list to remove: ")

remove_element(list_of_things, element_to_remove)
print(
    "You have chosen to remove",
    element_to_remove,
    "fron the set. The new set is ",
    list_of_things,
    ".",
)
