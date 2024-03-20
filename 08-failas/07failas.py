def skaitom():
    with open('07data.txt', 'r') as f:
        txt = f.read()
    return txt

def konvertuoti():
    duomenys = skaitom()
    # print(type(duomenys))
    duomSK = [int(x) for x in duomenys.split(' ')]
    print(duomSK)
    return duomSK

def rez():
    with open('07rez.txt', 'a') as f: #reiktu saugoti i kita faila, nes sugadins pirmini duomenu faila
        sar = konvertuoti()
        txt = str(sar)
        suma = sum(sar)
        f.write(txt[1:-1])
        f.write(f'eilutes suma = {suma}')
        print(f.closed)
    print(f.closed)

rez()