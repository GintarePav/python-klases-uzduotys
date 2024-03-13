x = [1, 2, 3, 4, 5, 2, 3]
print(x)
x.pop()
print(x)
a = x.pop()
print(a)
x.remove(2) #isima pirma sutikta 2
#pop reiksmeissaugo, remove ne

h = x.copy() #cia irgi kopija, taip pat kaip x[:]

del x[0]
print(x)