import random
ikiKiek = int(input("Iki kiek generuosime? "))
atsitiktinis1 = random.randint(0, ikiKiek)
print(atsitiktinis1)

atsitiktinis2 = random.randint(-ikiKiek, ikiKiek)
print(atsitiktinis2)

atsitiktinis3 = random.randrange(1, ikiKiek, 3) # kas trecia: 1, 4 , 7, etc
print(atsitiktinis3)

atsitiktinis4 = random.random()
print(atsitiktinis4)
print(type(atsitiktinis4)) # kaip JS, nuo 0 iki 1
print(int(atsitiktinis4 * 100))

raide = random.choice(['A', 'B', 'C', 'D'])