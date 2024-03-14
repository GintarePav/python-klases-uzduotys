sar1 = [2, 4, -5, 6, 8, -2, -7, 5]
sar2 = [2, -6, 5, 9, 2, 7, -4, -5, 1]

#skurti poru sarasa kuriu suma lyginis skaicius

sarPoru = []
for i in sar1:
    for j in sar2:
        suma = i + j
        if suma % 2 == 0:
            sarPoru.append([i, j])
print(sarPoru)


sarPorKitas = [[x, y] for x in sar1 for y in sar2 if (x + y) % 2 == 0]