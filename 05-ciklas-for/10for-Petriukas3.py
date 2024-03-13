#Petriuko pazymiai - reikia rasti didziausia pazymi ir kelintas jis yra

def ivedimas(nr):
    paz = int(input(f'Iveskite Petriuko {i}-aji pazymi: '))
    if 1<paz<=10:
        return paz
    else:
        return ivedimas(nr)

kiek = int(input("kiek Petriukas turi pazymiu? "))
did = kelintas = None

for i in range(1, kiek+1):
    p = ivedimas(i)
    if i == 0:
        did = p
        kelintas = i
    elif did <= p:
        did = p
        kelints = i


print(f'Petriuko max pazymys yra {did}; jis yra {kelintas}-as')
