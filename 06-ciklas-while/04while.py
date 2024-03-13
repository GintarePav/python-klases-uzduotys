# atspausdinti visus daliklius: 16 = 1, 2, 4, 6, 8, 16, o tada kiek ju yra
n = int(input('n='))
kiek = 0
ck = 0
while n >= ck:
    ck += 1
    if n % 2 == 0:
        print(ck, end=(', '))
        kiek += 1
print('Ju yra', kiek)