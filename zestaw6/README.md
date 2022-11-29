# Zadania
### OBOWIĄZKOWE DO PRZESŁANIA: dwa dowolne zadania z zestawu, z wyjątkiem 6.1.

### ZADANIE 6.2 (KLASA POINT)
W pliku points.py zdefiniować klasę Point wraz z potrzebnymi metodami. Punkty są traktowane jak wektory zaczepione w początku układu współrzędnych, o końcu w położeniu (x, y). Napisać kod testujący moduł points.

```python

class Point:
"""Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self): pass         # zwraca string "(x, y)"

    def __repr__(self): pass        # zwraca string "Point(x, y)"

    def __eq__(self, other): pass   # obsługa point1 == point2

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other): pass  # v1 + v2

    def __sub__(self, other): pass  # v1 - v2

    def __mul__(self, other): pass  # v1 * v2, iloczyn skalarny, zwraca liczbę

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self): pass          # długość wektora

    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points

# Kod testujący moduł.

import unittest

class TestPoint(unittest.TestCase): pass

```

### ZADANIE 6.3 (KLASA RECTANGLE)
W pliku rectangles.py zdefiniować klasę Rectangle wraz z potrzebnymi metodami. Prostokąt jest określony przez podanie dwóch wierzchołków, lewego dolnego i prawego górnego. Napisać kod testujący moduł rectangles.

```python
from points import Point

class Rectangle:
"""Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self): pass         # "[(x1, y1), (x2, y2)]"

    def __repr__(self): pass        # "Rectangle(x1, y1, x2, y2)"

    def __eq__(self, other): pass   # obsługa rect1 == rect2

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self): pass          # zwraca środek prostokąta

    def area(self): pass            # pole powierzchni

    def move(self, x, y): pass      # przesunięcie o (x, y)

# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase): pass
```