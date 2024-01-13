# Initialize count to zero
count = 0
# List of vowels
vowel_list = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
# Get string input
given_string = input("Enter string to evaluate: ")
# Loop through string and count vowels
for letter in given_string:
    if letter in vowel_list:
        count += 1
print("Number of vowels in string is: ", count)
