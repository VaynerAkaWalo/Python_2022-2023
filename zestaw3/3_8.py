first = "89412ihjdsf1232dasdas"
second = "10948yrsaifhohfa9sj2-13"

string = "Wspólne znaki: " + str(set(first).intersection(second)) + "\nNiepowtarzające się elementy pierwszego zbioru " + str(set(first)) + ",\ndrugiego zbioru: " + str(set(second))

print(string)


