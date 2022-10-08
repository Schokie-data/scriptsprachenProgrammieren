import math

liste = []
n = 0
while n < 3:
    n += 1
    text =  'Bitte ' + str(n) + '. Zahl eingeben: '
    i = int(input(text))
    if i < 0:
        break
    liste += i,
else:
    for i in liste:
        print(i,":",math.sqrt(i))


