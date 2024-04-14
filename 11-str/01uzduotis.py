# Sugeneruoti sarasa random skaiciu nuo -100 iki 100, o elementu turi buti 10000
# atrinkti 3 dazniausiai pasikartojancius, kurie ir kiek

import random

sar1 = []

for i in range(10000):
    randomNum = random.randint(-100, 100)
    sar1.append(randomNum)

sar2 = list(set(sar1))
kiek = 0
kuris = 0

# kiek2 = 0
# kuris2 = 0

# kiek3 = 0
# kuris3 = 0

for i in sar2:
    count = sar1.count(i)
    if count > kiek:
        kiek = count
        kuris = sar2[i]

print(f'kiek = {kiek}; kuris = {kuris}')

# print(f'kiek = {kiek2}; kuris = {kuris2}')
# print(f'kiek = {kiek3}; kuris = {kuris3}')


# def tikrinti(kiekX, kiekY, kurisZ):
#     for i in sar2:
#         count = sar1.count(i)
#         if count > kiekX:
#             kiekY = count
#             kurisZ = sar2[i]
#     print(f'kiek = {kiekY}; kuris = {kurisZ}')
