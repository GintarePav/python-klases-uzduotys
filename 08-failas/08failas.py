def skaitom():
    with open('08data.txt', 'r') as f:
        eilut = f.read()
        skSar = [int(x) for x in eilut.split()] # dar galima ideti if x != '\n', bet turbut reiktu regex, kad itrauktu skaicius aplink \n; o split be jokio argumento skippins visus whitespace
        print(skSar)

skaitom()