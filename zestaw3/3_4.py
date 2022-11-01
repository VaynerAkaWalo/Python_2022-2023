import sys

while True:
    string = input("Jeżeli chcesz zakończyć wpisz stop w przeciwnym wypadku podaj liczbę: ")
    if string.lower() == "stop":
        sys.exit(0)
    try:
        number = float(string)
        print("Twoja liczba: " + str(number) + ", trzecia potęga: " + str(number ** 3))
    except:
        print("Wprowadzono niepoprawne dane spróbuj jeszcze raz")
