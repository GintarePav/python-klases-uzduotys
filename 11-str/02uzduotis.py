sar = [5, 8, 9, 7, 8, 7, 9, 9, 7, 8]
sar2 = []

for i in sar:
    if i not in sar2:
        sar2.append(i)
        
print(sar2)