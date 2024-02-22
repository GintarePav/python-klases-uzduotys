# Suprogramuoti skaiciuotuva
# operacijos: + - * / saknis (q) laipsnis (^)
# 1. Ivedamas skaicius, e.g. a
# 2. Ivedama operacija: sudetis, daugyba, etc
# 3. Jei pasirinkta q, antro skaiciaus nereikia - spausdinamas saknies rezultatas, jei kita operacija is duotu - 4 zingsnis, jei netinkama operacija - prasoma kartoti operacijos ivedima
# 4. Ivedamas skaicius b
# 5. Gaunamas rezultatas
# Naudoti tiesini algoritma, salygas ir funkcijas

def naudotiSkaiciuotuva() :
    skaicius = int(input("Iveskite skaiciu: "))
    operacija = input("Iveskite operacija: ")

    def ivestiAntra():
        skaiciusDu = int(input("iveskite antra skaiciu: "))
        return skaiciusDu

    if operacija == "+" :
        return skaicius + ivestiAntra()
    if operacija == "-" :
        return skaicius - ivestiAntra()
    if operacija == "/" and ivestiAntra() > 0:
        return skaicius / ivestiAntra()
    if operacija == "*" :
        return skaicius * ivestiAntra()
    if operacija == "^" :
        return skaicius ** ivestiAntra()
    if operacija == "q" and skaicius >= 0:
        return skaicius ** 0.5
    else :
        print("Operacija negalima, bandykite dar karta.")
        return naudotiSkaiciuotuva()

skaiciuotuvoAtsakymas = naudotiSkaiciuotuva()

print(f'Atlikus jusu suvestus veiksmus skaiciuotuvas gavo atsakyma: {skaiciuotuvoAtsakymas}')
