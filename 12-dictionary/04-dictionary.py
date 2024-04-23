prekes = {
    'Duona': 1.25,
    'Vanduo': 0.68,
    'Konservai': 2.58,
    'Limonadas': 1.45,
    'Mesa': 7.54,
    'Traskuciai': 0.99,
    'Sausainiai': 2.49,
    'Spinatai': 0.79,
    'Citrina': 0.50
}

vyksta = True
suma = 0

while vyksta:
    default = "Tokios prekes nera"
    preke = input('Iveskite preke: ')
    
    if preke == 'Pabaiga':
        vyksta = False

    if preke in prekes:
        kiekis = int(input('Koks kiekis: '))
        suma += (prekes[preke] * kiekis)
    else:
        print(prekes.get(preke, default))

else: 
    print(f'Bendra krepselio suma: {suma} eur.')

    
    