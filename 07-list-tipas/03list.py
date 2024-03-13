# kopijos kurimas
x = [9, 8, 7, 4, 6, 8]
y = x[0:len(x)] #sukuria nauja sarasa; galima rasyti x[::], jei norim dar nurodyti kas kelinta skaiciu, arba x[:], jei visus is eiles
print(y)
x[0] = 1000
print(x)
print(y)
x.append(108)
print(x)
x.insert(1, -888)
print(x)
print(x.count(8)) #parodo kiek yra tam tikru verciu
print(x.index(8)) #parodys pirmojo 8 indeksa; jei po 8 padesim kableli ir parasysim 4, ieskos 8 nuo 4 indekso
x.reverse()
print(x)