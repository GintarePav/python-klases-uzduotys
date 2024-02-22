# apskaiciuoti faktoriala.
# 5! = 1 * 2 * 3 * 4 * 5 = 120

# n = 5
# n = n - 1 ==> n = 4
# n = n - 1 ==> n = 3
#...
# n = n - 1 ==> n = 0

n = int(input("Kokio skaiciaus faktoriala skaiciuosime? "))

def faktorialas(sk):
    if sk == 0:
        return 1
    else:
        return sk * faktorialas(sk-1)

rez = faktorialas(n)
print(f'{n}! = {rez}')