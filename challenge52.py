"""A program that checks if a string is a palindrome"""


# Using extended slice
def is_palindrome(string1):
    reversed_string = string1[::-1]
    if string1 == reversed_string:
        return True
    else:
        return False


string_to_check = "level"
print(is_palindrome(string_to_check))


# Using stack (yikes)
# Function to create empty stack and intit to 0.
def create_stack():
    stack = []
    return stack


# Function to determine size of stack.
def size(stack):
    return len(stack)


# Stack is empty if size is 0.
def is_empty(stack):
    if size(stack) == 0:
        return True


# Function to add item from stack increases size by 1.
def push(stack, item):
    stack.append(item)


# Function to remove item from stack decreases size by 1.
def pop(stack):
    if is_empty(stack):
        return
    return stack.pop()


# Stack based function to reverse a string.
def reverse(string):
    n = len(string)
    # Create an empty stack.
    stack = create_stack()
    # Push all characters of string to stack
    for i in range(0, n, 1):
        push(stack, string[i])
    # Make the string empty as all chars are saved in stack
    string = ""

    # Pop all chars of string and put them back into string
    for i in range(0, n, 1):
        string += pop(stack)
    return string


s = "Duffy the Airedale"
print("The original string is: ", end="")
print(s)
print("Reversed string is: ", end="")
print(reverse(s))  # Prints eladeriA eht yffuD


class Stack:
    def __init__(self):
        self.items = []

    # Add chars to stack.
    def push(self, item):
        self.items.append(item)

    # Remove chars from the stack LIFO
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    # If is empty we are done!
    def is_empty(self):
        return len(self.items) == 0


def reverse_string(input_string):
    stack = Stack()
    reversed_string = ""
    # Push each character of the input string onto the stack.
    for char in input_string:
        stack.push(char)

    while not stack.is_empty():
        # Calling pop so last char is first out making revesersed string.
        reversed_string += stack.pop()
    return reversed_string


input_string = "Vanderpump Rules"
reversed_string = reverse_string(input_string)
print("Reversed string: ", reversed_string)  # Returns seluR pmuprednaV
