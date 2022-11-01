x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;

# kod jest składniowo poprawny chociaż w pythonie zwykle nie używa się średników

# ==============================================================================================================

for i in "axby": if ord(i) < 100: print (i)

# kod nie uruchomi się ponieważ instrukcje w jednym wierszy nie mogą pojawić się dwie instrukcje złożone

# ==============================================================================================================

for i in "axby": print (ord(i) if ord(i) < 100 else i)

# mimo że w jednej lini znajdują się dwie instrukcje złożone to kod się uruchomi ponieważ druga instrukcja jest
# w nawiasie

