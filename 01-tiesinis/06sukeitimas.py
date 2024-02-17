a = 5
b = 8
print(f'a = {a}') # atitraukos yra tik logines, o ne sintakse

#1 budas
laikinas = a
a = b
b = laikinas
print(f'a = {a}')
print(f'a = {b}')

#2 budas
a, b = b, a # veikia tik python

#3 budas 
a = a + b # a = 13 (nes a = 5 + b = 8), b = 8
b = a - b # a = 13, b = 5
a = a - b # a = 8, b = 5
print(f'a = {a}')
print(f'a = {b}')