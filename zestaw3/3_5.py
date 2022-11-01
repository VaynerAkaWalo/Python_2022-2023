string = input("Podaj długość linijki: ")

number = int(string)

top = "|"
bot = "0"

for x in range(1, number + 1):
    top += "....|"
    bot += "{:5d}".format(x)

print(top + "\n" + bot)
