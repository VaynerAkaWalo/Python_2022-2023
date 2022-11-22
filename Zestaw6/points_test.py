import unittest
from points import *

class TestPoint(unittest.TestCase):

    def testStr(self):
        self.assertEqual(str(Point(1,2)), "(1, 2)")
        self.assertEqual(str(Point(5,4)), "(5, 4)")

    def testRepr(self):
        self.assertEqual(repr(Point(1,2)), "Point(1, 2)")
        self.assertEqual(repr(Point(5,4)), "Point(5, 4)")

    def testEq(self):
        self.assertEqual(Point(1, 2), Point(1, 2))
        self.assertEqual(Point(1, 3), Point(1, 3))

    def testNe(self):
        self.assertNotEqual(Point(1, 2), Point(-1, 2))
        self.assertNotEqual(Point(1, 2), Point(-1, 3))

    def testSum(self):
        self.assertEqual(Point(1, 2) + Point(1, 2), Point(2, 4))
        self.assertEqual(Point(3, 2) + Point(1, 3), Point(4, 5))

    def testSub(self):
        self.assertEqual(Point(5, 4) - Point(1, 2), Point(4, 2))
        self.assertEqual(Point(3, 2) - Point(5, 3), Point(-2, -1))

    def testMul(self):
        self.assertEqual(Point(2, 3) * Point(4, 5), 23)
        self.assertEqual(Point(-2, -4) * Point(2, 3), -16)

    def testCross(self):
        self.assertEqual(Point(2, 3).cross(Point(4, 5)), -2)
        self.assertEqual(Point(-2, 4).cross(Point(2, 3)), -14)

    def testLen(self):
        self.assertEqual(Point(3, 4).length(), 5)

if __name__ == '__main__':
    unittest.main()