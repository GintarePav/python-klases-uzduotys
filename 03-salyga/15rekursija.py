# apskaiciuoti suma iki ivesto skaiciaus
# 5 ==> 5 + 4 + 3 + 2 + 1

import math

n = int(input("Duok skaiciu sumavimui: "))

def sumavimas(sk):
    if sk == 1:
        return 1
    else: 
        return sk + sumavimas(sk-1)
    
rez = sumavimas(n)
print(f'{rez}')