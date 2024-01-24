"""A year is a leap year if the following conditions are satisfied: 
The year is multiple of 400.
The year is a multiple of 4 and not a multiple of 100.
"""
# Inputs a year
# Outputs yes or true if is a leap year and no or false if not.


def is_leap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("The year you entered is a leap year!")
    else:
        print("The year you entered is not a leap year!")


check_year = int(input("Enter year to determine if it is a leap year: "))

is_leap(check_year)
