def kuria(failas, tekstas):
    with open(failas, 'w', encoding='utf-8') as f:
        f.write(tekstas)

for i in range(1, 20):
    kuria(f'virusas\{i}byla.txt', f'{i}-oje byloje irasyta informacija \n')