txt = 'Tupi žvirblis kamine, su kailine kepure. Tu žvirbleli pulsi, visas susikulsi. AČIŲ'
lt  = 'ąčęėįšųūž'
txt2 = txt.lower()
kokios = []
kiek = 0

# for i in lt:
#     kiek += txt2.count(i)
#     if i in txt2:
#         kokios.append(i)

# print(f'kokios: {kokios}; kiek: {kiek}')

#rasti visas i ir kur
txt2.find("i")
kiekI = 0
kurI = []

for i in txt2:
    if i == "i":
        kiekI += 1
        kurI.append()

print(f'kiekI={kiekI}; kurI={kurI}')

