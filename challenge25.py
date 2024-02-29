""" A program to concatenate two lists. """


# concatenate takes two lists as inputs and returns a concatenated list.
def concatenate(list_1, list2):
    return list_1 + list2


# List examples
ages = [19, 26, 29]
languages = ["Python", "Swift", "C++"]
# Call the function
print(concatenate(ages, languages)