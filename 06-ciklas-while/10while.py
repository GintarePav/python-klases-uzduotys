# ivedamas skaicius, is kiek skaitmenu jis sudarytas?
# 3456 // 10
# 345 // 10
# 34 // 10
# 3 // 10
# 0, ats: 4

sk = int(input('sk='))
kiek = 0
kopija = sk
while sk > 0:
    sk = sk // 10 # sk //= 10
    kiek += 1

print(f'musu skaicius {kopija} sudarytas is {kiek} skaitmenu')
