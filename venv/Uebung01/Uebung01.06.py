
geburtsjahr = 0
while geburtsjahr > 2015 or geburtsjahr < 1582:
    geburtsjahr = int(input("Gib bitte ein Geburtsjahr ein "))
    if geburtsjahr > 2015 or geburtsjahr < 1582:
        print("Das Geburtsjahr", geburtsjahr,"ist nicht valide (1582 -2015)!")
