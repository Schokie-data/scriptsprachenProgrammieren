
geburtsjahr = 0
while geburtsjahr > 2015 or geburtsjahr < 1582:
    geburtsjahr = int(input("Gib bitte ein Geburtsjahr ein "))
    if geburtsjahr == 0:
        print("Durch die 0 wurde die Eingabe beendet")
        break
    elif geburtsjahr == 1:
        continue
    if geburtsjahr > 2015 or geburtsjahr < 1582:
        print("Das Geburtsjahr", geburtsjahr,"ist nicht valide (1582 -2015)!")

else:
    if (geburtsjahr % 4 == 0 and geburtsjahr % 100 != 0) or (geburtsjahr % 400 == 0):
        print("Das Geburtsjahr", geburtsjahr,"ist ein Schaltjahr!")
    else:
        print("Das Geburtsjahr", geburtsjahr,"ist kein Schaltjahr!")