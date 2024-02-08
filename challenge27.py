""" A program that sorts a list of strings alphabetically"""


def sort_strings(strings):
    sorted_strings = sorted(strings)
    return sorted_strings


strings = [
    "banana",
    "apple",
    "orange",
    "grape",
    "kiwi",
    "pineapple",
    "strawberry",
    "blueberry",
    "Watermelon",
    "peach",
    "mango",
    "cherry",
    "pear",
    "plum",
    "lemon",
]
new_sort = sort_strings(strings)
print(new_sort)
