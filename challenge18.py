# Create a program to find the largest among three numbers.
# Create a program to find the largest among three numbers.


def greatest_of_three(x, y, z):
    return max(x, y, z)


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

print("The biggest number is: ", max(x, y, z))
