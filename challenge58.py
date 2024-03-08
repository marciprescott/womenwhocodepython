"""A program converts a string to an integer and handles ValueError"""

# Inputs a string
# Ouptus an integer and handles ValueErrors


def convert_to_integer(string):
    """Inputs: A string
    Outputs: An integer"""
    try:
        return int(string)
    except ValueError:
        print("You did not enter a number, please enter a number!")
    return


s = input("Enter a number: ")
result = convert_to_integer(s)
print(result)  # Prints None if ValueError
