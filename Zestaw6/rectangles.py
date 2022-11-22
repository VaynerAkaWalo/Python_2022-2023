from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        return ("[" + str(self.pt1) + ", " + str(self.pt2) + "]")

    def __repr__(self):
        return ("Rectangle" + str(self))

    def __eq__(self, other):
        if(self.pt1 == other.pt1 and self.pt2 == other.pt2):
            return 1
        return 0

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):
        return Point((self.pt1 + self.pt2).x / 2, (self.pt1 + self.pt2).y / 2)

    def area(self):
        return abs(self.pt2.x - self.pt1.x) * abs(self.pt2.y - self.pt1.y)

    def move(self, x, y):
        self.pt1 = self.pt1 + Point(x, y)
        self.pt2 = self.pt2 + Point(x, y)
