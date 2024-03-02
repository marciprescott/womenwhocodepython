""""A program that counts the occurrences of each word in a text file"""

from collections import defaultdict


def find_word_count():
    counter = {}
    # Open text file
    with open("willowtheking.txt") as file:

        for line in file:
            # Convert characters to lower case and eliminate any punctuation
            for words in line.split():
                words = words.lower()
            words = words.replace(",", " ")
            words = words.replace("!", " ")
            words = words.replace(":", " ")
            words = words.replace("?", " ")
            words = words.replace(".", " ")
            words = words.replace("'", " ")
            counter[words] = counter.get(words, 0) + 1
            word_count = len(counter)

        return counter


result = find_word_count()
print("Individual word counts are as follows: \n ", result)
