# Write a program to print the multiplication table of a given number.
# Inputs- a number
# Outputs a  multiplication table of a given number.


def print_mulitplication_table(number):
    try:
        number = int(number)  # Convert input to integer
        print(f"Multiplication Table for {number}:")
        # Iterate from 1 to 10 to print the table
        for i in range(1, 11):
            result = number * i
            print(f"{number} x {i} = {result}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


# Taking user input and printing the multiplication table.
user_input = input("Enter a number: ")

# Call the funtion with user input.
print_mulitplication_table(user_input)
