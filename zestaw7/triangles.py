from points import Point
import math

class Triangle:
    """Klasa reprezentująca trójkąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)
        l1 = self.pt1.distance(self.pt2)
        l2 = self.pt1.distance(self.pt3)
        l3 = self.pt2.distance(self.pt3)
        if l1 >= l2 + l3 or l2 >= l1 + l3 or l3 >= l1 + l2:
            raise ValueError("Nierówność trójkąta nie jest zachowana")

    def __str__(self):
        return f'[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y}), ({self.pt3.x}, {self.pt3.y})]'

    def __repr__(self):
        return f'Triangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y}, {self.pt3.x}, {self.pt3.y})'
    # "Triangle(x1, y1, x2, y2, x3, y3)"

    def __eq__(self, other):
        if self.pt1 == other.pt1 or self.pt1 == other.pt2 or self.pt1 == other.pt3:
            if self.pt2 == other.pt1 or self.pt2 == other.pt2 or self.pt2 == other.pt3:
                if self.pt3 == other.pt1 or self.pt3 == other.pt2 or self.pt3 == other.pt3:
                    return True
        return False

    def __ne__(self, other):        # obsługa tr1 != tr2
        return not self == other

    def center(self):
        return Point((self.pt1.x + self.pt2.x + self.pt3.x)/3, (self.pt1.y + self.pt2.y + self.pt3.y)/3)

    def area(self):
        l1 = self.pt1.distance(self.pt2)
        l2 = self.pt1.distance(self.pt3)
        l3 = self.pt2.distance(self.pt3)
        p = (l1 + l2 + l3)/2
        return math.sqrt(p*(p-l1)*(p-l2)*(p-l3))

    def move(self, x, y):
        point = Point(x, y)
        self.pt1 += point
        self.pt2 += point
        self.pt3 += point
        return self

    def make4(self):
        point12 = Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)
        point23 = Point((self.pt2.x + self.pt3.x) / 2, (self.pt2.y + self.pt3.y) / 2)
        point13 = Point((self.pt1.x + self.pt3.x) / 2, (self.pt1.y + self.pt3.y) / 2)
        return (Triangle(self.pt1.x, self.pt1.y, point13.x, point13.y, point12.x, point12.y),
                Triangle(self.pt2.x, self.pt2.y, point23.x, point23.y, point12.x, point12.y),
                Triangle(self.pt3.x, self.pt3.y, point13.x, point13.y, point23.x, point23.y),
                Triangle(point23.x, point23.y, point13.x, point13.y, point12.x, point12.y))
