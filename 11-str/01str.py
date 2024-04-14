print('daug teksto ir daug kabuciu')
print('daug \'teksto\' ir daug kabuciu')
# kelias = 'c:\user\new\newData.txt'
#print(kelias) #printins error, reik naudot dvigubus slashus
kelias2 = 'c:\\user\\new\\newData.txt'
print(kelias2)
kitasKelias = r'c:\user\new\newData.txt' #prefix, atspausdints paprasta eilute
print(kitasKelias)
txt = 'labas rytas'
print(txt[-1]) #atspausdins paskutinis simboli
txt2 = 'labas rytas suraitytas ir kazkas dar parsuyta'
print(txt2[2:20:3])
t1 = 'Labai'
t2 = 'Noriu'
t3 = 'Namo'
t4 = '{} {} {}'.format(t1, t2, t3) #tas pats kas f''
print(t4)