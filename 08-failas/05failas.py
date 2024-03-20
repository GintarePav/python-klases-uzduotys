def kuria():
    with open('04data.txt', 'w', encoding='utf-8') as f:
        f.write('10, 15, 24, 14\n')
        f.write('-18, -15, -12, -14\n')

def skaito():
    with open('04data.txt', 'r', encoding='utf-8') as f:
        txt = f.readlines()
        print(type(txt))
        print(f.closed)

kuria()
print(skaito())

def papildoIrSkaito():
    with open('04data.txt', 'r+', encoding='utf-8') as f:
        f.seek(0, 2) # nukelia i failo pabaiga
        f.write('10, 10, 10, 10\n')
        print('mano failas:', f.read()) # neskaitys, nes turime seek(0, 2), t.y. stovime gale failo

papildoIrSkaito()