# Python neturi masyvo tipo (array), bet list (sarasas) yra labai panasus.

m = [5, 9, 8, 44, 7, 9, 7]
print(m)
print(type(m))
# elementai gali buti skirtingo tipo
# elementai numeruojami (indeksuojami) nuo 0
user = ['Jonas', 18, True, 1.50, [8, 9, 7, 9]]
print(user[0])
print(user[4])
print(user[4][0])
print(len(m))
print(m[len(m)-1]) #paskutinis elementas
print(m[len(m)//2]) #istrauks vidurini, kai nelyginis elementu skaicius

# sudeti visus elementus ir isvesti vidurki
suma = 0
for i in m:
    suma += i
    print(i)
vid = suma / len(m)
print(vid)

# list metodai
vid1 = sum(m) / len(m)

# geras come back yra klausti ar panaudoti metoda, ar ji suprogramuoti
did = max(m)

    # paprastas iteravimas:
for i in m:
    print(i, end = ", ")
print() #zymeklis nusoks i nauja eilute ir kitas print bus jau naujoj eilutej

    # iteravimas per indeksus:
for i in range(len(m)): #range(0, 7) nuo nulio iki 7; 7 nepaims
    print(m[i], end = ", ")
print()

# Budas nr. 1: surasti max reiksme
d1 = m[0]
for i in m: #cia imami elementai
    if d1 < i:
        d1 = i
print(d1)

# Budas nr. 2 (optimaliausias)
d3 = m[0] 
for i in range(1, len(m)): #cia imami indeksai
    if d3 < m[i]:
        d3 = m[i]



