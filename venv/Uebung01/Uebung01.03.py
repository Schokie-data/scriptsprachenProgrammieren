
zeichen = input('Gib bitte eine Zeichenfolge ein ')
if len(zeichen) < 3:
    print('Eine sehr kurze Zeichenkette!')
else:
    print('Die Zeichenkette hat mindestens 3 Zeichen')
print('Die eingegebene Zeichenfolge war', len(zeichen), 'Zeichen lang')