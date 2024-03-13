#Petriuko pazymiai - reikia apskaiciuoti vidurki

def ivedimas(nr):
    paz = int(input(f'Iveskite Petriuko {i}-aji pazymi: '))
    if 1<paz<=10:
        return paz
    else:
        return ivedimas(nr)

kiek = int(input("kiek Petriukas turi pazymiu? "))
suma = 0
for i in range(1, kiek+1):
    p = ivedimas(i)
    suma += p
        

vidurkis = suma / kiek
print(f'Petriuko vidurkis {vidurkis}')
