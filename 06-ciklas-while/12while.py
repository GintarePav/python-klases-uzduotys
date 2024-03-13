#apskaiciuoti skaitmenu suma
def skaiciuoti(sk):
    suma = 0
    while sk > 0:
        x1 = sk % 10 # suma += sk % 10
        sk = sk // 10 
        suma += x1 # tada sito nebereiktu
    return suma

skaicius = int(input('sk='))

print(f'musu skaiciaus {skaicius} skaitmenu suma lygi {skaiciuoti(skaicius)}')