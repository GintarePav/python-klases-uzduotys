list1 = [5, 8, 9, 14, 25]
list2 = [6, 7, 8, 15, 22]

# reikia naujo saraso, kuris is pirmo ima lyginius, o antro nelyginius skaicius

#zip metodas
kazkas = zip(list1, list2)
print(list(kazkas)) #sukuria tuple tipa paimdamas duomenis is keliu listu

sar = []
for i, j in zip(list1, list2):
    if i%2==0:
        sar.append(i)
    if j%2!=0:
        sar.append(j)
print(*sar)

sarKitas = [x + y for x, y in zip(list, list2)]
print(sarKitas)