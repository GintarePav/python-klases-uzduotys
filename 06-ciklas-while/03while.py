# atsapusdinti skaicius nuo 1 iki n, jei n > 13, nespausdinti 13

n = int(input("n="))
ck = 1

while ck <= n:
    if ck == 13:
        continue
    print(ck, end=(' '))
    ck += 1
else: 
    print('Ciklas pilnai ivyko')
print('Programa baige darba')