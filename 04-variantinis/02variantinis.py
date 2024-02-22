# ivedu menesi skaiciumi, rezultatas metu laikas tekstu, e.g. 1 ==> Ziema, 8 ==> Vasara

menesis = int(input("Iveskite menesi skaiciumi: "))
match menesis:
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
print(f'{menesis} = {tekstas}')