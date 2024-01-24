def reverse_string(s):
    str = ""
    for i in s:
        # Here is the reversal because we are adding i + str, if we added str + i it would not be reversed
        str = i + str
    return str


s = input("Enter string to reverse: ")
# Use end="" to eliminate printing strings

print("The reversed string (using a for loop) is : ", end="")
print(reverse_string(s))
