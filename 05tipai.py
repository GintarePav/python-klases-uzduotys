a = None
print(type(a))
print(a)

a = 5
print(type(a))
print(a)

a = 5.8
print(type(a))
print(a)

a = 1 + 1j
print(type(a))
print(a)

a = true
print(type(a))
print(a)

a = 'kazkas'
print(type(a))
print(a)

a = [8, 8.7, 9, true, 'tekstas', 8.7, 9] #list tipas, ne tas pats kas masybas, array
print(type(a))
print(a)

a = (8, 8.7, 9, true, 'tekstas', 8.7, 9) #griezta tvarka, nieko negalima keisti (en. tuple)
print(type(a))
print(a)

a = {8, 8.7, 9, true, 'tekstas', 8.7, 9} #aibe, nera pasikartojanciu elementu
print(type(a))
print(a)

a = {'sk1' : 5, 'sk2' : 8} #dictionary tipas
print(type(a))
print(a)

user = {'name': "Admim", "password": 000000, "license": false}