aibeA = set()
print(type(aibeA))
aibeA.add(5)
print(aibeA)
aibeB = {5, 8, 7, 14, 6, 5, 8}
print(aibeB)
sar1 = [5, 8, 9, 7, 8, 7, 4, 7, 9, 1, 4, 4, 1, 5]
laik = set(sar1)
laik1 = list(laik)
print(f'Unukaliu kiekis: {len(laik1)}')

print(1 in aibeB)
# print(aibeB[1]) aibe nesuindeksuota, jos surikuoti taip negalima