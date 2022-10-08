# Initialisierung
import random

zahlvon = int(input("Die Gehemzahl befindet sich zwischen "))
zahlbis = int(input("und "))

#geheimzahl = random.randint(zahlvon, zahlbis)
geheimzahl = int(input("Geheimzahl "))

eingabe = 0
zaehler = 0

untereGrenze = zahlvon
obereGrenze = zahlbis

while eingabe != geheimzahl:

    eingabe = random.randint(untereGrenze, obereGrenze)

    if eingabe < geheimzahl:
        print("Zahl zu klein ")
        untereGrenze = eingabe +1
    elif eingabe > geheimzahl:
        print("Zahl zu groß ")
        obereGrenze = eingabe -1

    zaehler += 1

if eingabe == geheimzahl:
    print("Richtig! Sie haben", zaehler, "Versuche benötigt, um die Geheimzahl", geheimzahl, "zu erraten")
else:
    print("Die richtige Zahl war ", geheimzahl)