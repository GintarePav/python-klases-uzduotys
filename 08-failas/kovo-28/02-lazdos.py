# 2. Suprogramuokite seną kinų žaidimą lazdomis. Žaidžia du žaidėjai. Yra 10 lazdelių. Žaidėjai paeiliui ima nuo vienos iki trijų lazdų. Pirmas žaidimą pradeda kompiuterio atsitiktiniu būdu sugeneruotas žaidėjas (tai gali būti žaidėjas Nr.1 arba žaidėjas Nr.2, jei yra suvedami žaidėjų vardai kompiuteris atsitiktiniu būdu parenkažaidėjo vardą)*.Žaidimas tęsiasi tol, kol nesibaigia lazdelės. Pralaimi tas, kuris paėmė paskutinę lazdelę. 
# Suprogramuokite  žaidimą taip, kad galėtų žaisti du žmonės. Žaidimo pradžioje yra 10 lazdelių*. Kiekviename žaidimo etape atspausdinamas žaidėjo numeris, lazdelių skaičius, ir užklausa, kiek lazdelių paims žaidėjas. Nepamirškite pakeisti žaidėjų eilės numerius ir mažinti lazdelių skaičių. Nepamirškite, pabaigoje išvesti laimėjusio žaidėjo numerio. Nepamirškite, kad žaidėjas negali paimti daugiau nei tris lazdeles (apsaugokite ir nuo 0 ir neigiamų skaičių), ir taip pat negali paimti lazdelių daugiau nei liko. 

import random
ataskaita = open('task02.txt', 'w', encoding='utf-8')
pirmasZaidejas = input('Irasykite pirmojo zaidejo varda: ')
ataskaita.write(f'Vienas zaidejas ivede varda {pirmasZaidejas}\n')
antrasZaidejas = input('Irasykite antrojo zaidejo varda: ')
ataskaita.write(f'Kitas zaidejas ivede varda {antrasZaidejas}\n')


def generuotiZaideja():
    atsitiktinis = random.randint(1, 2)
    if atsitiktinis == 1:
        print(f'Zaidima pradeda {pirmasZaidejas}. Jus busite pirmasis zaidejas.')
        ataskaita.write(f'Zaidima pradeda {pirmasZaidejas}. Jis bus vadinamas pirmuoju zaideju.\n')
    else:
        print(f'Zaidima pradeda {antrasZaidejas}. Jus busite pirmasis zaidejas.')
        ataskaita.write(f'Zaidima pradeda {antrasZaidejas}. Jis bus vadinamas pirmuoju zaideju.\n')

def imtiLazdeles(txt):
    kiekIma = int(input(f'Kiek lazdeliu ims {txt} zaidejas (nuo 1 iki 3)? '))
    if 0 < kiekIma < 4:
        return kiekIma
    else:
        print("Negalimas skaicius")
        ataskaita.write(f'Imamas negalimas skaicius.\n')
        return imtiLazdeles()
    
generuotiZaideja()   
lazdeles = int(input('Su kiek lazdeliu zaisite? '))
ataskaita.write(f'Bus zaidziama su {lazdeles} lazdelemis.\n')


while lazdeles > 0:
    kiekImaPirmas = imtiLazdeles("pirmas")
    ataskaita.write(f'Pirmas zaidejas ima {kiekImaPirmas} lazdeliu.\n')
    lazdeles -= kiekImaPirmas
    print(f'Lieka {lazdeles} lazdeliu.')
    ataskaita.write(f'Lieka {lazdeles} lazdeliu.\n')
    if lazdeles <=0:
        print("Paskutine lazdele paeme Pirmasis zaidejas. Zaidima laimejo Antrasis zaidejas.")
        ataskaita.write("Paskutine lazdele paeme Pirmasis zaidejas. Zaidima laimejo Antrasis zaidejas.\n")
        break

    kiekImaAntras =  imtiLazdeles("antras")
    ataskaita.write(f'Pirmas zaidejas ima {kiekImaAntras} lazdeliu.\n')
    lazdeles -= kiekImaAntras
    print(f'Lieka {lazdeles} lazdeliu.')
    ataskaita.write(f'Lieka {lazdeles} lazdeliu.\n')
    if lazdeles <=0:
        print("Paskutine lazdele paeme Antrasis zaidejas. Zaidima laimejo Pirmasis zaidejas.")
        ataskaita.write("Paskutine lazdele paeme Antrasis zaidejas. Zaidima laimejo Pirmasis zaidejas.\n")
        break

ataskaita.close()