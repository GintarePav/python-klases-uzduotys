import sys
duomSar = ['duom1.txt', 'duom2.txt', 'duom 3.txt', 'duom4.txt']
duomKlaida = []
duomInfo = []

try:
    for byla in duomSar:
        try:
            f = open(byla)
            duomInfo.append(f.read())
        except Exception:
            duomKlaida.append(byla)

            sys.exit() #baisi klaida, del to veliau print neispausdinami
finally:
    f = open('log.txt', 'a')
    for i in duomInfo:
        f.write(i)
        f.write('\n')
    f.write(str(duomKlaida))
    f.close()

print(duomInfo)
print(duomKlaida)