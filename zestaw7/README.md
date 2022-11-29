# Zadania 
### OBOWIĄZKOWE DO PRZESŁANIA: zadanie 7.6 i jedno z 7.1-7.5.

### ZADANIE 7.4 (KLASA TRIANGLE)
W pliku triangles.py zdefiniować klasę Triangle wraz z potrzebnymi metodami. Wykorzystać wyjątek ValueError do obsługi błędów. Napisać kod testujący moduł triangles.
```python
from points import Point

class Triangle:
"""Klasa reprezentująca trójkąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        # Należy zabezpieczyć przed sytuacją, gdy punkty są współliniowe.
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

    def __str__(self): pass         # "[(x1, y1), (x2, y2), (x3, y3)]"

    def __repr__(self): pass        # "Triangle(x1, y1, x2, y2, x3, y3)"

    def __eq__(self, other): pass   # obsługa tr1 == tr2

    def __ne__(self, other):        # obsługa tr1 != tr2
        return not self == other

    def center(self): pass          # zwraca środek trójkąta

    def area(self): pass            # pole powierzchni

    def move(self, x, y): pass      # przesunięcie o (x, y)

    def make4(self): pass           # zwraca krotkę czterech mniejszych
#     A       po podziale    A
#    / \                    / \
#   /   \                  +---+
#  /     \                / \ / \
# C-------B              C---+---B

# Kod testujący moduł.

import unittest

class TestTriangle(unittest.TestCase): pass
```

### ZADANIE 7.6 (ITERATORY)
Stworzyć następujące iteratory nieskończone:
1. (a) zwracający 0, 1, 0, 1, 0, 1, ...,
2. (b) zwracający przypadkowo jedną wartość z ("N", "E", "S", "W") [błądzenie przypadkowe na sieci kwadratowej 2D],
3. (c) zwracający 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, ... [numery dni tygodnia].