duomSar = ['duom1.txt', 'duom2.txt', 'duom 3.txt', 'duom4.txt']
duomKlaida = []
duomInfo = []

for byla in duomSar:
    try:
        f = open(byla)
        duomInfo.append(f.read())
    except Exception:
        duomKlaida.append(byla)

print(duomInfo)
print(duomKlaida)