import math

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __repr__(self):
        return "Point(" + str(self.x) + ", " + str(self.y) + ")"

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return 1
        return 0

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def length(self):
        return math.sqrt(self.x**2 + self.y**2)

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __hash__(self):
        return hash((self.x, self.y))

