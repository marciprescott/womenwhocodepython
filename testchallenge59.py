import unittest
from challenge59 import is_perfect_square


class TestPerfectSquare(unittest.TestCase):
    def test_perfect_square(self):
        self.assertTrue(is_perfect_square(0))
        self.assertTrue(is_perfect_square(1))
        self.assertTrue(is_perfect_square(4))
        self.assertTrue(is_perfect_square(9))
        self.assertTrue(is_perfect_square(16))
        self.assertFalse(is_perfect_square(2))
        self.assertFalse(is_perfect_square(3))
        self.assertFalse(is_perfect_square(5))
        self.assertFalse(is_perfect_square(6))
        self.assertFalse(is_perfect_square(7))
        self.assertFalse(is_perfect_square(8))


if __name__ == "__main__":
    unittest.main()
