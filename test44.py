import unittest
from unittest.mock import patch
from io import StringIO


def get_integer(prompt, error_message):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(error_message)


class TestGetInteger(unittest.TestCase):
    def test_valid_input(self):
        # Simulate user input of a valid integer
        user_input = "42\n"  # Simulate user entering "42"
        expected_output = 42

        # Capture stdout to test printed output
        with patch("sys.stdout", new=StringIO()) as fake_out:
            # Simulate user input
            with patch("builtins.input", return_value=user_input):
                result = get_integer(
                    "Please enter an integer: ", "entry must be an integer"
                )

        # Assert that printed output is empty
        self.assertEqual(fake_out.getvalue().strip(), "")

        # Assert that the function returned the expected integer
        self.assertEqual(result, expected_output)

    def test_invalid_input(self):
        # Simulate user input of a non-integer
        user_input = "not_an_integer\n"  # Simulate user entering "not_an_integer"
        error_message = "entry must be an integer"

        # Capture stdout to test printed output
        with patch("sys.stdout", new=StringIO()) as fake_out:
            # Simulate user input
            with patch("builtins.input", side_effect=[user_input, "42\n"]):
                result = get_integer("Please enter an integer: ", error_message)

        # Assert that error message is printed
        self.assertIn(error_message, fake_out.getvalue().strip())

        # Assert that the function eventually returns the valid integer after invalid input
        self.assertEqual(result, 42)


if __name__ == "__main__":
    unittest.main()
