import re


# Method one, using loop and conditionals
def remove_vowels(string):
    vowel_list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    result = ""
    for char in string_to_check:
        if char not in vowel_list:
            result += char
    return result


string_to_check = input("Enter string to remove values: ")
output_string = remove_vowels(string_to_check)
print(output_string)

# Finally using regular expressions because I haven't used them in a long while!


# Method two using list comprehension
def vowels_gone(string):

    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    result = "".join([char for char in string if char not in vowels])
    return result


input_string = input("Enter string to remove vowels from: ")
output_string = vowels_gone(input_string)
print(output_string)


def consonants_only(string):

    x = re.findall("[^aeiouAEIOU]", string)
    x = "".join(x)
    return x


string = input("Enter string to replace with consonants only:  ")
output_string = consonants_only(string)
print(output_string)
