# Patikrinti, ar įvestas blogas pažymys, i.e. neegzistuojantis, negalimas (nuo -begalybės iki 0 ir nuo 11 iki +begalybės)

pazymys =int(input('pazymys = '))
if pazymys <=0 or pazymys >= 11:
    print(f'{pazymys} - negalimas, kartokite įvedimą')
    pazymys =int(input('pazymys = '))

print('pazymys = ' + str(pazymys)) # reikia stringify, nes kitaip neveiks, bet jau atgyvenęs būdas

if not(1 <= pazymys <= 10): # neiginys paprasčiau
    print(f'{pazymys} - negalimas, kartokite įvedimą')
    pazymys = int(input('pazymys = '))


