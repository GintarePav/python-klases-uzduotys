#Petriuko pazymiai - reikia apskaiciuoti vidurki

kiek = int(input("kiek Petriukas turi pazymiu? "))
suma = 0
for i in range(1, kiek+1):
    paz = int(input(f'Iveskite Petriuko {i}-aji pazymi: '))
    if 1<paz<=10:
        suma += paz
    else:
        print("Netinkamas pazymys, bandykite dar karta")
        i -= 1 # neveiks sitaip, nesugris atgal ir neprasys buvusio skaiciaus is naujo
        

vidurkis = suma / kiek
print(f'Petriuko vidurkis {vidurkis}')
