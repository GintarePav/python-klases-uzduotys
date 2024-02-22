# ivedu menesi skaiciumi, rezultatas metu laikas tekstu, e.g. 1 ==> Ziema, 8 ==> Vasara, o tada dar ir menesis

menesis = int(input("Iveskite menesi skaiciumi: "))

# Funkcija 1
def menuo(sk):
    match sk:
        case 1 :
            tekstas = "Sausis"
        case 2 :
            tekstas = "Vasaris"
        case 3 :
            tekstas = "Kovas"
        case 4 :
            tekstas = "Balandis"
        case 5 :
            tekstas = "Geguze"
        case 6 :
            tekstas = "Birzelis"
        case 7 :
            tekstas = "Liepa"
        case 8 :
            tekstas = "Rugpjutis"
        case 9 :
            tekstas = "Rugsejis"
        case 10 :
            tekstas = "Spalis"
        case 11 :
            tekstas = "Lapkritis"
        case 12 :
            tekstas = "Gruodis"
        case _ :
            tekstas = "neegzistuojantis menesis"
    return tekstas

# Funkcija 2
def metuLaikas(sk):
    match sk:
        case 12 | 1 | 2:
            tekstas = "Ziema"
        case 3 | 4 | 5:
            tekstas = "Pavasaris"
        case 6 | 7 | 8 :
            tekstas = "Vasara"
        case 9 | 10 | 11 :
            tekstas = "Ruduo"
        case _ :
            tekstas = "Blogai ivesti duomenys"
    return tekstas

print(f'{menesis} = {metuLaikas(menesis)}, {menuo(menesis)}')