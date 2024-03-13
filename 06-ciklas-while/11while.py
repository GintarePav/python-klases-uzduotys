# ivedamas skaicius, is kiek skaitmenu jis sudarytas?
# 3456 // 10
# 345 // 10
# 34 // 10
# 3 // 10
# 0, ats: 4

def skaiciuoti(sk):
    while sk > 0:
        sk = sk // 10 # sk //= 10
        kiek += 1
    return kiek

skaicius = int(input('sk='))

print(f'musu skaicius {skaicius} sudarytas is {skaiciuoti(skaicius)} skaitmenu')
