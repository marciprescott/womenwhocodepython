"""A function that takes a string and returns the reverse of each word"""


def reverse_words(s):
    # Empty list to store chars that are popped
    words = str.split(s)
    stack = []
    reversed_words = ""
    for word in words:
        stack.append(word)
        print(stack)
        # Now an empty string to store the words we are popping next to reverse the string
        # While the stack still has words
    while stack:
        reversed_words += stack.pop() + " "
        print(reverse_words)
    return reversed_words


original_str = "Hello Duffy"
reversed = reverse_words(original_str)
print(reversed)  # prints Duffy Hello
# Unfortunately this doesn't solve the leetcode
# because of the space, it provides a space at the end between the last word and "

# Try with reversed
"""To reverse the words in a sentence while 
preserving the spaces between them, you can split the 
sentence into words, reverse the order of the words, 
and then join them back together with spaces. """


def reverseWords(s):
    words = sentence.split()  # Split the sentence into words
    reversed_words = words[::-1]  # Reverse the order of words
    reversed_sentence = " ".join(reversed_words)
    return reversed_sentence


print(reverse_words("The sky is blue"))  # Prints "blue is sky The"
