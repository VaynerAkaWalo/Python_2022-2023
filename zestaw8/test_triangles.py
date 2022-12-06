import pytest
from triangles import Triangle
from points import Point

class TestTriangles:

    @pytest.fixture(scope="class")
    def triangleA(self):
        return Triangle(1, 2, 5, 2, 3, 7)

    @pytest.fixture(scope="class")
    def triangleB(self):
        return Triangle(0, 0, 4, 0, 2, 3)

    def testFromPoints(self, triangleA, triangleB):
        assert Triangle.from_points((Point(1, 2), Point(5, 2), Point(3, 7))) == triangleA
        assert Triangle.from_points((Point(0, 0), Point(4, 0), Point(2, 3))) == triangleB

    def testStr(self, triangleA):
        assert str(triangleA) == "[(1, 2), (5, 2), (3, 7)]"

    def testRepr(self, triangleA):
        assert repr(triangleA) == "Triangle(1, 2, 5, 2, 3, 7)"

    def testEq(self, triangleA):
        assert triangleA == Triangle(1, 2, 5, 2, 3, 7)

    def testNe(self, triangleA, triangleB):
        assert triangleA != triangleB

    def testCent(self):
        assert Triangle(0, 0, 4, 0, 2, 3).center == Point(2, 1)

    def testArea(self, triangleB):
        assert Triangle(0, 0, 0, 3, 4, 0).area() == 6

    def testMove(self, triangleA):
        assert triangleA.move(1, 2) == Triangle(2, 4, 6, 4, 4, 9)
        triangleA.move(-1, -2)

    def testMake4(self, triangleB):
        assert triangleB.make4() == \
               (Triangle(0, 0, 1.0, 1.5, 2.0, 0.0),
                Triangle(4, 0, 3.0, 1.5, 2.0, 0.0),
                Triangle(2, 3, 1.0, 1.5, 3.0, 1.5),
                Triangle(3.0, 1.5, 1.0, 1.5, 2.0, 0.0))


    def testRight(self, triangleA):
        assert triangleA.right == 5

    def testLeft(self, triangleA):
        assert triangleA.left == 1

    def testTop(self, triangleA):
        assert triangleA.top == 7

    def testBottom(self, triangleA):
        assert triangleA.bottom == 2

    def testWidth(self, triangleA):
        assert triangleA.width == 4

    def testHeight(self, triangleA):
        assert triangleA.height == 5

    def testTopRight(self, triangleA):
        assert triangleA.topright == Point(5, 7)

    def testTopLeft(self, triangleA):
        assert triangleA.topleft == Point(1, 7)

    def testBottomRight(self, triangleA):
        assert triangleA.bottomright == Point(5, 2)

    def testBottomLeft(self, triangleA):
        assert triangleA.bottomleft == Point(1, 2)