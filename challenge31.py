"""A program that checks if a given string is a valid email address."""

import re


def valid_email(email):
    """This pattern will match any string that contains
    one or more characters that are not an @ symbol,
    followed by an @ symbol, followed by one or more characters
    that are not an @ symbol,
    followed by a period, followed by one or more characters
    that are not an @ symbol."""
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    return False


email = input("Enter email address to verify: ")
if valid_email(email):
    print("Valid email Address")
else:
    print("Invalid email address")
