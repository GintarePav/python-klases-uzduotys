# Apskaiciuoti skaiciaus kvadrata
# Jei skaicius = 13, isvesti pranesima
# Jei ne 13, kita pranesima

sk = int(input("Koks skaicius? "))
arTiesa = sk == 13 # loginis nkintamasis, prasminga kai reikia kurti labai sudetingus ir ilgus loginius reiskinius (i.e sk == 13)

if arTiesa : # sutrumpintas salygos sakinys
    print("...")
print('!!!')

kv = sk**2
print(f'kvadratas = {kv}')

### 

sk = int(input("Koks skaicius? "))
arTiesa = sk == 13

if arTiesa : 
    print("...")
if not(arTiesa) :
    print('!!!')

kv = sk**2
print(f'kvadratas = {kv}')

###

sk = int(input("Koks skaicius? "))
arTiesa = sk == 13

if arTiesa : # paprastas salygos sakinys
    print("...")
else :
    print('!!!')

kv = sk**2
print(f'kvadratas = {kv}')