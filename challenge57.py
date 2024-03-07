"""A function that returns the key with the maximum value in a dictionary."""

import unittest


def get_max_value_key(dict1):
    """Input dictionary
    Output - key with maximum value
    """
    if not dict1:
        return None
    max_key = None
    max_value = float("-inf")
    for key, value in dict1.items():
        # If the value is greater than max_value,

        if value > max_value:
            # Update max_value to the current value and max_key to the current key.
            max_key = key
            max_value = value

    return max_key


class TestGetMaxValueKey(unittest.TestCase):
    """Test Class"""

    def test_max_value_key(self):
        """Test Function"""
        # Test case where dictionary is not empty
        d1 = {"a": 10, "b": 20, "c": 30}
        self.assertEqual(get_max_value_key(d1), "c")

        # Test case where dictionary is empty
        d2 = {}
        self.assertIsNone(get_max_value_key(d2))


if __name__ == "__main__":
    unittest.main()
