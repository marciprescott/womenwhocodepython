# Write a program to count the occurrences of a specific character in a string
# Inputs - a string
# Outputs - number of occurences of specific char

# Get user input & test
string = input("Enter string to process: ")

char = input("Enter character to tabulate: ")


def count_character(string, char):
    count = 0

    for character in string:
        if character == char:
            count += 1
    return count


print(count_character(string, char))
