# Petriuko pažymiai
# Įvertinti pažymį: ar egzistuoja, ar geras, ar puikus:
# nuo -begalibybės iki 0 neegzistuoja
# 1-3 blogai
# 4-6 patenkinamai
# 7-9 gerai
# 10 puiku
# nui 11 iki +begalybės neegzistuoja

pazymys = int(input("Kiek gavo Petriukas? "))
# begalybe = (pazymys <= 0) or (pazymys >= 11)

if pazymys == 10: 
    print(f'{pazymys} - puikus') # čia iš pradžių buvo if begalybė, o 10 buvo pacoverinta elsu
elif 1 <= pazymys <= 3:
    print(f'{pazymys} - blogas')
elif 4 <= pazymys <= 6:
    print(f'{pazymys} - patenkinamas')
elif 7 <= pazymys <= 9:
    print(f'{pazymys} - geras')
else:
    print(f'{pazymys} yra negalimas pažymys') # geriausia elsui palikti sunkiausią sąlygą