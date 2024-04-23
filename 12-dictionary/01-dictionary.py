ATS = 'Deja sios prekes neturime'

prekes = {
    'Duona': 1.25,
    'Vanduo': 0.68,
    'Konservai': 2.58,
    'Limonadas': 1.45,
    'Mesa': 7.54
}

draugai = dict(Tomas = 28, Stasys = 35, Rima = 24, Tadas = 15)
print(draugai)
draugaiBeAmziaus = dict.fromkeys(['Vytas', 'Algis', "Gedas"])
print(draugaiBeAmziaus)
draugaiBeAmziaus1 = dict.fromkeys(['Vytas', 'Algis', "Gedas"], 0)
print(draugaiBeAmziaus1)

prekes['Mesa'] = 10.25
print(prekes)
print(prekes.get('AlusBeAlc'))
print(prekes.get('AlusbeAlc', ATS))
del prekes['Mesa']
prekes['Kiauliena'] = 7
print(prekes)

prekiuSar = list(prekes.keys())

print(sorted(prekes.keys()))

print('Zuvis' in prekes)

for k, v in prekes.items():
    print(f'Preke {k} kainuoja {v*0.79} be PVM')

aa = prekes.items()
print(aa)

kazkas = prekes.pop('Kiauliena')
print(kazkas) #issaugo verte

print(prekes.popitem())
print(prekes)

print(len(prekes))

prekes.setdefault('Pica')
print(prekes)

print(prekes['Duona'])
