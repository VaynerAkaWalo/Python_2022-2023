def make_ruler(number):
    top = "|"
    bot = "0"

    for x in range(1, number + 1):
        top += "....|"
        bot += "{:5d}".format(x)

    print(top + "\n" + bot)

def make_grid(dlu, wys):
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
