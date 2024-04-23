def skaityk():
    with open('12-dictionary/05-data.txt', 'r', encoding='utf-8') as f:
        eilutes = f.readlines()
        duomenys = {}
        for eilute in eilutes:
            vardas = eilute[:20].strip()
            likusiDalis = eilute[20:].strip()
            duomenys[vardas] = [int(i) for i in likusiDalis.split()]
    return duomenys

def rezultatas():
    duomenys = skaityk()
    for k, v in duomenys.items():
        duomenys[k].append(3*v[0] + 2*v[1] + v[2])
    return duomenys

def spausdinti(duomenys):
    with open('12-dictionary/05-rez.txt', 'w', encoding='utf-8') as f:
        f.write('\n---------------------------------------')
        f.write('|Vardas                    | Viso     |        |      |\n')
        f.write('---------------------------------------')
        for vardas, taskai in duomenys.items():
            f.write(f'| {vardas:18} | {taskai[4]} | {taskai[3]}   | {taskai[2]}  |  {taskai[1]}    |{taskai[0]}')
        f.close()

def trinti():
    with open('12-dictionary/05-rez.txt', 'w', encoding='utf-8') as f:
        pass

komanda = rezultatas()
surikiuotiPagalRez = dict(sorted)
print(surikiuotiPagalRez)