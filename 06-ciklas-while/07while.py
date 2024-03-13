# atspausdinti visus daliklius. Ar pirminis skaicius? Turi 2 daliklius - 1 ir save. OPTIMIZUOTA
n = int(input('n='))
pirminis = True
ck = 1
while n//2 > ck:
    ck += 1
    if n % ck == 0:
        pirminis = False
        break
if pirminis:
    print("skaicius pirminis")
else:
    print("skaicius sudetinis")