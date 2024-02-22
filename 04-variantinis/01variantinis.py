# ivedu menesi skaiciumi, rezultatas menesis tekstu, e.g. 1 ==> Sausis

menesis = int(input("Iveskite menesi skaiciumi: "))
match menesis:
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
        tekstas = "Blogai ivesti duomenys"

print(f'{menesis} = {tekstas}')