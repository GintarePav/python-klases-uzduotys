# sorted & sort

sar = [8, 6, 5, 2, 9, 4, 1, 13, 1, 4]
sar.sort() # surikiuoja ta pati sarasa, t.y. pradangina duomenis
print(sar)

sar2 = [8, 6, 5, 2, 9, 4, 1, 13, 1, 4]
print(sorted(sar2)) # sukuria nauja sarasa
print(sar2)

sar.sort(reverse=True)
print(sar)
sorted(sar2, reverse=True)
