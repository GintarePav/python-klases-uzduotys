# atspausdinti visus daliklius. Ar pirminis skaicius? Turi 2 daliklius - 1 ir save. OPTIMIZUOTA
n = int(input('n='))
kiek = 0
ck = 1
while n//2 > ck:
    ck += 1
    if n % ck == 0:
        kiek += 1
if kiek == 2:
    print("skaicius pirminis")
else:
    print("skaicius sudetinis")