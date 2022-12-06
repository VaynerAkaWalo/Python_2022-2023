import unittest
from triangles import Triangle
from points import Point


class TestRectangle(unittest.TestCase):
    def testStr(self):
        self.assertEqual(str(Triangle(1, 2, 5, 2, 3, 7)), "[(1, 2), (5, 2), (3, 7)]")

    def testRepr(self):
        self.assertEqual(repr(Triangle(1, 2, 5, 2, 3, 7)), "Triangle(1, 2, 5, 2, 3, 7)")

    def testEq(self):
        self.assertEqual(Triangle(1, 2, 5, 2, 3, 7), Triangle(1, 2, 5, 2, 3, 7))
        self.assertEqual(Triangle(1, 2, 5, 2, 3, 7), Triangle(5, 2, 3, 7, 1, 2))

    def testNe(self):
        self.assertNotEqual(Triangle(1, 2, 5, 2, 3, 7), Triangle(5, 2, 4, 7, 1, 2))

    def testCent(self):
        self.assertEqual(Triangle(0, 0, 4, 0, 2, 3).center(), Point(2, 1))

    def testArea(self):
        self.assertEqual(Triangle(0, 0, 0, 3, 4, 0).area(), 6)

    def testMove(self):
        self.assertEqual(Triangle(1, 2, 5, 2, 3, 7).move(1, 2), Triangle(2, 4, 6, 4, 4, 9))

    def testMake4(self):
        self.assertEqual(Triangle(0, 0, 0, 4, 2, 4).make4(), (
            Triangle(0, 0, 1.0, 2.0, 0.0, 2.0),
            Triangle(0, 4, 1.0, 4.0, 0.0, 2.0),
            Triangle(2, 4, 1.0, 2.0, 1.0, 4.0),
            Triangle(1.0, 4.0, 1.0, 2.0, 0.0, 2.0)))

if __name__ == '__main__':
    unittest.main()
