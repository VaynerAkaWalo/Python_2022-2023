# Zadania
### OBOWIĄZKOWE DO PRZESŁANIA: jedno zadanie

### ZADANIE 8.2 (KLASA TRIANGLE)
Wzbogacić klasę Triangle o nowe funkcjonalności (plik triangles.py).

Stworzyć metodę klasy o nazwie 'from_points', która pozwoli utworzyć trójkąt z listy lub krotki zawierającej trzy punkty. Wywołanie:
triangle = Triangle.from_points((point1, point2, point3))

Za pomocą dekoratora @property dodać atrybuty wirtualne zwracające liczbę (współrzędną): top, left, bottom, right, width, height. Dodać atrybuty wirtualne zwracające Point: topleft, bottomleft, topright, bottomright. Wymienione atrybuty wirtualne opisują prostokąt ograniczający dany trójkąt (bounding box). Można rozważyć zamianę metody center() na atrybut wirtualny.

W osobnym pliku (test_triangles.py) przygotować testy klasy Triangle w formacie dla modułu 'pytest'.