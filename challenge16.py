""" A function that counts the frequency of each word in a sentence"""


# Inputs a sentence, outputs a number representing the frequencey of each word in a sentence, using a dictionary for practice.
# A function that takes a string as its in;ut.
def word_counts(str):
    # Create a dictionary to store word counts.
    counts = dict()
    # Split the input string into a list of words using spaces as separators and store it in the 'words' list.
    words = str.split()
    # Iterate through words list.
    for word in words:
        if word in counts:
            # If the word is already in the dictionary increase count
            counts[word] += 1
        else:
            # The word isn't in dict so add word.
            counts[word] = 1
    return counts


# Driver code
print(
    word_counts(
        "apples, oranges, milk, oranges, bananas, milk, honey, honey, bread, spaghetti, butter, spaghetti, marinary sauce"
    )
)
