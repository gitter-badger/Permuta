import unittest
from permuta.math import factorial, binomial

class TestMathCounting(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(9), 362880)
        self.assertEqual(factorial(10), 3628800)

    def test_binomial(self):
        self.assertEqual(binomial(0,0), 1)
        self.assertEqual(binomial(0,1), 0)
        self.assertEqual(binomial(120,1231), 0)
        self.assertEqual(binomial(10, 3), 120)
        self.assertEqual(binomial(10, 1), 10)
        self.assertEqual(binomial(1243, 10), 2339835883576802918726133)
        self.assertEqual(binomial(1243, 20), 27325212682042866855639367404897873973276230)

