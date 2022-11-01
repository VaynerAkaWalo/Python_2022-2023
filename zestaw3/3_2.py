L = [3, 5, 4] ; L = L.sort()

# kod uruchomi się, ale instrukcje powinny być w osobnych liniach

# ==============================================================================================================

x, y = 1, 2, 3

# błąd - przypisanie 3 wartości do 2 zmiennych

# ==============================================================================================================
X = 1, 2, 3 ; X[1] = 4

# instrukcje powinny być w osobnych liniach, pierwsza instrukcja tworzy tuple natomiast druga próbuje ją modyfikować
# wartości w tuple są niemodyfikowalne

# ==============================================================================================================
X = [1, 2, 3] ; X[3] = 4

# druga instrukcja wychodzi poza indeks tablicy

# ==============================================================================================================
X = "abc" ; X.append("d")

# string nie wspiera append

# ==============================================================================================================
L = list(map(pow, range(8)))

# funkcja pow wymaga 2 argumentów

# ==============================================================================================================