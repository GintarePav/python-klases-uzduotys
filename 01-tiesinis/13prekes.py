# sudelioti prekes i dezes, apsibreziant, kiek yra prekiu, kiek telpa didelej dezej, kiek mazoj
# didelese telpa x prekiu, o mazose - y
# kiek reikes dideliu ir mazu deziu, o kiek liks nesupakuota?
# pvz: jei n = 259, x = 10, y = 5, tai ats. reiks 25 dideliu, 1 mazos dezes, o 4 prekes liks nepakuotos.

prekiuKiekis = int(input('kiek prekiu? '))
didelesDezesTalpa = int(input('kiek telpa didelej dezej? '))
mazosDezesTalpa = int(input('kiek telpa mazoj dezej? '))
kiekTelpaDidelej = prekiuKiekis // didelesDezesTalpa
kiekNetilpoDidelej = prekiuKiekis % didelesDezesTalpa
kiekTelpaMazoj = kiekNetilpoDidelej // mazosDezesTalpa
#kiekLiekaNepakuotu = kiekTelpaMazoj % mazosDezesTalpa 
likoViso = kiekNetilpoDidelej % kiekTelpaMazoj
# print(f'Is viso prekiu yra {prekiuKiekis}, dideleje dezeje telpa {kiekTelpaDidelej} prekiu, mazose {kiekTelpaMazoj}, o {kiekLiekaNepakuotu} lieka nesupakuota')
print(f'Is viso prekiu yra {prekiuKiekis}, dideleje dezeje telpa {kiekTelpaDidelej} prekiu, mazose {kiekTelpaMazoj}, o {likoViso} lieka nesupakuota')

#geriau pervadinti kiekNetilpoDidelej ir likoViso i Likutis, tada bus optimaliau