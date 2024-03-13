# print visus 5zenklius, kuriu skaitmenu suma lygi sandaugai
# 10000 iki 99999
kiek = 0
for i in range(10000, 99999)
    x1 = i // 10000
    x2 = i // 1000 % 10
    x3 = i // 100 % 10
    x4 = i // 10 % 10
    x5 = i % 10

    suma = x1+ x2 + x3 + x4 + x5
    sandauga = x1 * x2 * x3 * x4 * x5
    if suma == sandauga:
        print(i, end = ', ')
        kiek += 1
    print(f'')