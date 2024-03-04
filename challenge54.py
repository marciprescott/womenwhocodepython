"""A function to find all words in a sentence that start with a vowel"""

# Split the sentence
# Iterate through each word
# Check for vowels
# Collect words starting with vowels - list?
# Return result


def count_vowels(sentence):
    sentence = sentence.lower()
    words = sentence.split()
    word_count = 0
    starts_with_vowels = []
    for word in words:
        if (
            word[0] == "a"
            or word[0] == "e"
            or word[0] == "i"
            or word[0] == "o"
            or word[0] == "u"
        ):
            word_count += 1
            starts_with_vowels.append(word)
        else:
            continue
    return word_count, starts_with_vowels


sentence = input("Enter sentence to analyze: ")
result = count_vowels(sentence)
print("Count and list of words starting with vowels: ", result)
