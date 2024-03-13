txt = 'ąčęėįšųūŽĮĘĖ Man labai patinka anksti ryte keltis ir eiti i mokykla'
lt = ('ąčęėįšųūžĄČĘĖĮŠŲŪŽ')
kiekLt = 0
for i in txt: 
    if i in lt:
        kiekLt = kiekLt + 1
print(f'Sakinyje "{txt}" yra {kiekLt} zodziu(iai)')