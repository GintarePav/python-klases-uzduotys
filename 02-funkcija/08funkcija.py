def sumuoti(*args): #python funkcija priima argumentus, o JS parametrus ja deklaruojant; * sukuria masyva
    suma = sum(args)
    print(type(args))
    return suma

print(sumuoti(5,8))
print(sumuoti(sumuoti(5, 8), 9))
print(sumuoti(1, 2, 3, 4))