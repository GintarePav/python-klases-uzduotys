# nenaudoti min ir max
# Duoti 4 skaičiai - rasti min ir max

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
d = int(input('d = '))

### basic budas

if a >= b and a >= c and a >= d:
    did = a
elif b >= c and b >=d:
    did = b
elif c >= d:
    did = c
else :
    did = d

print(f' max = {did}')

### geresnis budas, nes galima daug pernaudoti ir trumpiau

did = a 
if did < b:
    did = b
if did < c:
    did = c
if did < d:
    did = d

print(f' max = {did}')

### dar geresnis budas

def didelis(x, y):
    if x >= y:
        return x
    else :
        return y
#did = didelis(a, b)
#did = didelis(did, c)
#did = didelis(did, d)
did = didelis(didelis(a,b), didelis(c,d))
print(f' max = {did}')