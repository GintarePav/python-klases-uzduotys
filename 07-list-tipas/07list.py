x = list(range(1, 21, 3)) # 3 gale nirodo, kad bus kas trecias skaicius
print(x)

xNew = []

for i in x:
    k = i*i
    xNew.append(k)
print(xNew)

#List Comprehension
xNaujas = [i*i for i in x] #tas pats kas virsuj, tik python yra
print(xNaujas)

# jei tik lyginius
for i in x:
    if i % 2 == 0:
        k = i*i
        xNew.append(k)
print(xNew)

# su List Comp.
xNaujo = [i*i for i in x if i % 2 == 0]
print(xNaujo)