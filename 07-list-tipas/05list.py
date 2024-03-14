# turim sarasa, kuriame lyginius elementus reikia paversti vienu didesniais.
# [1, 2, 4, 8, 7] -----> [1, 3, 5, 9, 7]

x = [5, 8, 14, -8, 25, 36, 21]
for i in x:
    if i % 2 == 0:
        i += 1
print(x) #nepakeis listo elementu. Su loopu galime tik iteruoti, bet i lista pakeisto elemento nesupushins


xNaujas = []
for i in x:
    if i % 2 == 0:
        i += 1
    xNaujas.append(i)
print(xNaujas) #sitas jau pakeis, nes issaugojame naujame liste


for i in range(len(x)):
    if x[i] % 2 ==0:
        x[i] += 1
print(x) #cia irgi pakeis, nes tam tikram elementui assigninam nauja reiksme