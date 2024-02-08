"""A program that removes the nth element from a list."""

# Create a variable to store the input list
# Enter the index at which the list item is stored
# Pop the element using .pop
# Print new list


list_input = ["bananas", " monkeys", "apples", "gorilla", "pandas"]
element_to_remove = int(input("Enter integer number of element to remove:"))
element_we_popped = list_input.pop(element_to_remove)
print(f"We removed {element_we_popped} from the list & the new list is {list_input}")
