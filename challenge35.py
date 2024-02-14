"""A simple unit test for a function that adds two numbers"""

import unittest


def add_two_nums(x, y):
    return x + y


class TestAddNumbers(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add_two_nums(3, 5), 8)

    def test_add_negative_numbers(self):
        self.assertEqual(add_two_nums(-3, -5), -8)

    def test_add_positive_and_negative_numbers(self):
        self.assertEqual(add_two_nums(3, -5), -2)

    def test_add_positive_numbers(self):
        self.assertEqual(add_two_nums(8, 8), 16)


if __name__ == "__main__":
    unittest.main()
