txt = '25, -125, 25, 41, -25, 47, 54, -54, -254'
listSk = [int(i) for i in txt.split(', ')]
print(listSk)

listSk.sort()
print(listSk)

listSk.sort(reverse=True)
print(listSk)