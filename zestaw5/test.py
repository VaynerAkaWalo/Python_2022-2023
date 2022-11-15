import unittest
from fracs import *

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1, 4]), [1, 8])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 4]), [2, 1])

    def test_is_positive(self):
        self.assertEqual(is_positive([1, -3]), False)
        self.assertEqual(is_positive([-1, 3]), False)
        self.assertEqual(is_positive([1, 3]), True)
        self.assertEqual(is_positive([-1, -3]), True)

    def test_is_zero(self):
        self.assertEqual(is_zero([0, 5]), True)
        self.assertEqual(is_zero([1, 5]), False)

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [1, 4]), 1)
        self.assertEqual(cmp_frac([1, -2], [1, 4]), False)
        self.assertEqual(cmp_frac([1, -2], [-1, 2]), 0)

    def test_frac2float(self):
        self.assertEqual(frac2float([2, 5]), 0.4)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
