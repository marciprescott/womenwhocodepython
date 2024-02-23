"""A program that reads an integer from the user and handles invalid inputs"""


def get_integer(prompt, error_message):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(error_message)


print(
    get_integer(
        prompt="Please enter an integer: ", error_message="entry must be an integer"
    )
)
