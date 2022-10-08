
zeichen = input("Gib bitte eine Zeichenfolge ein ")
umfang = 'kurz' if len(zeichen) <= 10 else 'lang'
if len(zeichen) < 3:
    print("Eine sehr kurze Zeichenkette!")
elif len(zeichen) > 10:
    print("Die Zeichenkette hat mehr als 10 Zeichen")
else:
    print("Die Zeichenkette hat mindestens 3 Zeichen")
print("Die eingegebene Zeichenfolge war", umfang)