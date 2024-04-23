auto_geras = {
    'Marke': 'Opel',
    'Kaina': 2500,
    'Turis': 1.4,
    'Dauztas': False
}

auto_blogas = {
    'Turis': 1.4,
    'Kaina': 2500,
    'Dauztas': False,
    'Marke': 'Opel'
}

print(auto_blogas == auto_geras) #bus true, nes vertes vienodos
print(id(auto_blogas))
print(id(auto_geras))

daugiau_info = {
    'Rida': 410250,
    'Spalva': 'Kibiro',
    'Kaina': 3500
}

auto_geras.update(daugiau_info)
print(auto_geras)
daugiau_info.update(auto_blogas)
print(daugiau_info)

auto_naujas = auto_geras|daugiau_info
print(auto_naujas)