"""A program that capitalizes the first letter of each word in a sentence"""


def capitalize_first_letter(sentence):
    processed = sentence.title()

    return processed


sentence = input("Enter a sentence for processing: ")
print(capitalize_first_letter(sentence))
