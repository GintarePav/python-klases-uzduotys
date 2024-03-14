#Petriukas mokosi ir gauna pazymius. Mamai rodo tik teigiamus, teciui tik >= 6, seneliams >= 8;

def ivestiDuomenis(kiek):
    paz = []
    i = 0
    while i < kiek:
        i += 1
        p = int(input(f'Iveskite {i}-aji pazymi'))
        if 1<=p<=10:
            paz.append(p)
        else:
            print("Netinkamas pazymys, bandykite dar karta")
            i -= 1 #for jau atgal nesugrazins iteracijos, tes toliau
    return paz

def isrinktiDuomenis(sarasas, kriterijus):
    sarNaujas = []
    for i in sarasas:
        if i >= kriterijus:
            sarNaujas.append(i)
    return sarNaujas

pazTikri = ivestiDuomenis(8)
pazMamai = isrinktiDuomenis(pazTikri, 4)
pazTeciui = isrinktiDuomenis(pazTikri, 6)
print(f'Mano pazymiai: {pazTikri}')
print(f'Rodomi teciui: {pazTeciui}')