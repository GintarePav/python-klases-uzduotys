# in 
# in neveiks su vidurkiu zemiau parasytoje programoje, nes per kableli skaicius gali buti ir jis tiesiog neieis i in(a,b,c)

pazymys =int(input('pazymys = '))

if pazymys == 10: 
    print(f'{pazymys} - puikus')
elif pazymys in(1, 2, 3):
    print(f'{pazymys} - blogas')
elif pazymys in(4, 5, 6):
    print(f'{pazymys} - patenkinamas')
elif pazymys in(7, 8, 9):
    print(f'{pazymys} - geras')
else:
    print(f'{pazymys} yra negalimas pažymys')