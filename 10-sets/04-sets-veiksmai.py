aibeA = {1, 2, 3, 4, 5}
aibeB = {1, 2, 3, 4, 5, 7, 11, 8}

#poaibis - subset
print(aibeA.issubset(aibeB)) #bus True
print(aibeB.issubset(aibeA)) #bus False

#virsaibis - superset
print(aibeB.issuperset(aibeA)) #True

#ar visi skirtingi - disjoint
aibeC = {12, 13, 14, 15}
print(aibeC.isdisjoint(aibeB)) #True, bet jei i C idetume 11, jau butu False

#sajunga - union
aibeD = aibeA.union(aibeB)
print(aibeD) #sujungia

#sandauga/sankirta - intersection
aibeE = aibeA.intersection(aibeB)
print(aibeE) #isspausdina tik bendras reiksmes

#skirtumas - difference
aibeF = aibeA.difference(aibeB) 
print(aibeF) #turetu grazinti tuos, kurie nera bendri

#aibes papildymas - update
aibeA.update(aibeB)
print(aibeA)

#salinimas - remove/discard/pop
aibeA.remove(1) #jei bus idetas neegzistuojantis skaicius, bus error
print(aibeA)

aibeA.discard(8)
print(aibeA) #nemes error, net jei nera tokio skaiciaus

aibeA.pop()
print(aibeA) #negalima pasakyti kuri skaiciu pasalina, nes aibeje nera indeksacijos; pop() grazina pasalinta elementa, jei assigninama kintamajam

#valymas - clear
aibeA.clear()
print(aibeA)