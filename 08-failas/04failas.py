with open('03duom.txt', 'r', encoding='utf-8') as f:
    txt = f.readline() 
    txt2 = f.readline()
    f.seek(0) #grazina i dokumento pradzia, bet cia nera pozicija, pvz. 5 nebus penkta eilute
    txt3 = f.readline()
print(txt+txt2+txt3) 
