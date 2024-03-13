# Jei isivedam 5, programa atsapusdina:
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3 
# etc

sk = int(input('sk='))

for j in range(sk):
    for i in range(1, (sk-j)+1):
        print(i, end=(' '))
    print()