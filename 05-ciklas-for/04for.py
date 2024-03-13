# range(start, stop, step)
# a = list(range(1, 100, 10))
# print(a)

# Atspausdinti skaicius nuo 1 iki n

pr = int(input("Nuo kiek skaiciuosim? "))
pb = int(input("Iki kiek skaiciuosim? "))
h = int(input("Kokiu zingsniu? "))
for i in range(pr, pb, h):
    print(i, end=', ')