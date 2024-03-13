# petriuko pazymiai

kiek = int(input("Kiek pazymiu turi Petriukas? "))
pazNr = 0
suma = 0
while kiek > pazNr:
    pazNr += 1
    paz = int(input(f'Iveskite {pazNr}-aji pazymi: '))
    if not(1 <= paz <= 10):
        print("Blogas pazymys, bandykite dar karta")
        pazNr -= 1
    else:
        suma += paz

print(f'Vidurkis = {suma / kiek}')