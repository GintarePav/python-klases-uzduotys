# Patikrinti, ar įvestas blogas pažymys, i.e. neegzistuojantis, negalimas (nuo -begalybės iki 0 ir nuo 11 iki +begalybės)
def isvedimas():
    pazymys = int(input('pazymys = '))
    if not(1 <= pazymys <= 10):
        print(f'{pazymys} negalimas, kartokite dar karta')
        return isvedimas() #rekursija
    else :
        return pazymys

pazymys = isvedimas()
    
print(f'pazymys = {pazymys}')

# Ciklu tipai: rekursija, ciklo sakiniai