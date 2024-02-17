#ivedamas penkiazenklis skaicius ir reikia rasti jo skaitmenu suma
#pvz: 12345, kaip gauti pirmaji skaiciu? 
#12345 // 10000 ==> 1
#12345 // 1000 ==> 12 % 10 ==> 2
#12345 // 100 ==> 123 % 10 ==> 3
#12345 // 10 ==> 1234 % 10 ==> 4
#12345 // 1 ==> 12345 % 10 ==> 5 / 12345 % 10 = 5

sk = int(input("Ivesk sesiazenkli nskaiciu: "))
x1 = sk // 100000
x2 = sk // 10000 % 10
x3 = sk // 1000 % 10
x4 = sk // 100 % 10
x5 = sk // 10 % 10
x6 = sk % 10

suma = x1 + x2 + x3 + x4 + x5 + x6
print(suma)

# kitas pvz su asmens kodu
ak = 39812121111
diena1 = ak / 1000000
print(diena1)
diena2 = ak / 100000
print(diena2)
dienaTikra = 10 * diena1 + diena2
print(dienaTikra)

ak = 39812121111
dienaTikra = ak // 10000 % 100
