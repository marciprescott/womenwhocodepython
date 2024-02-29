import unittest
from challenge33 import is_this_prime


class TestIsThisPrime(unittest.TestCase):
    def test_prime_numbers(self):
        self.assertTrue(is_this_prime(2))
        self.assertTrue(is_this_prime(3))
        self.assertTrue(is_this_prime(5))
        self.assertTrue(is_this_prime(7))
        self.assertTrue(is_this_prime(11))
        self.assertTrue(is_this_prime(13))
        self.assertTrue(is_this_prime(17))
        self.assertTrue(is_this_prime(19))

    def test_non_prime_numbers(self):
        self.assertFalse(is_this_prime(1))
        self.assertFalse(is_this_prime(4))
        self.assertFalse(is_this_prime(6))
        self.assertFalse(is_this_prime(8))
        self.assertFalse(is_this_prime(9))
        self.assertFalse(is_this_prime(10))
        self.assertFalse(is_this_prime(12))
        self.assertFalse(is_this_prime(15))


if __name__ == "__main__":
    unittest.main()
