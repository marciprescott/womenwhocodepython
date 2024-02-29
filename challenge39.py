# Take the content of the file as input.
# Save each word in a list after removing spaces and punctuation from the input string.
# Find the frequency of each word.
# Print the word which has a maximum frequency.
""" A program to find the most common (10) words in a text file"""

# Take the content of the file as input.
text = open("frank.txt", "r")
words = dict()
# Save each word in a list after
# removing spaces and punctuation
# from the input string.
for line in text:
    line_words = (
        line.lower()
        .replace(",", "")
        .replace(";", "")
        .replace(".", "")
        .replace("?", "")
        .replace("-", "")
        .replace("!", "")
        .replace('"', "")
        .split(" ")
    )
    # Iterate over each word in line
    for word in line_words:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

max_num = 0
most_common_word = ""
for key, value in words.items():
    if value > max_num:
        max_num = value
        most_common_word = key
    x = words.items()
print(x)
print("The most common word is: ", most_common_word)
print("With a count of: ", max_num)
"""Outputs: """