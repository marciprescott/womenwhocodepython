""" A program that uses a lambda function to square each element of a list """

square_element = lambda x: x**2

numbers = [8, 9, 5, 66, 2, 4]
squared_numbers = list(map(square_element, numbers))

# Ouputs  -- Origianl list:  [8, 9, 5, 66, 2, 4]
print("Origianl list: ", numbers)
# Outputs  -- Squared list:  [64, 81, 25, 4356, 4, 16]
print("Squared list: ", squared_numbers)
