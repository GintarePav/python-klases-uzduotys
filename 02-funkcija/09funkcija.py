def ivedimas(txt):
    sk = int(input(f'Koks {txt} skaicius? '))
    return sk

def veiksmai(a, b):
    rez = a + b
    return rez

def isvedimas(a, b, rez):
    print(f'{a} + {b} = {rez}')

sk1 = ivedimas('pirmas')
sk2 = ivedimas('antras')
rezultatas = veiksmai(sk1, sk2)
isvedimas(sk1, sk2, rezultatas)
