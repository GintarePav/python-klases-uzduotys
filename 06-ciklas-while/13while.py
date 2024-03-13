# ivestas skaicius. Perrasyti skaiciu atvirksciai, eg 123 -> 321
def skaiciuoti(sk):
    atvirksciai = 0
    while sk > 0:
        x1 = sk % 10
        sk = sk // 10 
        atvirksciai = atvirksciai * 10 + x1
    return atvirksciai

skaicius = int(input('sk='))

print(f'musu skaicius {skaicius} atvirksciai yra {skaiciuoti(skaicius)}')