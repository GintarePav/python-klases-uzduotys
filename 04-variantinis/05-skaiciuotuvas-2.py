# Suprogramuoti skaiciuotuva, kurio veiksmai: + - * / ^(laipsnis) q(saknis)
# q naudoti math.sqrt(x)
# rezultato isvedimas:
    # rezultatas = 15 BLOGAI
    # 5 + 10 = 15 GERAI
    # is skaiciaus 16 istraukus sakni gausim 4 GERAI
    # 5 ^ 3 = 125 GERAI
# povandeniniai akmenys: 
    # dalyba is 0 
    # saknis is neigiamo
# jei traukiam sakni, antro skaiciaus neprasom
# nekartoti kodo!!!

import math

def naudotiSkaiciuotuva():
    skaicius = int(input("Iveskite skaiciu: "))
    operacija = input("Iveskite operacija: ")

    def antrasSkaicius():
        return int(input("Iveskite antra skaiciu: "))

    match operacija:
        case "q" if skaicius >= 0:
            rezultatas = math.sqrt(skaicius)
            print(f"Is {skaicius} istraukus sakni gauname {rezultatas}")
            return
        case "+"| "-"| "*"| "^"| "/":
            antrasSkaicius = antrasSkaicius()
            match operacija:
                case "+" :
                    rezultatas = skaicius + antrasSkaicius
                case "-" :
                    rezultatas = skaicius - antrasSkaicius
                case "*" :
                    rezultatas = skaicius * antrasSkaicius 
                case "^" :
                    rezultatas = skaicius ** antrasSkaicius
                case "/":
                    if antrasSkaicius != 0:
                        rezultatas = skaicius / antrasSkaicius
                    else: 
                        print("Operacija neegzistuoja")
                        return naudotiSkaiciuotuva()
            print(f"{skaicius} {operacija} {antrasSkaicius} = {rezultatas}")  
        case _ :
            print("Operacija neegzistuoja")
            return naudotiSkaiciuotuva()
    
skaiciuotuvas = naudotiSkaiciuotuva()


