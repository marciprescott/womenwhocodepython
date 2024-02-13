import unittest
from challenge33 import is_prime


class TestIsPrime(unittest.TestCase):
    def test_prime_numbers(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        for num in primes:
            with self.subTest(num=num):
                self.assertTrue(is_prime(num), f"{num} is prime but not detected")

    def test_non_prime_numbers(self):
        non_primes = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]
        for num in non_primes:
            with self.subTest(num=num):
                self.assertFalse(is_prime(num), f"{num} is not prime but detected")

    def test_negative_numbers(self):
        self.assertFalse(is_prime(-1), "-1 is not prime but detected")
        self.assertFalse(is_prime(-2), "-2 is not prime but detected")

    def test_zero_and_one(self):
        self.assertFalse(is_prime(0), "0 is not prime but detected")
        self.assertFalse(is_prime(1), "1 is not prime but detected")


if __name__ == "__main__":
    unittest.main()
