"""A program that removes the nth element from a list."""

# Create a variable to store the input list
# Enter the index at which the list item is stored
# Pop the element using .pop
# Print new list
"""Delete nth element from a list using pop"""

list_input = ["bananas", " monkeys", "apples", "gorilla", "pandas"]
element_to_remove = int(input("Enter integer number of element to remove: "))
element_we_popped = list_input.pop(element_to_remove)
print(f"We removed {element_we_popped} from the list & the new list is {list_input}")

"""Delete using slicing """
# Create a variable to store the input list
# Store the list elements before the given index and after the given index
# using slicing which means it removes the item at the given index.
# Print new list after deletion


def remove_element(lst, nth_element):
    new_list = input_list[:nth_element] + input_list[nth_element + 1 :]
    return new_list


input_list = ["Welcome", "to", "my", "solution", "it", "was", "hard", "easy"]
nth_element = int(input("Enter element number to remove from list: "))
print(remove_element(input_list, nth_element))
