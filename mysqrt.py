# ALDA Blatt 1: Aufgabe 3

import math

# Funktion 1 mit if/else implementieren
def mysqrt1(number):
    if number < 0:
        print("mysqrt() funktioniert nicht für negative Zahlen, du Dussel!")
    else:
        return math.sqrt(number)

# Funktion 2 mit try/except implementieren
def mysqrt2(number):
    try:
        return math.sqrt(number)
    except ValueError:
        print("mysqrt() funktioniert nicht für negative Zahlen, du Dussel!")

# Funktionen aufrufen

print(mysqrt1(9))
print(mysqrt1(-4))

print(mysqrt2(9))
print(mysqrt2(-4))
