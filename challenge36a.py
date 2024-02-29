import unittest


class TestPrime(unittest.TestCase):
    def test_is_prime(self):
        num = int(input("Enter a number: "))
        self.assertTrue(
            num == 0
            or num % 2 == 0
            or num % 3 == 0
            or num % 5 == 0
            or num % 7 == 0
            or num % 9 == 0,
            f"{num} IS prime",
        )


if __name__ == "__main__":
    unittest.main()(edited)
