# trikampio plotas su Herono formule

import math

def plotas(a, b, c):
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return s

tr1 = plotas(5, 8, 4)
print(tr1)

tr2 = plotas(-2, 10, 10)
print(tr2) #nerodys, kad klaida yra, reikia apsirasyti klaida:

def plotas2(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError('Krastine turi buti teigiama')
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return s

tr3 = plotas2(-2, 10, 10)
print(tr3)