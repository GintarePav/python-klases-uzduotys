# (S - sulinys, Z - zirkles, P - popierius)
# zaidejas ir kompiuteris
# S vs P = P
# Z vs P = Z
# S vs Z = S

import random
arZaidziam = True

while arZaidziam:
    zaidejas = input('Irasykite savo pasirinkima: S, Z, P: ')
    kompiuteris = random.choice(['S', 'Z', 'P'])
    if zaidejas == 'S' or zaidejas == 'Z' or zaidejas == 'P':
        print(f'{zaidejas} (jus) vs {kompiuteris} (kompiuteris)')
        if zaidejas == 'S' and kompiuteris == 'P':
            print("Laimejo kompiuteris")
        elif zaidejas == 'P' and kompiuteris == 'Z':
            print("Laimejo kompiuteris")
        elif zaidejas == 'Z' and kompiuteris == 'S':
            print("Laimejo kompiuteris")
        elif zaidejas == kompiuteris:
            print("Lygiosios")
        else:
            print("Laimejote jus") 
        kartoti = input("Ar zaisite dar karta? T/N ")
        if kartoti != 'T':
            arZaidziam = False
            break
    else:
        print("Netinkamas pasirinkimas, bandykite dar karta")
