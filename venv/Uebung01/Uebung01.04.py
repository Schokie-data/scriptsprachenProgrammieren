
zeichen = input("Gib bitte eine Zeichenfolge ein ")
if len(zeichen) < 3:
    print("Eine sehr kurze Zeichenkette!")
elif len(zeichen) > 10:
    print("Die Zeichenkette hat mehr als 10 Zeichen")
else:
    print("Die Zeichenkette hat zwischen 3 und 10 Zeichen")
print("Die eingegebene Zeichenfolge war", len(zeichen), "Zeichen lang")