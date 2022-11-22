from rectangles import Rectangle
from points import Point
import unittest


class TestRectangle(unittest.TestCase):

    def testStr(self):
        self.assertEqual(str(Rectangle(1, 1, 3, 2)), "[(1, 1), (3, 2)]")

    def testRepr(self):
        self.assertEqual(repr(Rectangle(1, 1, 3, 2)), "Rectangle[(1, 1), (3, 2)]")

    def testEq(self):
        self.assertEqual(Rectangle(1, 1, 3, 2), Rectangle(1, 1, 3, 2))
        self.assertEqual(Rectangle(3, 2, 1, 1), Rectangle(3, 2, 1, 1))

    def testNe(self):
        self.assertNotEqual(Rectangle(1, 1, 3, 2), Rectangle(3, 2, 1, 1))

    def testCent(self):
        self.assertEqual(Rectangle(1, 1, 3, 2).center(), Point(2, 1.5))

    def testArea(self):
        self.assertEqual(Rectangle(1, 1, 3, 2).area(), 2)

    def testMove(self):
        rec = Rectangle(1, 1, 3, 2)
        rec.move(2, 3)
        self.assertEqual(rec, Rectangle(3, 4, 5, 5))

if __name__ == '__main__':
    unittest.main()