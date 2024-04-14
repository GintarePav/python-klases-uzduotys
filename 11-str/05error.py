# Bet kokios klaidos gaudymas
while True:
    try:
        sk = float(input("Iveskite skaiciu: "))
        break
    except ValueError as ex:
        print(f'Blogai ivesti duomenys; Klaida {ex}')
print(f'Duomenu ivedimas pavyko - {sk}')

# arba kaip funkcija
def ivedimas():
    while True:
        try:
            sk = float(input("Iveskite skaiciu: "))
            return sk
        except ValueError as ex:
            print(f'Blogai ivesti duomenys; Klaida {ex}')

sk = ivedimas()

# konkrecios klaidos ieskojimas
klaida = True
while klaida:
    try:
        sk = float(input("Iveskite skaiciu: "))
        rez = 100 / sk
        klaida = False
    except ValueError as ex:
        print(f'Blogai ivesti duomenys; Klaida {ex}')
    except ZeroDivisionError as ex:
        print("Dalinti is nulio negalima")
    
    else:
        print("Viskas ok") #ivykdoma kai pasibaigia ciklas
    finally:
        print("Siandien nedirbu") #ivykdoma visada

print(f'Duomenu ivedimas pavyko - {sk}')