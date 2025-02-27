import unittest
from main import *


class Test(unittest.TestCase):
    def test_multiply(self):
        """Test multiply function"""
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self):
        """Test divide function"""
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(5, 1), 5)
        self.assertAlmostEqual(divide(1, 3), 0.3333, places=4)

        # Test division by zero
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

    def test_sqrt(self):
        """Test sqrt function"""
        self.assertEqual(sqrt(4), 2)
        self.assertEqual(sqrt(9), 3)
        self.assertAlmostEqual(sqrt(2), 1.4142, places=4)

        # Edge case: negative numbers should raise an error
        with self.assertRaises(ValueError):
            sqrt(-1)


if __name__ == '__main__':
    unittest.main()