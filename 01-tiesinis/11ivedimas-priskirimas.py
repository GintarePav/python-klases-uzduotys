a = 5
b = 5
c = 5
a = b = c = 5

a = 5
b = 15
c = 20
a, b, c = 5, 15, 20 #duomenu ispakavimas

a, b, c = input('ivesk tris skaicius, su kableliais').split(', ') #reikia split, nes gaunasi string
a = int(a)
b = int(b)
c = int(c)