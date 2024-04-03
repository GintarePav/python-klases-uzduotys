#Isimti pasikartojancius ir paziureti kiek uztruks

import time

def fun(*args):
    sar = []
    for i in args: # i = paduotas sarasas
        for j in i: # j = elementas sarase
            if j not in sar:
                sar.append(j)
    return sar

sarA = list(range(10000))
sarB = list(range(2500, 16000, 3))
sarC = list(range(1000, 30000, 4))

pradzia1 = time.time()
fun(sarA, sarB, sarC)
trukme1 = time.time() - pradzia1
print(trukme1)

pradzia2 = time.time()
aibe1 = set(sarA)
aibe2 = aibe1.union(set(sarB), set(sarC))
trukme2 = time.time() - pradzia2
print(trukme2)