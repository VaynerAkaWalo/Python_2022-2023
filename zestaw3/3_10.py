roman = input("Podaj liczbe rzymską: ")

romandict = {
    "M": 1000,
    "D": 500,
    "C": 100,
    "L": 50,
    "X": 10,
    "V": 5,
    "I": 1
}

def roman2int(romanNumber):
    number = 0
    for x in range(len(romanNumber)):
        if x > 0 and romandict[romanNumber[x]] > romandict[romanNumber[x - 1]]:
            number += romandict[romanNumber[x]] - 2 * romandict[romanNumber[x - 1]]
        else:
            number += romandict[romanNumber[x]]

    return number
    

print(roman2int(roman))