wys = int(input("Podaj wysokość: "))
dlu = int(input("Podaj długość: "))

string = "\n"

for x in range(wys + 1):

    if x > 0:
        string += "|"
        for y in range(dlu):
            string += "   |"
        string += "\n"

    string += "+"
    for y in range(dlu):
        string += "---+"
    string += "\n"
    
print(string)