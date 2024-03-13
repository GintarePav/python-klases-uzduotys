paskolosDydis = int(input("Kokio dydzio paskola paeme Antanas? "))
# paskolosLaikas = 48 # menesiai, nes 4 metai
pastoviImoka = 250

# reikia menesio palukanu dydzio, visos imokos dydzio, likusios sumos kiek viena menesi
# mokejimo logika ir pirmo menesio imokos:
sumoketosPalukanos = round((paskolosDydis * 0.03), 2)
visaSumoketaSuma = round(sumoketosPalukanos + pastoviImoka, 2)
likusiSuma = paskolosDydis

for i in range(1, 48):
    sumoketosPalukanos = round((likusiSuma * 0.03), 2)
    visaSumoketaSuma = round(sumoketosPalukanos + pastoviImoka, 2)
    likusiSuma = round(likusiSuma - visaSumoketaSuma, 2)
    print(f'{i}-aji menesi palukanu dydis: {sumoketosPalukanos}; bendras imokos dydis: {visaSumoketaSuma}; likusi suma: {likusiSuma} eur.')
    if likusiSuma <= 250:
        sumoketosPalukanos = round((likusiSuma * 0.03), 2)
        likusiSuma -= round(sumoketosPalukanos, 2)
        visaSumoketaSuma = round(sumoketosPalukanos + likusiSuma, 2)
        likusiSuma = 0
        print(f'{i+1}-aji menesi Antanas baige moketi paskola; sumoketos palukanos: {sumoketosPalukanos}; bendras imokos dydis: {visaSumoketaSuma}; likusi suma: {likusiSuma} eur.')
    if likusiSuma == 0:
        break
    