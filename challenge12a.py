""" The The string is passed as an argument to a recursive 
function to reverse the string. 
In the function, the base condition is that if the length of the string 
is equal to 0 there is nothing left to process.
If not equal to 0, the reverse function is recursively called to slice the 
part of the string except the first character and add the first 
character to the end of the sliced string."""


def reverse_string(s):
    # Base case.
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]


s = input("Enter a string to reverse: ")
print("The reversed string (using recursion) is: ", end="")
print(reverse_string(s))
