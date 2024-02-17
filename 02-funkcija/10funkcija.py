def ivedimas(txt):
    sk = int(input(f'Koks {txt} skaicius? '))
    return sk

def veiksmai():
    sk1 = ivedimas('pirmas')
    sk2 = ivedimas('antras')
    rez = sk1 + sk2
    return rez, sk1, sk2

def isvedimas():
    rez, a, b = veiksmai()
    print(f'{a} + {b} = {rez}')

rezultatas = isvedimas()
print(rezultatas)
#isvedimas(sk1, sk2, rezultatas)