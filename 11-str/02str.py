txt = 'mano batai buvo du, kazkas atsitiko nerandu'
print(len(txt))
print(f'Sakinyje \'{txt}\' yra {(txt.count(" ")) + 1} zodz.')
print(txt.capitalize())
print(txt.upper())
print(txt.lower())
print(txt.isupper())
print(txt.find('at'))
print(txt.find('at', 7, -1)) #iki paskutinio

t = '123abc456'
print(t.isalnum())
t4 = '             '
print(len(t4))
print(t4.isspace())
t5 = 'l a b a s'
print(t5.isspace())
t6 = '  j k  '
print(t6.strip()) #panaikina pradzio ir gale tarpus
listTxt = t6.split()
print(listTxt)
zodis = ''.join(listTxt)
print(zodis)
meile = 'man labai patinka coca cola'
meile1 = meile.replace('coca cola', 'pepsi')
print(meile1)