# susumuoti visus skaicius nuo 1 iki n, kurie dalijasi is 3, 5 ir 7

n = int(input("n="))
suma = sum([x for x in range(1, n + 1) if x % 3 == 0 and x % 5 == 0 and x % 7 == 0])
print(suma)