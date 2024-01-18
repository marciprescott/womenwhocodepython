# Write a function that accepts a string and calculates the number of uppercase and lowercase letters in it.


# Initialize upper, lower to zero
str = input("Enter string to evaluate: ")
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = "abcdefghijklmnopqrstuvwxyz"

upper = 0
lower = 0
for i in str:
    if i in upper_case:
        upper += 1
    elif i in lower_case:
        lower += 1


print("The string you entered has {} uppercase letters".format(upper))
print("The string you entered has {} lowercase letters".format(lower))
